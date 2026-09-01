#!/usr/bin/env node

import {
  cpSync,
  existsSync,
  lstatSync,
  mkdirSync,
  readFileSync,
  readdirSync,
  rmSync,
  statSync,
  writeFileSync,
} from "node:fs";
import { dirname, isAbsolute, join, relative, resolve, sep } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const packageConfig = JSON.parse(readFileSync(join(repoRoot, "package.json"), "utf8"));
const fixedTarget = packageConfig.tanizyTarget;
const targets = new Set(["gemini-cli", "codex", "claude-code", "antigravity"]);
const aliases = new Map([
  ["gemini", "gemini-cli"],
  ["claude", "claude-code"],
]);
const geminiRouterSkill = "using-tanizy-agent";
const managedBlockStart = "<!-- BEGIN TANIZY PO AGENT MANAGED BLOCK -->";
const managedBlockEnd = "<!-- END TANIZY PO AGENT MANAGED BLOCK -->";

function usage() {
  const command = fixedTarget
    ? `npx ${packageConfig.name} --project <path> [--skill <name>]... [--dry-run] [--force]`
    : `npx ${packageConfig.name} --target <gemini-cli|codex|claude-code|antigravity> --project <path> [--skill <name>]... [--dry-run] [--force]`;

  console.log(`Usage:
  ${command}

Options:
  --skill <name>   Install or update one target-compatible skill. Repeat for multiple skills.
  --dry-run        Validate and print the complete write plan without writing.
  --force          Replace selected package-managed skills, files, and the PO managed block.
  --help           Show this help.
  --version        Show the package version.

Examples:
  npx @thanhndpo/tanizy-po-agent --target gemini-cli --project ../my-project
  npx @thanhndpo/tanizy-po-agent --target codex --project /path/to/project --skill five-whys-rca
  npx @thanhndpo/tanizy-po-agent@latest --target codex --project /path/to/project --skill five-whys-rca --force
  npx @thanhndpo/tanizy-po-agent --target claude-code --project /path/to/project --skill brainstorming --skill writing-requirements`);
}

function optionValue(argv, index, option) {
  const value = argv[index + 1];
  if (!value || value.startsWith("-")) {
    throw new Error(`Missing value for ${option}.`);
  }
  return value;
}

function parseArgs(argv) {
  const args = { dryRun: false, force: false, help: false, skills: [] };

  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (arg === "--dry-run") args.dryRun = true;
    else if (arg === "--force") args.force = true;
    else if (arg === "--target") {
      args.target = optionValue(argv, index, arg);
      index += 1;
    } else if (arg === "--project") {
      args.project = optionValue(argv, index, arg);
      index += 1;
    } else if (arg === "--skill") {
      args.skills.push(optionValue(argv, index, arg));
      index += 1;
    } else if (arg === "-h" || arg === "--help") {
      args.help = true;
    } else if (arg === "-v" || arg === "--version") {
      console.log(packageConfig.version);
      process.exit(0);
    } else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }

  if (args.target && aliases.has(args.target)) args.target = aliases.get(args.target);
  if (!args.target && fixedTarget) args.target = fixedTarget;
  args.skills = [...new Set(args.skills)];
  return args;
}

function allSkillDirectories() {
  const root = join(repoRoot, "core", "skills");
  return readdirSync(root)
    .filter((name) => statSync(join(root, name)).isDirectory())
    .sort();
}

function skillDirectories(target) {
  return allSkillDirectories().filter(
    (name) => target === "gemini-cli" || name !== geminiRouterSkill,
  );
}

function ensureValidArgs(args) {
  if (args.help) return;
  if (!args.target || !targets.has(args.target)) {
    throw new Error("Missing or invalid --target. Use gemini-cli, codex, claude-code, or antigravity.");
  }
  if (fixedTarget && args.target !== fixedTarget) {
    throw new Error(`This package only supports --target ${fixedTarget}.`);
  }
  if (!args.project) throw new Error("Missing --project.");

  const available = skillDirectories(args.target);
  const invalid = args.skills.filter((skill) => !available.includes(skill));
  if (invalid.length > 0) {
    throw new Error(
      `Unknown or unavailable skill for ${args.target}: ${invalid.join(", ")}. Available skills: ${available.join(", ")}`,
    );
  }
}

function skillDestinationRoot(target, projectRoot) {
  if (target === "gemini-cli") return join(projectRoot, "skills");
  if (target === "claude-code") return join(projectRoot, ".claude", "skills");
  return join(projectRoot, ".agents", "skills");
}

