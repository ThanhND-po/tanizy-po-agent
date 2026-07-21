#!/usr/bin/env node

import {
  cpSync,
  existsSync,
  mkdirSync,
  readFileSync,
  rmSync,
  writeFileSync,
} from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const rootPackage = JSON.parse(readFileSync(join(repoRoot, "package.json"), "utf-8"));
const outputRoot = join(repoRoot, "dist", "packages");

const targets = [
  {
    name: "gemini-cli",
    label: "Gemini CLI",
  },
  {
    name: "codex",
    label: "Codex",
  },
  {
    name: "claude-code",
    label: "Claude Code",
  },
  {
    name: "antigravity",
    label: "Antigravity",
  },
];

rmSync(outputRoot, { recursive: true, force: true });
mkdirSync(outputRoot, { recursive: true });

for (const target of targets) {
  const packageRoot = join(outputRoot, target.name);
  const adapterRoot = join(repoRoot, "adapters", target.name);

  if (!existsSync(adapterRoot)) {
    throw new Error(`Missing adapter directory: ${adapterRoot}`);
  }

  cpSync(join(repoRoot, "core", "skills"), join(packageRoot, "core", "skills"), { recursive: true });
  cpSync(adapterRoot, join(packageRoot, "adapters", target.name), { recursive: true });
  cpSync(join(repoRoot, "scripts", "install.mjs"), join(packageRoot, "scripts", "install.mjs"));
  cpSync(join(repoRoot, "LICENSE"), join(packageRoot, "LICENSE"));

  const packageName = `${rootPackage.name}-${target.name}`;
  const packageJson = {
    name: packageName,
    version: rootPackage.version,
    description: `${rootPackage.description} Target package for ${target.label}.`,
    license: rootPackage.license,
    type: "module",
    bin: {
      [`tanizy-po-install-${target.name}`]: "scripts/install.mjs",
    },
    tanizyTarget: target.name,
    files: [
      "core",
      "adapters",
      "scripts/install.mjs",
      "LICENSE",
    ],
    repository: rootPackage.repository,
    homepage: rootPackage.homepage,
    author: rootPackage.author,
    keywords: [...(rootPackage.keywords ?? []), `${target.name}-skills`],
  };

  writeFileSync(join(packageRoot, "package.json"), `${JSON.stringify(packageJson, null, 2)}\n`);
  writeFileSync(
    join(packageRoot, "README.md"),
    `# ${packageName}\n\n${rootPackage.description}\n\nThis package installs the Tanizy PO Agent skills for ${target.label}.\n\n## Install\n\n\`\`\`bash\n` +
      `npx ${packageName} --project /path/to/project\n` +
      `\`\`\`\n\nUse \`--dry-run\` to preview the files before installation.\n`,
  );

  console.log(`Built ${packageName}@${rootPackage.version} at ${packageRoot}`);
}
