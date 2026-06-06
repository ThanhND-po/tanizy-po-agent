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
- Research fallback when a requested artifact type has no local template.

## Repository Structure

```text
core/skills/              # Canonical skill source of truth
adapters/                 # Thin tool-specific entrypoints
scripts/install.mjs       # No-dependency installer
docs/                     # Install and manual-copy guides
```

Do not edit copied/generated skill files inside target projects as the source of truth. Update `core/skills/` in this repository, then reinstall into the target project.

## Requirements

- Node.js for the installer.
- No npm dependencies are required.
- Manual copy works without Node.js.

## Recommended Install

From this repository:

```bash
node scripts/install.mjs --target gemini-cli --project /path/to/project
node scripts/install.mjs --target codex --project /path/to/project
node scripts/install.mjs --target claude-code --project /path/to/project
node scripts/install.mjs --target antigravity --project /path/to/project
```

Preview the install first:

```bash
node scripts/install.mjs --target gemini-cli --project /path/to/project --dry-run
```

If destination files already exist, the installer stops. Re-run with `--force` when you intentionally want to overwrite Tanizy files in the target project.

## Manual Copy

You can install without scripts by copying the relevant adapter and skill folders. See [docs/manual-copy.md](docs/manual-copy.md).

Quick summary:

```text
Gemini CLI:  core/skills -> skills, adapters/gemini-cli/GEMINI.md -> GEMINI.md, adapters/gemini-cli/.gemini -> .gemini
Codex:       core/skills/* -> .agents/skills/, adapters/codex/AGENTS.md -> AGENTS.md
Claude Code: core/skills/* -> .claude/skills/, adapters/claude-code/CLAUDE.md -> CLAUDE.md
Antigravity: core/skills -> skills, adapters/antigravity/AGENTS.md -> AGENTS.md, adapters/antigravity/.agents -> .agents
```

## Tool Guides

- [Gemini CLI](docs/install-gemini-cli.md)
- [Codex](docs/install-codex.md)
- [Claude Code](docs/install-claude-code.md)
- [Antigravity](docs/install-antigravity.md)

## Important Behavior

- The agent asks in Vietnamese by default unless the project uses another language.
- The agent does not run version-control actions unless explicitly requested.
- The agent does not save generated artifacts until the user approves the content and confirms the path.
- Generated artifacts should be saved in the target project, not inside installed skill folders.

## License

MIT License. See [LICENSE](LICENSE).
