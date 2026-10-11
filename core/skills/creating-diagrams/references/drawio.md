# Draw.io Generation Guidelines

Read this reference fully before creating or editing a `.drawio` file.

## Source and Scope

This reference adapts useful techniques from
[`sparklabx/drawio-ai-kit`](https://github.com/sparklabx/drawio-ai-kit),
reviewed at commit `1a03d87b877ec738a2a98d38a4d8eeecf4ee66bc` (package 1.0.2) on 2026-10-11.
The upstream project is MIT-licensed by sparklabx.

The strongest adopted techniques are:

- Select a topology before layout;
- Match an existing template or archetype before free-hand generation;
- Describe logical structure before assigning coordinates;
- Use verified stencil names instead of recalling them;
- Validate structure, geometry, style, and business meaning separately;
- Render locally and correct visual defects before delivery.

This skill does not bundle or require the upstream runtime. It bundles a small,
offline catalog of verified native cloud styles, a rectangular connector router,
and a conservative geometry audit. Catalog provenance and license notices are in
`assets/THIRD_PARTY_NOTICES.md`. It keeps the broader
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

The bundled helpers need Python 3.9+ and its standard library only. Resolve their
paths from this skill's directory, independently of the target project. For cloud
architecture, read `cloud-architecture.md` for icon search and containment rules.

These helpers are installed together with the skill. The agent invokes
`cloud_catalog.py`, `route_drawio.py`, and `validate_drawio.py` as needed;
`drawio_geometry.py` and `audit_drawio.py` are internal modules imported by those
commands. The user does not need to launch each file. If Python is absent or
older than 3.9, use another available local tool or continue with manual XML and
explicitly report the checks that could not run. Do not install Python silently.

An installed `drawio-ai` may be older than this review. Check its help before
using `scaffold`, `suggest-layout`, or `render --check`. Use its local rules and
API documentation; do not guess command flags. A missing optional CLI does not
block manual XML or offline icon lookup.

Do not install `drawio-ai`, draw.io desktop, Graphviz, or another dependency
without explicit approval. Do not use optional logo-fetching commands because
they may call public CDNs.

## 2. Build Strategy

### 2.1 Confirm the contract

Use the approved fact list. Confirm:

- Diagram type and audience;
- Editable `.drawio` only or `.drawio` plus PNG/SVG preview;
- System or process boundary;
- Actors, lanes, entities, components, and relationships;
- Main direction;
- Happy, alternate, error, retry, and terminal paths;
- target draw.io environment when theme or stencil compatibility matters.

### 2.2 Match an archetype first

Before placing shapes, search the project for an existing diagram or template with the same type and conventions. Reuse its structure when it is current and correct. Do not copy stale labels or business behavior.

When `drawio-ai` is installed:

```bash
drawio-ai scaffold --list
drawio-ai types
drawio-ai workflow
```

Use a scaffold when its logical structure closely matches the fact list. Otherwise, create a new logical structure. Scaffold into a temporary output directory and inspect its imports/output paths before execution; never write generated files into the runtime or installed skill.

### 2.3 Define logical structure before geometry

List nodes, containers, parent-child relationships, and edges before assigning coordinates. For architecture diagrams, use a declarative layout engine when available. For manual XML, place containers first, then primary nodes, then secondary nodes, then edges and labels.

Never invent stencil identifiers. When `drawio-ai` is installed, batch icon
lookups:

```bash
drawio-ai search "service one, service two, service three"
```

For the manual cloud path, use `scripts/cloud_catalog.py` to retrieve exact native
styles offline. Use general shapes with explicit service labels when no match
exists. A visually similar icon for another service is not a valid substitute.

## 3. Topology Presets

Choose one dominant topology. Compose a secondary topology only when the fact list requires it.

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

- **Pipeline:** keep the main spine nodes at one vertical position. Put cross-cutting concerns in a separate band.
- **Hierarchy:** center parents over children and preserve real containment.
- **Network:** mirror repeated zones and align equivalent tiers. Use vertical routes mainly for cross-zone relationships.
- **Hub-and-spoke:** place producers on one side and consumers on the other. Separate fan-out/fan-in ports and parallel corridors. Share a trunk only when it represents a real junction or aggregate relationship.
- **Hybrid:** keep on-premise outside the cloud boundary. Show a real interconnect node when it is part of the architecture.
- **Mesh:** group by domain or account and use shared corridors. Split the diagram if relationship density hides meaning.
- **BPMN swimlane:** keep sequence flow inside a pool and message flow between pools. See `diagram-types.md` for semantic checks.

## 4. Layout and Routing

### 4.1 Direction and alignment

- Use one main direction.
- Align nodes that form the main path.
- Use a grid for repeated items instead of hand-stacking uneven rows.
- Keep equivalent nodes the same size.
- Size containers to their contents. Do not stretch a decorative frame across empty space.

Minimum manual-layout spacing:

| Element | Minimum size or gap |
|---|---|
| General action or component box | 120 x 40 px |
| Note box | 140 x 50 px |
| Decision gateway | 60 x 60 px |
| Horizontal gap between sibling boxes | 30 px |
| Vertical gap between rows | 40 px |
| Swimlane width | 120 px or wider |
| Edge corridor / clearance from a node | 24–40 px / 12 px |
| Gap between parallel routes / landing ports | 12–16 px / at least 8 px |

Increase width or height when a label would wrap awkwardly or clip.
Reserve a 28–44 px caption band below service icons, wider than the glyph when
needed. Reserve container title bands too. Compact layout means less unused
space, not less room for captions and routing.

### 4.2 Connector semantics

- Solid line: primary request, control, data, or sequence flow.
- Dashed line: response, dependency, synchronization, policy, lineage, or DR.
- Double-headed line: genuinely bidirectional communication or synchronization.
- Strong semantic color: error, blocking, or success path only when the legend defines it.

Keep connectors orthogonal when possible. Route around nodes and labels. Add waypoints for dense or exception paths. Align fan-out targets so branches stay short. Avoid back-pointing arrows unless they represent an explicit loop, feedback, retry, or synchronization.

For engine builds, start with ordinary `d.link(source, target)` and let the router
choose ports. Use a routing override only after a defect is observed. Keep
scaffold routing for diagrams that will be rearranged; use the engine's `bake`
contract for a fixed presentation only when supported by the installed version.

For manual rectangular architecture or flowcharts:

1. Position the main spine and groups first. Leave corridors between repeated
   tiers; put retry/exception routes in outer gutters.
2. Set explicit side ports: right `(1, 0.5)` → left `(0, 0.5)` for horizontal flow,
   bottom `(0.5, 1)` → top `(0.5, 0)` for vertical flow. Spread multiple edges
   across a side; avoid corner ports and stacked arrowheads.
3. Route with `scripts/route_drawio.py` if helpful. It preserves edge endpoints,
   arrow/dash semantics and container membership, avoids node/caption/title
   rectangles, and writes a separate draft. It preserves existing explicit ports.
4. Inspect the result and run `validate_drawio.py --strict --connectors`. If no
   clear route exists, enlarge the corridor or restructure node positions. Do not
   change the endpoint to a container unless the fact list actually describes a
   relationship with the whole container.

The local router uses explicit orthogonal polylines (`edgeStyle=none;
noEdgeStyle=1;rounded=0`) with fixed side pins and waypoints. This makes the saved
path auditable. These paths can need re-routing after nodes are dragged. An
`orthogonalEdgeStyle` with hints can be reinterpreted by draw.io; the static audit
reports such paths as skipped rather than claiming their rendered route is clean.
Do not run this router over sequence lifelines, ER cardinalities, BPMN message
flows or other specialized notation just to normalize their appearance.

For a hand-authored explicit edge, ports and waypoint coordinates must agree:

```xml
<mxCell id="a-to-b" edge="1" parent="1" source="a" target="b"
  style="edgeStyle=none;noEdgeStyle=1;rounded=0;html=1;endArrow=block;endFill=1;exitX=1;exitY=0.5;exitPerimeter=0;entryX=0;entryY=0.5;entryPerimeter=0;">
  <mxGeometry relative="1" as="geometry">
    <Array as="points"><mxPoint x="340" y="130"/><mxPoint x="340" y="230"/></Array>
  </mxGeometry>
</mxCell>
```

Here the source right port must be at `y=130`, target left port at `y=230`, and
`x=340` must lie in a clear corridor. Child node geometry is relative to its
parent; edge waypoints are relative to the edge's parent. Use the lowest common
container or root layer for cross-container edges, never a source-only container.

### 4.3 Labels

- Use short, business-meaningful labels.
- Use verb-first labels for activities and messages.
- Put long constraints in a note rather than inside a node.
- Give edge labels a solid local background only when required for readability.
- Reposition a label instead of allowing it to cover a node or connector.
- Prefer the middle of a long straight segment, offset 10–14 px from the line.
  The local router moves the primary label to its longest segment; rendered text
  width, HTML labels and extra child labels still need visual inspection.

## 5. Adaptive Visual System

### 5.1 Theme behavior

For text or lines directly on the canvas, omit hardcoded `fontColor` and `strokeColor` so draw.io can adapt them to the active theme.

For text inside a box with a fixed pale fill, use `fontColor=#333333` to retain contrast. If the target draw.io environment supports theme-aware color tokens, prefer `light-dark(lightValue,darkValue)` for container fills and accents. Otherwise use the fallback palette below.

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

Use no more than about 8 distinct fill colors in one diagram. Prefer neutral containers and let verified service icons carry brand or category color. Do not recolor official cloud icons.

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
3. Fix actionable errors and warnings in one pass. Record intentional notation
   exceptions; do not distort semantics merely to silence an aesthetic warning.
4. Render locally when possible.
5. Inspect the image for overlap, clipping, crossings, alignment, contrast, missing labels, and inconsistent abstraction.
6. Compare the visible diagram with the fact list.
7. Repeat after a correction. If the same routing failure remains after three
   attempts, report the specific limitation and keep the editable draft for review.

If `drawio-ai` is installed:

```bash
drawio-ai validate <file.drawio> --strict
drawio-ai suggest-layout <file.drawio>
drawio-ai render <file.drawio> -o <preview.png>
```

For the manual or fallback path:

```bash
python3 <creating-diagrams-skill-directory>/scripts/validate_drawio.py <file.drawio> --strict --connectors
```

Omit `--connectors` for specialized notation. The validator checks XML, IDs,
references, parent cycles, dimensions, sibling overlap, child overflow, catalog
cloud-style references, AWS fill colors, icon aspect, font/palette budgets, and
edge geometry. With `--connectors`, it also checks side pins, crowded ports,
explicit orthogonal paths, terminal direction, node/caption/title collisions,
crossings and overlapping line segments in absolute coordinates.

These are conservative rectangle checks. Caption bounds are estimated; arbitrary
HTML, rotated shapes, rendered text clipping, rounded/perimeter transformations,
and renderer-controlled paths are not fully modeled. Inspect `literal_routes_checked`
and `renderer_routes_skipped` in the summary. A known catalog style verifies a
reference against that snapshot, not availability in every draw.io version.
Render inspection is still required when a local renderer exists. Report a
missing render explicitly; never use a public renderer as an automatic fallback.

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
