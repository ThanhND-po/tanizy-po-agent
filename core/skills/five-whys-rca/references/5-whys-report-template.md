# {{report_heading}}

<!--
This template is the stakeholder-facing output of the Five Whys RCA process.

Generation rules:
- Do not expose internal interview states or quality-gate results.
- Do not output unresolved {{placeholders}}.
- Use "TBD", "Pending", "Unknown", or "N/A" only when the state itself is meaningful.
- Remove optional sections or rows when they are genuinely not applicable.
- Do not invent facts, evidence, owners, dates, decisions, conclusions, identities, roles, teams, or participation.
- Facilitator, Participants, Reviewer, Approver, and similar identity metadata must come from explicit user-provided or user-confirmed information.
- Never infer stakeholder metadata from the user profile, AI agent identity, repository context, or conversation ownership.
- For a Draft with missing optional identity metadata, use "Not provided" or remove the optional row.
- Analysis Date may default to the date the RCA analysis/report is prepared, but must not be reused as the problem occurrence date.
- For an Incident Report, use `INC-YYYY-NNN - 5 Whys Root Cause Analysis` as the heading and include Report Type and Incident ID.
- For a General RCA, use `5 Whys Root Cause Analysis` as the heading unless the user provides another report reference.
- Remove Incident ID, Legacy / External Reference, and Report Reference rows when they do not apply.
- Incident Report status may be Draft, Final, or Cancelled.
-->

## 1. Analysis Summary

| Field | Details |
|---|---|
| Report Type | {{Incident Report or remove for General RCA}} |
| Incident ID | {{INC-YYYY-NNN or remove}} |
| Legacy / External Reference | {{user_provided_reference_or_remove}} |
| Report Reference | {{user_provided_general_rca_reference_or_remove}} |
| Problem / Topic | {{problem_title}} |
| Analysis Status | {{Draft / Final / Cancelled}} |
| Analysis Date | {{analysis_date}} |
| Area / Process / System | {{scope_area}} |
| Facilitator | {{facilitator_or_not_provided}} |
| Participants | {{participants_or_not_provided}} |

### Problem

{{concise_problem_summary}}

### Root Cause

**Conclusion Status:** {{Confirmed / Probable / Unconfirmed}}

{{concise_root_cause_summary}}

### Objectives

**Containment objective:**

{{containment_objective_or_NA}}

**Short-term objective:**

{{short_term_objective}}

**Mid / long-term objective:**

{{mid_long_term_objective}}

---

## 2. Problem Definition

### 2.1 Problem Statement

{{specific_problem_statement}}

### 2.2 Expected Outcome

{{expected_outcome}}

### 2.3 Actual Outcome

{{actual_outcome}}

### 2.4 Impact

{{business_customer_operational_quality_financial_or_other_impact}}

### 2.5 Context

| Field | Details |
|---|---|
| When | {{time_or_period}} |
| Where | {{location_system_process_campaign_or_other_context}} |
| Detected / Observed By | {{detection_method_or_observer}} |
| Frequency / Occurrence | {{one_time_recurring_intermittent_or_unknown}} |
| Affected Scope | {{affected_scope}} |

### 2.6 Analysis Boundary

**In scope:**

{{what_this_analysis_investigates}}

**Out of scope:**

{{known_exclusions_or_NA}}

---

## 3. Objectives and Action Plan

<!--
Action ID conventions:
- C(n): Containment Action
- S(n): Short-term Action
- L(n): Mid / Long-term Action

Containment actions control immediate impact or exposure.
Short-term actions reduce near-term recurrence or risk.
Mid / long-term actions address systemic weaknesses and provide sustainable prevention.

Do not create an action only to fill a category.
If a category is not applicable, omit its rows or state N/A where appropriate.
-->

### 3.1 Containment Objective

{{containment_objective_or_NA}}

### 3.2 Short-term Objective

{{short_term_objective}}

### 3.3 Mid / Long-term Objective

{{mid_long_term_objective}}

