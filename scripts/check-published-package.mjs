#!/usr/bin/env node

import { mkdtempSync, readFileSync, rmSync } from "node:fs";
import { spawnSync } from "node:child_process";
import { join, resolve } from "node:path";
import { tmpdir } from "node:os";

const packageRoot = resolve(process.argv[2] ?? ".");
const npmCache = mkdtempSync(join(tmpdir(), "tanizy-npm-cache-"));

try {
  const result = spawnSync(
    "npm",
    ["pack", "--dry-run", "--json", "--cache", npmCache],
    {
      cwd: packageRoot,
      encoding: "utf8",
    },
  );

  if (result.status !== 0) {
    throw new Error(result.stderr || result.stdout || `npm pack exited with status ${result.status}`);
  }

  const report = JSON.parse(result.stdout);
  const files = report[0]?.files ?? [];
  const paths = files.map((file) => file.path);
  const forbidden = paths.filter((path) =>
    path === ".gitignore" ||
    path === ".npmignore" ||
    path === "docs" ||
    path.startsWith("docs/"),
  );

  if (forbidden.length > 0) {
    throw new Error(`Unexpected files in ${packageRoot}:\n${forbidden.join("\n")}`);
  }

  const packageJson = JSON.parse(readFileSync(join(packageRoot, "package.json"), "utf8"));
  const required = ["package.json", "README.md", "LICENSE"];
  const missing = required.filter((path) => !paths.includes(path));

  if (missing.length > 0) {
    throw new Error(`Required files missing from ${packageRoot}:\n${missing.join("\n")}`);
  }

  console.log(`${packageJson.name}@${packageJson.version}: ${paths.length} published files`);
} finally {
  rmSync(npmCache, { recursive: true, force: true });
}
