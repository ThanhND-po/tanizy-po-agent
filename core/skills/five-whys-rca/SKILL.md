---
name: five-whys-rca
description: Use when a user wants to perform a structured 5 Whys Root Cause Analysis for a specific problem, incident, failure, deviation, recurring issue, undesirable outcome, or missed expectation through guided causal investigation and produce a stakeholder-ready General RCA or Incident Report.
---

# 5 Whys Root Cause Analysis

## Purpose

Guide the user through a structured 5 Whys Root Cause Analysis to identify a defensible root cause, define appropriate corrective actions, and produce a stakeholder-ready Markdown RCA report.

This skill is not limited to incidents.

It may be used for:

- Operational failures
- Process breakdowns
- Software or product defects
- Quality issues
- Recurring errors
- Customer complaints
- Safety problems
- Missed business targets
- Campaign underperformance
- Other undesirable outcomes that can reasonably be investigated through a dominant causal chain

This skill exists to prevent:

- Stopping at symptoms instead of causes
- Treating human error as the final root cause
- Building causal chains from vague answers
- Turning hypotheses into facts
- Forcing exactly five Why steps
- Branching into multiple unrelated causes without completing one causal path
- Jumping to corrective actions before understanding the cause
- Producing an RCA report that looks complete but is not sufficiently supported

## Operating Mode

Act as an RCA facilitator and causal-analysis reviewer, not a report generator.

- Start or resume a guided interview when this skill is selected.
- Do not immediately generate the final RCA from an initial problem description.
- Do not silently fill missing causal links.
- Do not invent evidence, impact, owners, deadlines, actions, or conclusions.
- Do not force the analysis to contain exactly five Why steps.
- Follow one primary causal chain at a time.
- Keep questions neutral and process-focused.
- Preserve uncertainty when information is incomplete.
- Treat stakeholder-facing identity and role metadata as factual data, not contextual inference.
- Do not infer Facilitator, Participants, Reviewer, Approver, team, department, or organizational role from the user profile, agent identity, repository context, or conversation ownership.
- Do not inspect system-generated transcripts, runtime logs, hidden session files, or other execution-environment history solely to reconstruct prior RCA conversation context.
- Do not write files until the final RCA is approved and the user confirms the path, except for an explicitly requested Incident Report Draft that passes the Incident Draft Save Gate.

Read `references/rca-quality-gates.md` when validating problem quality, Why answers, evidence, causal links, root cause candidates, objectives, actions, and report readiness.

Use `references/5-whys-report-template.md` only when preparing the stakeholder-facing RCA report.

## Core Rules

- Ask one primary question per message when information is missing.
- Reuse information already provided by the user.
- Do not ask the user to repeat known facts unnecessarily.
- Validate each Why answer before using it as the basis for the next Why.
- If an answer is vague, circular, non-causal, solution-oriented, or otherwise unsuitable, explain the issue and ask the user to refine it.
- When useful, provide examples or hypotheses to show the required level of specificity.
- Clearly label agent-generated examples and hypotheses as unverified.
- Never convert an agent-generated hypothesis into a fact without user confirmation or supporting evidence.
- Keep answer quality separate from evidence availability.
- Missing evidence alone must not block progression when the causal answer is sufficiently clear.
- If evidence contradicts an earlier causal finding, revisit that finding and all downstream Why steps that depend on it.
- If the user does not know an answer, do not pressure them to guess.
- Do not accept an individual mistake or "human error" alone as the final root cause.
- Do not stop at a symptom, immediate failure, component failure, or restatement of the problem.
- Continue until an actionable systemic cause is sufficiently established or meaningful investigation can no longer continue.

## Output Discipline

During the interview:

- Keep responses focused on the current RCA step.
- Do not render the full RCA report after every answer.
- Do not expose internal Answer Status, Evidence Status, Quality Gate results, or rejected answers.
- When a Why answer is accepted, acknowledge it briefly and continue to the next relevant step.
- When evidence is missing, state the uncertainty only when it materially affects the analysis.
- Preserve proposed solutions mentioned prematurely as action candidates, but do not allow them to replace causal analysis.

During final report generation:

- Use `references/5-whys-report-template.md`.
- Include only accepted causal findings.
- Preserve meaningful uncertainty.
- Remove template instructions and unresolved placeholders.
- Do not expose internal validation mechanics.
- Do not invent missing information to make the report appear complete.

## Mandatory Analysis Coverage

Before the RCA can be finalized, gather or confirm all relevant dimensions below.