### Action Plan

| ID | Action | Owner | Due Date | Success Criteria | Status |
|---|---|---|---|---|---|
| C1 | {{containment_action}} | {{owner_or_TBD}} | {{date_or_TBD}} | {{observable_success_condition}} | {{Planned / In progress / Completed / N/A}} |
| S1 | {{short_term_action}} | {{owner_or_TBD}} | {{date_or_TBD}} | {{observable_success_condition}} | {{Planned / In progress / Completed}} |
| L1 | {{mid_long_term_action}} | {{owner_or_TBD}} | {{date_or_TBD}} | {{observable_success_condition}} | {{Planned / In progress / Completed}} |

### Action Notes

{{dependencies_constraints_rollout_notes_or_NA}}

---

## 4. 5 Whys Analysis

<!--
The analysis does not need to contain exactly five Why steps.
Include only accepted Why steps from the completed analysis.

Each Finding should explain the preceding condition.
Do not expose rejected answers, internal answer-quality states, or agent-generated hypotheses
that were not accepted as part of the analysis.

Evidence may still be pending. If so, state that explicitly without presenting the finding
as more certain than the available information supports.
-->

| Step | Why Question | Finding | Evidence / Basis |
|---|---|---|---|
| Why 1 | {{why_question_1}} | {{finding_1}} | {{evidence_basis_1}} |
| Why 2 | {{why_question_2}} | {{finding_2}} | {{evidence_basis_2}} |
| Why 3 | {{why_question_3}} | {{finding_3}} | {{evidence_basis_3}} |
| ... | ... | ... | ... |

### Analysis Notes

{{important_context_needed_to_understand_the_why_chain_or_NA}}

---

## 5. Root Cause

### Root Cause Statement

{{root_cause_statement}}

### Conclusion Status

{{Confirmed / Probable / Unconfirmed}}

### Supporting Basis

{{concise_explanation_of_the_facts_evidence_and_reasoning_supporting_the_root_cause}}

### Remaining Uncertainty

{{unverified_assumptions_missing_evidence_or_None}}

---

## 6. Evidence and References

<!--
Use this section for evidence that stakeholders may need to review independently.

Examples:
- system or application logs
- measurements and metrics
- screenshots
- database records
- inspection results
- test results
- documents
- direct observations
- participant or witness testimony

Do not fabricate links or references.
-->

| ID | Evidence / Reference | Type | Relevant To | Location / Link |
|---|---|---|---|---|
| E1 | {{evidence_description}} | {{Log / Metric / Observation / Test / Testimony / Document / Other}} | {{Problem / Why n / Root Cause / Action}} | {{reference_or_NA}} |

### Evidence Notes

{{limitations_missing_records_pending_verification_or_NA}}

---

## 7. Open Items and Alternative Paths

<!--
This section preserves unresolved investigation work without presenting it as an established
part of the primary causal chain.

Remove subsections that are not applicable.
-->

### 7.1 Open Items

| ID | Question / Item | Reason | Owner | Status |
|---|---|---|---|---|
| O1 | {{open_question_or_follow_up}} | {{why_it_remains_open}} | {{owner_or_TBD}} | {{Open / In progress / Closed}} |

### 7.2 Alternative Causal Paths

{{alternative_causes_or_paths_that_were_identified_but_not_established_in_the_primary_analysis_or_None}}

### 7.3 Additional Observations

{{relevant_observations_that_do_not_belong_to_the_primary_causal_chain_or_NA}}

---

## 8. Review and Approval

<!--
Optional.
Use only when the organization requires formal RCA review, acknowledgement, or sign-off.

Reviewer / approver identity must be explicitly provided or confirmed by the user.
Never infer reviewer or approver identity from project roles, user profile, or AI context.
-->

| Reviewer | Role | Decision | Date | Notes |
|---|---|---|---|---|
| {{reviewer}} | {{role}} | {{Approved / Changes requested / Acknowledged}} | {{date}} | {{notes}} |
