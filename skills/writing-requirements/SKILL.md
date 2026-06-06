---
name: writing-requirements
description: Use when a Product Owner needs formal requirement artifacts such as Epic, User Story, Use Case, Basic Design, API Spec, NFR, or related documentation from a spec or business request.
---

# Writing Requirements

Transform a feature spec or business request into formal requirement artifacts.

## Hard Gates

- Do not show a requirement artifact until the relevant template or research fallback has been applied.
- For User Stories, apply `templates/user-story-invest.md` and pass `templates/user-story-quality-checklist.md` before showing the result. If the checklist fails, refine the story and run the checklist again until it passes.
- Do not write a file until the user approves the artifact and confirms the output path.
- Do not run version-control actions.

## Workflow

1. **Gather context**
   - Read existing specs, epics, user stories, use cases, diagrams, business rules, and project docs that relate to the request.
   - If context is insufficient, ask one clarifying question at a time.
   - Before drafting, understand the feature, primary actor, expected business value, and key constraints.

2. **Choose artifact type**
   - If the user has not specified a type, ask which artifact to create:
     - Epic
     - User Story
     - Use Case
     - Basic Design
     - API Spec
     - Non-functional Requirement
     - Other
   - The user may choose multiple types; create them in a logical order.

3. **Use local template when available**
   - Epic: `templates/epic.md`
   - User Story: `templates/user-story.md`
   - Use Case table: `templates/use-case-table.md`
   - Use Case numbered steps: `templates/use-case-numbered-step.md`
   - User Story INVEST guide: `templates/user-story-invest.md`
   - User Story checklist: `templates/user-story-quality-checklist.md`

4. **Research fallback when no local template exists**
   - For Basic Design, API Spec, NFR, or any unsupported artifact, research current common industry structure before drafting when web access is available.
   - Prefer primary or authoritative sources such as official standard bodies, major platform documentation, or widely adopted methodology references.
   - Cite sources when the environment supports citations.
   - State assumptions and the chosen structure before or alongside the artifact.
   - If web access is unavailable, say that current-source verification was not possible and proceed with a conservative standard structure based on available context.

5. **Draft and review**
   - Fill all meaningful sections.
   - Do not invent unknown business rules; list them as open questions when needed.
   - Keep requirements implementation-neutral unless the artifact type requires technical detail.
   - Remove accidental placeholders before showing the user.

6. **Approval and save**
   - Present the artifact and ask for approval or revisions.
   - After approval, ask where to save it.
   - Suggested folders:
     - `docs/requirements/`
     - `docs/specs/`
     - `docs/design/`
   - Save only to the user-approved target project path.

7. **Next step**
   - Ask whether the user wants a diagram, another requirement artifact, or to stop.
   - Do not automatically invoke another workflow.

## Type-Specific Rules

### Epic

- Describe the product outcome and business value.
- Break into logically derived user stories only when supported by context.
- Mark unknown dependencies or risks as open questions, not fake certainty.

### User Story

- Read `templates/user-story-invest.md`.
- Draft using `templates/user-story.md`.
- Validate with `templates/user-story-quality-checklist.md`.
- Fix checklist issues silently before showing the output.

### Use Case

- Ask the user to choose table format, numbered-step format, or both.
- Use the matching local template.
- Include primary flow, alternate flows, exception flows, preconditions, postconditions, and business rules when relevant.

### Basic Design

- Use research fallback unless a project-specific template exists.
- Cover purpose, scope, component responsibilities, data/interface touchpoints, behavior, error handling, and traceability to requirements.

### API Spec

- Use research fallback unless a project-specific template exists.
- Cover endpoints or operations, request/response schemas, status/error handling, authentication/authorization, validation, examples, and compatibility notes.

### Non-functional Requirement

- Use research fallback unless a project-specific template exists.
- Cover measurable quality attributes such as performance, availability, security, privacy, auditability, scalability, accessibility, localization, maintainability, and observability as relevant.