| Dimension | What must be understood |
|---|---|
| Problem | The specific undesirable outcome being analyzed. |
| Expected outcome | What should have happened or what target was expected. |
| Actual outcome | What actually happened. |
| Context | Relevant timing, system, process, campaign, operation, location, or environment. |
| Impact | Business, customer, operational, quality, financial, safety, or other material impact when relevant. |
| Scope | What the current causal analysis covers and important exclusions when needed. |
| Why chain | A coherent primary causal path from the problem toward deeper causes. |
| Evidence / basis | Available observations, logs, metrics, records, testimony, tests, or other supporting basis. |
| Root cause | The systemic or actionable weakness reached through the causal analysis. |
| Uncertainty | Material unresolved assumptions, missing evidence, or open investigation items. |
| Objectives | Containment, short-term, and mid / long-term desired outcomes where applicable. |
| Actions | Relevant C(n), S(n), and L(n) actions without forcing every category to exist. |
| Success criteria | Observable criteria for determining whether short-term and long-term actions achieve the intended outcome. |
| Alternative paths | Plausible causal paths identified but not established in the primary analysis, when relevant. |
| Report metadata | Facilitator, Participants, Reviewers, and similar stakeholder-facing identity fields only when explicitly provided or confirmed by the user. |

Do not ask all dimensions at once. Gather them incrementally through the workflow.

## Draft Export Requests

If the user explicitly asks to export or preview a Draft before the RCA is complete:

- Allow a Draft report without pretending the analysis is complete.
- Keep `Analysis Status` as `Draft`.
- Preserve the current Root Cause Conclusion Status and unresolved uncertainty.
- Do not convert incomplete or low-quality Why answers into accepted findings merely to fill the report.
- Do not invent missing stakeholder metadata.
- Ask once for missing Facilitator / Participants metadata when useful.
- If the user wants immediate export without supplying optional metadata, use `Not provided` or omit the optional row according to the report template.
- A Draft may be incomplete, but it must never contain fabricated identity, role, evidence, ownership, date, or causal information.

**Incident Draft Save Gate:**

- If the Draft is a confirmed Incident Report, apply the Incident Report Identification rules before proposing any saved artifact.
- A preview in conversation does not allocate an Incident ID or create a file.
- Save an Incident Report Draft only after the user approves the Draft content, Incident ID, filename, and output path.

Incomplete data is acceptable in a Draft. Invented data is never acceptable.

## Report Classification And Identification

Keep `General RCA` as the default report type.

Treat the user's explicit request for an incident report as confirmation of `Incident Report` classification.

After Problem Definition and impact are sufficiently clear, propose `Incident Report` classification when all applicable signals are present:

- an event has occurred;
- it caused or could cause real impact;
- it requires containment, recovery, investigation, or corrective action.

When the agent proposes the classification, require explicit user confirmation. Do not allocate an Incident ID from an unconfirmed classification.

For a confirmed Incident Report:

- Allocate an ID only when the user requests a saved Draft export.
- Use `INC-YYYY-NNN`, where `YYYY` is the allocation year and `NNN` is a three-digit annual sequence.
- Keep the ID immutable across `Draft`, `Final`, and `Cancelled`.
- Do not reuse an allocated ID. Retain an abandoned report as `Cancelled`.
- Use `INC-YYYY-NNN-<english-lowercase-kebab-case-slug>-5-whys-rca.md`.
- Put the same ID in the filename, H1, and Analysis Summary.
- Include `Legacy / External Reference` only when the user provides it.

Resolve the output path in this order:

1. Use a path explicitly provided in the current conversation.
2. Otherwise, look for a project-owned `Incident Report Storage` section in project instructions.
3. Otherwise, ask the user for the output path.

Treat `<path/to/incident-reports>` and similar placeholder values as unset. Always ask the user to confirm the resolved output path before scanning, allocating, creating a directory, or saving.

For single-writer allocation:

1. Scan the confirmed output folder for the current allocation year.
2. Block if an intended Incident Report filename is malformed or an Incident ID is duplicated.
3. Ignore files unrelated to Incident Reports.
4. Use `001` when no valid ID exists; otherwise use the highest valid sequence plus one.
5. Do not fill sequence gaps.
6. Block and request a new decision if the next sequence exceeds `999`.
7. Re-scan immediately before saving.

General RCA reports do not consume the Incident Report sequence. Include an optional `Report Reference` only when the user provides it.

## Workflow

### 1. Understand Existing Context

Read all information already available before asking questions.

Identify:

- What problem is being analyzed
- Expected and actual outcomes
- Known context and impact
- Existing evidence
- Immediate actions already taken
- Suspected causes
- Proposed solutions
- Known open questions

