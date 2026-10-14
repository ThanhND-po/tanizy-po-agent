# Basic Design Authoring

A Basic Design document describes a **single screen** from the user and business perspective (外部設計 — external design). It is the handoff artifact from BA to Developer and QA. It does **not** cover database schema, API internals, or class structure — those belong to Detail Design.

**Scope of one Basic Design file = one screen or one closely related screen group.**

#### Workflow

1. **Resolve the output language** from the user's request or project instructions. Ask only when unresolved. Use the chosen language for all human-readable content in the output file. Keep column headers in English for consistency unless project policy specifies otherwise.

2. **Read `../templates/basic-design.md`** before drafting.

3. **Fill Section 1 — Metadata**
   - Follow the project's Screen ID convention. If none exists, propose `BD-[MODULE]-[TYPE][SEQ]`, where:
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
   - Do not use HTML line-break tags, literal line breaks, additional rows for the same element, or merged-cell placeholders.
   - For structured rules in `Initial State`, `Remarks`, or other cells, start with `• `, use ` • ` between independent rules, and use `; ` between values or sub-conditions of the same rule.
   - Use short labels such as `Default`, `Show when`, `Hide when`, `Role`, `On success`, or `On error`, then rely on automatic cell wrapping in the Markdown preview or destination spreadsheet.
   - Example: `• Default: Hidden • Show when: Approval Required with Correction Request; Approved; Confirmed Reward; Cancelled`.
   - Do not invent business rules; record unknowns in Section 5 — Open Questions.

7. **Fill Section 5 — Open Questions**
   - List any ambiguous requirements, missing specs, or stakeholder decisions needed before implementation.

8. **Quality check before showing the output**
   - Every element in Section 4 has a Classification, Required, I/O, and Initial State filled in.
   - No business rule has been invented; all unknowns are in Open Questions.
   - Section 2 answers all three overview questions.
   - No Detail Design content (DB schema, API routes, class names) has leaked into the document.
   - Every UI element occupies exactly one table row and one physical line.
   - No table cell contains HTML line-break tags or literal line breaks.
   - Structured rules start with `• `, separate independent rules with ` • `, and separate values or sub-conditions of the same rule with `; `.
