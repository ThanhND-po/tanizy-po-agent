# Install For Gemini CLI

## Install via npm (Recommended)

```bash
npx @thanhndpo/tanizy-po-agent --target gemini-cli --project /path/to/project --dry-run
npx @thanhndpo/tanizy-po-agent --target gemini-cli --project /path/to/project
```

## Install from Local Clone

From the `tanizy-po-agent` repository:

```bash
node scripts/install.mjs --target gemini-cli --project /path/to/project --dry-run
node scripts/install.mjs --target gemini-cli --project /path/to/project
```

Use `--force` only when you intentionally want to overwrite existing Tanizy files in the target project.

## Manual Copy

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