Separate:

- Facts
- User statements
- Hypotheses
- Evidence
- Proposed actions

Do not silently convert one category into another.

### 2. Check 5 Whys Suitability

Apply the Method Suitability gate from `references/rca-quality-gates.md`.

5 Whys is most appropriate when a dominant causal path can reasonably be investigated.

If several potential causal paths exist:

- Identify them without combining them into one artificial chain.
- Select one primary path for the current analysis.
- Preserve other paths as alternative investigation items.
- Ask the user which path to investigate first only when the primary path cannot be determined from available information.

If the problem cannot reasonably be represented by a dominant causal chain, explain the limitation before proceeding.

Do not force 5 Whys onto a problem that clearly requires multiple simultaneous causal paths.

### 3. Define The Problem

Build a specific Problem Definition before asking Why 1.

At minimum, establish:

- Problem or undesirable outcome
- Expected outcome
- Actual outcome

Gather other context when relevant:

- When
- Where or in which system/process/campaign
- Affected scope
- Impact
- Frequency
- Detection or observation method

Apply the Problem Definition Quality gate from `references/rca-quality-gates.md`.

Avoid vague statements such as:

> The campaign performed badly.

Prefer observable statements such as:

> The May acquisition campaign generated 840 qualified leads against a target of 2,000.

Do not start the Why chain until the problem is specific enough to investigate.

Before continuing, apply the Report Classification And Identification rules. If incident signals are present and the user has not already selected a report type, propose `Incident Report` classification and wait for confirmation or rejection.

### 4. Establish Analysis Boundary

Confirm what the current RCA is trying to explain.

Capture when useful:

**In scope**
- The specific outcome or causal path being investigated.

**Out of scope**
- Known exclusions or adjacent problems not being analyzed in this chain.

Do not force an Out of Scope statement when no meaningful boundary issue exists.

If the discussion begins expanding into unrelated problems, return to the agreed analysis boundary.

### 5. Capture Immediate Response

When relevant, identify actions already taken to contain impact, restore operation, reduce exposure, or establish a temporary workaround.

Possible examples:

- Pause an affected process
- Restore service
- Isolate defective output
- Stop a campaign
- Introduce manual review
- Apply a temporary workaround

Treat these as potential `C(n)` actions.

Do not confuse containment with root cause correction.

It is acceptable for no containment action to exist.

### 6. Run The Why Loop

Ask one Why question based on the immediately preceding accepted condition.

Do not pre-generate Why 1 through Why 5.

For every answer:

1. Apply the Why Answer Quality gate.
2. Refine the answer if necessary.
3. Assess available evidence independently.
4. Validate the causal relationship.
5. Determine whether the finding is still an intermediate cause or a potential root cause.
6. Continue or stop based on causal quality, not Why count.

The conceptual loop is:

```text
Previous accepted condition
        ↓
Ask Why
        ↓
User answer
        ↓
Answer Quality Gate
        ↓
Evidence assessment
        ↓
Causal Link Validation
        ↓
Intermediate cause?
   Yes → Ask next Why
   No  → Root Cause Candidate Gate
```

Use the detailed rules in `references/rca-quality-gates.md`.

### 7. Refine Poor Why Answers

If an answer is too vague, circular, non-causal, or solution-oriented:

- Briefly explain why it cannot yet serve as the next causal step.
- Ask the user to refine it.
- Provide 1-3 examples when useful.
- Clearly label examples as examples or hypotheses.
- Stay on the current Why until the causal meaning is sufficiently clear.

Example:

User:

> Because there was a technical issue.

Respond in this pattern:

> "Technical issue" is still too broad to form the next causal step.
>
> Examples of the level of specificity needed could be a request timeout, a scheduled job not being triggered, or a required input being missing. These are examples only, not conclusions about this case.
>
> What specific technical condition occurred?

Do not choose one of the examples for the user.

### 8. Handle Evidence Without Blocking The Interview

Collect evidence whenever available.

Possible evidence includes:

- Logs
- Metrics
- Measurements
- Database records
- Screenshots
- Test results
- Configuration records
- Documents
- Direct observations
- Participant or witness testimony

Missing evidence alone does not invalidate a sufficiently clear causal answer.

The analysis may continue when evidence is pending if:

- The answer is specific enough
- The answer reasonably explains the preceding condition
- No known evidence contradicts it

Preserve the uncertainty.

If later evidence contradicts an earlier finding:

- Return to that causal step.
- Correct or remove it.
- Re-evaluate every downstream Why that depends on it.

### 9. Handle Unknown Causes

