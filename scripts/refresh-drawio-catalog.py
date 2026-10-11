#!/usr/bin/env python3
"""Refresh the offline native-style catalog from a reviewed, local upstream checkout."""

import argparse
import gzip
import hashlib
import json
import re
import subprocess
from pathlib import Path


def build_catalog(checkout):
    aws_path = checkout / "catalog/aws.json"
    index_path = checkout / "data/shape-index.json.gz"
    aws = json.loads(aws_path.read_text(encoding="utf-8"))
    index = json.loads(gzip.decompress(index_path.read_bytes()))
    entries = []
    for kind, rows in (("group", aws["groups"]), ("icon", aws["icons"])):
        for row in rows:
            entries.append({**row, "name": "aws." + row["name"], "provider": "aws", "kind": kind})
    seen = set()
    for row in index:
        style = row["style"]
        shape = re.search(r"(?:^|;)shape=(mxgraph\.(?:azure|gcp2)\.[^;]+)", style)
        image = re.search(r"(?:^|;)image=(img/lib/azure2/[^;]+)", style)
        if not (shape or image) or row.get("type") != "vertex":
            continue
        ref = (shape or image).group(1)
        if ref in seen:
            continue
        seen.add(ref)
        provider = "gcp" if ref.startswith("mxgraph.gcp2.") else "azure"
        # Preserve paths in names: same Azure label can occur in several categories.
        name = ref.removeprefix("mxgraph.").removeprefix("img/lib/").removesuffix(".svg")
        name = re.sub(r"[^a-z0-9]+", ".", name.lower()).strip(".")
        entries.append({"name": name, "provider": provider, "kind": "icon",
                        "label": row["title"], "tags": row.get("tags", ""),
                        "style": style, "w": row["w"], "h": row["h"]})
    commit = subprocess.check_output(["git", "-C", str(checkout), "rev-parse", "HEAD"], text=True).strip()
    return {"meta": {"upstream": "https://github.com/sparklabx/drawio-ai-kit",
                     "commit": commit, "scope": "AWS catalog + native Azure/Azure2 and GCP2 index entries; no bundled bitmap logos",
                     "inputs_sha256": {str(p.relative_to(checkout)): hashlib.sha256(p.read_bytes()).hexdigest()
                                       for p in (aws_path, index_path)}},
            "entries": sorted(entries, key=lambda entry: entry["name"])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkout", type=Path, help="Local drawio-ai-kit checkout; no downloads are performed.")
    args = parser.parse_args()
    catalog = build_catalog(args.checkout.resolve())
    target = Path(__file__).resolve().parents[1] / "core/skills/creating-diagrams/assets/native-cloud-catalog.json.gz"
    target.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(catalog, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    target.write_bytes(gzip.compress(data, mtime=0))
    print(json.dumps({"path": str(target), "entries": len(catalog["entries"]), "bytes": target.stat().st_size,
                      "commit": catalog["meta"]["commit"]}))


if __name__ == "__main__":
    main()
