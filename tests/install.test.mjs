import assert from "node:assert/strict";
import { existsSync, mkdtempSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { spawnSync } from "node:child_process";
import test from "node:test";
import { fileURLToPath } from "node:url";

const repoRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const installer = join(repoRoot, "scripts", "install.mjs");

function runInstaller(projectRoot, ...args) {
  return runInstallerForTarget(projectRoot, "codex", ...args);
}

function runInstallerForTarget(projectRoot, target, ...args) {
  return spawnSync(
    process.execPath,
    [installer, "--target", target, "--project", projectRoot, ...args],
    { cwd: repoRoot, encoding: "utf8" },
  );
}

function withProject(run) {
  const projectRoot = mkdtempSync(join(tmpdir(), "tanizy-install-test-"));
  try {
    run(projectRoot);
  } finally {
    rmSync(projectRoot, { recursive: true, force: true });
  }
}

test("installs only the selected skill without copying the adapter", () => {
  withProject((projectRoot) => {
    const result = runInstaller(projectRoot, "--skill", "mtg-memos");

    assert.equal(result.status, 0, result.stderr);
    assert.equal(existsSync(join(projectRoot, ".agents", "skills", "mtg-memos", "SKILL.md")), true);
    assert.equal(existsSync(join(projectRoot, ".agents", "skills", "brainstorming")), false);
    assert.equal(existsSync(join(projectRoot, "AGENTS.md")), false);
  });
});

test("uses the target-specific skill directory", () => {
  const cases = [
    ["gemini-cli", join("skills", "mtg-memos")],
    ["claude-code", join(".claude", "skills", "mtg-memos")],
    ["antigravity", join(".agents", "skills", "mtg-memos")],
  ];

  for (const [target, relativeSkillRoot] of cases) {
    withProject((projectRoot) => {
      const result = runInstallerForTarget(projectRoot, target, "--skill", "mtg-memos");

      assert.equal(result.status, 0, result.stderr);
      assert.equal(existsSync(join(projectRoot, relativeSkillRoot, "SKILL.md")), true);
    });
  }
});

test("keeps the existing full install behavior when --skill is omitted", () => {
  withProject((projectRoot) => {
    const result = runInstaller(projectRoot);

    assert.equal(result.status, 0, result.stderr);
    assert.equal(existsSync(join(projectRoot, ".agents", "skills", "mtg-memos", "SKILL.md")), true);
    assert.equal(existsSync(join(projectRoot, ".agents", "skills", "brainstorming", "SKILL.md")), true);
    assert.equal(existsSync(join(projectRoot, "AGENTS.md")), true);
  });
});

test("supports repeated --skill options", () => {
  withProject((projectRoot) => {
    const result = runInstaller(
      projectRoot,
      "--skill",
      "brainstorming",
      "--skill",
      "writing-requirements",
    );

    assert.equal(result.status, 0, result.stderr);
    assert.equal(existsSync(join(projectRoot, ".agents", "skills", "brainstorming", "SKILL.md")), true);
    assert.equal(
      existsSync(join(projectRoot, ".agents", "skills", "writing-requirements", "SKILL.md")),
      true,
    );
  });
});

test("rejects unknown skill names before copying files", () => {
  withProject((projectRoot) => {
    const result = runInstaller(projectRoot, "--skill", "../unknown");

    assert.notEqual(result.status, 0);
    assert.match(result.stderr, /Unknown skill/);
    assert.equal(existsSync(join(projectRoot, ".agents")), false);
  });
});

test("reports a missing --skill value", () => {
  withProject((projectRoot) => {
    const result = runInstaller(projectRoot, "--skill");

    assert.notEqual(result.status, 0);
    assert.match(result.stderr, /Missing value for --skill/);
    assert.equal(existsSync(join(projectRoot, ".agents")), false);
  });
});

test("requires --force and cleanly replaces an existing selected skill", () => {
  withProject((projectRoot) => {
    const skillRoot = join(projectRoot, ".agents", "skills", "mtg-memos");
    mkdirSync(skillRoot, { recursive: true });
    writeFileSync(join(skillRoot, "stale.txt"), "stale\n");

    const blocked = runInstaller(projectRoot, "--skill", "mtg-memos");
    assert.notEqual(blocked.status, 0);
    assert.equal(readFileSync(join(skillRoot, "stale.txt"), "utf8"), "stale\n");

    const updated = runInstaller(projectRoot, "--skill", "mtg-memos", "--force");
    assert.equal(updated.status, 0, updated.stderr);
    assert.equal(existsSync(join(skillRoot, "SKILL.md")), true);
    assert.equal(existsSync(join(skillRoot, "stale.txt")), false);
  });
});