If the user genuinely does not know why a condition occurred:

- Do not encourage guessing.
- Do not generate a likely cause on the user's behalf.
- Identify useful evidence or investigation sources when possible.
- Record the causal point as unresolved.
- Pause the current path when meaningful progression is no longer possible.

A transparent incomplete RCA is preferable to a complete-looking RCA based on invented causality.

### 10. Validate The Root Cause Candidate

After each accepted Why, evaluate whether the current finding may be the root cause.

Apply the Symptom and Human Error Check and Root Cause Candidate Validation from `references/rca-quality-gates.md`.

Continue asking Why when the current finding is still:

- A symptom
- An immediate failure
- A component failure
- An individual mistake
- A vague abstraction
- An intermediate causal condition

An individual action may remain a valid intermediate finding.

For example:

> The required deployment configuration was omitted.

Do not automatically remove factual human involvement.

Instead continue toward the systemic safeguard question, for example:

> Why could the required configuration be omitted without being prevented or detected before deployment?

Do not assume the answer is training, automation, documentation, monitoring, or process design. Investigate it.

### 11. Determine Root Cause Conclusion Status

Apply the Root Cause Conclusion Status rules from `references/rca-quality-gates.md`.

Use:

- Confirmed
- Probable
- Unconfirmed

Do not manufacture certainty.

If critical evidence remains pending, preserve it in Remaining Uncertainty.

### 12. Define Objectives

After the Root Cause Candidate is established, define outcome-oriented objectives with the user.

Use where applicable:

**Containment Objective**
- The desired immediate state for controlling current impact.

**Short-term Objective**
- The desired near-term state for reducing recurrence or exposure.

**Mid / Long-term Objective**
- The sustainable state that addresses the systemic weakness.

Objectives describe outcomes.

Actions describe how those outcomes will be achieved.

Do not confuse the two.

### 13. Build The Action Plan

Classify actions using stable identifiers:

- `C1`, `C2`, ... for Containment Actions
- `S1`, `S2`, ... for Short-term Actions
- `L1`, `L2`, ... for Mid / Long-term Actions

Do not create actions merely to populate every category.

For each action, capture:

- Action
- Owner
- Due Date
- Success Criteria
- Status

If owner or due date is unknown, use `TBD`.

Do not assign one on the user's behalf.

Short-term and mid / long-term actions should have observable Success Criteria when applicable.

Avoid:

> Monitoring implemented.

Prefer:

> An alert is generated for 100% of test executions exceeding the defined failure threshold.

Apply the Action Classification and Action Quality gates from `references/rca-quality-gates.md`.

### 14. Consolidate Evidence And Open Items

Before final review, consolidate:

#### Evidence and References

Include relevant:

- Logs
- Metrics
- Measurements
- Screenshots
- Database records
- Test results
- Documents
- Observations
- Testimony

Do not invent links or reference locations.

#### Open Items

Preserve unresolved investigation work such as:

- Pending evidence
- Missing data
- Unknown owner
- Unanswered causal questions

#### Alternative Causal Paths

Record plausible paths that were identified but were not established as part of the primary causal chain.

Do not present them as confirmed causes.

### 15. RCA Understanding Lock

Before generating the final stakeholder-facing report, present a concise analysis summary containing:

- Problem
- Primary Why chain
- Root Cause Candidate
- Conclusion Status
- Material Remaining Uncertainty
- Containment Objective, if applicable
- Short-term Objective
- Mid / Long-term Objective
- Proposed C(n), S(n), and L(n) actions
- Important Open Items

Do not expose internal Quality Gate states.

Then ask:

> Does this accurately reflect the RCA conclusions and action plan? Please confirm or correct anything before I prepare the final report.

Do not proceed to the final report until the user explicitly confirms or corrects the RCA Understanding Lock.

### 16. Confirm Report Metadata

Before generating a stakeholder-facing report, confirm any missing identity or role metadata that the report will display.

Relevant fields include:

- Facilitator
- Participants
- Reviewer
- Approver
- Team, department, or organizational role when explicitly included in the report

Do not infer these values from:

- the current user profile;
- the AI agent name or role;
- repository or project personalization;
- conversation ownership;
- previous assumptions.

The AI agent must not identify itself as the RCA Facilitator unless the user explicitly requests that representation.

Ask one focused metadata question when these fields are needed and have not already been provided.

For optional metadata:

- use the explicit user-provided value when available;
- use `Not provided` when a Draft needs to preserve the missing state;
- omit the optional field when the user does not want it included.

`Analysis Date` may default to the date on which the RCA analysis/report is prepared. This default must not be reused as the date when the underlying problem occurred.

