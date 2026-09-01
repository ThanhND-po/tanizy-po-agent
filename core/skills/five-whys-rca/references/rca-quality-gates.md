# 5 Whys RCA Quality Gates

## Purpose

This reference defines the internal quality checks used by the `five-whys-rca` skill.

These checks exist to improve the quality of the analysis before information is accepted into the final 5 Whys Root Cause Analysis report.

This file is NOT a stakeholder-facing report template.

Do not expose internal states, rejected answers, gate results, scoring, or agent reasoning in the final RCA report unless the user explicitly asks for them.

## 1. Core Principles

The analysis MUST follow these principles:

1. Start from a specific observable problem or undesirable outcome.
2. Ask each Why based on the preceding accepted condition.
3. Follow one dominant causal chain at a time.
4. Do not force exactly five Why steps.
5. Do not treat speculation as verified fact.
6. Missing evidence alone does not block progression.
7. Do not accept an individual mistake or "human error" as the final root cause.
8. Do not stop at a symptom, component failure, or restatement of the problem.
9. Prefer neutral, process-focused questions over blame-oriented questions.
10. Stop only when the analysis reaches a sufficiently supported and actionable systemic cause, or when further investigation cannot reasonably continue.
11. Never invent facts, evidence, owners, dates, decisions, causal links, corrective actions, identities, roles, teams, or participation.
12. Stakeholder-facing identity and role metadata must come from explicit user-provided or user-confirmed information.
13. Preserve uncertainty when information is incomplete.

## 2. Internal Analysis States

The following states are internal workflow states.

They SHOULD NOT appear directly in the stakeholder-facing report.

### 2.1 Answer Status

Each Why answer has one of these states:

- `accepted`
- `needs_clarification`
- `rejected`
- `unknown`

Definitions:

`accepted`
: The answer provides a sufficiently clear causal explanation for the preceding condition.

`needs_clarification`
: The answer may contain useful information but is too vague, broad, ambiguous, circular, or incomplete to form the next causal step.

`rejected`
: The response does not answer the Why question, is only a solution, merely restates the problem, or otherwise cannot serve as a causal step.

`unknown`
: The user cannot currently determine the cause.

### 2.2 Evidence Status

Evidence quality is tracked independently from Answer Status.

Allowed states:

- `verified`
- `partially_verified`
- `pending`
- `contradicted`

Definitions:

`verified`
: Available evidence directly supports the causal finding.

`partially_verified`
: Some evidence supports the finding, but material confirmation is still missing.

`pending`
: The finding is sufficiently plausible and specific to continue the analysis, but supporting evidence has not yet been provided or reviewed.

`contradicted`
: Available evidence materially conflicts with the finding.

A `pending` evidence status MUST NOT by itself block progression to the next Why.

A `contradicted` status MUST trigger review of the affected causal step before the chain continues.

## 3. Gate 0 - Method Suitability

Before starting the Why chain, evaluate whether 5 Whys is reasonably suitable for the problem.

The method is suitable when:

- there is a specific problem, deviation, failure, or missed expectation;
- a dominant cause-and-effect path can reasonably be investigated;
- the analysis can proceed from observable conditions toward deeper causes.

Potential limitations include:

- several independent causes acting simultaneously;
- multiple interacting causal paths with no dominant chain;
- problems dominated by broad organizational, cultural, strategic, or external factors;
- situations where available participants have insufficient knowledge to establish meaningful causal steps.

If multiple potential paths exist:

1. identify them;
2. select one primary causal path for the current analysis;
3. preserve other paths as alternative investigation items;
4. do not combine unrelated paths into one artificial Why chain.

If 5 Whys is clearly insufficient, explain the limitation to the user.

Do not fabricate a linear causal chain merely to complete the method.

## 4. Gate 1 - Problem Definition Quality

The analysis MUST begin from a sufficiently specific problem statement.

A useful problem definition should establish, when relevant:

- what happened;
- expected outcome;
- actual outcome;
- when it happened or the applicable period;
- where or in which system, process, campaign, operation, or context it occurred;
- affected scope;
- observable impact;
- how the problem was detected or observed.

Reject or refine vague statements such as:

- "The campaign performed badly."
- "The system had issues."
- "Operations were inefficient."
- "There was a communication problem."

Prefer observable statements such as:

