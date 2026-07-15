# Install For Codex

## Install via npm (Recommended)

```bash
npx @thanhndpo/tanizy-po-agent --target codex --project /path/to/project --dry-run
npx @thanhndpo/tanizy-po-agent --target codex --project /path/to/project
```

## Install from Local Clone

From the `tanizy-po-agent` repository:

```bash
node scripts/install.mjs --target codex --project /path/to/project --dry-run
node scripts/install.mjs --target codex --project /path/to/project
```

Use `--force` only when you intentionally want to overwrite existing Tanizy files in the target project.

## Manual Copy

macOS / Linux:

```bash
mkdir -p /path/to/project/.agents/skills
cp -R core/skills/* /path/to/project/.agents/skills/
cp adapters/codex/AGENTS.md /path/to/project/AGENTS.md
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force C:\path\to\project\.agents\skills
Copy-Item -Recurse core/skills/* C:\path\to\project\.agents\skills\
Copy-Item adapters/codex/AGENTS.md C:\path\to\project\AGENTS.md
```

## After Install

Open the project in Codex. `AGENTS.md` provides routing rules, and installed skills live in `.agents/skills/`.
