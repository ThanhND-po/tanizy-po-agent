# Basic Design: [BD-XXX-XX] — [Screen Name]

## 1. Metadata

| Field | Value |
|---|---|
| Screen ID | [BD-MODULE-TYPESEQ — e.g. BD-STL-L01 / BD-STL-L01-M1] |
| Screen Name | [Full name of the screen] |
| Related Ticket | [Link or ID — e.g. Jira/Backlog ticket, User Story ID] |
| Author | [Name] |
| Date | [YYYY-MM-DD] |
| Status | Draft / In Review / Approved |

---

## 2. Specs Overview

**Purpose**
> What is this screen? What business goal or user need does it serve?

[Write 1–3 sentences answering this question.]

**User Capabilities**
> What can the user do on this screen?

- [Action 1]
- [Action 2]
- [Action 3]

**Entry Points**
> How does the user reach this screen? What triggers or navigation paths lead here?

- [Entry point 1 — e.g. "Click 'New Record' button on the List screen"]
- [Entry point 2 — e.g. "Direct URL / deep link"]

---

## 3. Screen Image

> Attach a wireframe, mockup, user flow, screen flow, or prototype image that illustrates the layout described in Section 4.
> If not yet available, leave this section blank and add the link or file once it is ready.

| Type | Link / File |
|---|---|
| Wireframe / Mockup | [Link or embed] |
| Screen Flow / User Flow | [Link or embed] |

---

## 4. Screen Inventory & Element Specs

> Number elements using hierarchical notation: top-level items are 1, 2, 3 … and child elements of a container (e.g. columns inside a table, fields inside a card) are 1.1, 1.2, 3.1, 3.2 …
>
> Column definitions:
> - **#** — Element number matching the annotated screen image
> - **Item Name** — Label or field name as displayed on the UI
> - **Classification** — UI component type: `label`, `text`, `textarea`, `dropdown`, `combobox`, `checkbox`, `radio`, `button`, `table`, `badge`, `icon`, `link`, `image`, `date-picker`, `toggle`, `tab`, `modal`, `card`, `section-header`
> - **Required** — Whether the field is mandatory for form submission: `Yes` / `No` / `N/A`
> - **Max Length** — Maximum number of characters or digits allowed (use `—` if not applicable)
> - **I/O** — Whether this element receives user input (`Input`), displays system data (`Output`), does both (`Both`), or triggers a behaviour (`Action`)
> - **Data Type** — Logical data type: `string`, `number`, `boolean`, `date`, `datetime`, `enum`, `array`, `file`, `—`
> - **Input Constraint** — Allowed character sets, formats, patterns, or ranges (e.g. `digits only`, `email format`, `YYYY-MM-DD`, `max 100`)
> - **Initial State** — The value or visual state the element shows when the screen first loads (e.g. `Blank`, `Today's date`, specific default value, `Disabled`)
> - **Remarks** — Business rules, validation logic, conditional behaviour, trigger actions, and any additional explanation

**Remark:** When showing info for `Initial State` and `Remarks`, if you need to describe complex logic, conditions, or role-based access, always use `<br>` to explicitly break lines and use bullet points (`-`) instead of writing inline with bold text. (e.g., `<br>- **Admin**: can edit.<br>- **User**: read-only.`)


| # | Item Name | Classification | Required | Max Length | I/O | Data Type | Input Constraint | Initial State | Remarks |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [Screen title / page heading] | label | N/A | — | Output | string | — | Text: "[Title text]" | Static label. Always visible. |
| 2 | | | | | | | | | |
| 3 | | | | | | | | | |
| 3.1 | | | | | | | | | |
| 3.2 | | | | | | | | | |
| 4 | | | | | | | | | |

---

## 5. Open Questions

> List any unresolved business rules, ambiguous requirements, or decisions pending stakeholder confirmation.

- [ ] [Question or open item — owner and due date if known]
