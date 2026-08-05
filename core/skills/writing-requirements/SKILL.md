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
- For Basic Design, use Local Markdown mode by default. Do not convert, upload, or sync the artifact to a spreadsheet unless the user explicitly requests or confirms it.

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

3. **Choose the Basic Design delivery mode**
   - Use **Local Markdown mode** by default when the user does not mention a spreadsheet. Do not interrupt the workflow to ask about spreadsheet delivery.
   - Use **Spreadsheet-ready mode** only when the user explicitly asks to manage or share the Basic Design through a spreadsheet.
   - If the user mentions team sharing, spreadsheet management, or conversion but the intended output is unclear, ask one targeted question: `Should this Basic Design remain a local Markdown artifact, or should it also be prepared for spreadsheet management?`
   - Treat spreadsheet conversion as a separate delivery step. Preserve the approved content and business rules; change only the table-cell formatting needed for spreadsheet management.
   - Do not upload or sync to a spreadsheet until the user confirms the destination and requested write scope.

4. **Use local template when available**
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
   - Present the artifact and ask for approval or revisions.
   - After approval, ask where to save it.
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
   - Create the output filename independently from the Screen ID using `bd-<descriptive-screen-name>.md`.
   - Do not include `[MODULE]`, `[TYPE]`, `[SEQ]` or the full Screen ID in the filename.
   - Example: Screen ID `BD-ATT-D01` with screen name `Attendance Record Details` uses `bd-attendance-record-details.md`.
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
   - Keep each UI element in exactly one Markdown table row and keep that row on one physical line in both delivery modes.
   - Apply the formatting for the selected delivery mode consistently across the table:
     - **Local Markdown mode (default):** For complex descriptions in `Initial State`, `Remarks`, or other cells, use `<br>` to create explicit line breaks. Use `<br>- **Label**: ...` for independent conditions or role-based rules instead of combining them with spaces and bold text.
     - **Spreadsheet-ready mode:** Do not use HTML line-break tags or literal line breaks inside cells. For structured rules in `Initial State`, `Remarks`, or other cells, start with `• `, use ` • ` between independent rules, and use `; ` between values or sub-conditions of the same rule. Use short labels and rely on automatic cell wrapping.
   - Do not mix Local Markdown and Spreadsheet-ready formatting in the same table.
   - Do not invent business rules; record unknowns in Section 5 — Open Questions.

7. **Fill Section 5 — Open Questions**
   - List any ambiguous requirements, missing specs, or stakeholder decisions needed before implementation.

8. **Quality check before showing the output**
   - Every element in Section 4 has a Classification, Required, I/O, and Initial State filled in.
   - No business rule has been invented; all unknowns are in Open Questions.
   - Section 2 answers all three overview questions.
   - No Detail Design content (DB schema, API routes, class names) has leaked into the document.
   - Every UI element occupies exactly one table row and one physical line.
   - The table uses only the selected delivery mode:
     - Local Markdown mode uses `<br>` and bullet points for complex descriptions and role-based logic.
     - Spreadsheet-ready mode contains no `<br>` tags or literal line breaks inside cells and uses `• ` separators for structured rules.

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
- Organize requirements by category and maintain a scannable catalog with at least: ID, Category, Item, Description, Target or Threshold, Priority, Status, Verification, and Source.
- Use the project's category taxonomy when one exists. Otherwise use ISO/IEC 25010:2023 as the baseline and add clearly labeled project-specific categories only when needed.
- Treat an NFR spec as the detailed source for quality concerns mentioned in a Feature Spec. Trace each source statement to an NFR ID and elaborate its scope, measurable target, verification method, and ownership.
- Do not invent targets or service levels. Use `TBD` and add an open question when the Feature Spec or stakeholder input is not measurable enough.
- Keep Priority, implementation Status, and Verification Result as separate concepts.
- Include only relevant categories. Mark a category `Not Applicable` with a reason when its omission could create material risk.
- Reject vague requirements such as `fast`, `secure`, `scalable`, or `user-friendly` unless they are converted into measurable and verifiable statements.
