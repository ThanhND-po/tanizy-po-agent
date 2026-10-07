# Tanizy PO Agent

Tanizy PO Agent is a portable Product Owner (PO) and structured problem-analysis package for AI coding agents. It helps refine product ideas, write requirement artifacts, create diagrams, and facilitate 5 Whys Root Cause Analysis (RCA) through reusable skill instructions.

## Supported Tools

- Antigravity 2.0 / Antigravity IDE
- Codex
- Claude Code

## What It Supports

- Brainstorming vague product ideas into approved Feature Specifications (Feature Specs, FS).
- Understanding Lock, explicit assumptions, Non-functional Requirements (NFR), and Decision Log before writing specs.
- Writing FS from sufficiently defined context using a shared local template, and requirements such as Epic, User Story (US), Use Case (UC), Basic Design (BD), Application Programming Interface (API) Specification, Acceptance Criteria (AC), and Change Request (CR).
- User Story quality gates that require happy path, alternative/edge, and exception/negative coverage.
- Creating diagrams such as Use Case, Sequence, Business Process Model and Notation (BPMN) process flow, Activity, and State diagrams.
- Creating code-first User Interface (UI) mockups with shadcn/ui components when image-generation tools are unavailable.
- Summarizing Japanese, Vietnamese, English, or multilingual Meeting (MTG) memos for team channels.
- Facilitating structured 5 Whys Root Cause Analysis and producing stakeholder-ready RCA reports.
- Managing structured updates to requirement artifacts, specs, document statuses, and index catalogs upon receiving feedback.
- Research fallback when a requested artifact type has no local template.

## Repository Structure

```text
core/skills/              # Canonical skill source of truth
adapters/                 # Thin tool-specific entrypoints
scripts/install.mjs       # No-dependency installer
scripts/build-target-packages.mjs
                           # Generates one npm package per supported tool
tests/                    # Installer tests used by GitHub Actions, not published to npm
docs/                     # Install and manual-copy guides
dist/packages/             # Generated package output, not source-controlled
```

Do not treat copied/generated skill files inside target projects as the package source of truth. Update `core/skills/` in this repository, then synchronize the intended skills into target projects. Preserve project-owned instructions and local changes when choosing between a selective install and a scoped synchronization.

## Install via npm (Recommended)

No need to clone. Just run:

```bash
npx @thanhndpo/tanizy-po-agent --target codex --project /path/to/project
npx @thanhndpo/tanizy-po-agent --target claude-code --project /path/to/project
npx @thanhndpo/tanizy-po-agent --target antigravity --project /path/to/project
```

Preview the install first:

```bash
npx @thanhndpo/tanizy-po-agent --target codex --project /path/to/project --dry-run
```

The full installer adds one marked Tanizy PO block to `AGENTS.md` or `CLAUDE.md`. Existing project instructions and managed blocks from other packages are preserved. Re-run with `--force` to refresh only Tanizy PO-managed skills, files, and that marked block.

An unchanged adapter from an older Tanizy PO installation is migrated into the managed block automatically. If an unmarked legacy adapter also contains inseparable local changes, the installer stops before writing. Move project-owned instructions outside the PO content, then retry.

The universal package intentionally keeps one simple install flow for Business Analysts (BA) and Product Owners (PO). It selects the tool-specific destination from `--target`; it does not copy npm metadata, scripts, or documentation into the target project.

### Install One Skill

Use `--skill` to install only one skill. The commands below list the shared skills available to Codex, Claude Code, and Antigravity. Replace `codex` with another compatible target when needed.

```bash
npx @thanhndpo/tanizy-po-agent --target codex --project /path/to/project --skill artifact-update-process
npx @thanhndpo/tanizy-po-agent --target codex --project /path/to/project --skill brainstorming
npx @thanhndpo/tanizy-po-agent --target codex --project /path/to/project --skill creating-diagrams
npx @thanhndpo/tanizy-po-agent --target codex --project /path/to/project --skill five-whys-rca
npx @thanhndpo/tanizy-po-agent --target codex --project /path/to/project --skill generating-mockup
npx @thanhndpo/tanizy-po-agent --target codex --project /path/to/project --skill mtg-memos
npx @thanhndpo/tanizy-po-agent --target codex --project /path/to/project --skill shadcn-ui
npx @thanhndpo/tanizy-po-agent --target codex --project /path/to/project --skill web-design-guidelines
npx @thanhndpo/tanizy-po-agent --target codex --project /path/to/project --skill writing-requirements
```

Repeat `--skill` to select multiple skills:

```bash
npx @thanhndpo/tanizy-po-agent --target codex --project /path/to/project \
  --skill brainstorming \
  --skill writing-requirements
```

Selective installation copies the selected skills and their required dependencies. Selecting `brainstorming` also installs its required `writing-requirements` dependency, which owns the shared FS template and authoring guide. The resolved dependency is shown in the install plan. Existing dependency destinations follow the same collision and `--force` rules as explicitly selected skills; review the resolved plan before refreshing them. It does not copy or overwrite the tool adapter, such as `AGENTS.md`, `CLAUDE.md`, or Antigravity rules. Use the full install once when the target project still needs those adapter files.

## Update to Latest Version

When a new version is published, update with:

```bash
npx @thanhndpo/tanizy-po-agent@latest --target codex --project /path/to/project --force
```

Update one skill without replacing the other installed skills or adapter files:

```bash
npx @thanhndpo/tanizy-po-agent@latest --target codex --project /path/to/project --skill <skill-name> --force
```

For a selective update, `--force` cleanly replaces the selected skill folders and resolved required dependencies. It does not modify the root adapter, unrelated skills or another package's files.

## Install from Local Clone

If you cloned this repository locally:

