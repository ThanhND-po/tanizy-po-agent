# Feature Spec Authoring

## Definition and Boundaries

A Feature Specification describes one coherent feature or a clearly bounded group of capabilities. It aligns PO/BA, Developer, UI/UX Designer and QA/Tester on the problem, goals, scope, actors, permissions, behavior, business rules, flows, exceptions and relevant constraints.
It covers why the capability is needed, what it provides and how the product behaves. It is developed during discovery/refinement, approved before implementation of the relevant scope and updated through approved changes.

- Epic: outcome and grouping of work; reference it without reproducing the backlog.
- User Story: one persona's goal and acceptance criteria; reference it without requiring story decomposition to create an FS.
- Basic Design: screen-level UI inventory and element rules; keep FS at behavior and interaction scope.
- API Spec / Detail Design: contracts and internal implementation; link to them where confirmed constraints affect behavior.
- NFR Spec: detailed measurable quality contract; capture applicable concerns in FS and reference detailed specifications where available.

## Template Use

- Read [Feature Spec template](../templates/feature-spec.md) before drafting. Existing FS files provide context and approved rules; they do not replace the canonical template.
- Read project instructions and documentation entrypoints available in the target project. Follow their links to applicable standards, owning modules and related artifacts; do not assume another project's folder layout exists.
- Use the template for the final document. During discovery, preserve Understanding Lock and incremental review before assembling it.
- Keep Understanding Summary, problem/goals, scope/non-goals, actors/permissions, key/exception flows, business rules, NFRs, dependencies/risks, assumptions, open questions, Decision Log and References. Mark non-applicable core concerns with a short reason rather than inventing content.
- Add screen/interaction and data/status sections only when relevant. Adapt headings or combine related sections if the required information remains easy to locate.
- Use project metadata, language, IDs, filenames and links. Do not copy unassigned IDs, dates, approval states or sample rows into a saved artifact.
- Record unknown behavior as OPEN, including whether it blocks the affected scope. An assumption or unanswered question is not approval.
- Do not invent performance targets, status transitions, API behavior, permissions, owners or deadlines. Mark proposed values explicitly and seek confirmation where needed.
- Do not research a replacement FS structure when this local template is available. Research may still be needed to verify domain facts or externally referenced contracts.
- Preserve an approved FS's structure when making a scoped update unless restructuring is explicitly requested. Do not migrate existing FS files automatically.

## Quality Gate

Before showing the final FS, verify:

- Required concerns are covered or explicitly non-applicable; template prompts and example rows have been removed.
- Actors, permissions, rules, scope and flows agree; current scope and approved future scope are distinct.
- Happy path, relevant alternate/exception behavior and recovery are understandable without guessing.
- Material rules and constraints are traceable to exact sources or explicit decisions; assumptions remain visibly unconfirmed.
- Shared project standards are referenced rather than redefined. Conflicts with approved requirements are surfaced for resolution.
- Unknowns identify their effect and blocking scope; no unresolved decision appears as an accepted requirement.
- FS detail remains within product behavior; links carry screen inventories, API contracts and internal design where applicable.
- Applicable NFRs are stated without fabricated targets. Decision Log states match actual user decisions.
- Project metadata, language, naming and links are valid. Self-review readiness is not user approval.

Fix drafting defects before presentation. Keep source-dependent questions visible for user resolution. Save only after the required content/path approval and run the target project's relevant validation.