function adapterSpec(target, projectRoot) {
  const adapterRoot = join(repoRoot, "adapters", target);
  if (target === "gemini-cli") {
    return { from: join(adapterRoot, "GEMINI.md"), to: join(projectRoot, "GEMINI.md") };
  }
  if (target === "claude-code") {
    return { from: join(adapterRoot, "CLAUDE.md"), to: join(projectRoot, "CLAUDE.md") };
  }
  return { from: join(adapterRoot, "AGENTS.md"), to: join(projectRoot, "AGENTS.md") };
}

function isInside(parent, candidate) {
  const rel = relative(resolve(parent), resolve(candidate));
  return rel === "" || (rel !== ".." && !rel.startsWith(`..${sep}`) && !isAbsolute(rel));
}

function assertSafeProjectDestination(projectRoot, candidate) {
  if (!isInside(projectRoot, candidate)) {
    throw new Error(`Unsafe destination outside project root: ${candidate}`);
  }
  if (lstatSync(projectRoot).isSymbolicLink()) {
    throw new Error(`Refusing to use a symbolic-link project root: ${projectRoot}`);
  }

  let cursor = resolve(projectRoot);
  const rel = relative(cursor, resolve(candidate));
  for (const part of rel.split(/[\\/]+/).filter(Boolean)) {
    cursor = join(cursor, part);
    if (existsSync(cursor) && lstatSync(cursor).isSymbolicLink()) {
      throw new Error(`Refusing to write through symbolic link: ${cursor}`);
    }
  }
}

function assertSafeManagedPath(expectedRoot, candidate) {
  if (!isInside(expectedRoot, candidate)) {
    throw new Error(`Unsafe destination outside managed root: ${candidate}`);
  }
  if (existsSync(candidate) && lstatSync(candidate).isSymbolicLink()) {
    throw new Error(`Refusing to replace symbolic link: ${candidate}`);
  }
}

function validateProjectRoot(projectRoot) {
  if (!existsSync(projectRoot)) {
    throw new Error(`Project path does not exist: ${projectRoot}`);
  }
  if (!statSync(projectRoot).isDirectory()) {
    throw new Error(`Project path is not a directory: ${projectRoot}`);
  }
  if (lstatSync(projectRoot).isSymbolicLink()) {
    throw new Error(`Refusing to use a symbolic-link project root: ${projectRoot}`);
  }
}

function copyPlan(target, projectRoot, requestedSkills) {
  const available = skillDirectories(target);
  const selected = requestedSkills.length > 0 ? requestedSkills : available;
  const selective = requestedSkills.length > 0;
  const sourceRoot = join(repoRoot, "core", "skills");
  const destinationRoot = skillDestinationRoot(target, projectRoot);
  const plan = selected.map((skill) => ({
    kind: "replace-directory",
    from: join(sourceRoot, skill),
    to: join(destinationRoot, skill),
    managedRoot: destinationRoot,
  }));

  if (!selective) {
    plan.push({ kind: "managed-block", ...adapterSpec(target, projectRoot) });

    if (target === "gemini-cli") {
      plan.push(
        {
          kind: "replace-directory",
          from: join(repoRoot, "adapters", "gemini-cli", ".gemini", "commands", "po"),
          to: join(projectRoot, ".gemini", "commands", "po"),
          managedRoot: join(projectRoot, ".gemini", "commands"),
        },
        {
          kind: "seed-file",
          from: join(repoRoot, "adapters", "gemini-cli", ".geminiignore"),
          to: join(projectRoot, ".geminiignore"),
        },
      );
    }

    if (target === "antigravity") {
      plan.push({
        kind: "managed-file",
        from: join(repoRoot, "adapters", "antigravity", ".agents", "rules", "tanizy-po.md"),
        to: join(projectRoot, ".agents", "rules", "tanizy-po.md"),
        managedRoot: join(projectRoot, ".agents", "rules"),
      });
    }
  }

  return { available, plan, selected, selective };
}

function fileContent(path) {
  return readFileSync(path, "utf8").replace(/\r\n/g, "\n").trimEnd();
}

function managedBlockContent(template) {
  return `${managedBlockStart}\n${template.trim()}\n${managedBlockEnd}`;
}

function looksLikeUnmarkedPoAdapter(content) {
  return /^# Tanizy PO Agent(?: For [^\n]+)?\s*$/m.test(content.trimStart());
}

