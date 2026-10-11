"""Icon provenance and opt-in connector geometry checks; no renderer simulation."""

import itertools
import re
from collections import defaultdict

from cloud_catalog import indexed_styles, style_signature
from drawio_geometry import absolute_boxes, axis_aligned, geometry, hits, literal_path, number, obstacles, port_side, segment_relation, tokens


def audit(cells, check_connectors=False):
    errors, warnings = [], []
    metrics = {"literal_routes_checked": 0, "renderer_routes_skipped": 0}
    # Detect cycles even through layer / edge parents, before resolving coordinates.
    for cell_id in cells:
        visited, current = set(), cell_id
        while current in cells:
            if current in visited:
                errors.append(f'Cell "{cell_id}" has a parent cycle.')
                break
            visited.add(current)
            current = cells[current].get("parent")
    if errors:
        return errors, warnings, metrics
    styles = indexed_styles()
    for cell_id, cell in cells.items():
        style = tokens(cell.get("style", ""))
        signature = style_signature(cell.get("style", ""))
        cloud_ref = any(re.match(r"mxgraph\.(aws4|azure|gcp2)\.", value) or value.startswith("img/lib/azure2/")
                        for key, value in signature)
        entry = styles.get(signature)
        if cloud_ref and not entry:
            warnings.append(f'Cloud style on "{cell_id}" is not verified by the bundled catalog: {signature}. '
                            'Look it up in a newer local catalog; this does not prove the stencil is nonexistent.')
        if entry and entry["kind"] == "icon":
            if style.get("aspect") != "fixed":
                warnings.append(f'Cloud icon "{cell_id}" is missing aspect=fixed.')
            canonical = tokens(entry["style"])
            if entry["provider"] == "aws" and style.get("fillColor", "").lower() != canonical.get("fillColor", "").lower():
                warnings.append(f'AWS icon "{cell_id}" changes its catalog fillColor.')
        if cell.get("edge") == "1":
            g = geometry(cell)
            if g is None or g.get("relative") != "1":
                errors.append(f'Edge "{cell_id}" requires mxGeometry relative="1".')
            if g is not None:
                for point in g.findall(".//mxPoint"):
                    try:
                        number(point.get("x")), number(point.get("y"))
                    except ValueError:
                        errors.append(f'Edge "{cell_id}" has a non-finite waypoint or label offset.')
    if not check_connectors or errors:
        return errors, warnings, metrics
    try:
        boxes = absolute_boxes(cells)
        obs = obstacles(cells, boxes)
    except (ValueError, RecursionError) as exc:
        errors.append("Cannot resolve connector geometry: " + str(exc))
        return errors, warnings, metrics
    routes, ports = {}, defaultdict(list)
    for cell_id, cell in cells.items():
        if cell.get("edge") != "1":
            continue
        style = tokens(cell.get("style", ""))
        valid_ports = True
        for prefix, ref in (("exit", cell.get("source")), ("entry", cell.get("target"))):
            try:
                x, y = number(style[prefix + "X"]), number(style[prefix + "Y"])
                side = port_side(x, y)
                if not side:
                    raise ValueError("port must be on one side, away from corners")
            except (KeyError, ValueError):
                warnings.append(f'Edge "{cell_id}" has no valid explicit {prefix} port.')
                valid_ports = False
                continue
            box = boxes.get(ref)
            if box:
                ports[(ref, side)].append((cell_id, x * box.w, y * box.h))
        try:
            path = literal_path(cell, boxes) if valid_ports else None
        except ValueError:
            errors.append(f'Edge "{cell_id}" has an invalid pin offset or waypoint.')
            continue
        if path is None:
            metrics["renderer_routes_skipped"] += 1
            continue
        if not all(axis_aligned(a, b) for a, b in zip(path, path[1:])):
            warnings.append(f'Edge "{cell_id}" has diagonal segments in its explicit route.')
            continue
        # Drop zero-length points before auditing terminal directions.
        path = [point for index, point in enumerate(path) if index == 0 or point != path[index - 1]]
        metrics["literal_routes_checked"] += 1
        routes[cell_id] = path
        if len(path) < 2:
            warnings.append(f'Edge "{cell_id}" has a zero-length route.')
            continue
        for prefix, a, b in (("exit", path[0], path[1]), ("entry", path[-1], path[-2])):
            side = port_side(number(style[prefix + "X"]), number(style[prefix + "Y"]))
            nx, ny = {"L": (-1, 0), "R": (1, 0), "T": (0, -1), "B": (0, 1)}[side]
            dx, dy = b[0] - a[0], b[1] - a[1]
            if dx * nx + dy * ny <= 0 or abs(dx * ny - dy * nx) > 0.01:
                warnings.append(f'Edge "{cell_id}" approaches its {prefix} port from the wrong direction.')
        for rect in obs:
            if any(hits(a, b, rect) for a, b in zip(path, path[1:])):
                warnings.append(f'Edge "{cell_id}" crosses {rect.role} "{rect.owner}".')
    for (node, side), items in ports.items():
        for a, b in itertools.combinations(items, 2):
            if a[0] != b[0] and abs(a[1] - b[1]) + abs(a[2] - b[2]) < 8:
                warnings.append(f'Edges "{a[0]}" and "{b[0]}" crowd the {side} port of "{node}".')
    for (id_a, path_a), (id_b, path_b) in itertools.combinations(routes.items(), 2):
        relations = {segment_relation(a, b, c, d) for a, b in zip(path_a, path_a[1:]) for c, d in zip(path_b, path_b[1:])}
        if "overlap" in relations:
            warnings.append(f'Edges "{id_a}" and "{id_b}" have overlapping segments; separate corridors or model a real junction.')
        elif "crossing" in relations:
            warnings.append(f'Edges "{id_a}" and "{id_b}" cross; review the layout or show a line jump.')
    return errors, warnings, metrics
