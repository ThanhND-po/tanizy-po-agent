# Manual Copy Installation

Use this guide when you have downloaded or cloned `tanizy-po-agent` locally and want to copy files into another project without running the installer.

Replace `/path/to/project` with your target project path.

To install or update one skill manually, copy only its directory to the tool-specific skills root. For example, replace `<skills-root>` below with `.agents/skills` or `.claude/skills` as documented in each section:

```bash
cp -R core/skills/five-whys-rca /path/to/project/<skills-root>/
```

The npm installer provides the safer cross-platform equivalent with `--skill five-whys-rca`.

When copying `brainstorming`, also copy `writing-requirements` to the same tool-specific skills root. It owns the canonical Feature Specification (FS) template and authoring guide referenced by brainstorming. The npm installer resolves this required dependency automatically.

## Root Adapter Ownership

Do not overwrite an existing `AGENTS.md` or `CLAUDE.md`. Append the relevant adapter template inside one package-owned block:

```markdown
<!-- BEGIN TANIZY PO AGENT MANAGED BLOCK -->
[paste the target adapter template here]
<!-- END TANIZY PO AGENT MANAGED BLOCK -->
```

Keep project instructions and other package blocks outside these markers.

## Already Available User-Level Skills

If the runtime already provides Tanizy skills at user level, merge the matching adapter block into each target project's instructions without copying skills again. For Antigravity, also merge the package-owned `tanizy-po.md` rule while preserving other rules.

Use skill locations supplied by the runtime or installation configuration. Keep project context and artifact paths relative to the target project; resolve templates and references from the loaded skill's location. Ensure required dependencies such as `writing-requirements` are also available. If a skill location is missing or ambiguous, supply it explicitly instead of searching the entire home directory.

The npm installer remains a project-level installer. Passing an agent configuration directory as `--project` does not establish a supported user-level installation.

## Project-Owned Configuration

Keep project standards, validator commands, naming rules, and output paths outside the Tanizy managed block.

For Incident Reports, projects may declare a default folder in their own instructions:

```markdown
## Incident Report Storage

- Default output path: `<path/to/incident-reports>`
```

Replace the placeholder with a project-relative path. The `five-whys-rca` skill confirms the resolved path before scanning the folder, allocating an Incident ID, creating a directory, or saving a report.

## Codex

macOS / Linux:

```bash
mkdir -p /path/to/project/.agents/skills
cp -R core/skills/{artifact-update-process,brainstorming,creating-diagrams,five-whys-rca,generating-mockup,mtg-memos,shadcn-ui,web-design-guidelines,writing-requirements} /path/to/project/.agents/skills/
# Merge adapters/codex/AGENTS.md into the marked PO block.
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force C:\path\to\project\.agents\skills
$poSkillNames = @("artifact-update-process", "brainstorming", "creating-diagrams", "five-whys-rca", "generating-mockup", "mtg-memos", "shadcn-ui", "web-design-guidelines", "writing-requirements")
foreach ($poSkillName in $poSkillNames) { Copy-Item -Recurse "core/skills/$poSkillName" C:\path\to\project\.agents\skills\ }
# Merge adapters/codex/AGENTS.md into the marked PO block.
```

## Claude Code

macOS / Linux:

```bash
mkdir -p /path/to/project/.claude/skills
cp -R core/skills/{artifact-update-process,brainstorming,creating-diagrams,five-whys-rca,generating-mockup,mtg-memos,shadcn-ui,web-design-guidelines,writing-requirements} /path/to/project/.claude/skills/
# Merge adapters/claude-code/CLAUDE.md into the marked PO block.
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force C:\path\to\project\.claude\skills
$poSkillNames = @("artifact-update-process", "brainstorming", "creating-diagrams", "five-whys-rca", "generating-mockup", "mtg-memos", "shadcn-ui", "web-design-guidelines", "writing-requirements")
foreach ($poSkillName in $poSkillNames) { Copy-Item -Recurse "core/skills/$poSkillName" C:\path\to\project\.claude\skills\ }
# Merge adapters/claude-code/CLAUDE.md into the marked PO block.
```

## Antigravity

macOS / Linux:

```bash
mkdir -p /path/to/project/.agents/skills
cp -R core/skills/{artifact-update-process,brainstorming,creating-diagrams,five-whys-rca,generating-mockup,mtg-memos,shadcn-ui,web-design-guidelines,writing-requirements} /path/to/project/.agents/skills/
# Merge adapters/antigravity/AGENTS.md into the marked PO block.
mkdir -p /path/to/project/.agents/rules
cp adapters/antigravity/.agents/rules/tanizy-po.md /path/to/project/.agents/rules/tanizy-po.md
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force C:\path\to\project\.agents\skills
$poSkillNames = @("artifact-update-process", "brainstorming", "creating-diagrams", "five-whys-rca", "generating-mockup", "mtg-memos", "shadcn-ui", "web-design-guidelines", "writing-requirements")
foreach ($poSkillName in $poSkillNames) { Copy-Item -Recurse "core/skills/$poSkillName" C:\path\to\project\.agents\skills\ }
# Merge adapters/antigravity/AGENTS.md into the marked PO block.
New-Item -ItemType Directory -Force C:\path\to\project\.agents\rules
Copy-Item adapters/antigravity/.agents/rules/tanizy-po.md C:\path\to\project\.agents\rules\tanizy-po.md
```
