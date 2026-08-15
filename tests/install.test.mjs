import assert from "node:assert/strict";
import {
  existsSync,
  mkdtempSync,
  mkdirSync,
  readFileSync,
  rmSync,
  writeFileSync,
} from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { spawnSync } from "node:child_process";
import test from "node:test";
import { fileURLToPath } from "node:url";

const repoRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const installer = join(repoRoot, "scripts", "install.mjs");
const writingRequirementsRoot = join(repoRoot, "core", "skills", "writing-requirements");
const poBlockStart = "<!-- BEGIN TANIZY PO AGENT MANAGED BLOCK -->";
const poBlockEnd = "<!-- END TANIZY PO AGENT MANAGED BLOCK -->";
const qcManagedBlock = [
  "<!-- BEGIN TANIZY QC AGENT MANAGED BLOCK -->",
  "## Tanizy QC Agent for Codex",
  "Start QC only after an explicit request.",
  "<!-- END TANIZY QC AGENT MANAGED BLOCK -->",
].join("\n");

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

function adapterPath(target, projectRoot) {
  if (target === "gemini-cli") return join(projectRoot, "GEMINI.md");
  if (target === "claude-code") return join(projectRoot, "CLAUDE.md");
  return join(projectRoot, "AGENTS.md");
}

function contentOutsidePoBlock(content) {
  const start = content.indexOf(poBlockStart);
  const end = content.indexOf(poBlockEnd);
  assert.ok(start >= 0 && end > start, "Expected one complete PO managed block");
  return `${content.slice(0, start)}${content.slice(end + poBlockEnd.length)}`;
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

test("dry run prints the managed plan without writing", () => {
  withProject((projectRoot) => {
    const result = runInstaller(projectRoot, "--dry-run");

    assert.equal(result.status, 0, result.stderr);
    assert.match(result.stdout, /Adapter: managed PO block/);
    assert.match(result.stdout, /Dry run complete\. No files were written\./);
    assert.equal(existsSync(join(projectRoot, "AGENTS.md")), false);
    assert.equal(existsSync(join(projectRoot, ".agents")), false);
  });
});

test("full install uses a managed adapter block and target-compatible skills", () => {
  const cases = [
    ["gemini-cli", join("skills", "using-tanizy-agent")],
    ["codex", join(".agents", "skills", "using-tanizy-agent")],
    ["claude-code", join(".claude", "skills", "using-tanizy-agent")],
    ["antigravity", join(".agents", "skills", "using-tanizy-agent")],
  ];

  for (const [target, routerPath] of cases) {
    withProject((projectRoot) => {
      const result = runInstallerForTarget(projectRoot, target);
      const adapter = readFileSync(adapterPath(target, projectRoot), "utf8");

      assert.equal(result.status, 0, result.stderr);
      assert.match(adapter, /BEGIN TANIZY PO AGENT MANAGED BLOCK/);
      assert.equal(adapter.match(/BEGIN TANIZY PO AGENT MANAGED BLOCK/g)?.length, 1);
      assert.equal(existsSync(join(projectRoot, routerPath)), target === "gemini-cli");
      if (target === "antigravity") {
        assert.equal(
          existsSync(join(projectRoot, ".agents", "rules", "tanizy-po.md")),
          true,
        );
      }
    });
  }
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
    assert.match(result.stderr, /Unknown or unavailable skill/);
    assert.equal(existsSync(join(projectRoot, ".agents")), false);
  });
});

