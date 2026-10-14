---
name: writing-requirements
description: Use when a Product Owner needs formal requirement artifacts such as Feature Spec, Epic, User Story, Use Case, Basic Design, API Spec, NFR, or related documentation from a spec or business request.
---

# Writing Requirements

Create Feature Specs from sufficiently defined context and derive formal requirement artifacts from approved specs or business requests.

## Hard Gates

- Do not show a requirement artifact until the relevant template or research fallback has been applied.
- For Feature Specs, read `templates/feature-spec.md` and `references/feature-spec-authoring.md`, then apply its quality gate before showing the final draft.
- For User Stories, apply `templates/user-story-invest.md` and pass the **User Story Quality Gate** below before showing the result.
- Save only within the user-approved content, scope and output paths. Reuse existing approval for that same write set; obtain any missing approval before saving.
- For Basic Design, use Local Markdown mode by default. Do not convert, upload, or sync the artifact to a spreadsheet unless the user explicitly requests or confirms it.
- For Basic Design tables, keep each UI element in one physical row. Do not use HTML line-break tags or literal line breaks inside cells; use the structured-rule separators in `references/basic-design-authoring.md`.

## Document Metadata Quality Gate

Read [Document Metadata Contract](references/document-metadata.md) and the target project policy before assigning or changing metadata. Apply the contract to every supported artifact, including standalone Use Cases, and run the project metadata/template validator after saving.

## User Story Quality Gate

A User Story fails quality gate if any condition below is true. If it fails, refine it silently and run the gate again until it passes.

- **[Single-Persona]** Every Acceptance Criterion and Scenario must describe behavior observable from the persona named in the Story Statement. If an AC or Scenario describes behavior of a different persona, it must be split into a separate User Story or moved into `Given` (precondition) context.
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

## Estimation Quality Gate

An estimation fails the quality gate if any condition below is true. If it fails, re-evaluate it silently and run the gate again until it passes.

- **[Scale Mismatch]** A User Story uses T-shirt sizing instead of Story Points, or a Change Request/Epic uses Story Points instead of T-shirt sizing.
- **[Over-sizing]** A User Story is estimated at ≥ 13 SP without being flagged for breakdown, or a Change Request/Epic is estimated at XXL without being flagged for breakdown.
- **[Missing Context]** The estimation does not account for complexity, effort, and uncertainty (for User Stories), or overall scope impact (for Epics/CRs).
- **[Total Mismatch]** When breaking down an Epic/CR into User Stories, the total Story Points of child stories significantly exceeds the expected range of the parent T-shirt size (e.g., Parent is `S` but total child SP is `13`) without a re-estimation or scope adjustment.

## Workflow

1. **Gather context**
   - Read the target project instructions and available documentation entrypoints; follow project-defined links to applicable standards and related artifacts without assuming a fixed folder layout.
   - Read existing specs, epics, user stories, use cases, diagrams, business rules, and project docs that relate to the request.
   - If context is insufficient, ask one clarifying question at a time.
   - Before drafting, understand the feature, primary actor, expected business value, and key constraints.

2. **Choose artifact type**
   - If the user has not specified a type, ask which artifact to create:
     - Feature Spec
     - Epic
     - Change Request
     - User Story
     - Use Case
     - Basic Design
     - API Spec
     - Non-functional Requirement
     - Other
   - The user may choose multiple types; create them in a logical order.

3. **Choose the Basic Design delivery mode**
   - Use **Local Markdown mode** by default when the user does not mention a spreadsheet. Do not interrupt the workflow to ask about spreadsheet delivery.
   - Use **Spreadsheet-ready mode** only when the user explicitly asks to manage or share the Basic Design through a spreadsheet.
   - If the user mentions team sharing, spreadsheet management, or conversion but the intended output is unclear, ask one targeted question: `Should this Basic Design remain a local Markdown artifact, or should it also be prepared for spreadsheet management?`
   - Treat spreadsheet conversion as a separate delivery step. Preserve the approved content, business rules, and canonical single-line table-cell formatting.
   - Do not upload or sync to a spreadsheet until the user confirms the destination and requested write scope.