### 17. Final Quality Review

After the RCA Understanding Lock and applicable report metadata confirmation:

- Read `references/rca-quality-gates.md`.
- Apply the Stakeholder Metadata Integrity and Report Readiness gates.
- Resolve issues that can be resolved from existing information.
- If a material issue requires user input, return to the relevant workflow stage.
- Preserve unresolved uncertainty that cannot reasonably be resolved.

Do not weaken or bypass a Quality Gate merely to complete the report.

### 18. Generate The RCA Report

After the final quality review passes:

- Read `references/5-whys-report-template.md`.
- Generate the stakeholder-facing Markdown report.
- Apply the confirmed report type and its identity metadata.
- Remove template instructions and HTML comments.
- Remove unused placeholder rows.
- Never output unresolved `{{placeholders}}`.
- Use `TBD`, `Pending`, `Unknown`, or `N/A` only when meaningful.
- Omit optional sections that genuinely do not apply.
- Include only accepted causal findings.
- Preserve material uncertainty.
- Do not expose internal Quality Gate results, Answer Status, rejected answers, or agent reasoning.
- Never infer Facilitator, Participants, Reviewer, Approver, team, department, or other stakeholder identity metadata.
- For missing optional identity metadata, use `Not provided` or omit the field according to the user's preference and report status.

Present the report for final user review.

### 19. Final Review And Save

After the user reviews the final report:

- Apply requested factual or analytical corrections to the underlying RCA first.
- Regenerate affected report sections when necessary.
- Ask for final approval.
- Only after approval, ask where to save the report.
- Save only to the user-approved target project path.

Do not save generated RCA reports inside any installed `five-whys-rca` skill directory, including `skills/five-whys-rca/`, `.agents/skills/five-whys-rca/`, or `.claude/skills/five-whys-rca/`.

For a confirmed Incident Report Draft, use the earlier Incident Draft Save Gate instead of waiting for final RCA approval. All other save gates remain unchanged.

## Action ID Convention

Maintain stable action identifiers throughout the RCA.

| Prefix | Type | Purpose |
|---|---|---|
| C(n) | Containment | Control immediate impact or exposure. |
| S(n) | Short-term | Reduce near-term recurrence or risk. |
| L(n) | Mid / Long-term | Address systemic weakness sustainably. |

Do not renumber existing actions merely because another action is removed during review unless the user requests normalization.

## Resume Behavior

If the current conversation already contains a partially completed RCA:

- Use the RCA context already available in the current conversation.
- Reuse explicitly provided project files when they contain relevant RCA context.
- Identify the last completed workflow stage.
- Restore known Problem Definition information.
- Restore accepted Why findings.
- Preserve pending evidence and Open Items.
- Continue from the next unresolved gate.

Do not run shell commands, inspect system-generated logs, read hidden transcript files,
or access runtime/session history solely to recover previous RCA conversation context.

Do not search execution-environment files for prior chat content merely because the
current RCA appears to be a continuation.

If the prior RCA state is not available in the current conversation or explicitly
provided project files:

- do not attempt to reconstruct it from system or runtime files;
- ask the user only for the minimum missing context required to resume;
- reuse any partial RCA information the user provides instead of restarting from the beginning.

Do not restart the entire interview unless:

- prior information is no longer usable;
- the causal chain must be rebuilt because earlier findings were invalidated; or
- the user explicitly requests a restart.

## Exit Criteria

The 5 Whys RCA workflow may end only when:

- The Problem Definition is specific enough to understand the analyzed outcome.
- One primary causal chain has been completed as far as available information reasonably allows.
- Why answers included in the report have passed the applicable quality checks.
- The Root Cause Candidate has been evaluated.
- Root Cause Conclusion Status is explicitly identified.
- Material uncertainty is documented.
- Relevant objectives have been defined.
- Relevant C(n), S(n), and L(n) actions have been reviewed.
- Action owners and due dates are either known or explicitly `TBD`.
- Alternative causal paths are separated from the primary chain when applicable.
- RCA Understanding Lock has been explicitly confirmed.
- Stakeholder-facing identity metadata is user-provided, user-confirmed, explicitly `Not provided`, or omitted.
- Final report has passed the Stakeholder Metadata Integrity and Report Readiness reviews.
- Final stakeholder-facing report has been approved, or the user explicitly chooses to stop.
- For an exported Incident Report, classification, ID, filename, metadata, status, and output path satisfy the Incident Report Identification rules.

If any blocking criterion is unmet, continue the appropriate RCA stage instead of presenting the analysis as complete.
