#!/usr/bin/env node

import { cpSync, existsSync, mkdirSync, readFileSync, readdirSync, statSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");

const targets = new Set(["gemini-cli", "codex", "claude-code", "antigravity"]);
const aliases = new Map([
  ["gemini", "gemini-cli"],
  ["claude", "claude-code"],
]);

function usage() {
  console.log(`Usage:
  npx @thanhndpo/tanizy-po-agent --target <gemini-cli|codex|claude-code|antigravity> --project <path> [--dry-run] [--force]

Or from a local clone:
  node scripts/install.mjs --target <gemini-cli|codex|claude-code|antigravity> --project <path> [--dry-run] [--force]

Examples:
  npx @thanhndpo/tanizy-po-agent --target gemini-cli --project ../my-project
  npx @thanhndpo/tanizy-po-agent --target codex --project /path/to/project --dry-run
  npx @thanhndpo/tanizy-po-agent --target claude-code --project /path/to/project --force
`);
}

function parseArgs(argv) {
  const args = { dryRun: false, force: false };

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--dry-run") {
      args.dryRun = true;
    } else if (arg === "--force") {
      args.force = true;
    } else if (arg === "--target") {
      args.target = argv[++i];
    } else if (arg === "--project") {
      args.project = argv[++i];
    } else if (arg === "-h" || arg === "--help") {
      args.help = true;
    } else if (arg === "-v" || arg === "--version") {
      const pkg = JSON.parse(readFileSync(join(repoRoot, "package.json"), "utf-8"));
      console.log(pkg.version);
      process.exit(0);
    } else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }

  if (args.target && aliases.has(args.target)) {
    args.target = aliases.get(args.target);
  }

  return args;
}

function ensureValidArgs(args) {
  if (args.help) {
    usage();
    process.exit(0);
  }
  if (!args.target || !targets.has(args.target)) {
    throw new Error("Missing or invalid --target.");
  }
  if (!args.project) {
    throw new Error("Missing --project.");
  }
}

function copyPlan(target, projectRoot) {
  const coreSkills = join(repoRoot, "core", "skills");

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
    { from: coreSkills, to: join(projectRoot, "skills") },
    { from: join(repoRoot, "adapters", "antigravity", "AGENTS.md"), to: join(projectRoot, "AGENTS.md") },
    { from: join(repoRoot, "adapters", "antigravity", ".agents"), to: join(projectRoot, ".agents") },
  ];
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

  const plan = copyPlan(args.target, projectRoot);
  console.log(`Tanizy PO Agent install target: ${args.target}`);
  console.log(`Project: ${projectRoot}`);

  for (const item of plan) {
    const exists = existsSync(item.to);
    console.log(`${args.dryRun ? "Would copy" : "Copy"} ${relative(item.from)} -> ${item.to}${exists ? " (exists)" : ""}`);

    if (args.dryRun) {
      continue;
    }

    if (exists && !args.force) {
      throw new Error(`Destination exists. Re-run with --force to overwrite: ${item.to}`);
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