> The May acquisition campaign generated 840 qualified leads against a target of 2,000.

or:

> The scheduled settlement job did not process 312 eligible transactions during the 02:00 execution window.

Do not require every contextual field when it is genuinely irrelevant.

## 5. Gate 2 - Why Answer Quality

Before using an answer as the basis for the next Why, evaluate whether it adequately explains the preceding condition.

A usable answer SHOULD:

- describe a cause or condition that could reasonably produce the preceding outcome;
- be specific enough to investigate further;
- add causal information instead of repeating the preceding statement;
- describe what occurred rather than only proposing what should be done;
- avoid vague labels when a more concrete condition can be identified.

### 5.1 Common Answer Failures

#### A. Restatement

Question:

> Why did the campaign generate fewer qualified leads than expected?

Poor answer:

> Because the campaign underperformed.

Result:

`needs_clarification`

Reason:

The answer restates the problem instead of explaining it.

#### B. Overly vague cause

Question:

> Why did the scheduled process fail?

Poor answer:

> Because of a technical issue.

Result:

`needs_clarification`

The agent should ask what specific technical condition occurred.

#### C. Solution instead of cause

Question:

> Why did invalid configuration reach production?

Poor answer:

> We need to add automated validation.

Result:

`rejected`

The proposed validation MAY be preserved internally as an action candidate.

The agent must continue investigating the condition that allowed the invalid configuration to reach production.

#### D. Unsupported blame

Question:

> Why was the required configuration missing?

Answer:

> The developer forgot it.

This MAY describe an intermediate event, but it MUST NOT be accepted as the final root cause.

Prefer neutral normalization such as:

> The required configuration was not applied before deployment.

Then continue with a process-focused question such as:

> Why could the required configuration be omitted without being detected before deployment?

#### E. Circular answer

Question:

> Why did customer response time increase?

Poor answer:

> Because responses took longer.

Result:

`rejected`

The answer provides no new causal information.

## 6. Gate 3 - Feedback and Refinement Protocol

When a Why answer fails the Answer Quality Gate:

1. briefly explain what is insufficient;
2. identify the type of issue, such as vague, circular, non-causal, or solution-oriented;
3. ask the user to refine the answer;
4. when useful, provide 1 to 3 examples of the required level of specificity;
5. clearly label agent-generated examples as examples or hypotheses;
6. never promote an agent-generated hypothesis into the causal chain unless the user confirms or evidence supports it;
7. remain on the current Why until the causal meaning is sufficiently clear.

Example:

> "Technical issue" is still too broad to form the next causal step.
>
> Examples of the level of specificity needed could be:
> - the API request timed out;
> - the scheduled job was not triggered;
> - a mandatory field was missing from the input.
>
> These are examples only, not conclusions about this case.
>
> What specific technical condition occurred here?

## 7. Gate 4 - Unknown Cause Handling

If the user genuinely does not know the answer:

- do not pressure the user to guess;
- do not select a hypothesis on the user's behalf;
- record the causal step as unresolved;
- identify useful investigation evidence when possible;
- allow the user to provide additional information;
- pause or terminate the current causal chain if the missing cause prevents meaningful progression.

Example:

Question:

> Why did the database query take 40 seconds?

User:

> I don't know.

Acceptable handling:

> The cause of this step is currently unknown.
>
> Useful evidence may include the query execution plan, slow-query log, lock or wait events, and database resource metrics.
>
> We can pause this causal path here until additional evidence is available.

Do not invent a likely database cause.

## 8. Gate 5 - Causal Link Validation

For every accepted Why step, validate the relationship:

```text
Previous condition
    happened because
Current finding
```

The relationship should remain meaningful when reviewed in reverse:

```text
Current finding
    therefore contributed to
Previous condition
```

Example:

```text
No deployment configuration validation
    therefore
an invalid configuration was released
    therefore
the scheduled job did not execute
    therefore
transactions were not processed
```

If the causal relationship becomes unclear, weak, or unrelated:

- do not continue deeper;
- revisit the affected Why;
- refine or replace the causal step.

Do not connect two statements merely because both are true.

Correlation alone is not a sufficient causal link.

## 9. Gate 6 - Evidence Handling

Evidence can include, but is not limited to:

