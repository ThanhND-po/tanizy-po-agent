---
name: writing-requirements
description: Use when a Product Owner needs formal requirement artifacts such as Epic, User Story, Use Case, Basic Design, API Spec, NFR, or related documentation from a spec or business request.
---

# Writing Requirements

Transform a feature spec or business request into formal requirement artifacts.

## Hard Gates

- Do not show a requirement artifact until the relevant template or research fallback has been applied.
- For User Stories, apply `templates/user-story-invest.md` and pass the **User Story Quality Gate** below before showing the result.
- Do not write a file until the user approves the artifact and confirms the output path.
- Do not run version-control actions.

## User Story Quality Gate

A User Story fails quality gate if any condition below is true. If it fails, refine it silently and run the gate again until it passes.

- Story statement has a generic persona, unclear goal, repeated value, or multiple unrelated goals.
- Acceptance Criteria do not include happy path behavior.
- Acceptance Criteria do not include alternative or edge behavior, unless explicitly marked `N/A` with a reason.
- Acceptance Criteria do not include exception or negative behavior, unless explicitly marked `N/A` with a reason.
- Usage Scenarios do not include Happy Path, Alternative/Edge, and Exception/Negative scenarios.
- Any Acceptance Criterion is vague, untestable, or combines multiple behaviors.
- Unknown business rules are invented instead of listed as open questions.
- **[Negotiable]** Any section of the artifact — including story statement, Acceptance Criteria, and Scenarios — contains implementation-binding technical terms. Implementation-binding terms include, but are not limited to:
  - UI component names: `Combobox`, `Dropdown`, `Modal`, `Checkbox`, `RadioButton`, `DataGrid`, specific icon names, etc.
  - Cloud or infrastructure services: `AWS Lambda`, `S3`, `Firebase`, `Kafka`, `Redis`, etc.
  - Framework or library names: `React`, `Vue`, `Spring Boot`, `FastAPI`, etc.
  - Database technology or schema details: `PostgreSQL`, `MongoDB`, table names, column names, etc.
  - Specific API endpoints, HTTP methods, or protocol constraints unless the story is explicitly about an API contract.
  - When such terms appear in user input context, rephrase them as behavior or capability descriptions (e.g., `select from a list` instead of `use a Combobox`; `serverless processing` instead of `AWS Lambda`).

Use `templates/user-story-quality-checklist.md` as the detailed review reference when the gate is hard to evaluate.

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
   - Keep requirements implementation-neutral unless the artifact type requires technical detail. This applies to every section: story statement, Acceptance Criteria, and Scenarios. If the user mentioned specific UI components, services, or frameworks during discussion, convert them to behavior or capability descriptions in the artifact.
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
- Validate with the User Story Quality Gate.
- Use `templates/user-story-quality-checklist.md` for detailed self-review when needed.
- Fix gate or checklist issues silently before showing the output.

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
