# Install For Claude Code

## Install via npm (Recommended)

```bash
npx @thanhndpo/tanizy-po-agent --target claude-code --project /path/to/project --dry-run
npx @thanhndpo/tanizy-po-agent --target claude-code --project /path/to/project
```

Install or update only one skill:

```bash
npx @thanhndpo/tanizy-po-agent --target claude-code --project /path/to/project --skill mtg-memos
npx @thanhndpo/tanizy-po-agent@latest --target claude-code --project /path/to/project --skill mtg-memos --force
```

Repeat `--skill` to select multiple skills. A selective install changes only `.claude/skills/<skill-name>` and does not copy or overwrite `CLAUDE.md`.

A full install adds or refreshes only the marked Tanizy PO block in `CLAUDE.md`. Existing project instructions and Tanizy QC content are preserved.

## Install from Local Clone

From the `tanizy-po-agent` repository:

```bash
node scripts/install.mjs --target claude-code --project /path/to/project --dry-run
node scripts/install.mjs --target claude-code --project /path/to/project
node scripts/install.mjs --target claude-code --project /path/to/project --skill mtg-memos
```

Use `--force` only when you intend to refresh PO-managed skills and the PO managed block. It does not authorize replacing project-owned or QC-managed adapter content.

## Manual Copy

macOS / Linux:

```bash
mkdir -p /path/to/project/.claude/skills
cp -R core/skills/{brainstorming,creating-diagrams,generating-mockup,mtg-memos,shadcn-ui,web-design-guidelines,writing-requirements} /path/to/project/.claude/skills/
# Merge adapters/claude-code/CLAUDE.md into the marked PO block. Do not overwrite an existing CLAUDE.md.
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force C:\path\to\project\.claude\skills
$poSkillNames = @("brainstorming", "creating-diagrams", "generating-mockup", "mtg-memos", "shadcn-ui", "web-design-guidelines", "writing-requirements")
foreach ($poSkillName in $poSkillNames) { Copy-Item -Recurse "core/skills/$poSkillName" C:\path\to\project\.claude\skills\ }
# Merge adapters/claude-code/CLAUDE.md into the marked PO block. Do not overwrite an existing CLAUDE.md.
```

## After Install

Open Claude Code in the target project. Claude Code should discover the installed skills from `.claude/skills/`; the managed PO block in `CLAUDE.md` provides routing guidance. `using-tanizy-agent` is Gemini-only and is not installed for Claude Code.
