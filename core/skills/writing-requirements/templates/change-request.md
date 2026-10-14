---
id: CR-YYYY-NNN
title: "[Change Request Name]"
document_type: change-request
status: draft
priority: critical | high | medium | low
requested_by: "[Requester Name]"
requested_date: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [change-request]
---

# CR-YYYY-NNN: [Change Request Name]

<!-- Adapt the sample frontmatter, document_type, IDs, field names and status/labels to the target project schema; omit fields that do not apply. Apply ../references/document-metadata.md and project policy. draft is a new-draft example. Add completed_date only when known; completion does not prove PROD release. Add approval_status separately only when known. -->

## Metadata

| Field | Value |
|---|---|
| Status | Draft |

## Overview

| Field | Value |
|---|---|
| Related Feedback / Jira | [Jira ID / Feedback ID] - [Brief summary of customer/user request] |
| Primary Persona | [Who is the primary actor this impacts?] |
| Target Release | [Release version or sprint] |

## User Story
- As a **[role]**, I want to **[action]** so that **[benefit]**.

## Acceptance Criteria
- [Acceptance criterion 1]
- [Acceptance criterion 2]

## Background / Context
- [Why is this change needed? What is the current problem or limitation?]

## Change Description
- [Detailed description of what needs to be changed]

## Affected Modules
- `[Module A]` - [Specific impact description]
- `[Module B]` - [Specific impact description]

## Requirements Changes
- `[REQ-XXX-001]` - **Modified**: [Description of change]
- `[REQ-XXX-NNN]` - **New**: [New requirement description]
- `[REQ-XXX-002]` - **Deprecated**: [Reason for deprecation]

## Impact Analysis

### Affected Data Entities
- `[Entity Name]` - [What changed: added field, logic change, etc.]

### Affected Integration Points
- `[Module A]` → `[Module B]`: [Description of change]

### Dependencies to Consider
- `[Module C]` depends on `[Module A]` → needs verification
- [List any other modules with dependencies that require checking]

## Estimation
- **Effort**: [XS / S / M / L / XL / XXL] *(Refer to estimation-guide.md)*
- **Timeline**: [Estimated time or target date]

## Open Questions & Risks
- [List any unknowns blocking implementation or risks involved]

## Notes
- [Additional notes, references, screenshots, links, etc.]