4. **Use local template when available**
   - Feature Spec: `templates/feature-spec.md` and `references/feature-spec-authoring.md`
   - Epic: `templates/epic.md`
   - Change Request: `templates/change-request.md`
   - User Story: `templates/user-story.md`
   - Use Case table: `templates/use-case-table.md`
   - Use Case numbered steps: `templates/use-case-numbered-step.md`
   - User Story INVEST guide: `templates/user-story-invest.md`
   - User Story checklist: `templates/user-story-quality-checklist.md`
   - Basic Design: `templates/basic-design.md`
   - API Spec: `templates/api-spec.md`
   - Non-functional Requirement: `templates/nfr.md`
   - Estimation guide: `templates/estimation-guide.md`

5. **Research fallback when no local template exists**
   - For any unsupported artifact, research current common industry structure before drafting when web access is available.
   - Prefer primary or authoritative sources such as official standard bodies, major platform documentation, or widely adopted methodology references.
   - Cite sources when the environment supports citations.
   - State assumptions and the chosen structure before or alongside the artifact.
   - If web access is unavailable, say that current-source verification was not possible and proceed with a conservative standard structure based on available context.

6. **Draft**
   - Fill all meaningful sections.
   - Do not invent unknown business rules; list them as open questions when needed.
   - Keep requirements implementation-neutral unless the artifact type requires technical detail. This applies to every section: story statement, Acceptance Criteria, and Scenarios. If the user mentioned specific UI components, services, or frameworks during discussion, convert them to behavior or capability descriptions in the artifact.
   - Remove accidental placeholders before proceeding.

7. **Run Quality Gate Checklist (for User Stories)**
   - Open `templates/user-story-quality-checklist.md` and evaluate each item against the draft.
   - Record the result of each checklist item (`[x]` pass / `[ ]` fail) in a scratchpad or internal note — this is the **evidence** that the gate was executed.
   - If any item fails, fix the draft silently and re-run the checklist until all items pass.
   - Do NOT show the User Story to the user until the checklist is fully passed.

8. **Approval and save**
   - Present the artifact for review. Reuse approval and target paths already supplied for the same content and scope; ask only for missing approval or an unresolved destination.
   - Apply the filename prefix for the selected artifact type and propose an English lowercase kebab-case descriptive filename.
   - Keep the business ID in frontmatter and content, not in the filename.
   - Use the owning module folder defined by the project structure, such as `requirements/`, `designs/`, `epics/`, `feature-specs/` or `api-specs/`.
   - Save only to the user-approved target project path.
   - Run the project Markdown validator (if it exists) after saving.

9. **Next step**
   - Ask whether the user wants a diagram, another requirement artifact, or to stop.
   - Do not automatically invoke another workflow.

## Artifact Filename Quality Gate

Use the naming convention from the project `README.md` (if it exists), or from the table below:

| Artifact type | Filename format |
|---|---|
| User Story or Requirement | `req-<descriptive-name>.md` |
| Basic Design | `bd-<descriptive-name>.md` |
| Change Request | `cr-<year>-<descriptive-name>.md` |
| Epic | `epic-<descriptive-name>.md` |
| Feature Spec | `fs-<descriptive-name>.md` |
| API Spec | `api-<descriptive-name>.md` |
| Non-functional Requirement | `nfr-<descriptive-name>.md` |

An artifact filename fails the gate if any condition below is true:

- The prefix does not match the artifact type.
- The descriptive name is not English lowercase kebab-case.
- The filename contains the business ID, module code or sequence.
- The descriptive name does not identify the primary capability, screen or business change.
- The descriptive name repeats the artifact prefix or uses a generic name such as `document`, `requirement`, `screen` or `new-file`.
- The filename conflicts with an existing file in the target directory.
- A customer-facing product label required for tracking has been translated or replaced, for example `Ikura`.

Business IDs such as `REQ-ATT-001`, `BD-ATT-D01` and `CR-2026-001` remain in frontmatter, H1, Metadata and index labels. They do not determine the filename.

## Type-Specific Rules

### Feature Spec

