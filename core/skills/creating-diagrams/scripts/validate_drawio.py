#!/usr/bin/env python3
"""Validate uncompressed draw.io XML with Python standard library only."""

from __future__ import annotations

import argparse
import json
import math
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple


@dataclass(frozen=True)
class Box:
    cell_id: str
    parent_id: str
    x: float
    y: float
    width: float
    height: float


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def style_tokens(style: str) -> Dict[str, str]:
    result: Dict[str, str] = {}
    for token in style.split(";"):
        if "=" in token:
            key, value = token.split("=", 1)
            result[key.strip()] = value.strip()
    return result


def finite_number(raw: Optional[str]) -> Optional[float]:
    if raw is None or raw == "":
        return 0.0
    try:
        value = float(raw)
    except ValueError:
        return None
    return value if math.isfinite(value) else None


def graph_models(root: ET.Element) -> Tuple[List[Tuple[str, ET.Element]], List[str]]:
    name = local_name(root.tag)
    if name == "mxGraphModel":
        return [("page-1", root)], []
    if name != "mxfile":
        return [], [f"Unsupported root element <{name}>."]

    models: List[Tuple[str, ET.Element]] = []
    errors: List[str] = []
    diagrams = [child for child in root if local_name(child.tag) == "diagram"]
    if not diagrams:
        return [], ["<mxfile> does not contain any <diagram> pages."]

    for index, diagram in enumerate(diagrams, start=1):
        page_name = diagram.get("name") or f"page-{index}"
        nested = next(
            (child for child in diagram if local_name(child.tag) == "mxGraphModel"),
            None,
        )
        if nested is not None:
            models.append((page_name, nested))
            continue

        text = (diagram.text or "").strip()
        if text.startswith("<mxGraphModel"):
            try:
                models.append((page_name, ET.fromstring(text)))
            except ET.ParseError as exc:
                errors.append(f"[{page_name}] Invalid embedded mxGraphModel: {exc}.")
        else:
            errors.append(
                f"[{page_name}] Compressed or unrecognized diagram content is not supported. "
                "Save as uncompressed XML before validation."
            )
    return models, errors


def cell_geometry(cell: ET.Element) -> Optional[ET.Element]:
    return next(
        (child for child in cell if local_name(child.tag) == "mxGeometry"),
        None,
    )


def overlap(a: Box, b: Box, tolerance: float = 1.0) -> bool:
    overlap_x = min(a.x + a.width, b.x + b.width) - max(a.x, b.x)
    overlap_y = min(a.y + a.height, b.y + b.height) - max(a.y, b.y)
    return overlap_x > tolerance and overlap_y > tolerance


