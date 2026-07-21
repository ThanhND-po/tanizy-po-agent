# Install For Antigravity

## Install via npm (Recommended)

```bash
npx @thanhndpo/tanizy-po-agent --target antigravity --project /path/to/project --dry-run
npx @thanhndpo/tanizy-po-agent --target antigravity --project /path/to/project
```

## Install from Local Clone

From the `tanizy-po-agent` repository:

```bash
node scripts/install.mjs --target antigravity --project /path/to/project --dry-run
node scripts/install.mjs --target antigravity --project /path/to/project
```

Use `--force` only when you intentionally want to overwrite existing Tanizy files in the target project.

## Manual Copy

macOS / Linux:

```bash
mkdir -p /path/to/project/.agents/skills
cp -R core/skills/* /path/to/project/.agents/skills/
cp adapters/antigravity/AGENTS.md /path/to/project/AGENTS.md
mkdir -p /path/to/project/.agents/rules
cp adapters/antigravity/.agents/rules/tanizy-po.md /path/to/project/.agents/rules/tanizy-po.md
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force C:\path\to\project\.agents\skills
Copy-Item -Recurse core/skills/* C:\path\to\project\.agents\skills\
Copy-Item adapters/antigravity/AGENTS.md C:\path\to\project\AGENTS.md
New-Item -ItemType Directory -Force C:\path\to\project\.agents\rules
Copy-Item adapters/antigravity/.agents/rules/tanizy-po.md C:\path\to\project\.agents\rules\tanizy-po.md
```

## After Install

Open the project in Antigravity. `AGENTS.md` and `.agents/rules/tanizy-po.md` provide the stable routing entrypoints. The rule points the agent to local workflow files under `.agents/skills/`.
