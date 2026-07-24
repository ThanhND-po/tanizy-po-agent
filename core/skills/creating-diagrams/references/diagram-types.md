# Diagram Type Selection and Review Rules

Read only the section for the selected diagram type.

## Selection Matrix

| Communication need | Type | Primary question answered |
|---|---|---|
| Scope, actors, and user goals | Use Case | Who can do what within the system boundary? |
| Ordered calls between people and systems | Sequence | In what order do participants exchange messages? |
| Decision flow within one behavior | Activity or flowchart | What happens next under each condition? |
| Ownership and cross-role handoffs | Swimlane activity | Who owns each step and handoff? |
| Formal executable or importable business process | BPMN 2.0 | What process semantics must a BPMN tool preserve? |
| Lifecycle of one entity | State | Which states and transitions are allowed? |
| Conceptual or logical data relationships | ERD | Which entities relate and with what cardinality? |
| Components, integrations, or deployment topology | Architecture or component | What parts exist and how do they connect? |

## Use Case

- Put actors outside the system boundary and use cases inside it.
- Name use cases as user goals, not screen names or technical endpoints.
- Use `include` only for behavior that is always reused.
- Use `extend` only for optional or conditional behavior attached to a clear extension point.
- Avoid decomposing implementation steps inside a Use Case diagram.

Review:

- Every actor and goal exists in the fact list.
- Associations cross the system boundary correctly.
- `include` and `extend` directions and meanings are correct.
- The diagram does not imply sequence or timing.

## Sequence

- Order participants left to right from initiator through internal systems to external dependencies.
- Keep time top to bottom.
- Use `alt`, `opt`, and `loop` for alternate, optional, and repeated behavior.
- Distinguish synchronous calls, asynchronous messages, and return messages.
- Split the diagram when it exceeds 8 participants or about 15 main messages.

Review:

- Each message has a sender, receiver, and business-meaningful label.
- Alternate and error branches return to a valid outcome.
- Response messages do not appear before their request.
- Participant order minimizes crossings.

## Activity or Flowchart

- Use one start and one or more explicit end outcomes.
- Give every decision an outcome label such as Yes/No or Approved/Rejected.
- Merge branches explicitly when they rejoin.
- Show loops with a clear condition and exit.
- Keep the main direction consistent.

Review:

- Every decision has at least two meaningful outcomes.
- Every path reaches an end, merge, or documented loop.
- Actions use verb-first labels.
- Error and retry paths do not terminate silently.

## Swimlane Activity

- Use lanes for roles, teams, or systems with real ownership.
- Keep the main flow left to right and stack lanes top to bottom unless the project standard says otherwise.
- Put each action in exactly one owning lane.
- Keep handoff edges short and make the receiving action easy to identify.
- Use neutral lane backgrounds. Do not assign a decorative color to every lane.

Review:

- Every owner from the fact list has a lane.
- Each handoff crosses the correct lane boundary.
- Decision ownership is explicit.
- Alternate paths and terminal outcomes remain visible without relying on a legend alone.

## BPMN 2.0

- Confirm the target BPMN tool and its import constraints before generating XML.
- Use pools for participants and lanes for responsibility inside a participant.
- Keep sequence flow inside one pool.
- Use message flow only between pools.
- Give every pool at least one valid start and end path.
- Use XOR for exactly one path, AND for all paths, and OR for one or more paths.
- Use red only for error, cancel, or terminate semantics.
- Do not claim that Mermaid or an informal draw.io flowchart is BPMN 2.0 compliant.

Review:

- Every flow object belongs to a lane and pool.
- A splitting gateway has at least two outgoing flows.
- A merging gateway has at least two incoming flows.
- No sequence flow crosses a pool boundary.
- No message flow stays inside one pool.
- Events, tasks, gateways, and flows use the expected BPMN semantics.

## State

- Use the diagram for the lifecycle of one named entity.
- Show an initial state and all terminal states.
- Label transitions with the triggering event and add a guard when the transition is conditional.
- Separate business states from transient UI or processing steps.
- Show invalid or prohibited transitions only when they matter to the audience.

Review:

- Every state is mutually understandable and business-relevant.
- Every nonterminal state has a valid outgoing transition.
- Transition labels describe triggers, not outcomes alone.
- Error, cancellation, and reopening behavior are explicit when applicable.

## ERD

- Confirm whether the audience needs a conceptual or logical model.
- Show identifiers and only the attributes needed for the stated purpose.
- Use consistent cardinality notation.
- Name relationships when cardinality alone is ambiguous.
- Resolve many-to-many relationships with an associative entity in a logical model.

Review:

- Each entity has a stable identifier where the model level requires it.
- Optionality and cardinality match the business rules.
- Foreign-key direction is consistent with the selected notation.
- Derived or sensitive attributes are marked or omitted deliberately.

## Architecture or Component

- Choose one dominant topology: pipeline, hierarchy, network, hub-and-spoke, hybrid, mesh, or component interaction.
- Keep business behavior separate from deployment and infrastructure detail.
- Nest containers according to real ownership or deployment boundaries.
- Place sources or clients on the left, the core system in the center, and consumers or external systems on the right when a request or data flow is shown.
- Put governance, security, observability, or CI/CD in a cross-cutting band only when their relationships are in scope.

Review:

- Every boundary has a clear meaning.
- Components appear at a consistent abstraction level.
- External and managed services are not falsely nested inside private infrastructure.
- Connector direction and semantics match the fact list.
- Repeated nodes or links are grouped without hiding critical relationships.