def validate_page(page_name: str, model: ET.Element) -> Tuple[List[str], List[str], Dict[str, int]]:
    errors: List[str] = []
    warnings: List[str] = []
    cells = [element for element in model.iter() if local_name(element.tag) == "mxCell"]
    ids = [cell.get("id", "") for cell in cells]
    id_counts = Counter(ids)

    if not cells:
        errors.append(f"[{page_name}] No <mxCell> elements found.")
        return errors, warnings, {"cells": 0, "vertices": 0, "edges": 0}

    if "" in id_counts:
        errors.append(f"[{page_name}] One or more mxCell elements have no id.")
    duplicates = sorted(cell_id for cell_id, count in id_counts.items() if cell_id and count > 1)
    if duplicates:
        errors.append(f"[{page_name}] Duplicate cell IDs: {', '.join(duplicates)}.")

    id_set = {cell_id for cell_id in ids if cell_id}
    for required in ("0", "1"):
        if required not in id_set:
            errors.append(f'[{page_name}] Missing required root cell id="{required}".')

    child_ids = {cell.get("parent", "") for cell in cells if cell.get("parent")}
    boxes: List[Box] = []
    fill_colors = set()
    font_sizes = set()
    vertices = 0
    edges = 0

    for cell in cells:
        cell_id = cell.get("id", "<missing>")
        parent_id = cell.get("parent")
        source_id = cell.get("source")
        target_id = cell.get("target")
        is_vertex = cell.get("vertex") == "1"
        is_edge = cell.get("edge") == "1"
        style = style_tokens(cell.get("style", ""))

        for attribute, reference in (
            ("parent", parent_id),
            ("source", source_id),
            ("target", target_id),
        ):
            if reference and reference not in id_set:
                errors.append(
                    f'[{page_name}] Cell "{cell_id}" has dangling {attribute}="{reference}".'
                )

        if is_edge:
            edges += 1
            if not source_id or not target_id:
                warnings.append(
                    f'[{page_name}] Edge "{cell_id}" has no complete source and target pair.'
                )

        if not is_vertex:
            continue

        vertices += 1
        geometry = cell_geometry(cell)
        if geometry is None:
            errors.append(f'[{page_name}] Vertex "{cell_id}" has no mxGeometry.')
            continue

        x = finite_number(geometry.get("x"))
        y = finite_number(geometry.get("y"))
        width = finite_number(geometry.get("width"))
        height = finite_number(geometry.get("height"))
        if None in (x, y, width, height):
            errors.append(f'[{page_name}] Vertex "{cell_id}" has non-numeric geometry.')
            continue
        if width <= 0 or height <= 0:
            errors.append(f'[{page_name}] Vertex "{cell_id}" must have positive width and height.')
            continue

        boxes.append(
            Box(
                cell_id=cell_id,
                parent_id=parent_id or "",
                x=float(x),
                y=float(y),
                width=float(width),
                height=float(height),
            )
        )

        fill = style.get("fillColor")
        if fill and fill.lower() not in {"none", "default"}:
            fill_colors.add(fill.lower())

        font_size = style.get("fontSize")
        if font_size:
            parsed_size = finite_number(font_size)
            if parsed_size is None:
                warnings.append(f'[{page_name}] Vertex "{cell_id}" has invalid fontSize.')
            else:
                font_sizes.add(parsed_size)
                if parsed_size > 18:
                    warnings.append(
                        f'[{page_name}] Vertex "{cell_id}" uses fontSize={font_size}; '
                        "keep large text in one dedicated title area."
                    )

        if (
            "resourceIcon" in (cell.get("style") or "")
            and style.get("aspect") != "fixed"
        ):
            warnings.append(
                f'[{page_name}] Resource icon "{cell_id}" is missing aspect=fixed.'
            )

    leaf_boxes = [box for box in boxes if box.cell_id not in child_ids]
    by_parent: Dict[str, List[Box]] = defaultdict(list)
    for box in leaf_boxes:
        by_parent[box.parent_id].append(box)

    for siblings in by_parent.values():
        for index, first in enumerate(siblings):
            for second in siblings[index + 1 :]:
                if overlap(first, second):
                    warnings.append(
                        f'[{page_name}] Sibling vertices "{first.cell_id}" and '
                        f'"{second.cell_id}" overlap.'
                    )

    box_by_id = {box.cell_id: box for box in boxes}
    for box in boxes:
        parent = box_by_id.get(box.parent_id)
        if not parent:
            continue
        if (
            box.x < -1
            or box.y < -1
            or box.x + box.width > parent.width + 1
            or box.y + box.height > parent.height + 1
        ):
            warnings.append(
                f'[{page_name}] Vertex "{box.cell_id}" spills outside parent '
                f'"{parent.cell_id}".'
            )

    if len(fill_colors) > 8:
        warnings.append(
            f"[{page_name}] Diagram uses {len(fill_colors)} fill colors; target 8 or fewer."
        )
    if len(font_sizes) > 4:
        warnings.append(
            f"[{page_name}] Diagram uses {len(font_sizes)} font sizes; target 4 or fewer."
        )

    return errors, warnings, {"cells": len(cells), "vertices": vertices, "edges": edges}


def validate_xml(xml_text: str) -> Dict[str, object]:
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as exc:
        return {
            "ok": False,
            "errors": [f"Invalid XML: {exc}."],
            "warnings": [],
            "pages": 0,
            "summary": {"cells": 0, "vertices": 0, "edges": 0},
        }

    models, model_errors = graph_models(root)
    errors = list(model_errors)
    warnings: List[str] = []
    summary = {"cells": 0, "vertices": 0, "edges": 0}

    for page_name, model in models:
        page_errors, page_warnings, page_summary = validate_page(page_name, model)
        errors.extend(page_errors)
        warnings.extend(page_warnings)
        for key in summary:
            summary[key] += page_summary[key]

    return {
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "pages": len(models),
        "summary": summary,
    }


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate uncompressed draw.io XML without external dependencies."
    )
    parser.add_argument("path", help="Path to .drawio/.xml, or - to read stdin.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return a nonzero exit code when warnings are present.",
    )
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    if args.path == "-":
        xml_text = sys.stdin.read()
    else:
        try:
            xml_text = Path(args.path).read_text(encoding="utf-8")
        except OSError as exc:
            print(json.dumps({"ok": False, "errors": [str(exc)], "warnings": []}, indent=2))
            return 2

    result = validate_xml(xml_text)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    if result["errors"]:
        return 1
    if args.strict and result["warnings"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
