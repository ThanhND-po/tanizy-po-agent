import assert from 'node:assert/strict';
import { cpSync, existsSync, mkdtempSync, readFileSync, readdirSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join, resolve } from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import test, { after } from 'node:test';

const repoRoot = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const scratch = mkdtempSync(join(tmpdir(), 'tanizy-package-test-'));
after(() => rmSync(scratch, { recursive: true, force: true }));
const targets = ['codex', 'claude-code', 'antigravity'];
const version = JSON.parse(readFileSync(join(repoRoot, 'package.json'), 'utf8')).version;

function run(command, args, cwd = repoRoot) {
  const result = spawnSync(command, args, { cwd, encoding: 'utf8' });
  assert.equal(result.status, 0, result.stderr || result.stdout);
  return result;
}

function assertTree(source, destination) {
  const entries = readdirSync(source, { withFileTypes: true })
    .filter((entry) => !['.DS_Store', '__pycache__'].includes(entry.name) && !entry.name.endsWith('.pyc'));
  assert.deepEqual(readdirSync(destination).sort(), entries.map((entry) => entry.name).sort(), destination);
  for (const entry of entries) {
    const from = join(source, entry.name);
    const to = join(destination, entry.name);
    if (entry.isDirectory()) assertTree(from, to);
    else assert.deepEqual(readFileSync(to), readFileSync(from), to);
  }
}

for (const fixedTarget of [null, ...targets]) {
  test(`npm tarball installs and updates ${fixedTarget ?? 'universal'} without changing project artifacts`, () => {
    const source = fixedTarget ? join(repoRoot, 'dist', 'packages', fixedTarget) : repoRoot;
    const packed = run('npm', ['pack', '--json', '--cache', join(scratch, 'cache'), '--pack-destination', scratch], source);
    const [report] = JSON.parse(packed.stdout);
    assert.equal(report.version, version);
    const unpacked = mkdtempSync(join(scratch, 'unpacked-'));
    run('tar', ['-xzf', join(scratch, report.filename), '-C', unpacked]);
    const packageRoot = join(unpacked, 'package');
    const config = JSON.parse(readFileSync(join(packageRoot, 'package.json'), 'utf8'));
    assert.equal(config.tanizyTarget ?? null, fixedTarget);
    assertTree(join(repoRoot, 'core'), join(packageRoot, 'core'));
    const forbidden = report.files.filter(({ path }) => /^(docs|tests|\.github)\//.test(path));
    assert.deepEqual(forbidden, []);

    for (const target of fixedTarget ? [fixedTarget] : targets) {
      const project = mkdtempSync(join(scratch, 'project-'));
      const adapter = join(project, target === 'claude-code' ? 'CLAUDE.md' : 'AGENTS.md');
      const instructions = '# Project rules\nRead metadata-policy.json.\n';
      writeFileSync(adapter, instructions);
      const policy = '{"delivery":["queued","building","live"],"approval":["accepted"]}\n';
      const artifact = '---\nstatus: live\napproval_status: accepted\n---\n## 1. Metadata\n\n| Field | Value |\n|---|---|\n| Status | Live |\n\nApproval evidence: revision 2. Scope: phase 1. HTTP status: 200.\n';
      writeFileSync(join(project, 'metadata-policy.json'), policy);
      writeFileSync(join(project, 'existing.md'), artifact);
      const args = ['--project', project, ...(fixedTarget ? [] : ['--target', target])];
      const install = (...extra) => run(process.execPath, [join(packageRoot, 'scripts', 'install.mjs'), ...args, ...extra], scratch);
      const skillRoot = join(project, target === 'claude-code' ? '.claude' : '.agents', 'skills');
      install('--dry-run');
      assert.equal(existsSync(skillRoot), false);
      assert.equal(readFileSync(adapter, 'utf8'), instructions);
      for (const skill of ['artifact-update-process', 'brainstorming', 'generating-mockup']) {
        install('--skill', skill, '--force');
        assert.equal(readFileSync(adapter, 'utf8'), instructions);
      }
      for (const resource of [
        'writing-requirements/references/document-metadata.md',
        'writing-requirements/references/basic-design-authoring.md',
        'creating-diagrams/references/interactive-html.md',
        'web-design-guidelines/SKILL.md', 'shadcn-ui/SKILL.md',
      ]) assert.deepEqual(readFileSync(join(skillRoot, resource)), readFileSync(join(repoRoot, 'core', 'skills', resource)));
      const stale = join(skillRoot, 'writing-requirements', 'obsolete.md');
      writeFileSync(stale, 'old metadata guidance\n');
      install('--force');
      assert.equal(existsSync(stale), false);
      assertTree(join(repoRoot, 'core', 'skills'), skillRoot);
      assert.ok(readFileSync(adapter, 'utf8').startsWith(instructions));
      if (target === 'antigravity') {
        assert.deepEqual(readFileSync(join(project, '.agents', 'rules', 'tanizy-po.md')),
          readFileSync(join(repoRoot, 'adapters', target, '.agents', 'rules', 'tanizy-po.md')));
      }
      assert.equal(readFileSync(join(project, 'metadata-policy.json'), 'utf8'), policy);
      assert.equal(readFileSync(join(project, 'existing.md'), 'utf8'), artifact);
      if (fixedTarget) {
        const rejected = spawnSync(process.execPath, [join(packageRoot, 'scripts', 'install.mjs'), ...args,
          '--target', targets.find((other) => other !== target), '--force'], { encoding: 'utf8' });
        assert.notEqual(rejected.status, 0);
        assert.match(rejected.stderr, /only supports/);
      }
    }
  });
}

test('package check detects a missing hidden Antigravity rule', () => {
  const fixture = mkdtempSync(join(scratch, 'missing-rule-'));
  for (const path of ['package.json', 'README.md', 'LICENSE', 'core', 'adapters', 'scripts/install.mjs']) {
    cpSync(join(repoRoot, path), join(fixture, path), { recursive: true });
  }
  // Exclude a real required resource from the tarball, while keeping it in source.
  writeFileSync(join(fixture, 'adapters', 'antigravity', '.npmignore'), '.agents/\n');
  const result = spawnSync(process.execPath, [join(repoRoot, 'scripts', 'check-published-package.mjs'), fixture], { encoding: 'utf8' });
  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /Required files missing/);
  assert.match(result.stderr, /adapters\/antigravity\/\.agents\/rules\/tanizy-po\.md/);
});
