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

Repeat `--skill` to select multiple skills. A selective install changes only the selected skills and required dependencies under `.agents/skills/<skill-name>` and does not copy or overwrite `AGENTS.md`.

Selecting `brainstorming` or `artifact-update-process` also installs `writing-requirements`, which owns the shared Feature Specification (FS) resources and document metadata contract. Selecting `generating-mockup` also installs `web-design-guidelines`, `creating-diagrams` and `shadcn-ui` for its supported modes. The resolved dependency is shown in the install plan. Existing dependency destinations follow the same collision and `--force` rules as explicitly selected skills; review the resolved plan before refreshing them.

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

Open the project in Codex. The managed Product Owner (PO) block in `AGENTS.md` provides routing rules, and this installer places skills in `.agents/skills/`. The adapter also uses user-level skills when their locations are supplied by the runtime or installation configuration.

For skills already available at user level and project-owned configuration such as Incident Report Storage, see the [manual-copy guide](manual-copy.md#already-available-user-level-skills). This installer supports project-level destinations only.
