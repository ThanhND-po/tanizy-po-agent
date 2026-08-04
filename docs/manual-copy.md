# Manual Copy Installation

Use this guide when you have downloaded or cloned `tanizy-po-agent` locally and want to copy files into another project without running the installer.

Replace `/path/to/project` with your target project path.

To install or update one skill manually, copy only its directory to the tool-specific skills root. For example, replace `<skills-root>` below with `skills`, `.agents/skills`, or `.claude/skills` as documented in each section:

```bash
cp -R core/skills/mtg-memos /path/to/project/<skills-root>/
```

The npm installer provides the safer cross-platform equivalent with `--skill mtg-memos`.

## Gemini CLI

macOS / Linux:

```bash
cp -R core/skills /path/to/project/skills
cp adapters/gemini-cli/GEMINI.md /path/to/project/GEMINI.md
cp -R adapters/gemini-cli/.gemini /path/to/project/.gemini
cp adapters/gemini-cli/.geminiignore /path/to/project/.geminiignore
```

Windows PowerShell:

```powershell
Copy-Item -Recurse core/skills C:\path\to\project\skills
Copy-Item adapters/gemini-cli/GEMINI.md C:\path\to\project\GEMINI.md
Copy-Item -Recurse adapters/gemini-cli/.gemini C:\path\to\project\.gemini
Copy-Item adapters/gemini-cli/.geminiignore C:\path\to\project\.geminiignore
```

After copying, run in Gemini CLI:

```text
/memory refresh
/commands reload
```

## Codex

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

## Claude Code

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

## Antigravity

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
