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
   - Read existing specs, epics, user stories, use cases, diagrams, business rules, and project docs that relate to the request.
   - If context is insufficient, ask one clarifying question at a time.
   - Before drafting, understand the feature, primary actor, expected business value, and key constraints.

2. **Choose artifact type**
   - If the user has not specified a type, ask which artifact to create:
     - Epic
     - Change Request
     - User Story
     - Use Case
     - Basic Design
     - API Spec
     - Non-functional Requirement
     - Other
   - The user may choose multiple types; create them in a logical order.

3. **Use local template when available**
   - Epic: `templates/epic.md`
   - Change Request: `templates/change-request.md`
   - User Story: `templates/user-story.md`
   - Use Case table: `templates/use-case-table.md`
   - Use Case numbered steps: `templates/use-case-numbered-step.md`
   - User Story INVEST guide: `templates/user-story-invest.md`
   - User Story checklist: `templates/user-story-quality-checklist.md`
   - Basic Design: `templates/basic-design.md`
   - Estimation guide: `templates/estimation-guide.md`

4. **Research fallback when no local template exists**
   - For Basic Design, API Spec, NFR, or any unsupported artifact, research current common industry structure before drafting when web access is available.
   - Prefer primary or authoritative sources such as official standard bodies, major platform documentation, or widely adopted methodology references.
   - Cite sources when the environment supports citations.
   - State assumptions and the chosen structure before or alongside the artifact.
   - If web access is unavailable, say that current-source verification was not possible and proceed with a conservative standard structure based on available context.

5. **Draft**
   - Fill all meaningful sections.
   - Do not invent unknown business rules; list them as open questions when needed.
   - Keep requirements implementation-neutral unless the artifact type requires technical detail. This applies to every section: story statement, Acceptance Criteria, and Scenarios. If the user mentioned specific UI components, services, or frameworks during discussion, convert them to behavior or capability descriptions in the artifact.
   - Remove accidental placeholders before proceeding.

6. **Run Quality Gate Checklist (for User Stories)**
   - Open `templates/user-story-quality-checklist.md` and evaluate each item against the draft.
   - Record the result of each checklist item (`[x]` pass / `[ ]` fail) in a scratchpad or internal note — this is the **evidence** that the gate was executed.
   - If any item fails, fix the draft silently and re-run the checklist until all items pass.
   - Do NOT show the User Story to the user until the checklist is fully passed.

7. **Approval and save**
   - Present the artifact and ask for approval or revisions.
   - After approval, ask where to save it.
   - Suggested folders:
     - `docs/requirements/`
     - `docs/specs/`
     - `docs/design/`
   - Save only to the user-approved target project path.

8. **Next step**
   - Ask whether the user wants a diagram, another requirement artifact, or to stop.
   - Do not automatically invoke another workflow.

## Type-Specific Rules

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

A Basic Design document describes a **single screen** from the user and business perspective (外部設計 — external design). It is the handoff artifact from BA to Developer and QA. It does **not** cover database schema, API internals, or class structure — those belong to Detail Design.

**Scope of one Basic Design file = one screen or one closely related screen group.**

#### Workflow

1. **Ask for the output language** at the start: English (default), Japanese, or Vietnamese. Use the chosen language for all human-readable content in the output file. Keep column headers in English for consistency.

2. **Read `templates/basic-design.md`** before drafting.

