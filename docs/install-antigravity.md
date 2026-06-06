# Install For Antigravity

## Recommended

From the `tanizy-po-agent` repository:

```bash
node scripts/install.mjs --target antigravity --project /path/to/project --dry-run
node scripts/install.mjs --target antigravity --project /path/to/project
```

Use `--force` only when you intentionally want to overwrite existing Tanizy files in the target project.

## Manual Copy

macOS / Linux:

```bash
cp -R core/skills /path/to/project/skills
cp adapters/antigravity/AGENTS.md /path/to/project/AGENTS.md
cp -R adapters/antigravity/.agents /path/to/project/.agents
```

Windows PowerShell:

```powershell
Copy-Item -Recurse core/skills C:\path\to\project\skills
Copy-Item adapters/antigravity/AGENTS.md C:\path\to\project\AGENTS.md
Copy-Item -Recurse adapters/antigravity/.agents C:\path\to\project\.agents
```

## After Install

Open the project in Antigravity. `AGENTS.md` and `.agents/rules/tanizy-po.md` provide the stable routing entrypoints. The rule points the agent to local workflow files under `skills/`.
