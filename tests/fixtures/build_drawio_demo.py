#!/usr/bin/env python3
"""Build a fictional AWS demo through the bundled offline catalog and router."""

import argparse
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "core/skills/creating-diagrams/scripts"))
from cloud_catalog import search
from route_drawio import route_model
from validate_drawio import validate_xml


def build_demo():
    mxfile = ET.Element("mxfile")
    diagram = ET.SubElement(mxfile, "diagram", {"id": "aws-demo", "name": "AWS serverless — illustrative"})
    model = ET.SubElement(diagram, "mxGraphModel", {"grid": "1", "gridSize": "10", "page": "1", "pageWidth": "1200", "pageHeight": "610", "background": "#FFFFFF"})
    root = ET.SubElement(model, "root")
    ET.SubElement(root, "mxCell", {"id": "0"})
    ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})

    def vertex(name, label, x, y, w, h, style, parent="1"):
        cell = ET.SubElement(root, "mxCell", {"id": name, "value": label, "vertex": "1", "parent": parent, "style": style})
        ET.SubElement(cell, "mxGeometry", {"as": "geometry", "x": str(x), "y": str(y), "width": str(w), "height": str(h)})

    def icon(name, query, label, x, y, parent="region"):
        item = search(query, "aws", "icon", 1)[0]
        scale = 56 / max(item["w"], item["h"])
        vertex(name, label, x, y, item["w"] * scale, item["h"] * scale, item["style"], parent)

    vertex("title", "AWS serverless application", 40, 20, 1100, 36,
           "text;html=1;align=left;verticalAlign=middle;fontSize=18;fontStyle=1;fillColor=none;strokeColor=none;")
    vertex("subtitle", "Illustrative architecture · native AWS icons · offline connector routing", 40, 58, 1100, 26,
           "text;html=1;align=left;fontSize=12;fontColor=#64748B;fillColor=none;strokeColor=none;")
    region_style = search("region", "aws", "group", 1)[0]["style"]
    vertex("region", "AWS Region", 400, 120, 740, 360, region_style + "startSize=38;")
    vertex("browser", "Browser / client", 40, 350, 120, 56,
           "rounded=1;whiteSpace=wrap;html=1;fillColor=#F1F5F9;strokeColor=#94A3B8;fontColor=#334155;fontSize=12;")
    icon("cloudfront", "cloudfront", "CloudFront", 240, 350, "1")
    icon("s3", "s3", "S3 static assets", 50, 80)
    icon("apigw", "api gateway", "API Gateway", 50, 230)
    icon("lambda", "lambda", "Lambda\nAPI handler", 240, 230)
    icon("dynamodb", "dynamodb", "DynamoDB", 430, 230)
    icon("sqs", "sqs", "SQS", 430, 80)
    icon("worker", "lambda", "Lambda\nBackground worker", 630, 80)
    for i, (source, target, label) in enumerate([
        ("browser", "cloudfront", "HTTPS"), ("cloudfront", "s3", "static origin"),
        ("cloudfront", "apigw", "API origin"), ("apigw", "lambda", "invoke"),
        ("lambda", "dynamodb", "read / write"), ("lambda", "sqs", "enqueue"),
        ("sqs", "worker", "consume"),
    ], 1):
        cell = ET.SubElement(root, "mxCell", {"id": f"e{i}", "source": source, "target": target, "edge": "1", "parent": "1", "value": label,
                             "style": "edgeStyle=orthogonalEdgeStyle;html=1;endArrow=block;endFill=1;fontSize=11;strokeWidth=1.5;strokeColor=#475569;fontColor=#334155;"})
        ET.SubElement(cell, "mxGeometry", {"as": "geometry", "relative": "1"})
    vertex("note", "CloudFront is global. Regional managed services are outside a VPC in this example.\nNo project infrastructure is asserted; this is a skill verification fixture.", 40, 530, 1100, 50,
           "text;html=1;align=left;fontSize=12;fontColor=#64748B;fillColor=none;strokeColor=none;")
    route_model(model)
    return mxfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    demo = build_demo()
    xml = ET.tostring(demo, encoding="unicode")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(xml, encoding="utf-8")
    import json
    result = validate_xml(xml, check_connectors=True)
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] and not result["warnings"] else 1


if __name__ == "__main__":
    sys.exit(main())