function renderManagedBlock(existing, template) {
  const block = managedBlockContent(template);
  const start = existing.indexOf(managedBlockStart);
  const end = existing.indexOf(managedBlockEnd);
  const startCount = existing.split(managedBlockStart).length - 1;
  const endCount = existing.split(managedBlockEnd).length - 1;

  if (startCount !== endCount || startCount > 1 || (start >= 0 && end < start)) {
    throw new Error("Adapter must contain zero or one complete Tanizy PO managed block.");
  }
  if (start >= 0) {
    const suffixStart = end + managedBlockEnd.length;
    return `${existing.slice(0, start)}${block}${existing.slice(suffixStart)}`;
  }
  if (!existing.trim()) return `${block}\n`;
  if (existing.trim() === template.trim()) return `${block}\n`;
  if (looksLikeUnmarkedPoAdapter(existing)) {
    throw new Error(
      "Unmarked legacy Tanizy PO adapter contains content that cannot be separated safely. Move project-owned instructions outside the legacy PO content or restore the package adapter before retrying.",
    );
  }
  const separator = existing.endsWith("\n\n") ? "" : existing.endsWith("\n") ? "\n" : "\n\n";
  return `${existing}${separator}${block}\n`;
}

function inspectOperation(item, force) {
  if (item.kind === "seed-file") {
    if (!existsSync(item.to)) return "create";
    if (!lstatSync(item.to).isFile()) {
      throw new Error(`Expected a project-owned file at seed destination: ${item.to}`);
    }
    return "preserve";
  }

  if (item.kind === "managed-block") {
    if (!existsSync(item.to)) return "create";
    if (!lstatSync(item.to).isFile() || lstatSync(item.to).isSymbolicLink()) {
      throw new Error(`Expected a regular adapter file: ${item.to}`);
    }
    const current = readFileSync(item.to, "utf8");
    const next = renderManagedBlock(current, fileContent(item.from));
    if (current === next) return "unchanged";
    if (current.includes(managedBlockStart) && !force) return "conflict";
    return current.includes(managedBlockStart) ? "update" : "merge";
  }

  assertSafeManagedPath(item.managedRoot, item.to);
  if (!existsSync(item.to)) return "create";

  const destination = lstatSync(item.to);
  if (item.kind === "managed-file" && !destination.isFile()) {
    throw new Error(`Expected a managed file destination: ${item.to}`);
  }
  if (item.kind === "replace-directory" && !destination.isDirectory()) {
    throw new Error(`Expected a managed directory destination: ${item.to}`);
  }
  if (item.kind === "managed-file" && fileContent(item.from) === fileContent(item.to)) {
    return "unchanged";
  }
  return force ? "replace" : "conflict";
}

function preflight(projectRoot, plan, force) {
  const inspected = plan.map((item) => {
    assertSafeProjectDestination(projectRoot, item.to);
    return { ...item, action: inspectOperation(item, force) };
  });
  const conflicts = inspected.filter((item) => item.action === "conflict");
  if (conflicts.length > 0) {
    const paths = conflicts.map((item) => `- ${item.to}`).join("\n");
    throw new Error(
      `Package-managed destinations already exist or differ:\n${paths}\nRe-run with --force after reviewing the dry run.`,
    );
  }
  return inspected;
}

function applyOperation(projectRoot, item) {
  if (item.action === "preserve" || item.action === "unchanged") return;
  assertSafeProjectDestination(projectRoot, item.to);

  if (item.kind === "managed-block") {
    const current = existsSync(item.to) ? readFileSync(item.to, "utf8") : "";
    const next = renderManagedBlock(current, fileContent(item.from));
    mkdirSync(dirname(item.to), { recursive: true });
    writeFileSync(item.to, next, "utf8");
    return;
  }

  if (item.action === "replace") {
    assertSafeManagedPath(item.managedRoot, item.to);
    rmSync(item.to, { recursive: true, force: true });
  }
  mkdirSync(dirname(item.to), { recursive: true });
  cpSync(item.from, item.to, { recursive: true, force: false });
}

function printPlan(projectRoot, target, selected, selective, inspected, dryRun) {
  console.log(`Tanizy PO Agent ${packageConfig.version}`);
  console.log(`Target: ${target}`);
  console.log(`Project root: ${projectRoot}`);
  console.log(`Skills: ${selected.join(", ")}`);
  console.log(`Adapter: ${selective ? "unchanged by selective install" : "managed PO block"}`);

  for (const item of inspected) {
    console.log(`${dryRun ? "Plan" : "Apply"} [${item.action}] ${relative(projectRoot, item.to)}`);
  }
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  ensureValidArgs(args);
  if (args.help) {
    usage();
    return;
  }

  const projectRoot = resolve(args.project);
  validateProjectRoot(projectRoot);
  const { plan, selected, selective } = copyPlan(args.target, projectRoot, args.skills);
  const inspected = preflight(projectRoot, plan, args.force);
  printPlan(projectRoot, args.target, selected, selective, inspected, args.dryRun);

  if (args.dryRun) {
    console.log("Dry run complete. No files were written.");
    return;
  }

  for (const item of inspected) applyOperation(projectRoot, item);
  console.log("Install complete.");
}

main().catch((error) => {
  console.error(`Error: ${error.message}`);
  usage();
  process.exit(1);
});
