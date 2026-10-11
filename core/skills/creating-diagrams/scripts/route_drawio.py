#!/usr/bin/env python3
"""Route rectangular architecture/flowchart connectors locally; preserve graph semantics."""

import argparse
import heapq
import itertools
import json
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

from drawio_geometry import absolute_boxes, geometry, hits, obstacles, port, port_side, segment_relation, tokens
from validate_drawio import graph_models, validate_xml


NORMAL = {"L": (-1, 0), "R": (1, 0), "T": (0, -1), "B": (0, 1)}


def pin(side, fraction):
    return {"L": (0, fraction), "R": (1, fraction), "T": (fraction, 0), "B": (fraction, 1)}[side]


def facing(a, b):
    dx, dy = b.x + b.w / 2 - a.x - a.w / 2, b.y + b.h / 2 - a.y - a.h / 2
    if abs(dx) >= abs(dy):
        return ("R", "L") if dx >= 0 else ("L", "R")
    return ("B", "T") if dy >= 0 else ("T", "B")


def simplify(points):
    result = []
    for point in points:
        if result and point == result[-1]:
            continue
        if len(result) >= 2 and ((result[-2][0] == result[-1][0] == point[0]) or
                                 (result[-2][1] == result[-1][1] == point[1])):
            result.pop()
        result.append(point)
    return result


def find_path(start, end, rects, used):
    xs = sorted({start[0], end[0]} | {x for r in rects for x in (r.x, r.x + r.w)} |
                {min(start[0], end[0], *(r.x for r in rects)) - 30,
                 max(start[0], end[0], *(r.x + r.w for r in rects)) + 30})
    ys = sorted({start[1], end[1]} | {y for r in rects for y in (r.y, r.y + r.h)} |
                {min(start[1], end[1], *(r.y for r in rects)) - 30,
                 max(start[1], end[1], *(r.y + r.h for r in rects)) + 30})
    origin = (xs.index(start[0]), ys.index(start[1]), "")
    goal = (xs.index(end[0]), ys.index(end[1]))
    queue, best, previous = [(0, 0, origin)], {origin: 0}, {}
    blocked = {}
    while queue:
        _, cost, state = heapq.heappop(queue)
        if cost != best[state]:
            continue
        ix, iy, direction = state
        if (ix, iy) == goal:
            path = []
            while True:
                path.append((xs[state[0]], ys[state[1]]))
                if state == origin:
                    return simplify(path[::-1])
                state = previous[state]
        for jx, jy, nd in ((ix - 1, iy, "H"), (ix + 1, iy, "H"), (ix, iy - 1, "V"), (ix, iy + 1, "V")):
            if not (0 <= jx < len(xs) and 0 <= jy < len(ys)):
                continue
            a, b = (xs[ix], ys[iy]), (xs[jx], ys[jy])
            key = tuple(sorted((a, b)))
            if key not in blocked:
                blocked[key] = any(hits(a, b, rect) for rect in rects)
            if blocked[key]:
                continue
            penalty = sum(1000 if relation == "overlap" else 400
                          for c, d in used if (relation := segment_relation(a, b, c, d)))
            new_cost = cost + abs(a[0] - b[0]) + abs(a[1] - b[1]) + (20 if direction and direction != nd else 0) + penalty
            nxt = (jx, jy, nd)
            if new_cost < best.get(nxt, float("inf")):
                best[nxt], previous[nxt] = new_cost, state
                heuristic = abs(b[0] - end[0]) + abs(b[1] - end[1])
                heapq.heappush(queue, (new_cost + heuristic, new_cost, nxt))
    return None


