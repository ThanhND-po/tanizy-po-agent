# Cloud Architecture: Facts, Icons and Boundaries

Read with `drawio.md` for AWS, Azure, GCP and mixed architecture diagrams.

## Establish what the diagram asserts

Distinguish a logical component view from a deployment/network view. Show only
confirmed services, regions, accounts/projects, zones, subnets, protocols and
directions. A nice template is a layout reference, not evidence that the system
uses Multi-AZ, NAT, an Internet Gateway, a private endpoint or a failover route.
Label a fictional demonstration as an illustrative architecture.

## Resolve icons before building

**Installed engine:** read `drawio-ai workflow` and
`drawio-ai principles --mode aws|azure|gcp|databricks` for the selected domain.
Batch searches, then use the exact returned `name` and style. Avoid unapproved
`logo`/CDN fetching. Check available commands with the installed CLI's help.

```bash
drawio-ai search "s3, lambda, api gateway"
drawio-ai scaffold --list
```

**Offline fallback:** the bundled native-style catalog is searchable without
Node, network access or the upstream runtime:

```bash
python3 <skill-directory>/scripts/cloud_catalog.py "s3, lambda, api gateway" --provider aws --kind icon --limit 2
python3 <skill-directory>/scripts/cloud_catalog.py "vpc, region" --provider aws --kind group
python3 <skill-directory>/scripts/cloud_catalog.py "virtual machine, function apps" --provider azure --limit 2
python3 <skill-directory>/scripts/cloud_catalog.py "compute engine, big query" --provider gcp --limit 2
```

Results contain exact `style`, intrinsic `w/h`, label, provider and catalog name.
Use the returned style verbatim for the glyph; add `aspect=fixed` where absent.
Scale width and height proportionally into a consistent 48–64 px icon area;
reserve a separate caption band. Keep official fills, strokes, image paths and
resource identifiers. Containers grow around children instead of being scaled
like icons. For repeated regions/zones, align equivalent tiers and node sizes.

Check the semantic match, not just the first search hit. A resource-specific icon
(e.g. an S3 access point) is different from the service icon. Search returns no
result and a nonzero status for an unsupported term; use a clearly named general
box or a newer installed catalog rather than guessing a stencil ID.

The offline snapshot contains the upstream AWS catalog, native Azure/Azure2
styles (including draw.io-local `img/lib/azure2/...svg` paths), and a **limited,
older native GCP2 set**. It is not the entire upstream bitmap catalog and does not
promise current coverage of every cloud product. Assets are resolved by draw.io;
verify compatibility in the target editor and render before claiming success.
The catalog has provenance and licenses in `assets/THIRD_PARTY_NOTICES.md`.

## Containment checks

| Domain | Boundaries and placement to verify |
|---|---|
| AWS | Account / Region / VPC / AZ / Subnet where they are in scope. An AZ spans VPCs in reality; within one VPC, AZ columns are a visual grouping of its subnets. Subnets reside in one AZ. Global services such as CloudFront and Route 53 sit outside a Region boundary. Regional managed services such as S3, DynamoDB and SQS normally sit outside the VPC. A VPC endpoint inside a subnet is a separate resource from the service it reaches. |
| Azure | Subscription / Resource Group / VNet / Subnet as applicable. Resource Groups are management boundaries, not mandatory network parents. Show a managed PaaS service outside the subnet unless its confirmed deployment mode injects it there; a private endpoint is a separate subnet resource. Do not force AWS's AZ→Subnet hierarchy onto Azure. |
| GCP | Organization / Folder / Project as applicable. VPC networks are global; subnets are regional and span zones. Put zonal compute inside a zone only when specified. Do not nest a global VPC inside a single region simply to mimic AWS. |
| Mixed / OSS | Keep provider ownership and on-premise boundaries distinct. Label self-managed software with its confirmed host/runtime. Use neutral component boxes if no verified brand asset exists. |

These are review checks, not permission to infer infrastructure. Do not assume
public/private status from a frame color. A deployment view needs confirmed
routing/exposure; a logical view can omit that detail explicitly.

## Review architecture and readability independently

- Compare every service and link with the fact list, including direction and
  protocol when supplied. Mark unknown relationships instead of inventing them.
- Use neutral scope frames and official icon colors. Avoid one large frame per
  service; pack related services while retaining captions and route corridors.
- Keep arrowheads on the resource that the relationship actually reaches. Move
  a heavily connected glyph, enlarge it moderately, or split the view before
  retargeting a line to a broader boundary.
- Show numbered paths only when ordering is meaningful; do not imply synchronous
  request ordering for independent event consumers.
- Render locally and inspect blank icons, caption clipping, arrow direction,
  repeated-zone consistency and boundaries. XML/catalog PASS alone is insufficient.

Primary references: [AWS icon resources](https://aws.amazon.com/architecture/icons/),
[AWS VPC subnets](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html),
[Azure virtual network concepts](https://learn.microsoft.com/en-us/azure/virtual-network/concepts-and-best-practices),
[GCP VPC overview](https://cloud.google.com/vpc/docs/overview).
