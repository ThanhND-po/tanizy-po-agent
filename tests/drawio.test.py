"""Regression tests for diagram correctness, offline icons and connector routing."""

import json
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / "core/skills/creating-diagrams/scripts"
sys.path.insert(0, str(SCRIPTS))

from cloud_catalog import load_catalog, search
from drawio_geometry import absolute_boxes, literal_path, tokens
from route_drawio import route_model
from validate_drawio import validate_xml
sys.path.insert(0, str(REPO / "tests/fixtures"))
from build_drawio_demo import build_demo


def model():
    root = ET.fromstring('<mxGraphModel><root><mxCell id="0"/><mxCell id="1" parent="0"/></root></mxGraphModel>')
    return root


def node(m, name, x, y, w=100, h=60, parent="1", style="", label=""):
    cell = ET.SubElement(m.find("root"), "mxCell", {"id": name, "vertex": "1", "parent": parent, "style": style, "value": label})
    ET.SubElement(cell, "mxGeometry", {"x": str(x), "y": str(y), "width": str(w), "height": str(h), "as": "geometry"})
    return cell


def edge(m, name, source, target, style="", points=(), parent="1", label=""):
    cell = ET.SubElement(m.find("root"), "mxCell", {"id": name, "edge": "1", "parent": parent, "source": source, "target": target, "style": style, "value": label})
    g = ET.SubElement(cell, "mxGeometry", {"relative": "1", "as": "geometry"})
    if points:
        array = ET.SubElement(g, "Array", {"as": "points"})
        for x, y in points:
            ET.SubElement(array, "mxPoint", {"x": str(x), "y": str(y)})
    return cell


def check(m, connectors=False):
    return validate_xml(ET.tostring(m, encoding="unicode"), connectors)


PINS = "edgeStyle=none;noEdgeStyle=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"


class OfflineCatalog(unittest.TestCase):
    def test_exact_service_beats_specialized_resource(self):
        for query, name in (("s3", "aws.s3"), ("lambda", "aws.lambda"), ("api gateway", "aws.api_gateway")):
            self.assertEqual(search(query, "aws", "icon", 1)[0]["name"], name)

    def test_unsupported_service_does_not_silently_substitute(self):
        self.assertEqual(search("imaginary quantum database", "aws"), [])
        self.assertEqual(search("cloud run", "gcp"), [])

    def test_catalog_is_offline_unique_and_has_provenance(self):
        catalog = load_catalog()
        names = [e["name"] for e in catalog["entries"]]
        self.assertEqual(len(names), len(set(names)))
        self.assertEqual(len(catalog["meta"]["commit"]), 40)
        self.assertEqual({e["provider"] for e in catalog["entries"]}, {"aws", "azure", "gcp"})
        for entry in catalog["entries"]:
            self.assertNotIn("data:image", entry["style"])
            self.assertNotIn("https://", entry["style"])

    def test_all_catalog_styles_are_recognized(self):
        # Check each glyph in isolation; layout/palette budgets are unrelated.
        for entry in load_catalog()["entries"]:
            m = model()
            node(m, "glyph", 20, 20, style=entry["style"] + ";aspect=fixed;")
            result = check(m)
            self.assertEqual(result["errors"], [], entry["name"])
            self.assertFalse(any("not verified" in w for w in result["warnings"]), entry["name"])

    def test_azure_and_gcp_search_return_exact_local_assets(self):
        self.assertIn("img/lib/azure2/", search("function apps", "azure", limit=1)[0]["style"])
        self.assertIn("mxgraph.gcp2.compute_engine_2", search("compute engine", "gcp", limit=1)[0]["style"])

    def test_unknown_cloud_style_and_recolor_are_reported(self):
        m = model()
        node(m, "fake", 20, 20, style="shape=mxgraph.aws4.nonexistent;aspect=fixed;")
        self.assertTrue(any("not verified" in w for w in check(m)["warnings"]))
        m = model()
        style = search("s3", "aws", limit=1)[0]["style"].replace("fillColor=#7AA116", "fillColor=#FF0000")
        node(m, "recolored", 20, 20, style=style)
        self.assertTrue(any("fillColor" in w for w in check(m)["warnings"]))


