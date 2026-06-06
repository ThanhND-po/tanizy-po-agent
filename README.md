# Tanizy PO Agent

Tanizy PO Agent is a portable Gemini CLI workflow package for Product Owners. It helps refine ideas, write requirement artifacts, and create product diagrams through reusable skill instructions and slash commands.

## What It Supports

- Brainstorming vague product ideas into approved feature specs.
- Understanding Lock, explicit assumptions, non-functional requirements, and Decision Log before writing specs.
- Writing requirements such as Epic, User Story, Use Case, Basic Design, API Spec, and Non-functional Requirements.
- Creating diagrams such as Use Case, Sequence, BPMN-style process flow, Activity, and State diagrams.
- Research fallback when a requested artifact type has no local template.

## Requirements

- Gemini CLI installed and authenticated.
- A project folder where you want to use the agent.

## Install Into A Project

Copy these folders/files into the root of your target project:

```text
.gemini/
GEMINI.md
skills/
```

Then restart Gemini CLI or run:

```text
/memory refresh
/commands reload
```

## Usage

Use one of the project commands:

```text
/po:route Tôi muốn làm rõ ý tưởng về tính năng quản lý đơn hàng
/po:brainstorming Tôi muốn xây một tính năng loyalty cho khách hàng
/po:requirements Viết User Story cho luồng đăng nhập
/po:diagram Tạo sequence diagram cho luồng duyệt yêu cầu
```

## Important Behavior

- The agent asks in Vietnamese by default.
- The agent does not run version-control actions.
- The agent does not save generated artifacts until the user approves the content and confirms the path.
- Generated artifacts should be saved in the target project, not inside `skills/`.
- Gemini CLI `@path` syntax injects files or folders; it is not a skill alias. Use `/po:*` commands for routing.

## Repository Structure

```text
.gemini/commands/po/      # Gemini CLI slash commands
GEMINI.md                 # Project memory entrypoint
skills/                   # Tanizy PO workflows and templates
```

## Templates

The source of truth for requirement templates is:

```text
skills/writing-requirements/templates/
```

Current local templates include Epic, User Story, Use Case table, Use Case numbered steps, INVEST guide, and User Story quality checklist.

## License

MIT License. See [LICENSE](LICENSE).
