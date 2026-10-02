# Install For Codex

## Install via npm (Recommended)

```bash
npx @thanhndpo/tanizy-po-agent --target codex --project /path/to/project --dry-run
npx @thanhndpo/tanizy-po-agent --target codex --project /path/to/project
```

Install only one skill:

```bash
npx @thanhndpo/tanizy-po-agent --target codex --project /path/to/project --skill five-whys-rca
```

Update only that skill from the latest npm release:

```bash
npx @thanhndpo/tanizy-po-agent@latest --target codex --project /path/to/project --skill five-whys-rca --force
```

Repeat `--skill` to select multiple skills. A selective install changes only `.agents/skills/<skill-name>` and does not copy or overwrite `AGENTS.md`.

A full install adds or refreshes only the marked Tanizy PO block in `AGENTS.md`. Existing project instructions and Tanizy QC content are preserved.

## Install from Local Clone

From the `tanizy-po-agent` repository:

```bash
node scripts/install.mjs --target codex --project /path/to/project --dry-run
node scripts/install.mjs --target codex --project /path/to/project
node scripts/install.mjs --target codex --project /path/to/project --skill five-whys-rca
```

Use `--force` only when you intend to refresh PO-managed skills and the PO managed block. It does not authorize replacing project-owned or QC-managed adapter content.

## Manual Copy

macOS / Linux:

```bash
mkdir -p /path/to/project/.agents/skills
cp -R core/skills/{artifact-update-process,brainstorming,creating-diagrams,five-whys-rca,generating-mockup,mtg-memos,shadcn-ui,web-design-guidelines,writing-requirements} /path/to/project/.agents/skills/
# Merge adapters/codex/AGENTS.md into the marked PO block. Do not overwrite an existing AGENTS.md.
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force C:\path\to\project\.agents\skills
$poSkillNames = @("artifact-update-process", "brainstorming", "creating-diagrams", "five-whys-rca", "generating-mockup", "mtg-memos", "shadcn-ui", "web-design-guidelines", "writing-requirements")
foreach ($poSkillName in $poSkillNames) { Copy-Item -Recurse "core/skills/$poSkillName" C:\path\to\project\.agents\skills\ }
# Merge adapters/codex/AGENTS.md into the marked PO block. Do not overwrite an existing AGENTS.md.
```

## After Install

Open the project in Codex. The managed PO block in `AGENTS.md` provides routing rules, and installed skills live in `.agents/skills/`. `using-tanizy-agent` is Gemini-only and is not installed for Codex.