class Structure(unittest.TestCase):
    def test_multiple_pages_have_independent_ids(self):
        mxfile = ET.Element("mxfile")
        for name in ("one", "two"):
            ET.SubElement(mxfile, "diagram", {"name": name}).append(model())
        self.assertEqual(check(mxfile)["errors"], [])

    def test_duplicate_dangling_and_invalid_geometry_fail(self):
        m = model()
        node(m, "a", 0, 0)
        node(m, "a", 200, 0)
        edge(m, "e", "a", "missing")
        node(m, "nan", "NaN", 200)
        self.assertGreaterEqual(len(check(m)["errors"]), 3)

    def test_parent_cycle_fails_without_hanging(self):
        m = model()
        node(m, "a", 0, 0, parent="b")
        node(m, "b", 0, 0, parent="a")
        self.assertTrue(any("cycle" in e for e in check(m)["errors"]))

    def test_relative_edge_badges_do_not_count_as_absolute_overlap(self):
        m = model()
        node(m, "a", 0, 0)
        node(m, "b", 300, 0)
        e = edge(m, "e", "a", "b", PINS)
        badge = node(m, "badge", 0.5, 0, 24, 24, parent="e")
        badge.find("mxGeometry").set("relative", "1")
        self.assertEqual(check(m)["warnings"], [])

    def test_invalid_edge_waypoint_is_an_error(self):
        m = model()
        node(m, "a", 0, 0)
        node(m, "b", 300, 0)
        edge(m, "e", "a", "b", PINS, [("NaN", 30)])
        self.assertTrue(any("non-finite" in e for e in check(m)["errors"]))


class ConnectorAudit(unittest.TestCase):
    def test_crossing_at_a_waypoint_is_not_missed(self):
        m = model()
        node(m, "a", 0, 150)
        node(m, "b", 400, 150)
        node(m, "c", 200, 0)
        node(m, "d", 500, 350)
        edge(m, "horizontal", "a", "b", PINS)
        edge(m, "bent", "c", "d", "edgeStyle=none;noEdgeStyle=1;exitX=0.5;exitY=1;entryX=0;entryY=0.5;", [(250, 180), (350, 180), (350, 380)])
        self.assertTrue(any('"horizontal" and "bent"' in w for w in check(m, True)["warnings"]))

    def test_invalid_pin_offset_reports_error_instead_of_crashing(self):
        m = model()
        node(m, "a", 0, 100)
        node(m, "b", 300, 100)
        edge(m, "e", "a", "b", PINS + "exitDx=NaN;")
        self.assertTrue(any("invalid pin offset" in e for e in check(m, True)["errors"]))

    def test_relative_port_does_not_turn_its_node_into_a_passable_frame(self):
        m = model()
        node(m, "a", 0, 100)
        node(m, "obstacle", 180, 100)
        node(m, "port", 1, 0.5, 8, 8, parent="obstacle").find("mxGeometry").set("relative", "1")
        node(m, "b", 360, 100)
        edge(m, "e", "a", "b", PINS)
        self.assertTrue(any('crosses node "obstacle"' in w for w in check(m, True)["warnings"]))

    def test_unrelated_orthogonal_edges_cross(self):
        m = model()
        node(m, "a", 0, 150)
        node(m, "b", 400, 150)
        node(m, "c", 200, 0)
        node(m, "d", 200, 350)
        edge(m, "horizontal", "a", "b", PINS)
        edge(m, "vertical", "c", "d", "edgeStyle=none;noEdgeStyle=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;")
        self.assertTrue(any('"horizontal" and "vertical" cross' in w for w in check(m, True)["warnings"]))

    def test_literal_edge_through_node_is_caught(self):
        m = model()
        node(m, "a", 0, 100)
        node(m, "obstacle", 180, 100)
        node(m, "b", 360, 100)
        edge(m, "e", "a", "b", PINS)
        self.assertTrue(any('crosses node "obstacle"' in w for w in check(m, True)["warnings"]))

    def test_cross_parent_coordinates_are_resolved(self):
        m = model()
        node(m, "group", 200, 100, 500, 300, style="container=1;")
        node(m, "a", 0, 200)
        node(m, "obstacle", 0, 100, parent="group")
        node(m, "b", 380, 100, parent="group")
        edge(m, "e", "a", "b", PINS)
        self.assertTrue(any('crosses node "obstacle"' in w for w in check(m, True)["warnings"]))

    def test_edge_parent_offsets_apply_to_waypoints(self):
        m = model()
        node(m, "group", 200, 100, 500, 300, style="container=1;")
        node(m, "a", 20, 80, parent="group")
        node(m, "b", 300, 180, parent="group")
        e = edge(m, "e", "a", "b", PINS, [(200, 110), (200, 210)], parent="group")
        cells = {c.get("id"): c for c in m.iter("mxCell")}
        self.assertEqual(literal_path(e, absolute_boxes(cells)), [(320, 210), (400, 210), (400, 310), (500, 310)])

    def test_diagonal_and_wrong_terminal_are_reported(self):
        m = model()
        node(m, "a", 0, 100)
        node(m, "b", 300, 200)
        e = edge(m, "e", "a", "b", PINS)
        self.assertTrue(any("diagonal" in w for w in check(m, True)["warnings"]))
        e.find("mxGeometry").append(ET.fromstring('<Array as="points"><mxPoint x="100" y="230"/></Array>'))
        self.assertTrue(any("wrong direction" in w for w in check(m, True)["warnings"]))

    def test_render_controlled_path_is_explicitly_skipped(self):
        m = model()
        node(m, "a", 0, 100)
        node(m, "b", 300, 100)
        edge(m, "e", "a", "b", PINS.replace("edgeStyle=none;noEdgeStyle=1", "edgeStyle=orthogonalEdgeStyle"))
        self.assertEqual(check(m, True)["summary"]["renderer_routes_skipped"], 1)
        self.assertEqual(check(m, True)["summary"]["literal_routes_checked"], 0)

    def test_stacked_ports_and_shared_segments_are_caught(self):
        m = model()
        node(m, "a", 0, 100)
        node(m, "b", 300, 100)
        edge(m, "e1", "a", "b", PINS)
        edge(m, "e2", "a", "b", PINS)
        warnings = check(m, True)["warnings"]
        self.assertTrue(any("crowd" in w for w in warnings))
        self.assertTrue(any("overlapping segments" in w for w in warnings))


