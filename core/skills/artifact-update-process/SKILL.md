---
name: artifact-update-process
description: Use when applying feedback, change requests, or review comments to existing requirement artifacts, specifications, or project documentation, ensuring document statuses, frontmatter metadata, cross-references, and index catalogs remain consistent.
---

# Artifact Update Process

Manage structured updates to existing requirement artifacts, specifications, and project documentation when applying review feedback, change requests, or status updates.

## Hard Gates

- **[No Arbitrary Overwrite]** If incoming feedback or a requested change conflicts with an existing approved requirement, locked decision, or Decision Log entry, do not overwrite it silently. Stop, highlight the conflict, and ask the user for explicit resolution before updating.
- **[Scope Identification First]** Identify the affected artifacts and evidenced dependencies before editing. Expand to parent docs, child specs, diagrams or catalogs only when the requested change affects their content or references.
- **[Metadata Integrity]** Preserve existing metadata and update project-required fields for delivery, approval, revision, dates and history only where applicable. Do not add delivery metadata to an artifact merely because it was edited. Ensure no corrupted or invisible characters exist.
- **[Index Synchronization]** Never leave index or catalog files out of sync. When an artifact changes status or scope, discover and update the corresponding index files (e.g., `README.md`, `master-index.md`, `docs/index.md`).
- **[Approval Before Write]** Save only within the user-approved content, scope and target paths. Reuse existing approval for that same write set; obtain any missing approval before saving.

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
  - Read the target project metadata/status policy and [Document Metadata Contract](../writing-requirements/references/document-metadata.md). The installer includes `writing-requirements` as a required dependency. If a manual or legacy installation lacks this resource, request its location or installation before changing metadata. Classify by document type and owning path; apply delivery metadata only where the project policy allows it.
  - `status`: Preserve the existing delivery value for content-only edits. Change it only with an explicit confirmed delivery decision, using the project enum. Saving or approving a document never implies a delivery transition.
  - `approval_status`: Record known document approval separately using project-controlled values. Preserve historical approval evidence and identify the revision it covers; do not claim it approves changed content.
  - `version`: Increment version following project convention (e.g., patch for minor clarifications/fixes, minor for functional changes, major for breaking redesigns).
  - Use the project date field, such as `updated`, for the actual change date (`YYYY-MM-DD`); preserve the established field name rather than introducing a competing date field.
  - Record history using the project convention. Do not introduce nested YAML when the project requires flat frontmatter.
- Apply the content modifications:
  - Preserve existing structure, terminology, and formatting conventions.
  - For tabular requirements (such as Basic Design), maintain single-line cell rules and structured separators.
  - Mark superseded requirements or add notes where historical context is important.

### 4. Synchronize Index Catalogs & Cross-References

- Update all relevant index/catalog files identified in Step 1:
  - Synchronize delivery Status in Metadata and current catalog rows identified by exact artifact path/link or ID. Support project Metadata headings, including numbered headings. Preserve approval fields, revision-specific evidence, scope notes, history, HTTP/product statuses, Decision Logs and Open Questions; separate mixed cells before replacing a delivery value. Never infer parent or child delivery state.
  - Ensure links point to correct relative paths.
  - Update document description or scope if the feature definition changed.
- If an identifier changed (e.g., Story ID, AC ID), update references in related artifacts to prevent broken links.

### 5. Review & User Confirmation Gate

- Present a concise diff or summary of changes to the user:
  - Files modified and new/updated statuses.
  - Key requirement changes and conflict resolutions.
  - Updated index entries.
- Ask in Vietnamese by default (or the project's established language).
- Reuse existing approval for the same proposed changes and destination paths; ask only for missing approval or a changed write set.

## Metadata Standards

Read and follow the target project metadata policy; do not maintain a competing enum in this skill. When the project uses flat YAML, keep revision history in content instead of nested frontmatter. Optional approval metadata must not be filled with invented values. A content edit changes the update date/history, not delivery status. Where `status` is the project delivery field, do not introduce a competing `delivery_status`.

Before writing, check one literal canonical delivery value on applicable artifacts, separate known approval, consistent Metadata/current catalog rows, preserved history and valid project fields. Run the project's Markdown and metadata/template validation after saving. A registered migration exception applies only to its exact original metadata; never regenerate or extend a baseline automatically to hide new errors.

## Quality Checklist

Before finalizing:
- [ ] No zero-width spaces (`\u200b`) or invalid characters in frontmatter or markdown.
- [ ] Conflicting decisions were surfaced and approved by the user, not silently overwritten.
- [ ] Delivery status is preserved unless a confirmed delivery change was requested; known approval, revision and update date are tracked separately.
- [ ] Applicability, canonical values, Metadata/current catalogs and templates pass project validation; baseline issues are reported separately.
- [ ] All in-scope files and cross-references were updated together.
- [ ] Index files (`master-index.md`, `README.md`, or docs index) match current document statuses.
- [ ] User confirmed the output paths and approved the changes before writing.
