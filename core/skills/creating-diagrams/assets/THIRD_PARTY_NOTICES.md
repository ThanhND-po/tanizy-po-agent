# Native Cloud Style Catalog

`native-cloud-catalog.json.gz` contains 1,844 verified style records, not icon
artwork or fetched logos. Source: [sparklabx/drawio-ai-kit](https://github.com/sparklabx/drawio-ai-kit)
commit `1a03d87b877ec738a2a98d38a4d8eeecf4ee66bc`, reviewed 2026-10-11.

- AWS styles: upstream `catalog/aws.json`, including 983 icons and 19 groups.
  The upstream catalog data structure/code is MIT, copyright (c) 2026 sparklabx.
  The license is reproduced in `LICENSE-drawio-ai-kit.txt`.
- Azure/Azure2 and GCP2 styles: native references extracted from upstream
  `data/shape-index.json.gz`. The index originates from
  [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp), via
  [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill), and is
  generated from the official draw.io libraries under Apache-2.0. The Apache
  license is reproduced in `LICENSE-Apache-2.0.txt`.
- The referenced AWS, Microsoft Azure and Google Cloud icons remain their owners'
  trademarks and are subject to their respective usage terms. These licenses do
  not relicense brand artwork or imply endorsement. No bitmap logo bundle is
  redistributed here. AWS terms: https://aws.amazon.com/architecture/icons/.

The gzip JSON's `meta` records the upstream commit and SHA-256 hashes of both
inputs. The maintainer helper `scripts/refresh-drawio-catalog.py` (at repository
root) rebuilds the catalog from a reviewed local checkout without making network
requests. On refresh, review source/license changes and update this notice,
the draw.io reference, and catalog tests. GCP2 coverage is intentionally limited;
Azure2 image paths refer to assets already shipped with draw.io.
