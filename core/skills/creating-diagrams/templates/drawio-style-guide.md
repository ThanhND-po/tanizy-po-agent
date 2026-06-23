# Draw.io Style Guide — Adaptive Theme (Light & Dark Mode)

> **⚡ AI Agent: Read this file before creating or editing any `.drawio` file.**
>
> Purpose: Ensure every diagram renders correctly on both **Light Mode** and **Dark Mode** in draw.io desktop, app.diagrams.net, and the VS Code extension.

---

## 1. Core Principle: Adaptive Theme First

Draw.io automatically converts Text and Stroke colors (black ↔ white) when the user switches themes — **if and only if** those properties are not hardcoded.

| Element location | `fontColor` rule | `strokeColor` rule | Reason |
|---|---|---|---|
| **On canvas** (arrow label, edge label, UML actor label, floating text) | ❌ DO NOT set | ❌ DO NOT set | draw.io auto-adapts to theme |
| **Inside a box** (actor, phase header, note, database box) | ✅ MUST be `#333333` | ✅ Use semantic zone color | Pastel fill does not adapt; dark text ensures contrast |
| **Semantic line** (colored arrow: error/success) | ❌ DO NOT set | ✅ Use semantic color only | Label still adapts; only the line color is fixed |

**Golden rule**: If an element sits directly ON the canvas background → omit `fontColor`/`strokeColor`. If an element sits INSIDE a box with a fill color → hardcode `fontColor=#333333`.

---

## 2. Color Palette

### 2.1 Fill Colors — Actor Zones / Semantic Groups

| Token | fillColor | strokeColor (box border) | Meaning |
|---|---|---|---|
| 🟢 User / Client Side | `#d5e8d4` | `#82b366` | Light green — user-facing, client app |
| 🔵 Core System / CMS | `#dae8fc` | `#6c8ebf` | Light blue — core system, shared data |
| 🟣 Backend Services | `#e1d5e7` | `#9673a6` | Light purple — service layer, backend |
| 🟡 Batch / External | `#fff2cc` | `#d6b656` | Light yellow — batch jobs, external services |
| 🔴 Critical / Error | `#f8cecc` | `#b85450` | Light red — security-critical, error states |
| ⬜ Infra / Database | `#F5F5F5` | `#999999` | Light grey — infrastructure, DB |
| 🔷 Title Background | `#f5f5f5` | `#CCCCCC` | Light grey — title bar, section header |

### 2.2 Connection / Edge Colors

| Type | strokeColor | fontColor (label) | strokeWidth | Notes |
|---|---|---|---|---|
| Request (plain solid) | *(omit)* | *(omit)* | 1 | Auto-adapts |
| Response (plain dashed) | *(omit)* | *(omit)* | 1 | dashed=1 |
| Critical / Error path | `#b85450` | *(omit)* | 2 | Semantic red; label still adapts |
| Success path | `#82b366` | *(omit)* | 2 | Semantic green; label still adapts |
| Lifeline (Sequence) | *(omit)* | — | 1 | dashed=1 dashPattern=5 5 |

---

## 3. XML Style Snippets

> **Important note**: To "omit" a property, simply do not write it in the `style=""` string. Do **not** write `fontColor=none` or `strokeColor=default`.

### 3.1 Title / Section Header

```xml
style="text;html=1;align=center;fontSize=14;fontStyle=1;fillColor=#f5f5f5;strokeColor=#CCCCCC;rounded=1;fontColor=#333333;"
```

### 3.2 Actor Box (Rounded, pastel fill)

```xml
style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontStyle=1;fontSize=11;fontColor=#333333;"
```

### 3.3 UML Actor Icon (Label on canvas — adaptive)

```xml
style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;fontStyle=1;"
```
*(No `fontColor` — label auto-adapts to theme)*

### 3.4 Phase Header / Swimlane Header (light grey fill)

