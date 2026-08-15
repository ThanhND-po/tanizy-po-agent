# Manual Copy Installation

Use this guide when you have downloaded or cloned `tanizy-po-agent` locally and want to copy files into another project without running the installer.

Replace `/path/to/project` with your target project path.

To install or update one skill manually, copy only its directory to the tool-specific skills root. For example, replace `<skills-root>` below with `skills`, `.agents/skills`, or `.claude/skills` as documented in each section:

```bash
cp -R core/skills/mtg-memos /path/to/project/<skills-root>/
```

The npm installer provides the safer cross-platform equivalent with `--skill mtg-memos`.

## Root Adapter Ownership

Do not overwrite an existing `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md`. Append the relevant adapter template inside one package-owned block:

```markdown
<!-- BEGIN TANIZY PO AGENT MANAGED BLOCK -->
[paste the target adapter template here]
<!-- END TANIZY PO AGENT MANAGED BLOCK -->
```

Keep project instructions and other package blocks outside these markers. For Codex, Claude Code, and Antigravity, do not copy the Gemini-only `using-tanizy-agent` skill.

## Gemini CLI

macOS / Linux:

```bash
cp -R core/skills /path/to/project/skills
# Merge adapters/gemini-cli/GEMINI.md into the marked PO block.
mkdir -p /path/to/project/.gemini/commands
cp -R adapters/gemini-cli/.gemini/commands/po /path/to/project/.gemini/commands/po
# Copy .geminiignore only when the target file does not exist.
```

Windows PowerShell:

```powershell
Copy-Item -Recurse core/skills C:\path\to\project\skills
# Merge adapters/gemini-cli/GEMINI.md into the marked PO block.
New-Item -ItemType Directory -Force C:\path\to\project\.gemini\commands
Copy-Item -Recurse adapters/gemini-cli/.gemini/commands/po C:\path\to\project\.gemini\commands\po
# Copy .geminiignore only when the target file does not exist.
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
cp -R core/skills/{brainstorming,creating-diagrams,generating-mockup,mtg-memos,shadcn-ui,web-design-guidelines,writing-requirements} /path/to/project/.agents/skills/
# Merge adapters/codex/AGENTS.md into the marked PO block.
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force C:\path\to\project\.agents\skills
$poSkillNames = @("brainstorming", "creating-diagrams", "generating-mockup", "mtg-memos", "shadcn-ui", "web-design-guidelines", "writing-requirements")
foreach ($poSkillName in $poSkillNames) { Copy-Item -Recurse "core/skills/$poSkillName" C:\path\to\project\.agents\skills\ }
# Merge adapters/codex/AGENTS.md into the marked PO block.
```

## Claude Code

macOS / Linux:

```bash
mkdir -p /path/to/project/.claude/skills
cp -R core/skills/{brainstorming,creating-diagrams,generating-mockup,mtg-memos,shadcn-ui,web-design-guidelines,writing-requirements} /path/to/project/.claude/skills/
# Merge adapters/claude-code/CLAUDE.md into the marked PO block.
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force C:\path\to\project\.claude\skills
$poSkillNames = @("brainstorming", "creating-diagrams", "generating-mockup", "mtg-memos", "shadcn-ui", "web-design-guidelines", "writing-requirements")
foreach ($poSkillName in $poSkillNames) { Copy-Item -Recurse "core/skills/$poSkillName" C:\path\to\project\.claude\skills\ }
# Merge adapters/claude-code/CLAUDE.md into the marked PO block.
```

## Antigravity

macOS / Linux:

```bash
mkdir -p /path/to/project/.agents/skills
cp -R core/skills/{brainstorming,creating-diagrams,generating-mockup,mtg-memos,shadcn-ui,web-design-guidelines,writing-requirements} /path/to/project/.agents/skills/
# Merge adapters/antigravity/AGENTS.md into the marked PO block.
mkdir -p /path/to/project/.agents/rules
cp adapters/antigravity/.agents/rules/tanizy-po.md /path/to/project/.agents/rules/tanizy-po.md
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force C:\path\to\project\.agents\skills
$poSkillNames = @("brainstorming", "creating-diagrams", "generating-mockup", "mtg-memos", "shadcn-ui", "web-design-guidelines", "writing-requirements")
foreach ($poSkillName in $poSkillNames) { Copy-Item -Recurse "core/skills/$poSkillName" C:\path\to\project\.agents\skills\ }
# Merge adapters/antigravity/AGENTS.md into the marked PO block.
New-Item -ItemType Directory -Force C:\path\to\project\.agents\rules
Copy-Item adapters/antigravity/.agents/rules/tanizy-po.md C:\path\to\project\.agents\rules\tanizy-po.md
```