class Routing(unittest.TestCase):
    def test_aligned_spine_stays_straight_when_another_edge_branches(self):
        m = model()
        node(m, "hub", 0, 200)
        node(m, "straight", 400, 200)
        node(m, "above", 400, 0)
        spine = edge(m, "spine", "hub", "straight")
        edge(m, "branch", "hub", "above")
        route_model(m)
        self.assertEqual(float(tokens(spine.get("style"))["exitY"]), 0.5)
        self.assertIsNone(spine.find("mxGeometry/Array[@as='points']"))
        self.assertEqual(check(m, True)["warnings"], [])

    def test_impossible_fixed_port_does_not_fall_back_to_crossing_a_caption(self):
        m = model()
        node(m, "glyph", 0, 0, 48, 48, style="verticalLabelPosition=bottom;fontSize=12;", label="Caption below")
        node(m, "b", 0, 200)
        edge(m, "e", "glyph", "b", "exitX=0.5;exitY=1;entryX=0.5;entryY=0;")
        with self.assertRaises(ValueError):
            route_model(m)

    def test_fanout_is_ordered_by_target_position(self):
        m = model()
        node(m, "hub", 0, 100, 100, 100)
        node(m, "bottom", 400, 180)
        node(m, "top", 400, 20)
        e1 = edge(m, "first-in-xml", "hub", "bottom")
        e2 = edge(m, "second-in-xml", "hub", "top")
        route_model(m)
        self.assertLess(float(tokens(e2.get("style"))["exitY"]), float(tokens(e1.get("style"))["exitY"]))
        self.assertEqual(check(m, True)["warnings"], [])

    def test_aws_demo_has_verified_icons_and_seven_clear_routes(self):
        result = check(build_demo(), True)
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["warnings"], [])
        self.assertEqual(result["summary"]["literal_routes_checked"], 7)

    def test_avoids_obstacle_without_changing_semantics(self):
        m = model()
        node(m, "a", 0, 100)
        node(m, "obstacle", 180, 100)
        node(m, "b", 360, 100)
        e = edge(m, "e", "a", "b", "edgeStyle=orthogonalEdgeStyle;endArrow=open;startArrow=none;dashed=1;", label="request")
        report = route_model(m)
        self.assertEqual(report["routed"], ["e"])
        self.assertEqual((e.get("source"), e.get("target")), ("a", "b"))
        style = tokens(e.get("style"))
        self.assertEqual((style["endArrow"], style["startArrow"], style["dashed"]), ("open", "none", "1"))
        result = check(m, True)
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["warnings"], [])
        self.assertEqual(result["summary"]["literal_routes_checked"], 1)

    def test_fanout_gets_distinct_side_ports(self):
        m = model()
        node(m, "hub", 0, 160, 120, 120)
        for i, y in enumerate((0, 180, 360)):
            node(m, f"target{i}", 400, y)
            edge(m, f"e{i}", "hub", f"target{i}")
        route_model(m)
        self.assertEqual(check(m, True)["warnings"], [])

    def test_avoids_caption_band(self):
        m = model()
        node(m, "a", 0, 160)
        node(m, "glyph", 220, 100, 48, 48, style="verticalLabelPosition=bottom;fontSize=12;", label="Long service caption")
        node(m, "b", 400, 160)
        edge(m, "e", "a", "b")
        route_model(m)
        self.assertEqual(check(m, True)["warnings"], [])

    def test_specialized_edges_are_preserved(self):
        m = model()
        node(m, "a", 0, 0)
        node(m, "b", 400, 0)
        e = edge(m, "e", "a", "b", "edgeStyle=entityRelationEdgeStyle;endArrow=ERmany;")
        before = ET.tostring(e)
        self.assertEqual(route_model(m)["skipped"], ["e"])
        self.assertEqual(ET.tostring(e), before)

    def test_cli_preserves_input_and_strict_exit_status(self):
        m = model()
        node(m, "a", 0, 100)
        node(m, "obstacle", 180, 100)
        node(m, "b", 360, 100)
        edge(m, "e", "a", "b", PINS)
        with tempfile.TemporaryDirectory() as temp:
            source, output = Path(temp) / "draft.drawio", Path(temp) / "routed.drawio"
            original = ET.tostring(m)
            source.write_bytes(original)
            result = subprocess.run([sys.executable, "-B", str(SCRIPTS / "route_drawio.py"), str(source), "--output", str(output)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(source.read_bytes(), original)
            good = subprocess.run([sys.executable, "-B", str(SCRIPTS / "validate_drawio.py"), str(output), "--strict", "--connectors"], capture_output=True, text=True)
            bad = subprocess.run([sys.executable, "-B", str(SCRIPTS / "validate_drawio.py"), str(source), "--strict", "--connectors"], capture_output=True, text=True)
            self.assertEqual(good.returncode, 0, good.stdout)
            self.assertEqual(bad.returncode, 1)
            same = subprocess.run([sys.executable, "-B", str(SCRIPTS / "route_drawio.py"), str(source), "--output", str(source)], capture_output=True, text=True)
            self.assertEqual(same.returncode, 1)
            self.assertEqual(source.read_bytes(), original)


class InstalledSkill(unittest.TestCase):
    def test_helpers_execute_from_each_installed_skill(self):
        for target in ("codex", "claude-code", "antigravity"):
            with self.subTest(target=target), tempfile.TemporaryDirectory() as temp:
                project = Path(temp)
                install = subprocess.run(["node", str(REPO / "scripts/install.mjs"), "--target", target,
                                          "--project", str(project), "--skill", "creating-diagrams"], capture_output=True, text=True)
                self.assertEqual(install.returncode, 0, install.stderr)
                folder = ".claude" if target == "claude-code" else ".agents"
                installed = project / folder / "skills/creating-diagrams/scripts"
                lookup = subprocess.run([sys.executable, "-B", str(installed / "cloud_catalog.py"), "s3", "--provider", "aws", "--limit", "1"],
                                        cwd=temp, capture_output=True, text=True)
                self.assertEqual(lookup.returncode, 0, lookup.stderr)
                self.assertEqual(json.loads(lookup.stdout)["s3"][0]["name"], "aws.s3")
                source, output = project / "demo.drawio", project / "routed.drawio"
                source.write_bytes(ET.tostring(build_demo()))
                routed = subprocess.run([sys.executable, "-B", str(installed / "route_drawio.py"), str(source), "--output", str(output)],
                                        cwd=temp, capture_output=True, text=True)
                self.assertEqual(routed.returncode, 0, routed.stdout + routed.stderr)
                validation = subprocess.run([sys.executable, "-B", str(installed / "validate_drawio.py"), str(output), "--strict", "--connectors"],
                                            cwd=temp, capture_output=True, text=True)
                self.assertEqual(validation.returncode, 0, validation.stdout + validation.stderr)


if __name__ == "__main__":
    unittest.main()
