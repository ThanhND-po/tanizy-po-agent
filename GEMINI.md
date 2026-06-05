# Tanizy PO Agent

This project contains portable Product Owner skills for Gemini CLI.

@./skills/using-tanizy-agent/SKILL.md

## Usage

- Use `/po:route <request>` when you want the agent to choose the right PO workflow.
- Use `/po:brainstorming <idea>` to refine a vague idea before writing artifacts.
- Use `/po:requirements <request>` to create Epic, User Story, Use Case, Basic Design, API Spec, NFR, or another requirement artifact.
- Use `/po:diagram <request>` to create Use Case, Sequence, BPMN, Activity, State, or another diagram.

Gemini CLI `@path` syntax injects file or folder context. It is not a skill alias mechanism, so do not expect `@brainstorming` to route by skill name.