3. **Fill Section 1 — Metadata**
3. **Fill Section 1 — Metadata**
   - Assign a Screen ID using the format `BD-[MODULE]-[TYPE][SEQ]`, where:
     - `[MODULE]` = short module/feature code in UPPERCASE (e.g. `AUTH`, `STL`, `ORD`)
     - `[TYPE]` = single letter identifying the screen type:

       | Letter | Screen Type | Example |
       |---|---|---|
       | `L` | List / Search results | `BD-STL-L01` |
       | `D` | Detail / View | `BD-STL-D01` |
       | `C` | Create / New | `BD-STL-C01` |
       | `E` | Edit / Update | `BD-STL-E01` |
       | `X` | Delete confirmation | `BD-STL-X01` |
       | `W` | Wizard / Multi-step flow | `BD-STL-W01` |
       | `P` | Preview / Read-only variant | `BD-STL-P01` |
       | `S` | Settings / Configuration | `BD-STL-S01` |
       | `O` | Other / Unclassified | `BD-STL-O01` |

     - `[SEQ]` = 2-digit sequence within the same module+type (01, 02 …)
     - **Modals and child overlays** append `-M[n]` to their parent screen ID, e.g. `BD-STL-L01-M1`, `BD-STL-L01-M2`. Modal IDs do not have their own top-level entry.
   - Ask the user for the related ticket or User Story ID if not already known.

4. **Fill Section 2 — Specs Overview**
   - Answer all three questions: purpose/business goal, what the user can do, how the user reaches this screen.
   - Do not invent facts; list unknowns as open questions.

5. **Fill Section 3 — Screen Image**
   - Ask the user if a wireframe, mockup, screen flow, or prototype is available.
   - If yes: insert the link or embed the file reference.
   - If no: leave the table cells blank. Do not fabricate a placeholder image or ASCII diagram.

6. **Fill Section 4 — Screen Inventory & Element Specs**
   - List every visible UI element on the screen.
   - Use hierarchical numbering: top-level items are `1, 2, 3 …`; child elements of a container (e.g. columns in a table, fields in a card) are `1.1, 1.2, 3.1 …`
   - For each element, fill all columns: Item Name, Classification, Required, Max Length, I/O, Data Type, Input Constraint, Initial State, Remarks.
   - Allowed Classification values: `label`, `text`, `textarea`, `dropdown`, `combobox`, `checkbox`, `radio`, `button`, `table`, `badge`, `icon`, `link`, `image`, `date-picker`, `toggle`, `tab`, `modal`, `card`, `section-header`.
   - Classification names are UI-component terms and are **allowed** in this artifact type because they describe the external interface, not the internal implementation.
   - Required: `Yes` / `No` / `N/A` (use N/A for outputs and non-form elements).
   - Max Length: number of characters for text inputs; `—` for outputs and non-text elements.
   - I/O: `Input` (user enters data), `Output` (system displays data), `Both` (editable pre-filled field), `Action` (button/link that triggers a behaviour).
   - Initial State: the value or visual state when the screen first loads — e.g. `Blank`, `Today's date`, a specific default, `Disabled`, `Active`.
   - Remarks: business rules, validation logic, conditional behaviour (show/hide/enable/disable conditions), trigger actions, cross-field dependencies.
   - **Formatting:** For `Initial State` and `Remarks`, or any complex descriptions, always use `<br>` tags to explicitly break lines for readability. Use bullet points (`-`) for complex conditions or role-based descriptions instead of running them together with spaces and bold text (e.g., use `<br>- **Admin**: ...<br>- **User**: ...`).
   - Do not invent business rules; record unknowns in Section 5 — Open Questions.

7. **Fill Section 5 — Open Questions**
   - List any ambiguous requirements, missing specs, or stakeholder decisions needed before implementation.

8. **Quality check before showing the output**
   - Every element in Section 4 has a Classification, Required, I/O, and Initial State filled in.
   - No business rule has been invented; all unknowns are in Open Questions.
   - Section 2 answers all three overview questions.
   - No Detail Design content (DB schema, API routes, class names) has leaked into the document.
   - Complex descriptions and role-based logic in the table use `<br>` and bullet points instead of inline spaces and bolding.

### API Spec

- Use research fallback unless a project-specific template exists.
- Cover endpoints or operations, request/response schemas, status/error handling, authentication/authorization, validation, examples, and compatibility notes.

### Non-functional Requirement

- Use research fallback unless a project-specific template exists.
- Cover measurable quality attributes such as performance, availability, security, privacy, auditability, scalability, accessibility, localization, maintainability, and observability as relevant.
