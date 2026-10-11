"""Shared geometry for the local connector router and conservative static audit."""

import html
import math
import re
from dataclasses import dataclass


def tokens(style):
    return dict(part.split("=", 1) for part in style.split(";") if "=" in part)


def geometry(cell):
    return cell.find("mxGeometry")


def number(value, default=0):
    result = float(value if value is not None else default)
    if not math.isfinite(result):
        raise ValueError("Non-finite geometry")
    return result


@dataclass(frozen=True)
class Rect:
    owner: str
    x: float
    y: float
    w: float
    h: float
    role: str = "node"

    def expanded(self, margin):
        return Rect(self.owner, self.x - margin, self.y - margin,
                    self.w + 2 * margin, self.h + 2 * margin, self.role)


def absolute_boxes(cells):
    boxes = {}

    def resolve(cell_id, trail):
        if cell_id in boxes:
            return boxes[cell_id]
        if cell_id in trail:
            raise ValueError("Parent cycle at " + cell_id)
        cell = cells.get(cell_id)
        if cell is None or cell.get("vertex") != "1":
            return None
        parent_id = cell.get("parent")
        if cells.get(parent_id) is not None and cells[parent_id].get("edge") == "1":
            return None  # Relative edge labels require rendered path geometry.
        g = geometry(cell)
        if g is None:
            return None
        parent = resolve(parent_id, trail | {cell_id})
        x, y = number(g.get("x")), number(g.get("y"))
        if parent:
            if g.get("relative") == "1":
                x, y = x * parent.w, y * parent.h
            x, y = x + parent.x, y + parent.y
        offset = g.find("mxPoint[@as='offset']")
        if offset is not None:
            x, y = x + number(offset.get("x")), y + number(offset.get("y"))
        boxes[cell_id] = Rect(cell_id, x, y, number(g.get("width")), number(g.get("height")))
        return boxes[cell_id]

    for cell_id in cells:
        resolve(cell_id, set())
    return boxes


def plain_label(cell):
    value = re.sub(r"<br\s*/?>", "\n", cell.get("value", ""), flags=re.I)
    return html.unescape(re.sub(r"<[^>]+>", "", value))


def obstacles(cells, boxes):
    parents = {cell.get("parent") for cell in cells.values()
               if cell.get("vertex") == "1" and geometry(cell) is not None and geometry(cell).get("relative") != "1"}
    result = []
    for cell_id, box in boxes.items():
        cell = cells[cell_id]
        style = tokens(cell.get("style", ""))
        is_container = cell_id in parents or style.get("container") == "1" or style.get("swimlane") == "1"
        if is_container:
            # Container outlines are passable; the title band is a text obstacle.
            result.append(Rect(cell_id, box.x, box.y, box.w,
                               min(box.h, number(style.get("startSize"), 30)), "header"))
            continue
        result.append(box)
        label = plain_label(cell)
        if label and style.get("verticalLabelPosition") == "bottom":
            fs = number(style.get("fontSize"), 12)
            lines = label.splitlines() or [label]
            width = max(box.w, max(map(len, lines)) * fs * 0.6 + 12)
            result.append(Rect(cell_id, box.x + (box.w - width) / 2, box.y + box.h + 2,
                               width, len(lines) * fs * 1.4 + 8, "caption"))
    return result


def hits(a, b, rect):
    """True for an axis-aligned segment crossing a rectangle interior."""
    eps = 0.01
    if abs(a[0] - b[0]) < eps:
        return (rect.x + eps < a[0] < rect.x + rect.w - eps and
                max(min(a[1], b[1]), rect.y) < min(max(a[1], b[1]), rect.y + rect.h) - eps)
    if abs(a[1] - b[1]) < eps:
        return (rect.y + eps < a[1] < rect.y + rect.h - eps and
                max(min(a[0], b[0]), rect.x) < min(max(a[0], b[0]), rect.x + rect.w) - eps)
    return False


def axis_aligned(a, b):
    return abs(a[0] - b[0]) < 0.01 or abs(a[1] - b[1]) < 0.01


def port(box, x, y):
    return (box.x + x * box.w, box.y + y * box.h)


def port_side(x, y):
    if not 0 <= x <= 1 or not 0 <= y <= 1:
        return None
    sides = [(x == 0, "L"), (x == 1, "R"), (y == 0, "T"), (y == 1, "B")]
    found = [side for match, side in sides if match]
    return found[0] if len(found) == 1 else None


def literal_path(cell, boxes):
    style = tokens(cell.get("style", ""))
    if style.get("curved") == "1" or style.get("edgeStyle", "none") not in ("none", "") and style.get("noEdgeStyle") != "1":
        return None
    if any(number(style.get(key)) != 0 for key in ("exitDx", "exitDy", "entryDx", "entryDy")):
        return None  # Offset pin transformations must be checked by the renderer.
    source, target = boxes.get(cell.get("source")), boxes.get(cell.get("target"))
    if not source or not target:
        return None
    try:
        sx, sy, tx, ty = [number(style[key]) for key in ("exitX", "exitY", "entryX", "entryY")]
    except (KeyError, ValueError):
        return None
    g = geometry(cell)
    if g is None:
        return None
    origin = boxes.get(cell.get("parent"))
    ox, oy = (origin.x, origin.y) if origin else (0, 0)
    points = [(number(p.get("x")) + ox, number(p.get("y")) + oy)
              for p in g.findall("Array[@as='points']/mxPoint")]
    return [port(source, sx, sy)] + points + [port(target, tx, ty)]


def segment_relation(a, b, c, d):
    """Return overlap/crossing for perpendicular or collinear orthogonal segments."""
    eps = 0.1
    horizontal1, horizontal2 = abs(a[1] - b[1]) < eps, abs(c[1] - d[1]) < eps
    if horizontal1 == horizontal2:
        fixed, axis = (1, 0) if horizontal1 else (0, 1)
        if abs(a[fixed] - c[fixed]) < eps:
            shared = min(max(a[axis], b[axis]), max(c[axis], d[axis])) - max(min(a[axis], b[axis]), min(c[axis], d[axis]))
            if shared > eps:
                return "overlap"
    else:
        if not horizontal1:
            a, b, c, d = c, d, a, b
        # Include intersections at a bend or segment endpoint: touching a wire
        # there can falsely imply a junction just as an interior crossing can.
        if min(a[0], b[0]) - eps <= c[0] <= max(a[0], b[0]) + eps and min(c[1], d[1]) - eps <= a[1] <= max(c[1], d[1]) + eps:
            return "crossing"
    return None
