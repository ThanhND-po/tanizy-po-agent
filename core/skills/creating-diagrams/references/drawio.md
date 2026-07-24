# Draw.io Generation Guidelines

Read this reference fully before creating or editing a `.drawio` file.

## Source and Scope

This reference adapts useful techniques from
[`sparklabx/drawio-ai-kit`](https://github.com/sparklabx/drawio-ai-kit),
reviewed at commit `c9ed43d3ab0d83b42ab98a9e46724fa0b251f668` on 2026-07-24.
The upstream project is MIT-licensed by sparklabx.

The strongest adopted techniques are:

- select a topology before layout;
- match an existing template or archetype before free-hand generation;
- describe logical structure before assigning coordinates;
- use verified stencil names instead of recalling them;
- validate structure, geometry, style, and business meaning separately;
- render locally and correct visual defects before delivery.

This skill does not bundle or require the upstream runtime. It keeps the broader
Product Owner diagram coverage, privacy gates, approval workflow, and manual XML
fallback of `creating-diagrams`.

## Contents

1. Tool preflight
2. Build strategy
3. Topology presets
4. Layout and routing
5. Adaptive visual system
6. XML contract
7. Validation loop
8. Pre-delivery checklist

## 1. Tool Preflight

Check local tools without installing anything:

```bash
command -v drawio-ai || true
command -v drawio || true
command -v python3 || true
```

Choose one path:

- **Engine path:** If `drawio-ai` is available and the request is a supported
  architecture or BPMN diagram, use its template, catalog, layout, validation,
  and render workflow.
- **Manual path:** For Use Case, Sequence, Activity, State, ERD, unsupported
  domains, or environments without `drawio-ai`, generate uncompressed XML and
  use the bundled validator plus local visual inspection.

Do not install `drawio-ai`, draw.io desktop, Graphviz, or another dependency
without explicit approval. Do not use optional logo-fetching commands because
they may call public CDNs.

## 2. Build Strategy

### 2.1 Confirm the contract

Use the approved fact list. Confirm:

- diagram type and audience;
- editable `.drawio` only or `.drawio` plus PNG/SVG preview;
- system or process boundary;
- actors, lanes, entities, components, and relationships;
- main direction;
- happy, alternate, error, retry, and terminal paths;
- target draw.io environment when theme or stencil compatibility matters.

### 2.2 Match an archetype first

Before placing shapes, search the project for an existing diagram or template
with the same type and conventions. Reuse its structure when it is current and
correct. Do not copy stale labels or business behavior.

When `drawio-ai` is installed:

```bash
drawio-ai scaffold --list
drawio-ai types
drawio-ai workflow
```

Use the closest scaffold when less than half of its logical structure needs to
change. Otherwise create a new logical structure.

### 2.3 Define logical structure before geometry

List nodes, containers, parent-child relationships, and edges before assigning
coordinates. For architecture diagrams, use a declarative layout engine when
available. For manual XML, place containers first, then primary nodes, then
secondary nodes, then edges and labels.

Never invent stencil identifiers. When `drawio-ai` is installed, batch icon
lookups:

```bash
drawio-ai search "service one, service two, service three"
```

For the manual path, prefer built-in general shapes unless an exact local
stencil name can be verified.

## 3. Topology Presets

Choose one dominant topology. Compose a secondary topology only when the fact
list requires it.

| Topology | Use | Default layout |
|---|---|---|
| Pipeline | Request, data, ETL, or tier flow | Left to right stages |
| Hierarchy | Organization, ownership, or nested scope | Top to bottom |
| Network | Deployment, VPC/VNet, zones, or tiers | Nested boundaries with aligned tiers |
| Hub-and-spoke | Bus, broker, shared gateway, fan-in or fan-out | Hub centered between producers and consumers |
| Hybrid | On-premise and cloud, primary and DR | Separate peer frames |
| Mesh | Many-to-many connectivity | Clustered domains with bundled routes |
| Sequence | Numbered walkthrough over an architecture | Participants left to right, steps top to bottom |
| BPMN swimlane | Role-based business process | Lanes top to bottom, flow left to right |

Topology rules:

- **Pipeline:** keep the main spine nodes at one vertical position. Put
  cross-cutting concerns in a separate band.
- **Hierarchy:** center parents over children and preserve real containment.
- **Network:** mirror repeated zones and align equivalent tiers. Use vertical
  routes mainly for cross-zone relationships.
- **Hub-and-spoke:** place producers on one side and consumers on the other.
  Bundle fan-out or fan-in routes instead of drawing a web of crossings.
- **Hybrid:** keep on-premise outside the cloud boundary. Show a real
  interconnect node when it is part of the architecture.
- **Mesh:** group by domain or account and use shared corridors. Split the
  diagram if relationship density hides meaning.
- **BPMN swimlane:** keep sequence flow inside a pool and message flow between
  pools. See `diagram-types.md` for semantic checks.

## 4. Layout and Routing

### 4.1 Direction and alignment

- Use one main direction.
- Align nodes that form the main path.
- Use a grid for repeated items instead of hand-stacking uneven rows.
- Keep equivalent nodes the same size.
- Size containers to their contents. Do not stretch a decorative frame across
  empty space.

Minimum manual-layout spacing:

| Element | Minimum size or gap |
|---|---|
| General action or component box | 120 x 40 px |
| Note box | 140 x 50 px |
| Decision gateway | 60 x 60 px |
| Horizontal gap between sibling boxes | 30 px |
| Vertical gap between rows | 40 px |
| Swimlane width | 120 px or wider |

Increase width or height when a label would wrap awkwardly or clip.

### 4.2 Connector semantics

- Solid line: primary request, control, data, or sequence flow.
- Dashed line: response, dependency, synchronization, policy, lineage, or DR.
- Double-headed line: genuinely bidirectional communication or synchronization.
- Strong semantic color: error, blocking, or success path only when the legend
  defines it.

Keep connectors orthogonal when possible. Route around nodes and labels. Add
waypoints for dense or exception paths. Align fan-out targets so branches stay
short. Avoid back-pointing arrows unless they represent an explicit loop,
feedback, retry, or synchronization.

### 4.3 Labels

- Use short, business-meaningful labels.
- Use verb-first labels for activities and messages.
- Put long constraints in a note rather than inside a node.
- Give edge labels a solid local background only when required for readability.
- Reposition a label instead of allowing it to cover a node or connector.

## 5. Adaptive Visual System

### 5.1 Theme behavior

For text or lines directly on the canvas, omit hardcoded `fontColor` and
`strokeColor` so draw.io can adapt them to the active theme.

For text inside a box with a fixed pale fill, use `fontColor=#333333` to retain
contrast. If the target draw.io environment supports theme-aware color tokens,
prefer `light-dark(lightValue,darkValue)` for container fills and accents.
Otherwise use the fallback palette below.

Do not write `fontColor=none` or `strokeColor=default`. Omit the property.

### 5.2 Restrained fallback palette

| Meaning | Fill | Border |
|---|---|---|
| User or client | `#d5e8d4` | `#82b366` |
| Core system | `#dae8fc` | `#6c8ebf` |
| Backend service | `#e1d5e7` | `#9673a6` |
| External or batch | `#fff2cc` | `#d6b656` |
| Critical or error | `#f8cecc` | `#b85450` |
| Infrastructure or database | `#f5f5f5` | `#999999` |

Use no more than about 8 distinct fill colors in one diagram. Prefer neutral
containers and let verified service icons carry brand or category color. Do not
recolor official cloud icons.

### 5.3 Typography

- Use 3 or 4 font sizes at most.
- Keep normal labels at 14 px or smaller.
- Use one larger title only in a dedicated title area.
- Use consistent font weight for equivalent elements.
- Do not use color as the only signal.

## 6. XML Contract

Prefer uncompressed XML so the artifact is reviewable and locally validatable.
Accept either:

- a root `<mxGraphModel>`; or
- an `<mxfile>` containing one or more uncompressed `<diagram>` elements with
  nested `<mxGraphModel>` content.

Required rules:

- Include root cells `id="0"` and `id="1"` on every page.
- Keep IDs unique within each page.
- Reference existing node IDs from every `source`, `target`, and `parent`.
- Give every visible vertex a valid `mxGeometry`.
- Use positive width and height.
- Keep sibling leaf nodes from overlapping.
- Keep child nodes within their parent container.
- Add `aspect=fixed` to resource icons.
- Escape XML text correctly.
- Do not place project data in metadata fields that the diagram does not need.

Example manual skeleton:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxGraphModel grid="1" gridSize="10" guides="1" page="1"
  pageWidth="1169" pageHeight="827" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
  </root>
</mxGraphModel>
```

## 7. Validation Loop

Run the loop until structure and visual review are both clean:

1. Build the temporary `.drawio`.
2. Validate structure.
3. Fix all reported errors and warnings in one pass.
4. Render locally when possible.
5. Inspect the image for overlap, clipping, crossings, alignment, contrast,
   missing labels, and inconsistent abstraction.
6. Compare the visible diagram with the fact list.
7. Repeat after any correction.

If `drawio-ai` is installed:

```bash
drawio-ai validate <file.drawio> --strict
drawio-ai render <file.drawio> -o <preview.png>
```

For the manual or fallback path:

```bash
python3 <creating-diagrams-skill-directory>/scripts/validate_drawio.py <file.drawio> --strict
```

The bundled validator checks uncompressed XML, required cells, duplicate IDs,
dangling references, geometry, sibling overlap, child overflow, icon aspect
ratio, font-size budget, and palette size. It does not verify stencil existence,
connector crossings, text clipping, or visual quality. Render inspection is
still required when a local renderer exists.

## 8. Pre-Delivery Checklist

- [ ] Diagram type and output format are confirmed.
- [ ] Every visible fact matches the approved fact list.
- [ ] No unverified actor, system, path, state, entity, or component was added.
- [ ] Main direction and topology are consistent.
- [ ] No node, label, or connector visibly overlaps.
- [ ] Canvas text and plain lines remain theme-adaptive.
- [ ] Fixed-fill boxes retain readable contrast.
- [ ] Official icons use verified stencil names and original colors.
- [ ] XML structure passes the available local validator.
- [ ] A local render was inspected, or the missing visual check is reported.
- [ ] No content was sent to a public renderer or external service.
- [ ] Final destination is confirmed before saving into the project.
