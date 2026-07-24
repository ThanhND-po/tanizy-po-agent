---
name: creating-diagrams
description: Create or revise diagrams for Product Owner and delivery work, including Use Case, Sequence, Activity, Swimlane, BPMN-style flow, BPMN 2.0, State, ERD, architecture, component, Mermaid, draw.io, and standalone interactive HTML. Use when the user asks to visualize a process, system interaction, lifecycle, data model, architecture, or business flow. Clarify the diagram type and output format, protect project information, validate locally, and review business coverage before saving.
---

# Creating Diagrams

Create diagrams that are correct, readable, editable where needed, and grounded in confirmed project facts.

## Hard Gates

- Do not generate the diagram until the context, diagram type, and output format are clear.
- If the type or format is missing, ask one focused question at a time and recommend a default based on the request.
- Do not write a final artifact into the target project until the user approves the proposed diagram and confirms the destination. Temporary local preview files are allowed.
- Do not run version-control actions.
- Do not send project content, diagram source, labels, or screenshots to public renderers, diagram websites, paste services, or third-party AI services.
- Use only local tools already available. Do not install a dependency unless the user explicitly asks.
- Do not invent actors, systems, decisions, paths, states, entities, relationships, or infrastructure.

## Workflow

1. **Understand the context**
   - Read the related requirements, use cases, business rules, APIs, data models, and existing diagrams.
   - State any unverified assumption.

2. **Confirm diagram type**
   - If the user named a type, verify that it matches the communication need.
   - If no type was named, read the selection matrix in `references/diagram-types.md`, recommend one, and ask for confirmation.
   - After the type is selected, apply only its relevant reference section.

3. **Confirm output format**
   - If the user explicitly requested draw.io, treat `.drawio` as confirmed and ask only whether a PNG or SVG preview is also needed.
   - Otherwise choose from the format table below and ask for confirmation when the choice affects editability or standards compliance.

   | Need | Recommended format |
   |---|---|
   | Editable source for ongoing review | draw.io `.drawio` |
   | Browser-openable, responsive stakeholder review | Standalone `.html` |
   | Inline diagram in Markdown or repository docs | Mermaid |
   | UML-heavy source with existing local tooling | PlantUML |
   | Import into Camunda, Bizagi, or another BPMN tool | BPMN 2.0 XML |
   | Quick text-only sketch | ASCII |

4. **Create the fact list**
   - Record the boundary, audience, actors or lanes, entities, trigger, happy path, alternate and error paths, decisions, terminal outcomes, relationships, and assumptions.
   - Use the fact list as the business coverage baseline.
   - Ask one focused question when a required fact is unknown.

5. **Load only the output-specific reference**
   - For draw.io, read `references/drawio.md` fully before generating XML.
   - For standalone interactive HTML, read `references/interactive-html.md` fully.
   - For all formats, use the selected section in `references/diagram-types.md`.

6. **Generate a temporary draft**
   - Use domain-specific labels from the confirmed context.
   - Establish the main direction and happy path first.
   - Add alternate, error, retry, and terminal paths from the fact list.
   - Keep one abstraction level. Split the diagram when the selected type becomes unreadable.

7. **Validate in three passes**
   - **Structure:** validate syntax, IDs, references, geometry, and notation rules with an installed local tool or the bundled validator where applicable.
   - **Business coverage:** compare every visible node and path with the fact list.
   - **Readability:** inspect text clipping, overlap, crossings, direction, spacing, contrast, and label clarity.
   - Report checks that could not be run. Do not describe an unperformed check as passed.

8. **Present for review, then save**
   - Summarize the selected type, format, scope, key paths, assumptions, validation result, and any limitations.
   - Show a local preview when available.
   - After approval, ask for the destination and save the final artifact.
   - Prefer `docs/diagrams/<descriptive-name>.<ext>` unless the project has another convention.

## Output Rules

### Draw.io

- Follow `references/drawio.md`, including its tool preflight, topology, layout, adaptive theme, connector, XML, and validation rules.
- Prefer the `drawio-ai` declarative engine only when it is already installed and the requested architecture or BPMN type is supported.
- Otherwise generate uncompressed draw.io XML and run:

```bash
python3 <creating-diagrams-skill-directory>/scripts/validate_drawio.py <path-to-file.drawio> --strict
```

- If the draw.io desktop CLI is available, render a local PNG or SVG and inspect it. Static XML validation does not prove visual correctness.
- Never use optional icon or logo fetching that makes outbound requests unless the user explicitly approves it.

### Standalone Interactive HTML

- Use HTML for communication and review, not to claim BPMN 2.0 compliance.
- Keep the artifact self-contained and offline-safe.
- Ensure the happy path remains understandable without interaction.
- Validate desktop, narrow viewport, keyboard operation, visible focus, connector alignment, and the no-JavaScript baseline as required by `references/interactive-html.md`.

### Mermaid, PlantUML, BPMN 2.0 XML, and ASCII

- Use the selected notation faithfully.
- Do not call a public renderer.
- Run an installed local validator or renderer when available.
- Distinguish BPMN-style flowcharts from standards-compliant BPMN 2.0 XML.
