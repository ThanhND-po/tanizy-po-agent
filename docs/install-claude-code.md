# Install For Claude Code

## Recommended

From the `tanizy-po-agent` repository:

```bash
node scripts/install.mjs --target claude-code --project /path/to/project --dry-run
node scripts/install.mjs --target claude-code --project /path/to/project
```

Use `--force` only when you intentionally want to overwrite existing Tanizy files in the target project.

## Manual Copy

macOS / Linux:

```bash
mkdir -p /path/to/project/.claude/skills
cp -R core/skills/* /path/to/project/.claude/skills/
cp adapters/claude-code/CLAUDE.md /path/to/project/CLAUDE.md
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force C:\path\to\project\.claude\skills
Copy-Item -Recurse core/skills/* C:\path\to\project\.claude\skills\
Copy-Item adapters/claude-code/CLAUDE.md C:\path\to\project\CLAUDE.md
```

## After Install

Open Claude Code in the target project. Claude Code should discover the installed skills from `.claude/skills/`; `CLAUDE.md` provides routing guidance.