def route_model(model, clearance=12):
    cells = {cell.get("id"): cell for cell in model.iter("mxCell")}
    boxes = absolute_boxes(cells)
    obs = obstacles(cells, boxes)
    expanded = [rect.expanded(clearance) for rect in obs]
    selected, skipped, slots = [], [], defaultdict(list)
    for cell_id, cell in cells.items():
        if cell.get("edge") != "1":
            continue
        style = tokens(cell.get("style", ""))
        a, b = boxes.get(cell.get("source")), boxes.get(cell.get("target"))
        if (not a or not b or a.owner == b.owner or style.get("curved") == "1" or
                style.get("edgeStyle", "none") not in ("none", "", "orthogonalEdgeStyle")):
            skipped.append(cell_id)
            continue
        sides = facing(a, b)
        selected.append((cell_id, cell, a, b, sides))
        for endpoint, box, side, other in zip(("exit", "entry"), (a, b), sides, (b, a)):
            coordinate = other.y + other.h / 2 if side in ("L", "R") else other.x + other.w / 2
            slots[(box.owner, side)].append((coordinate, cell_id, endpoint))
    fractions = {}
    for (owner, side), items in slots.items():
        items = sorted(items)
        box = boxes[owner]
        center = box.y + box.h / 2 if side in ("L", "R") else box.x + box.w / 2
        aligned = [index for index, (coordinate, _, _) in enumerate(items) if abs(coordinate - center) < 0.01]
        for index, (_, cell_id, endpoint) in enumerate(items):
            fraction = (index + 1) / (len(items) + 1)
            # Keep a straight spine at the middle port; place branches above/below it.
            # Evenly spreading all pins would add a small, needless jog to the spine.
            if len(aligned) == 1:
                anchor = aligned[0]
                if index <= anchor:
                    fraction = 0.5 * (index + 1) / (anchor + 1)
                else:
                    fraction = 0.5 + 0.5 * (index - anchor) / (len(items) - anchor)
            fractions[(cell_id, endpoint)] = fraction
    used = []
    for cell_id, cell, a, b, preferred in selected:
        style = tokens(cell.get("style", ""))
        candidates = []
        for endpoint, box, side in zip(("exit", "entry"), (a, b), preferred):
            if endpoint + "X" in style or endpoint + "Y" in style:
                xy = (float(style[endpoint + "X"]), float(style[endpoint + "Y"]))
                fixed_side = port_side(*xy)
                if not fixed_side:
                    raise ValueError(f'{cell_id}: explicit {endpoint} port must be on one side, away from corners')
                candidates.append([(fixed_side, xy)])
            else:
                frac = fractions[(cell_id, endpoint)]
                candidates.append([(s, pin(s, frac if s == side else 0.5)) for s in [side] + [s for s in NORMAL if s != side]])
        winner = None
        for (sa, pa), (sb, pb) in itertools.product(*candidates):
            start, end = port(a, *pa), port(b, *pb)
            first = (start[0] + NORMAL[sa][0] * clearance, start[1] + NORMAL[sa][1] * clearance)
            last = (end[0] + NORMAL[sb][0] * clearance, end[1] + NORMAL[sb][1] * clearance)
            if any(hits(start, first, r) for r in expanded if not (r.owner == a.owner and r.role == "node")):
                continue
            if any(hits(last, end, r) for r in expanded if not (r.owner == b.owner and r.role == "node")):
                continue
            middle = find_path(first, last, expanded, used)
            if middle:
                winner = (simplify([start] + middle + [end]), pa, pb)
                break
        if winner is None:
            raise ValueError(f'{cell_id}: no clear route; increase the corridor or move a node')
        points, pa, pb = winner
        style.update({"edgeStyle": "none", "noEdgeStyle": "1", "rounded": "0", "curved": "0",
                      "exitX": str(pa[0]), "exitY": str(pa[1]), "entryX": str(pb[0]), "entryY": str(pb[1]),
                      "exitPerimeter": "0", "entryPerimeter": "0", "exitDx": "0", "exitDy": "0", "entryDx": "0", "entryDy": "0"})
        # Keep named style tokens (e.g. UML notation) and arrow/dash semantics intact.
        named = [part for part in cell.get("style", "").split(";") if part and "=" not in part]
        cell.set("style", ";".join(named + [f"{key}={value}" for key, value in style.items()]) + ";")
        g = geometry(cell)
        if g is None:
            g = ET.SubElement(cell, "mxGeometry", {"as": "geometry"})
        g.set("relative", "1")
        for old in g.findall("Array[@as='points']"):
            g.remove(old)
        parent = boxes.get(cell.get("parent"))
        ox, oy = (parent.x, parent.y) if parent else (0, 0)
        if len(points) > 2:
            array = ET.SubElement(g, "Array", {"as": "points"})
            for x, y in points[1:-1]:
                ET.SubElement(array, "mxPoint", {"x": f"{x - ox:g}", "y": f"{y - oy:g}"})
        segments = list(zip(points, points[1:]))
        used.extend(segments)
        if cell.get("value"):
            lengths = [abs(c[0] - d[0]) + abs(c[1] - d[1]) for c, d in segments]
            longest = max(range(len(lengths)), key=lengths.__getitem__)
            total = sum(lengths)
            if total:
                g.set("x", f"{2 * (sum(lengths[:longest]) + lengths[longest] / 2) / total - 1:g}")
                g.set("y", "-12")
    return {"routed": [row[0] for row in selected], "skipped": skipped}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--output", type=Path, required=True, help="New draft file; the input is preserved.")
    parser.add_argument("--clearance", type=float, default=12)
    args = parser.parse_args()
    try:
        if args.output.resolve() == args.path.resolve():
            raise ValueError("Choose a separate --output path to preserve the input")
        if not 0 < args.clearance < float("inf"):
            raise ValueError("--clearance must be finite and positive")
        xml = args.path.read_text(encoding="utf-8")
        validation = validate_xml(xml)
        if validation["errors"]:
            raise ValueError("Fix XML errors first: " + "; ".join(validation["errors"]))
        root = ET.fromstring(xml)
        models, errors = graph_models(root)
        if errors or any(model not in list(root.iter()) for _, model in models):
            raise ValueError("Router requires nested, uncompressed mxGraphModel elements")
        report = {name: route_model(model, args.clearance) for name, model in models}
        args.output.write_text(ET.tostring(root, encoding="unicode"), encoding="utf-8")
        print(json.dumps({"ok": True, "output": str(args.output.resolve()), "pages": report}, indent=2))
        return 0
    except (OSError, ValueError, KeyError, ET.ParseError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}))
        return 1


if __name__ == "__main__":
    sys.exit(main())
