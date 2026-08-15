# Install For Gemini CLI

## Install via npm (Recommended)

```bash
npx @thanhndpo/tanizy-po-agent --target gemini-cli --project /path/to/project --dry-run
npx @thanhndpo/tanizy-po-agent --target gemini-cli --project /path/to/project
```

Install or update only one skill:

```bash
npx @thanhndpo/tanizy-po-agent --target gemini-cli --project /path/to/project --skill mtg-memos
npx @thanhndpo/tanizy-po-agent@latest --target gemini-cli --project /path/to/project --skill mtg-memos --force
```

Repeat `--skill` to select multiple skills. A selective install changes only `skills/<skill-name>` and does not copy or overwrite `GEMINI.md`, `.gemini/`, or `.geminiignore`.

A full install adds or refreshes only the marked Tanizy PO block in `GEMINI.md`, replaces the package-owned `.gemini/commands/po` directory, and creates `.geminiignore` only when it is missing. Existing project instructions and Tanizy QC content are preserved.

## Install from Local Clone

From the `tanizy-po-agent` repository:

```bash
node scripts/install.mjs --target gemini-cli --project /path/to/project --dry-run
node scripts/install.mjs --target gemini-cli --project /path/to/project
node scripts/install.mjs --target gemini-cli --project /path/to/project --skill mtg-memos
```

Use `--force` only when you intend to refresh PO-managed skills, commands, and the PO managed block. It does not authorize replacing project-owned or QC-managed adapter content.

## Manual Copy

macOS / Linux:

```bash
cp -R core/skills /path/to/project/skills
# Merge adapters/gemini-cli/GEMINI.md into the marked PO block. Do not overwrite an existing GEMINI.md.
mkdir -p /path/to/project/.gemini/commands
cp -R adapters/gemini-cli/.gemini/commands/po /path/to/project/.gemini/commands/po
# Copy .geminiignore only when the target file does not exist.
```

Windows PowerShell:

```powershell
Copy-Item -Recurse core/skills C:\path\to\project\skills
# Merge adapters/gemini-cli/GEMINI.md into the marked PO block. Do not overwrite an existing GEMINI.md.
New-Item -ItemType Directory -Force C:\path\to\project\.gemini\commands
Copy-Item -Recurse adapters/gemini-cli/.gemini/commands/po C:\path\to\project\.gemini\commands\po
# Copy .geminiignore only when the target file does not exist.
```

## After Install

Open Gemini CLI in the target project and run:

```text
/memory refresh
/commands reload
```

Available commands:

```text
/po:route <request>
/po:brainstorming <idea>
/po:requirements <request>
/po:diagram <request>
```