```bash
node scripts/install.mjs --target codex --project /path/to/project
node scripts/install.mjs --target claude-code --project /path/to/project
node scripts/install.mjs --target antigravity --project /path/to/project
```

Install or update one skill from the local clone:

```bash
node scripts/install.mjs --target codex --project /path/to/project --skill artifact-update-process
node scripts/install.mjs --target codex --project /path/to/project --skill brainstorming
node scripts/install.mjs --target codex --project /path/to/project --skill creating-diagrams
node scripts/install.mjs --target codex --project /path/to/project --skill five-whys-rca
node scripts/install.mjs --target codex --project /path/to/project --skill generating-mockup
node scripts/install.mjs --target codex --project /path/to/project --skill mtg-memos
node scripts/install.mjs --target codex --project /path/to/project --skill shadcn-ui
node scripts/install.mjs --target codex --project /path/to/project --skill web-design-guidelines
node scripts/install.mjs --target codex --project /path/to/project --skill writing-requirements
```

For an update from the local clone, add `--force` to the command for the selected skill.

Preview first:

```bash
node scripts/install.mjs --target codex --project /path/to/project --dry-run
```

## Manual Copy

You can install without scripts by copying target-compatible skills and manually merging the marked PO adapter block. See the [manual-copy guide](https://github.com/ThanhND-po/tanizy-po-agent/blob/main/docs/manual-copy.md). Do not overwrite a shared root adapter with a raw file copy.

Quick summary:

```text
Codex:       shared core skills -> .agents/skills, PO block -> AGENTS.md
Claude Code: shared core skills -> .claude/skills, PO block -> CLAUDE.md
Antigravity: shared core skills -> .agents/skills, PO block -> AGENTS.md, tanizy-po.md -> .agents/rules
```

## Tool Guides

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
dist/packages/codex/
dist/packages/claude-code/
dist/packages/antigravity/
```

Each generated package contains only target-compatible skills, one tool adapter, the installer, `package.json`, `README.md`, and `LICENSE`. The generated package fixes its target, so the user can run:

```bash
npx @thanhndpo/tanizy-po-agent-codex --project /path/to/project
```

The target-specific packages support the same selective install options:

```bash
npx @thanhndpo/tanizy-po-agent-codex@latest --project /path/to/project --skill <skill-name> --force
```

Publish a generated package only after reviewing its dry-run output:

```bash
node scripts/check-published-package.mjs dist/packages/codex
npm publish dist/packages/codex --access public
```

The GitHub Actions package check validates the universal package and all generated packages. It rejects `.gitignore`, `.npmignore`, and `docs/` from published package contents.

## Maintainer Documentation

[Publish to npm](https://github.com/ThanhND-po/tanizy-po-agent/blob/main/docs/publish-npm.md) is a maintainer-only release guide. It documents this repository's package checks, target-package build flow, npm authentication and release verification. It is not required for installing or using the skills.

## Feature Spec Resources and Project Conventions

- The canonical FS template and authoring/quality guidance live in `core/skills/writing-requirements/`. `brainstorming` reads them after its discovery gates; `writing-requirements` uses them when feature context is sufficiently defined.
- Templates describe product behavior and source-backed decisions. Screen inventories, API contracts and internal implementation remain in their appropriate artifacts.
- Adapters locate project context through available entrypoints and project conventions. They do not prescribe a product folder layout, standards index path or validator command. Keep those locators in project-owned instructions outside managed blocks.
- Updating the package does not automatically migrate existing Feature Specs.

## Project and User-Level Skill Locations

The installer manages project-level destinations shown above. Adapters resolve skills from locations supplied by the runtime or installation configuration, including skills already installed at user level. They read context and save artifacts in the target project, independently of the skill installation directory.

If Tanizy skills are already available at user level, merge the relevant adapter block into each target project's instructions without copying skills again. See [manual-copy guidance](docs/manual-copy.md#already-available-user-level-skills). This installer does not provide a user-level install mode; do not pass an agent configuration directory as `--project` to simulate one.

## Important Behavior

- The agent asks in Vietnamese by default unless the project uses another language.
- The agent does not save generated artifacts until the user approves the content and confirms the path.
- Generated artifacts should be saved in the target project, not inside installed skill folders.

## PO + QC Coexistence

[Tanizy QC Agent](https://github.com/ThanhND-po/tanizy-qc-agent) is the companion Quality Control (QC) package for spec-first gap analysis, Test Viewpoints, Test Cases, automation export, execution-backed reports, and optional supporting evidence.

The packages have separate ownership boundaries:

- Tanizy PO manages only its marked block in the root adapter, its installed PO skills, and `tanizy-po.md` for Antigravity.
- Tanizy QC manages its own marked adapter block, `qc-*` skills, project-owned `qc/` artifacts, and `tanizy-qc.md` for Antigravity.
- Install order does not change the intended result. A full `--force` update must preserve project instructions and the other package's managed block.
- PO may hand off an approved spec, but QC starts only after an explicit QC request. QC treats PO and requirement artifacts as read-only source input.
- A selective PO skill update does not modify the root adapter.

Recommended handoff:

1. PO creates or updates an approved spec.
2. The user explicitly invokes QC and supplies the exact source locator and approval state.
3. QC applies its own Scope, Persist, Lock, Manual Result, Execution, and Release Verdict gates.
4. Missing business decisions return to PO or the stakeholder through the QC Gap Report and Open Questions.
5. PO Open maps to QC `OPEN`; PO Answered maps to QC `ANSWERED` until the governing source is updated; PO Deferred remains QC `OPEN` unless an authorized person explicitly accepts the documented risk; QC uses `RESOLVED` only with the exact updated source reference.

## License

MIT License. See [LICENSE](LICENSE).
