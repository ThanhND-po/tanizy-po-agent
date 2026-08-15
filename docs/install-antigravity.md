# Install For Antigravity

## Install via npm (Recommended)

```bash
npx @thanhndpo/tanizy-po-agent --target antigravity --project /path/to/project --dry-run
npx @thanhndpo/tanizy-po-agent --target antigravity --project /path/to/project
```

Install or update only one skill:

```bash
npx @thanhndpo/tanizy-po-agent --target antigravity --project /path/to/project --skill mtg-memos
npx @thanhndpo/tanizy-po-agent@latest --target antigravity --project /path/to/project --skill mtg-memos --force
```

Repeat `--skill` to select multiple skills. A selective install changes only `.agents/skills/<skill-name>` and does not copy or overwrite `AGENTS.md` or `.agents/rules/`.

A full install adds or refreshes only the marked Tanizy PO block in `AGENTS.md` and the package-owned `.agents/rules/tanizy-po.md` file. Existing project instructions, Tanizy QC content, and other Antigravity rules are preserved.

## Install from Local Clone

From the `tanizy-po-agent` repository:

```bash
node scripts/install.mjs --target antigravity --project /path/to/project --dry-run
node scripts/install.mjs --target antigravity --project /path/to/project
node scripts/install.mjs --target antigravity --project /path/to/project --skill mtg-memos
```

Use `--force` only when you intend to refresh PO-managed skills, `tanizy-po.md`, and the PO managed block. It does not authorize replacing project-owned or QC-managed content.

## Manual Copy

macOS / Linux:

```bash
mkdir -p /path/to/project/.agents/skills
cp -R core/skills/{brainstorming,creating-diagrams,generating-mockup,mtg-memos,shadcn-ui,web-design-guidelines,writing-requirements} /path/to/project/.agents/skills/
# Merge adapters/antigravity/AGENTS.md into the marked PO block. Do not overwrite an existing AGENTS.md.
mkdir -p /path/to/project/.agents/rules
cp adapters/antigravity/.agents/rules/tanizy-po.md /path/to/project/.agents/rules/tanizy-po.md
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force C:\path\to\project\.agents\skills
$poSkillNames = @("brainstorming", "creating-diagrams", "generating-mockup", "mtg-memos", "shadcn-ui", "web-design-guidelines", "writing-requirements")
foreach ($poSkillName in $poSkillNames) { Copy-Item -Recurse "core/skills/$poSkillName" C:\path\to\project\.agents\skills\ }
# Merge adapters/antigravity/AGENTS.md into the marked PO block. Do not overwrite an existing AGENTS.md.
New-Item -ItemType Directory -Force C:\path\to\project\.agents\rules
Copy-Item adapters/antigravity/.agents/rules/tanizy-po.md C:\path\to\project\.agents\rules\tanizy-po.md
```

## After Install

Open the project in Antigravity. The managed PO block in `AGENTS.md` contains project-wide PO routing and writing preferences. `.agents/rules/tanizy-po.md` is a thin Antigravity-specific route to local workflows under `.agents/skills/`. `using-tanizy-agent` is Gemini-only and is not installed for Antigravity.