- system or application logs;
- metrics or measurements;
- database records;
- screenshots;
- inspection results;
- experiment or test results;
- configuration records;
- direct observations;
- participant or witness testimony;
- documents or procedural records.

Evidence availability and answer quality MUST remain separate.

The following combination is valid:

```yaml
answer_status: accepted
evidence_status: pending
```

The following combination requires rework:

```yaml
answer_status: accepted
evidence_status: contradicted
```

When evidence is pending:

- preserve the uncertainty;
- do not describe the finding as confirmed;
- continue the causal analysis only if the finding is sufficiently specific and plausible.

When later evidence changes a prior finding, revisit every downstream Why that depends on it.

## 10. Gate 7 - Symptom and Human Error Check

Before accepting a Root Cause Candidate, determine whether the current answer is still only:

- a symptom;
- a failure event;
- a component failure;
- a vague label;
- an individual error;
- an instruction such as "be more careful";
- a restatement of a preceding condition.

Examples that normally require another Why:

- "The server crashed."
- "The component failed."
- "The operator made a mistake."
- "The developer forgot."
- "There was poor communication."
- "The campaign was not optimized."

For individual actions, ask what process, design, validation, training, control, or safeguard allowed the error to occur or remain undetected.

Do not rewrite factual human actions out of the analysis.

They may remain valid intermediate causes.

They simply MUST NOT be treated as sufficient systemic root causes on their own.

## 11. Gate 8 - Root Cause Candidate Validation

A Root Cause Candidate is ready for conclusion review only when all applicable conditions below are satisfied:

- it causally explains the preceding accepted condition;
- it is not merely a restatement of the problem;
- it is deeper than an immediate symptom;
- it is not based solely on individual blame;
- it identifies a process, control, design, procedural, organizational, or other systemic weakness that can reasonably be addressed;
- a concrete corrective or preventive response can be defined;
- no known evidence materially contradicts the candidate;
- remaining uncertainty is explicitly identifiable.

The number of Why steps is irrelevant.

The analysis MAY stop at Why 3.

The analysis MAY continue beyond Why 5.

Do not ask another Why only to satisfy the name of the method.

## 12. Root Cause Conclusion Status

Use one of the following stakeholder-facing conclusion statuses.

### Confirmed

Use `Confirmed` only when:

- the relevant causal chain is sufficiently supported;
- the root cause has material supporting evidence;
- no critical causal link remains unresolved;
- no known evidence contradicts the conclusion.

### Probable

Use `Probable` when:

- the causal chain is coherent;
- the candidate reasonably explains the problem;
- some material supporting evidence remains pending or incomplete;
- there is no known contradiction strong enough to invalidate the chain.

### Unconfirmed

Use `Unconfirmed` when:

- the root cause remains a plausible candidate;
- one or more critical causal links remain unresolved;
- evidence is insufficient to support a stronger conclusion.

Never manufacture certainty to obtain a `Confirmed` result.

## 13. Gate 9 - Action Classification

Actions use the following identifiers.

### C(n) - Containment Action

Purpose:

- control current impact;
- stop further exposure;
- restore service or operation;
- isolate affected scope;
- provide an immediate workaround.

Containment does not need to remove the root cause.

Examples:

- temporarily disable the affected automation;
- isolate defective inventory;
- pause an affected campaign;
- manually validate pending transactions.

### S(n) - Short-term Action

Purpose:

- reduce near-term recurrence;
- add temporary or tactical safeguards;
- stabilize the process while systemic work is underway.

Examples:

- temporary manual verification;
- additional monitoring;
- a tactical validation rule;
- interim review or approval control.

### L(n) - Mid / Long-term Action

Purpose:

- remove or materially reduce the systemic weakness;
- introduce sustainable prevention or detection;
- improve design, process, automation, controls, training, ownership, or governance.

Examples:

- architecture redesign;
- automated validation;
- permanent control or safeguard;
- regression test coverage;
- process redesign;
- revised operating procedure.

Do not create actions merely to populate all three categories.

A valid RCA may have:

- no containment action;
- several short-term actions;
- one long-term action;

or another combination appropriate to the problem.

## 14. Gate 10 - Action Quality

Every proposed action MUST:

- clearly state what will change;
- be materially related to the analyzed problem or causal chain;
- avoid vague formulations such as "improve quality", "be more careful", "monitor better", or "communicate more";
- avoid invented owners or deadlines;
- preserve `TBD` when owner or due date has not been decided.

