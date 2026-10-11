#!/usr/bin/env python3
"""Search verified native cloud styles offline. Python standard library only."""

import argparse
import gzip
import json
import re
import unicodedata
from functools import lru_cache
from pathlib import Path


@lru_cache(maxsize=1)
def load_catalog():
    path = Path(__file__).resolve().parents[1] / "assets/native-cloud-catalog.json.gz"
    return json.loads(gzip.decompress(path.read_bytes()))


def normalized(text):
    return re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", text).lower()).strip()


def search(query, provider=None, kind=None, limit=5):
    q = normalized(query)
    if not q:
        return []
    ranked = []
    for entry in load_catalog()["entries"]:
        if provider and entry["provider"] != provider or kind and entry["kind"] != kind:
            continue
        name, label = normalized(entry["name"]), normalized(entry["label"])
        haystack = normalized(" ".join(str(entry.get(key, "")) for key in ("name", "label", "tags", "category")))
        if not all(token in haystack.split() for token in q.split()):
            continue
        score = 100 * (query.lower() == entry["name"].lower()) + 60 * (q == label)
        score += 80 * (q == normalized(entry["name"].split(".", 1)[-1]))
        score += 40 * (q == name or name.endswith(" " + q)) + 10 * (q in label)
        # Prefer the current Azure2 library to legacy Azure shapes on equivalent matches.
        score += 2 * entry["name"].startswith("azure2.")
        ranked.append((score, entry["name"], entry))
    ranked.sort(key=lambda item: (-item[0], item[1]))
    return [entry for _, _, entry in ranked[:limit]]


def style_signature(style):
    tokens = dict(token.split("=", 1) for token in style.split(";") if "=" in token)
    return tuple((key, tokens[key]) for key in ("shape", "resIcon", "image") if tokens.get(key))


@lru_cache(maxsize=1)
def indexed_styles():
    return {style_signature(entry["style"]): entry for entry in load_catalog()["entries"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help='Service name or comma-separated names: "s3, lambda, api gateway".')
    parser.add_argument("--provider", choices=("aws", "azure", "gcp"))
    parser.add_argument("--kind", choices=("icon", "group"))
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be positive")
    queries = [query.strip() for query in args.query.split(",") if query.strip()]
    result = {query: search(query, args.provider, args.kind, args.limit) for query in queries}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result and all(result.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
