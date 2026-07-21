# Tanizy PO Agent

Tanizy PO Agent is a portable Product Owner workflow package for AI coding agents. It helps refine product ideas, write requirement artifacts, and create diagrams through reusable skill instructions.

## Supported Tools

- Gemini CLI
- Antigravity 2.0 / Antigravity IDE
- Codex
- Claude Code

## What It Supports

- Brainstorming vague product ideas into approved feature specs.
- Understanding Lock, explicit assumptions, non-functional requirements, and Decision Log before writing specs.
- Writing requirements such as Epic, User Story, Use Case, Basic Design, API Spec, and Non-functional Requirements.
- User Story quality gates that require happy path, alternative/edge, and exception/negative coverage.
- Creating diagrams such as Use Case, Sequence, BPMN-style process flow, Activity, and State diagrams.
- Creating code-first UI mockups with shadcn/ui components when image-generation tools are unavailable.
- Research fallback when a requested artifact type has no local template.

## Repository Structure

```text
core/skills/              # Canonical skill source of truth
adapters/                 # Thin tool-specific entrypoints
scripts/install.mjs       # No-dependency installer
scripts/build-target-packages.mjs
                           # Generates one npm package per supported tool
docs/                     # Install and manual-copy guides
dist/packages/             # Generated package output, not source-controlled
```

Do not edit copied/generated skill files inside target projects as the source of truth. Update `core/skills/` in this repository, then reinstall into the target project.

## Install via npm (Recommended)

No need to clone. Just run:

```bash
npx @thanhndpo/tanizy-po-agent --target gemini-cli --project /path/to/project
npx @thanhndpo/tanizy-po-agent --target codex --project /path/to/project
npx @thanhndpo/tanizy-po-agent --target claude-code --project /path/to/project
npx @thanhndpo/tanizy-po-agent --target antigravity --project /path/to/project
```

Preview the install first:

```bash
npx @thanhndpo/tanizy-po-agent --target gemini-cli --project /path/to/project --dry-run
```

If destination files already exist, the installer stops. Re-run with `--force` when you intentionally want to overwrite Tanizy files in the target project.

The universal package intentionally keeps one simple install flow for BA/PO users. It selects the tool-specific destination from `--target`; it does not copy npm metadata, scripts, or documentation into the target project.

## Update to Latest Version

When a new version is published, update with:

```bash
npx @thanhndpo/tanizy-po-agent@latest --target gemini-cli --project /path/to/project --force
```

## Install from Local Clone

If you cloned this repository locally:

```bash
node scripts/install.mjs --target gemini-cli --project /path/to/project
node scripts/install.mjs --target codex --project /path/to/project
node scripts/install.mjs --target claude-code --project /path/to/project
node scripts/install.mjs --target antigravity --project /path/to/project
```

Preview first:

```bash
node scripts/install.mjs --target gemini-cli --project /path/to/project --dry-run
```

## Manual Copy

You can install without scripts by copying the relevant adapter and skill folders. See the [manual-copy guide](https://github.com/ThanhND-po/tanizy-po-agent/blob/main/docs/manual-copy.md).

Quick summary:

```text
Gemini CLI:  core/skills -> skills, adapters/gemini-cli/GEMINI.md -> GEMINI.md, adapters/gemini-cli/.gemini -> .gemini
Codex:       core/skills/* -> .agents/skills/, adapters/codex/AGENTS.md -> AGENTS.md
Claude Code: core/skills/* -> .claude/skills/, adapters/claude-code/CLAUDE.md -> CLAUDE.md
Antigravity: core/skills -> skills, adapters/antigravity/AGENTS.md -> AGENTS.md, adapters/antigravity/.agents -> .agents
```

## Tool Guides

- [Gemini CLI](https://github.com/ThanhND-po/tanizy-po-agent/blob/main/docs/install-gemini-cli.md)
- [Codex](https://github.com/ThanhND-po/tanizy-po-agent/blob/main/docs/install-codex.md)
- [Claude Code](https://github.com/ThanhND-po/tanizy-po-agent/blob/main/docs/install-claude-code.md)
- [Antigravity](https://github.com/ThanhND-po/tanizy-po-agent/blob/main/docs/install-antigravity.md)

## Build Target-Specific npm Packages

The repository keeps `core/skills/` as the single source of truth. To generate smaller packages for users who already know their tool, run:

```bash
npm run build:target-packages
```

This creates ignored build output under `dist/packages/`:

```text
dist/packages/gemini-cli/
dist/packages/codex/
dist/packages/claude-code/
dist/packages/antigravity/
```

Each generated package contains only the shared skills, one tool adapter, the installer, `package.json`, `README.md`, and `LICENSE`. The generated package fixes its target, so the user can run:

```bash
npx @thanhndpo/tanizy-po-agent-codex --project /path/to/project
```

Publish a generated package only after reviewing its dry-run output:

```bash
node scripts/check-published-package.mjs dist/packages/codex
npm publish dist/packages/codex --access public
```

The GitHub Actions package check validates the universal package and all generated packages. It rejects `.gitignore`, `.npmignore`, and `docs/` from published package contents.

## Important Behavior

- The agent asks in Vietnamese by default unless the project uses another language.
- The agent does not run version-control actions unless explicitly requested.
- The agent does not save generated artifacts until the user approves the content and confirms the path.
- Generated artifacts should be saved in the target project, not inside installed skill folders.

## License

MIT License. See [LICENSE](LICENSE).
