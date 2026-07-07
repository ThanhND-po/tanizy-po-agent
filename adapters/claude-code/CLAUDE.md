# Tanizy PO Agent For Claude Code

Use the installed Tanizy PO skills when the user asks for Product Owner workflows.

## Skill Routing

- Use `brainstorming` for vague ideas, scope clarification, discovery, and feature spec validation.
- Use `writing-requirements` for Epic, User Story, Use Case, Basic Design, API Spec, NFR, or requirement documents.
- Use `creating-diagrams` for Use Case Diagram, Sequence Diagram, BPMN-style flow, Activity Diagram, State Diagram, or flowcharts.
- Use `generating-mockup` for UI mockups or screen wireframes.

## Rules

- Do not bypass skill hard gates.
- Ask in Vietnamese by default unless the project uses another language.
- Do not save generated artifacts until the user approves the content and confirms the path.
- Save outputs in the target project, not inside `.claude/skills/`.
- Do not run version-control actions unless explicitly requested.

Installed skills live in `.claude/skills/`.