Short-term and mid / long-term actions SHOULD include an observable Success Criteria.

A useful Success Criteria describes an outcome.

Poor:

> Automated validation implemented.

Better:

> 100% of configurations missing mandatory fields are rejected before deployment.

Poor:

> Team training completed.

Better:

> All operators pass the revised procedure assessment and no unverified manual override occurs during the next four weekly runs.

Completion of an action is not automatically proof that the action was effective.

## 15. Gate 11 - Objectives Quality

Objectives describe the desired state.

Actions describe how the organization intends to achieve that state.

Do not confuse them.

Example:

Short-term objective:

> Prevent additional invalid payments while the permanent control is being implemented.

Short-term action:

> Add manual review for payments exceeding the affected validation threshold.

Mid / long-term objective:

> Prevent invalid payment requests from entering the processing workflow.

Mid / long-term action:

> Add automated request validation before payment processing.

Objectives SHOULD be concise and outcome-oriented.

## 16. Gate 12 - Stakeholder Metadata Integrity

Stakeholder-facing report metadata is factual information.

The agent MUST NOT infer:

- Facilitator
- Participants
- Reviewer
- Approver
- Organizational role
- Team
- Department
- Sign-off identity

from:

- the current user profile;
- personalization instructions;
- repository or project context;
- the AI agent name or role;
- conversation ownership;
- previous assumptions.

The AI agent MUST NOT identify itself as the RCA Facilitator unless the user explicitly requests this representation.

Use identity or role metadata only when it is:

- explicitly provided by the user; or
- explicitly confirmed by the user.

For missing optional metadata:

- `Not provided` MAY be used in a Draft to preserve an explicit incomplete state;
- the optional row or section MAY be omitted when the user does not want it included;
- `TBD` SHOULD NOT be used for Facilitator or Participants unless the user explicitly uses that status.

`Analysis Date` MAY default to the current RCA analysis/report date.

This default MUST NOT be interpreted as:

- the date the problem occurred;
- the incident date;
- the campaign execution date;
- another historical event date.

A Draft report MAY contain incomplete metadata.

Incomplete information MUST remain visibly incomplete.

Missing information and inferred information are not equivalent.

Prefer an explicit incomplete state over a plausible but unverified value.

## 17. Gate 13 - Report Readiness

Before generating the stakeholder-facing report, verify that:

- the problem statement is sufficiently specific for the current report status;
- accepted Why steps form a coherent primary causal chain as far as the analysis has progressed;
- rejected or abandoned answers are not exported as accepted findings;
- agent-generated hypotheses are not presented as facts;
- evidence uncertainty is preserved;
- the Root Cause Conclusion Status matches the available support;
- Root Cause and Remaining Uncertainty do not contradict each other;
- action IDs use C(n), S(n), or L(n) correctly;
- actions do not contain invented owners or deadlines;
- Success Criteria are observable where applicable;
- alternative causal paths are clearly separated from the primary chain;
- stakeholder-facing identity and role metadata passes Gate 12;
- internal quality-gate states are not exposed;
- no unresolved template placeholders remain;
- optional sections are removed when genuinely not applicable.

For a user-requested Draft before the RCA is complete:

- do not require the causal analysis to look complete;
- retain incomplete or unresolved areas explicitly;
- do not upgrade a poor or unresolved Why answer into an accepted finding;
- do not invent metadata or causal content merely to satisfy the template.

The final report MUST use:

`references/5-whys-report-template.md`

Do not add internal quality-check sections to the stakeholder-facing report.

## 18. Quality Gate Failure Behavior

A gate failure does not automatically terminate the RCA.

Use the following behaviors:

`REFINE`
: Ask the user to improve the current input.

`INVESTIGATE`
: Identify evidence or information required to proceed.

`REVISIT`
: Return to an earlier causal step because new information invalidates a downstream assumption.

`PAUSE`
: Stop the current causal path because the required cause is currently unknown.

`CONTINUE`
: Proceed to the next Why.

`CONCLUDE`
: Proceed from the Why loop to Root Cause and Action Planning.

The agent MUST prefer an incomplete but transparent analysis over a complete-looking analysis based on invented causality.
