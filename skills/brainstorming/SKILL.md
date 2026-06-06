---
name: brainstorming
description: Use when a Product Owner wants to refine a vague idea, eliminate unclear requirements, validate intent, compare approaches, and turn the idea into an approved feature spec before creating requirements or diagrams.
---

# Brainstorming Ideas Into Specs

## Purpose

Turn raw or unclear product ideas into clear, validated feature specs through structured dialogue before writing formal artifacts.

This skill exists to prevent:

- rush-to-goal behavior
- hidden assumptions
- shallow clarification
- product concepts being guessed incorrectly
- specs that look complete but encode the wrong intent

## Operating Mode

Act as a product discovery facilitator and senior reviewer, not a document generator.

- Do not rush to a solution.
- Do not silently fill concept gaps.
- Do not treat "simple" ideas as exempt from clarification.
- Do not write Epic, User Story, Use Case, diagram, Basic Design, API Spec, NFR, or any other formal artifact while brainstorming is active.
- Do not write files until the final spec is approved and the user confirms the path.

## Core Rules

- Ask one question per message when information is missing.
- Prefer multiple-choice questions when the decision space is clear.
- Use open-ended questions only when the answer cannot be meaningfully constrained.
- If the user is unsure, propose reasonable defaults and mark them as assumptions.
- Keep a running **Decision Log** during the discussion.
- Continue clarifying until the intent is specific enough that another PO, designer, developer, or QA would not need to guess.

## Mandatory Discovery Coverage

Before proposing any design or spec, gather or confirm all relevant dimensions below. Do not ask them all at once; work through them incrementally.

| Dimension | What must be understood |
|---|---|
| Current context | Existing docs, flows, constraints, prior decisions, and what already exists. |
| Problem | What pain, opportunity, or business need is being solved. |
| Users / actors | Who uses or is affected by the feature, including role differences. |
| Desired outcome | What changes when the feature succeeds. |
| Scope | What is in scope and explicitly out of scope. |
| Key flows | Happy path, important alternate paths, and major exception paths. |
| Business rules | Policies, permissions, validations, limits, and state rules. |
| Data concepts | Important entities, records, inputs, outputs, ownership, and retention if relevant. |
| Dependencies | Upstream/downstream features, systems, teams, approvals, or operational processes. |
| Success metrics | How the Product Owner will know the feature worked. |
| Non-goals | What the feature must not solve right now. |
| Risks | Ambiguity, compliance, operational, usability, migration, or rollout risks. |

## Mandatory Non-Functional Requirements

Explicitly clarify or propose assumptions for:

- Performance expectations
- Scale: users, data volume, traffic, or frequency
- Security and privacy constraints
- Reliability and availability needs
- Accessibility or localization needs, if user-facing
- Maintenance and ownership expectations
- Auditability, observability, or compliance needs, if relevant

If the user does not know, propose conservative defaults and ask for confirmation. Do not omit NFRs just because the feature sounds small.

## Workflow

### 1. Understand Current Context

Read project context first when available:

- specs
- requirements
- diagrams
- backlog notes
- product docs
- previous decisions

Identify what already exists, what is being proposed, and what appears implicit but unconfirmed.

Do not design yet.

### 2. Clarify Incrementally

Ask one meaningful question at a time. Each question should either:

- remove ambiguity
- confirm an assumption
- choose between real trade-offs
- define scope or non-scope
- expose a risk

Avoid low-value questions. If a detail can be inferred safely from project files, infer it and mark it as an assumption for confirmation.

### 3. Understanding Lock

Before proposing any approach, pause and present:

#### Understanding Summary

Use 5-7 concise bullets covering:

- what is being built
- why it exists
- who it is for
- key flows or behaviors
- key constraints
- explicit non-goals
- success criteria

#### Assumptions

List all assumptions explicitly, including proposed NFR defaults.

#### Open Questions

List unresolved questions and identify whether each blocks design or can be deferred.

Then ask:

> Does this accurately reflect your intent? Please confirm or correct anything before we move to design.

Do not proceed until the user explicitly confirms or corrects the Understanding Lock.

### 4. Explore Product Approaches

After Understanding Lock is confirmed:

- Propose 2-3 viable approaches.
- Lead with the recommended option.
- Explain trade-offs using a PO lens:
  - user experience
  - business value
  - operational impact
  - delivery complexity
  - extensibility
  - risk
  - maintenance
- Apply YAGNI ruthlessly. Do not add future scope without a clear reason.

Record accepted decisions and rejected alternatives in the Decision Log.

### 5. Present The Spec Incrementally

Once an approach is accepted, present the feature spec in small sections. Keep each section short enough for review before moving on.

Cover, as relevant:

- Problem Statement
- Goals and Non-goals
- Actors and Permissions
- Scope
- Key Flows
- Alternate and Exception Flows
- Business Rules
- Data Concepts
- Non-Functional Requirements
- Dependencies
- Risks
- Success Metrics
- Open Questions
- Decision Log

After each substantial section, ask:

> Does this look right so far?

Revise before continuing when the user corrects something.

### 6. Final Review And Save

After all sections are validated:

- Run a self-review for contradictions, missing flows, vague wording, hidden assumptions, and scope creep.
- Present the final spec summary.
- Ask for final approval.
- Only after approval, ask where to save the spec, for example `docs/specs/<feature-name>.md`.
- Save only to the user-approved target project path.

The saved spec must include:

- Understanding Summary
- Assumptions
- Final Feature Spec
- Non-Functional Requirements
- Decision Log
- Open Questions

### 7. Choose Next Artifact

After the spec is approved and saved, ask what to do next:

- Epic
- User Story
- Use Case
- Diagram
- Basic Design
- API Spec
- Non-functional Requirement
- Done

Do not automatically invoke another workflow.

## Decision Log

Maintain this throughout the conversation:

| Decision | Alternatives Considered | Rationale | Status |
|---|---|---|---|
| [Decision made] | [Options considered] | [Why chosen] | Accepted / Rejected / Deferred |

The Decision Log is mandatory and must be preserved in the final spec.

## Exit Criteria

Brainstorming mode may end only when:

- Understanding Lock has been explicitly confirmed.
- At least one approach has been accepted or a no-build decision has been made.
- Major assumptions and NFR defaults are documented.
- Key risks are acknowledged.
- Decision Log is complete.
- Final spec is approved or the user explicitly chooses to stop.

If any criterion is unmet, continue refinement instead of writing formal artifacts.
