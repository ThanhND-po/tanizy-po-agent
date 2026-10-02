---
name: artifact-update-process
description: Use when applying feedback, change requests, or review comments to existing requirement artifacts, specifications, or project documentation, ensuring document statuses, frontmatter metadata, cross-references, and index catalogs remain consistent.
---

# Artifact Update Process

Manage structured updates to existing requirement artifacts, specifications, and project documentation when applying review feedback, change requests, or status updates.

## Hard Gates

- **[No Arbitrary Overwrite]** If incoming feedback or a requested change conflicts with an existing approved requirement, locked decision, or Decision Log entry, do not overwrite it silently. Stop, highlight the conflict, and ask the user for explicit resolution before updating.
- **[Scope Identification First]** Before editing any file, identify all directly and indirectly impacted artifacts (blast radius), including parent docs, child specs, diagrams, and index files.
- **[Metadata Integrity]** Every updated artifact must maintain or update its YAML frontmatter / metadata header (such as `status`, `version`, `last_updated`, and `changelog`). Ensure no corrupted or invisible characters exist.
- **[Index Synchronization]** Never leave index or catalog files out of sync. When an artifact changes status or scope, discover and update the corresponding index files (e.g., `README.md`, `master-index.md`, `docs/index.md`).
- **[Approval Before Write]** Do not write or overwrite files until the user reviews and approves the proposed changes and confirms the target paths.

## Workflow

### 1. Discover Context & Map Scope

- Inspect the user feedback, change request, or review comments.
- Locate the primary artifact(s) to be updated.
- Search for project catalog and index files:
  - Check for `master-index.md`, `README.md`, `docs/index.md`, or project-specific document tracking tables.
  - If a specific index file mentioned in feedback is missing, locate the existing documentation registry or fallback to the parent directory `README.md`.
- Identify linked dependencies:
  - Parent Epics, child User Stories, linked Use Cases, Basic Designs, API Specs, Data Dictionaries, or Decision Logs.
  - Confirm the list of in-scope files with the user if the impact radius is broad or ambiguous.

### 2. Conflict & Decision Review Gate

Before drafting any changes, compare the feedback against current artifact content:

- Check if the feedback reverses an earlier approved decision or contradicts another active requirement.
- If a conflict is found:
  1. Clearly state the existing decision (with source file and line reference if available).
  2. Contrast it with the requested change.
  3. Explain the potential impact or trade-offs.
  4. Ask the user whether to supersede the previous decision, create a new variant, or reject/modify the feedback.
- Do not proceed with drafting until the conflict resolution is agreed upon.

### 3. Draft Document Updates & State Transitions

- Update the YAML frontmatter / metadata header according to project standards:
  - `status`: Transition the document state appropriately (e.g., `DRAFT`, `IN_REVIEW`, `APPROVED`, `UPDATED`, `DEPRECATED`).
  - `version`: Increment version following project convention (e.g., patch for minor clarifications/fixes, minor for functional changes, major for breaking redesigns).
  - `last_updated`: Update to current date (`YYYY-MM-DD`).
  - `changelog` / `revision_history`: Add an entry summarizing the change, date, and reason.
- Apply the content modifications:
  - Preserve existing structure, terminology, and formatting conventions.
  - For tabular requirements (such as Basic Design), maintain single-line cell rules and structured separators.
  - Mark superseded requirements or add notes where historical context is important.

### 4. Synchronize Index Catalogs & Cross-References

- Update all relevant index/catalog files identified in Step 1:
  - Update status badges, status columns, or version indicators.
  - Ensure links point to correct relative paths.
  - Update document description or scope if the feature definition changed.
- If an identifier changed (e.g., Story ID, AC ID), update references in related artifacts to prevent broken links.

### 5. Review & User Confirmation Gate

- Present a concise diff or summary of changes to the user:
  - Files modified and new/updated statuses.
  - Key requirement changes and conflict resolutions.
  - Updated index entries.
- Ask in Vietnamese by default (or the project's established language).
- Write files only after the user approves the diff and confirms destination paths.

## Metadata Standards

When an artifact uses YAML frontmatter, ensure it follows this standard structure:

```yaml
---
id: REQ-001
title: Document Title
status: UPDATED # DRAFT | IN_REVIEW | APPROVED | UPDATED | DEPRECATED
version: 1.1.0
last_updated: 2026-10-02
changelog:
  - version: 1.1.0
    date: 2026-10-02
    summary: Updated Acceptance Criteria based on review feedback.
---
```

If the project uses an inline Markdown table for metadata instead of YAML, update that table consistently.

## Quality Checklist

Before finalizing:
- [ ] No zero-width spaces (`\u200b`) or invalid characters in frontmatter or markdown.
- [ ] Conflicting decisions were surfaced and approved by the user, not silently overwritten.
- [ ] Document status, version, and date accurately reflect the updates.
- [ ] All in-scope files and cross-references were updated together.
- [ ] Index files (`master-index.md`, `README.md`, or docs index) match current document statuses.
- [ ] User confirmed the output paths and approved the changes before writing.