- Use this workflow when the feature context is sufficiently defined or already approved. Reuse existing explicit decisions; do not repeat discovery merely to populate a template.
- If material product intent or scope remains unclear, clarify it through `brainstorming` when available before finalizing the affected FS content.
- Read `templates/feature-spec.md` and `references/feature-spec-authoring.md`; use the local structure rather than research fallback.
- Apply the Feature Spec quality gate in the authoring reference. Keep unresolved source-dependent behavior visible as Open Questions.
- Keep product behavior in FS; reference screen inventories, API contracts and internal implementation in the appropriate artifacts.
- Preserve approved existing FS content and structure during a scoped update unless restructuring is requested.

### Epic

- Describe the product outcome and business value.
- Break into logically derived user stories only when supported by context.
- Mark unknown dependencies or risks as open questions, not fake certainty.
- **Estimation**: Use T-shirt sizing (XS/S/M/L/XL/XXL). Refer to `templates/estimation-guide.md` Section 3 for definitions.

### Change Request

- Read `templates/change-request.md`.
- A Change Request describes a scope-bounded change to an existing system (enhancement, bug fix, regulatory, or process change).
- Include Impact Analysis covering affected systems, modules, teams, data, and users.
- **Estimation**: Use T-shirt sizing (XS/S/M/L/XL/XXL). Refer to `templates/estimation-guide.md` Section 3 for definitions.
- Link downstream Epics or User Stories in the Requirements Changes section.
- Do not invent impact assessments; list unknowns as open questions.

### User Story

- Read `templates/user-story-invest.md`.
- Draft using `templates/user-story.md`.
- Validate with the User Story Quality Gate.
- Use `templates/user-story-quality-checklist.md` for detailed self-review when needed.
- Fix gate or checklist issues silently before showing the output.
- **Estimation**: Use Story Points (Fibonacci: 1/2/3/5/8/13). Refer to `templates/estimation-guide.md` Section 2 for definitions and Section 5 for reference stories.

### Use Case

- Ask the user to choose table format, numbered-step format, or both.
- Use the matching local template.
- Include primary flow, alternate flows, exception flows, preconditions, postconditions, and business rules when relevant.

### Basic Design

Read [Basic Design authoring](references/basic-design-authoring.md) and `templates/basic-design.md` only for this artifact type. They define screen scope, IDs, inventory fields and review rules. Reuse the user's chosen language and project ID convention; ask only when unresolved.

### API Spec

- Read `templates/api-spec.md` and `references/api-nfr-authoring.md`.
- Treat the Markdown tables as the primary review contract. Keep every operation, field, rule, response, and error easy to scan in tables.
- Use OpenAPI YAML only as a supplementary appendix for developer design and tooling. Do not replace table content with YAML.
- Follow the project-supported OpenAPI version. If none is defined, state the chosen version as an assumption.
- Keep the operation summary and detailed operation sections synchronized.
- Document authentication, authorization, validation, idempotency, pagination/filtering, status and error semantics, compatibility, and examples when relevant.
- Do not include real credentials, tokens, secrets, personal data, or production-only values in examples.
- If tables and the OpenAPI appendix conflict, flag the conflict as an open question instead of silently choosing one.

### Non-functional Requirement

- Read `templates/nfr.md` and `references/api-nfr-authoring.md`.
- Organize requirements by category and maintain a scannable catalog with at least: ID, Category, Item, Description, Target or Threshold, Priority, Implementation Status, known Approval Status, Verification, Verification Result, and Source.
- Use the project's category taxonomy when one exists. Otherwise use ISO/IEC 25010:2023 as the baseline and add clearly labeled project-specific categories only when needed.
- Treat an NFR spec as the detailed source for quality concerns mentioned in a Feature Spec. Trace each source statement to an NFR ID and elaborate its scope, measurable target, verification method, and ownership.
- Do not invent targets or service levels. Use `TBD` and add an open question when the Feature Spec or stakeholder input is not measurable enough.
- Keep Priority, Implementation Status, Approval Status, and Verification Result as separate concepts; use the project delivery policy for implementation tracking.
- Include only relevant categories. Mark a category `Not Applicable` with a reason when its omission could create material risk.
- Reject vague requirements such as `fast`, `secure`, `scalable`, or `user-friendly` unless they are converted into measurable and verifiable statements.