```xml
style="rounded=0;whiteSpace=wrap;html=1;fillColor=#F0F4F8;strokeColor=#CCCCCC;fontSize=11;fontStyle=1;fontColor=#333333;"
```

### 3.5 Lifeline (Sequence Diagram)

```xml
style="endArrow=none;dashed=1;dashPattern=5 5;"
```
*(No `strokeColor` — auto-adapts)*

### 3.6 Request Arrow (Solid)

```xml
style="html=1;endArrow=block;endFill=1;fontSize=10;"
```
*(No `strokeColor`, no `fontColor`)*

### 3.7 Response Arrow (Dashed)

```xml
style="html=1;endArrow=open;dashed=1;fontSize=10;"
```
*(No `strokeColor`, no `fontColor`)*

### 3.8 Note Box

```xml
style="shape=note;whiteSpace=wrap;html=1;size=14;fillColor=#FFF2CC;strokeColor=#D6B656;fontSize=9;align=left;fontColor=#333333;"
```

### 3.9 Database / Storage

```xml
style="shape=mxgraph.flowchart.database;fillColor=#F5F5F5;strokeColor=#999999;fontColor=#333333;fontSize=10;"
```

### 3.10 Decision Gateway (Diamond)

```xml
style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontColor=#333333;fontSize=10;"
```

---

## 4. Layout & Spacing Rules (Preventing Overlap)

### 4.1 Minimum Element Sizes

| Element | Width (px) | Height (px) | Notes |
|---|---|---|---|
| Actor Box | 120 | 40 | Increase if label exceeds 15 characters |
| Phase Header | 160 | 30 | — |
| Note Box | 140 | 50 | Increase for long text |
| UML Actor Icon | 30 | 60 | Add ~20px below for the label |
| Decision Gateway | 60 | 60 | — |
| Swimlane Lane | ≥ 120 | Variable | — |

### 4.2 Spacing

- **Between adjacent boxes on the same row**: minimum **30px** horizontal gap
- **Between consecutive rows (top-to-bottom)**: minimum **40px** vertical gap
- **Edge labels** must not overlap a box: use `align=center` and `labelBackgroundColor=#ffffff` when a label is obscured

### 4.3 Overlap Detection

Before saving, verify:
- Do any two boxes have `(x, y, width, height)` coordinates that intersect?
- Does any arrow label fall inside another box's bounding area?
- If yes → adjust `x`, `y` to separate them, preferring increased vertical spacing.

---

## 5. Pre-Save Checklist (Required before exporting XML)

- [ ] Plain arrows (Request/Response): **NO** `strokeColor` in style
- [ ] Arrow labels and canvas-level text: **NO** `fontColor` in style
- [ ] Text inside boxes (actor, phase, note, DB): has `fontColor=#333333`
- [ ] Lifelines: **NO** `strokeColor`
- [ ] UML Actor labels (outside box): **NO** `fontColor`
- [ ] No two elements overlap (bounding boxes do not intersect)
- [ ] Every box is large enough to display its label without clipping
- [ ] File XML starts with `<mxGraphModel>` and has valid structure

---

## 6. File XML Template (Skeleton)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxGraphModel dx="1422" dy="762" grid="1" gridSize="10" guides="1" tooltips="1"
  connect="1" arrows="1" fold="1" page="1" pageScale="1"
  pageWidth="1169" pageHeight="827" math="0" shadow="0">
  <root>
    <mxCell id="0" />
    <mxCell id="1" parent="0" />
    <!-- Elements go here with id="2", id="3", etc. -->
  </root>
</mxGraphModel>
```

**ID rules**:
- `id="0"` and `id="1"` are required and must not be removed
- All other elements start from `id="2"` and increment sequentially with no duplicates
- Edges (arrows) reference node IDs via `source="X"` and `target="Y"`

---

*Version: 1.0 | Based on draft/guidelines/DIAGRAM_STYLE_GUIDE.md*
