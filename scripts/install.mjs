#!/usr/bin/env node

import { cpSync, existsSync, mkdirSync, readFileSync, readdirSync, rmSync, statSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const packageConfig = JSON.parse(readFileSync(join(repoRoot, "package.json"), "utf-8"));
const fixedTarget = packageConfig.tanizyTarget;

const targets = new Set(["gemini-cli", "codex", "claude-code", "antigravity"]);
const aliases = new Map([
  ["gemini", "gemini-cli"],
  ["claude", "claude-code"],
]);

function usage() {
  const command = fixedTarget
    ? `npx ${packageConfig.name} --project <path> [--skill <name>]... [--dry-run] [--force]`
    : `npx ${packageConfig.name} --target <gemini-cli|codex|claude-code|antigravity> --project <path> [--skill <name>]... [--dry-run] [--force]`;

  console.log(`Usage:
  ${command}

Or from a local clone:
  node scripts/install.mjs --target <gemini-cli|codex|claude-code|antigravity> --project <path> [--skill <name>]... [--dry-run] [--force]

Examples:
  npx @thanhndpo/tanizy-po-agent --target gemini-cli --project ../my-project
  npx @thanhndpo/tanizy-po-agent --target codex --project /path/to/project --skill mtg-memos
  npx @thanhndpo/tanizy-po-agent@latest --target codex --project /path/to/project --skill mtg-memos --force
  npx @thanhndpo/tanizy-po-agent --target claude-code --project /path/to/project --skill brainstorming --skill writing-requirements
`);
}

function parseArgs(argv) {
  const args = { dryRun: false, force: false, skills: [] };

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--dry-run") {
      args.dryRun = true;
    } else if (arg === "--force") {
      args.force = true;
    } else if (arg === "--target") {
      args.target = optionValue(argv, i, arg);
      i += 1;
    } else if (arg === "--project") {
      args.project = optionValue(argv, i, arg);
      i += 1;
    } else if (arg === "--skill") {
      args.skills.push(optionValue(argv, i, arg));
      i += 1;
    } else if (arg === "-h" || arg === "--help") {
      args.help = true;
    } else if (arg === "-v" || arg === "--version") {
      console.log(packageConfig.version);
      process.exit(0);
    } else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }

  if (args.target && aliases.has(args.target)) {
    args.target = aliases.get(args.target);
  }

  if (!args.target && fixedTarget) {
    args.target = fixedTarget;
  }

  return args;
}

function optionValue(argv, index, option) {
  const value = argv[index + 1];
  if (!value || value.startsWith("-")) {
    throw new Error(`Missing value for ${option}.`);
  }
  return value;
}

function ensureValidArgs(args) {
  if (args.help) {
    usage();
    process.exit(0);
  }
  if (!args.target || !targets.has(args.target)) {
    throw new Error("Missing or invalid --target.");
  }
  if (fixedTarget && args.target !== fixedTarget) {
    throw new Error(`This package only supports --target ${fixedTarget}.`);
  }
  if (!args.project) {
    throw new Error("Missing --project.");
  }

  const availableSkills = skillDirectories();
  const invalidSkills = args.skills.filter((skill) => !availableSkills.includes(skill));
  if (invalidSkills.length > 0) {
    throw new Error(
      `Unknown skill: ${invalidSkills.join(", ")}. Available skills: ${availableSkills.join(", ")}`,
    );
  }

  args.skills = [...new Set(args.skills)];
}

function copyPlan(target, projectRoot, selectedSkills) {
  const coreSkills = join(repoRoot, "core", "skills");

  if (selectedSkills.length > 0) {
    const skillsRoot = skillDestinationRoot(target, projectRoot);
    return selectedSkills.map((skill) => ({
      from: join(coreSkills, skill),
      to: join(skillsRoot, skill),
      replaceOnForce: true,
    }));
  }

  if (target === "gemini-cli") {
    return [
      { from: coreSkills, to: join(projectRoot, "skills") },
      { from: join(repoRoot, "adapters", "gemini-cli", "GEMINI.md"), to: join(projectRoot, "GEMINI.md") },
      { from: join(repoRoot, "adapters", "gemini-cli", ".gemini"), to: join(projectRoot, ".gemini") },
      { from: join(repoRoot, "adapters", "gemini-cli", ".geminiignore"), to: join(projectRoot, ".geminiignore") },
    ];
  }

  if (target === "codex") {
    return [
      ...skillDirectories().map((skill) => ({
        from: join(coreSkills, skill),
        to: join(projectRoot, ".agents", "skills", skill),
      })),
      { from: join(repoRoot, "adapters", "codex", "AGENTS.md"), to: join(projectRoot, "AGENTS.md") },
    ];
  }

  if (target === "claude-code") {
    return [
      ...skillDirectories().map((skill) => ({
        from: join(coreSkills, skill),
        to: join(projectRoot, ".claude", "skills", skill),
      })),
      { from: join(repoRoot, "adapters", "claude-code", "CLAUDE.md"), to: join(projectRoot, "CLAUDE.md") },
    ];
  }

  return [
    ...skillDirectories().map((skill) => ({
      from: join(coreSkills, skill),
      to: join(projectRoot, ".agents", "skills", skill),
    })),
    { from: join(repoRoot, "adapters", "antigravity", "AGENTS.md"), to: join(projectRoot, "AGENTS.md") },
    { from: join(repoRoot, "adapters", "antigravity", ".agents", "rules"), to: join(projectRoot, ".agents", "rules") },
  ];
}

function skillDestinationRoot(target, projectRoot) {
  if (target === "gemini-cli") {
    return join(projectRoot, "skills");
  }
  if (target === "claude-code") {
    return join(projectRoot, ".claude", "skills");
  }
  return join(projectRoot, ".agents", "skills");
}

function skillDirectories() {
  const skillsRoot = join(repoRoot, "core", "skills");
  return readdirSync(skillsRoot)
    .filter((name) => statSync(join(skillsRoot, name)).isDirectory())
    .sort();
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  ensureValidArgs(args);

  const projectRoot = resolve(args.project);
  if (!existsSync(projectRoot)) {
    throw new Error(`Project path does not exist: ${projectRoot}`);
  }

  const plan = copyPlan(args.target, projectRoot, args.skills);
  console.log(`Tanizy PO Agent install target: ${args.target}`);
  console.log(`Project: ${projectRoot}`);
  console.log(`Skills: ${args.skills.length > 0 ? args.skills.join(", ") : "all"}`);

  for (const item of plan) {
    const exists = existsSync(item.to);
    console.log(`${args.dryRun ? "Would copy" : "Copy"} ${relative(item.from)} -> ${item.to}${exists ? " (exists)" : ""}`);

    if (args.dryRun) {
      continue;
    }

    if (exists && !args.force) {
      throw new Error(`Destination exists. Re-run with --force to overwrite: ${item.to}`);
    }

    if (exists && item.replaceOnForce) {
      rmSync(item.to, { recursive: true, force: true });
    }

    mkdirSync(dirname(item.to), { recursive: true });
    cpSync(item.from, item.to, { recursive: true, force: true });
  }

  console.log(args.dryRun ? "Dry run complete." : "Install complete.");
}

function relative(path) {
  return path.startsWith(repoRoot) ? path.slice(repoRoot.length + 1) : path;
}

main().catch((error) => {
  console.error(`Error: ${error.message}`);
  usage();
  process.exit(1);
});