test("rejects the Gemini-only router for other targets", () => {
  withProject((projectRoot) => {
    const result = runInstaller(projectRoot, "--skill", "using-tanizy-agent");

    assert.notEqual(result.status, 0);
    assert.match(result.stderr, /unavailable skill for codex: using-tanizy-agent/);
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

test("preserves project instructions and the QC block across PO install and force update", () => {
  withProject((projectRoot) => {
    const adapter = join(projectRoot, "AGENTS.md");
    const projectInstructions = "# Project Agents\n\n## Project Rules\nKeep local release rules.";
    writeFileSync(adapter, `${projectInstructions}\n\n${qcManagedBlock}\n`, "utf8");

    const installed = runInstaller(projectRoot);
    assert.equal(installed.status, 0, installed.stderr);

    const afterInstall = readFileSync(adapter, "utf8");
    assert.ok(afterInstall.includes(projectInstructions));
    assert.ok(afterInstall.includes(qcManagedBlock));
    assert.equal(afterInstall.match(/BEGIN TANIZY PO AGENT MANAGED BLOCK/g)?.length, 1);

    const footer = "\n## Project Footer\nKeep this footer.\n";
    const stalePoBlock = `${afterInstall}${footer}`.replace(
      "This project uses Tanizy PO Agent skills for Product Owner workflows.",
      "Stale PO routing text.",
    );
    writeFileSync(adapter, stalePoBlock, "utf8");

    const blocked = runInstaller(projectRoot);
    assert.notEqual(blocked.status, 0);
    assert.equal(readFileSync(adapter, "utf8"), stalePoBlock);

    const updated = runInstaller(projectRoot, "--force");
    assert.equal(updated.status, 0, updated.stderr);

    const afterForce = readFileSync(adapter, "utf8");
    assert.equal(contentOutsidePoBlock(afterForce), contentOutsidePoBlock(stalePoBlock));
    assert.ok(afterForce.includes(projectInstructions));
    assert.ok(afterForce.includes(qcManagedBlock));
    assert.ok(afterForce.endsWith(footer));
    assert.doesNotMatch(afterForce, /Stale PO routing text/);
    assert.equal(afterForce.match(/BEGIN TANIZY PO AGENT MANAGED BLOCK/g)?.length, 1);
  });
});

test("Antigravity install manages only the PO rule", () => {
  withProject((projectRoot) => {
    const rulesRoot = join(projectRoot, ".agents", "rules");
    const qcRule = join(rulesRoot, "tanizy-qc.md");
    const poRule = join(rulesRoot, "tanizy-po.md");
    mkdirSync(rulesRoot, { recursive: true });
    writeFileSync(qcRule, "QC RULE SENTINEL\n", "utf8");

    const installed = runInstallerForTarget(projectRoot, "antigravity");
    assert.equal(installed.status, 0, installed.stderr);
    assert.equal(readFileSync(qcRule, "utf8"), "QC RULE SENTINEL\n");
    assert.match(readFileSync(poRule, "utf8"), /For Product Owner work/);

    writeFileSync(poRule, "STALE PO RULE\n", "utf8");
    const updated = runInstallerForTarget(projectRoot, "antigravity", "--force");
    assert.equal(updated.status, 0, updated.stderr);
    assert.equal(readFileSync(qcRule, "utf8"), "QC RULE SENTINEL\n");
    assert.doesNotMatch(readFileSync(poRule, "utf8"), /STALE PO RULE/);
  });
});

test("converts an unchanged legacy adapter into a managed block", () => {
  withProject((projectRoot) => {
    const legacy = readFileSync(join(repoRoot, "adapters", "codex", "AGENTS.md"), "utf8");
    const adapter = join(projectRoot, "AGENTS.md");
    writeFileSync(adapter, legacy, "utf8");

    const result = runInstaller(projectRoot);
    const migrated = readFileSync(adapter, "utf8");

    assert.equal(result.status, 0, result.stderr);
    assert.match(migrated, /BEGIN TANIZY PO AGENT MANAGED BLOCK/);
    assert.equal(migrated.match(/BEGIN TANIZY PO AGENT MANAGED BLOCK/g)?.length, 1);
  });
});

test("refuses an unmarked legacy adapter with inseparable local changes", () => {
  withProject((projectRoot) => {
    const legacy = readFileSync(join(repoRoot, "adapters", "codex", "AGENTS.md"), "utf8");
    const adapter = join(projectRoot, "AGENTS.md");
    writeFileSync(adapter, `${legacy}\n## Local Rule\nPreserve me.\n`, "utf8");

    const result = runInstaller(projectRoot, "--force");

    assert.notEqual(result.status, 0);
    assert.match(result.stderr, /Unmarked legacy Tanizy PO adapter/);
    assert.equal(existsSync(join(projectRoot, ".agents", "skills")), false);
  });
});

test("preflights malformed blocks and late collisions before writing", () => {
  withProject((projectRoot) => {
    const adapter = join(projectRoot, "AGENTS.md");
    writeFileSync(adapter, `${poBlockStart}\nIncomplete block.\n`, "utf8");

    const malformed = runInstaller(projectRoot);
    assert.notEqual(malformed.status, 0);
    assert.match(malformed.stderr, /zero or one complete Tanizy PO managed block/);
    assert.equal(existsSync(join(projectRoot, ".agents", "skills")), false);
  });

  withProject((projectRoot) => {
    const collision = join(projectRoot, ".agents", "skills", "writing-requirements");
    mkdirSync(collision, { recursive: true });
    writeFileSync(join(collision, "KEEP"), "keep\n", "utf8");

    const result = runInstaller(projectRoot);
    assert.notEqual(result.status, 0);
    assert.equal(readFileSync(join(collision, "KEEP"), "utf8"), "keep\n");
    assert.equal(existsSync(join(projectRoot, ".agents", "skills", "brainstorming")), false);
    assert.equal(existsSync(join(projectRoot, "AGENTS.md")), false);
  });
});

test("keeps Basic Design table formatting portable", () => {
  const files = [
    join(writingRequirementsRoot, "SKILL.md"),
    join(writingRequirementsRoot, "templates", "basic-design.md"),
  ];

  for (const path of files) {
    const content = readFileSync(path, "utf8");

    assert.doesNotMatch(content, /<br\s*\/?\s*>/i, `${path} must not use HTML line breaks`);
    assert.match(content, /`• `/, `${path} must define the structured-rule prefix`);
    assert.match(content, /` • `/, `${path} must define the independent-rule separator`);
    assert.match(content, /`; `/, `${path} must define the sub-condition separator`);
  }
});
