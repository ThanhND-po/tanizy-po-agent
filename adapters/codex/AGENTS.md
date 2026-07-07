# Tanizy PO Agent For Codex

This project uses Tanizy PO Agent skills for Product Owner workflows.

## Skill Routing

- For vague product ideas, unclear scope, or discovery work, use the `brainstorming` skill.
- For Epic, User Story, Use Case, Basic Design, API Spec, NFR, or requirement documents, use the `writing-requirements` skill.
- For Use Case Diagram, Sequence Diagram, BPMN-style flow, Activity Diagram, State Diagram, or flowcharts, use the `creating-diagrams` skill.
- For UI mockups or screen wireframes from a description or prototype, use the `generating-mockup` skill.

## Rules

- Do not skip workflow gates in the selected skill.
- Ask in Vietnamese by default unless the project uses another language.
- Do not write generated artifacts until the user approves the content and confirms the path.
- Save outputs in the target project, not inside `.agents/skills/`.
- Do not run version-control actions unless the user explicitly asks for them.

Installed skills live in `.agents/skills/`.
