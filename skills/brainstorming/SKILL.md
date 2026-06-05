---
name: brainstorming
description: Use when a Product Owner wants to refine a vague idea, clarify scope, compare product approaches, and turn the idea into an approved feature spec before creating requirements or diagrams.
---

# Brainstorming Ideas Into Specs

Help a Product Owner turn an unclear idea into a scoped feature design through short, structured dialogue.

## Hard Gates

- Do not produce Epic, User Story, Use Case, diagram, Basic Design, API Spec, NFR, or any other formal artifact during brainstorming.
- Do not write a file until the user approves the feature spec and confirms the output path.
- Ask one question at a time when information is missing.

## Workflow

1. **Read project context first**
   - Inspect relevant docs, existing specs, requirements, diagrams, backlog notes, or product context in the target project.
   - If the idea spans multiple independent features, call that out and help the user split it before writing a spec.

2. **Clarify the idea**
   - Identify primary actor, problem, desired outcome, business value, constraints, and important non-goals.
   - Prefer multiple-choice questions when the choice materially changes scope.

3. **Compare approaches**
   - Propose 2-3 product approaches with trade-offs.
   - Use a product/business lens: user experience, operational impact, risk, dependencies, and scope.
   - Recommend one approach and explain why.

4. **Present the feature spec for approval**
   - Scale the spec to complexity; simple ideas can be short.
   - Use these sections when relevant:
     - Problem Statement
     - Feature Scope: in scope / out of scope
     - Actors and User Segments
     - Key Flows
     - Constraints and Business Rules
     - Success Metrics
     - Dependencies
     - Open Questions
   - Ask the user to approve or request changes.

5. **Save only after approval**
   - Ask where to save the spec, for example `docs/specs/<feature-name>.md`.
   - Save to the target project path chosen by the user.
   - Do not save into `skills/` or any agent-internal folder.

6. **Self-review before closing**
   - Remove unresolved placeholder markers or vague wording unless explicitly approved as an open question.
   - Check for scope creep, contradictions, unclear actors, and missing high-level exception flows.
   - Ask the user to confirm the saved spec before moving on.

7. **Ask what to do next**
   - Offer next artifact choices:
     - Epic
     - User Story
     - Use Case
     - Diagram
     - Basic Design
     - API Spec
     - Non-functional Requirement
     - Done

## Output Quality

- Keep the user in control of scope and next steps.
- Use Vietnamese by default unless project context indicates otherwise.
- Keep artifacts implementation-neutral unless the user explicitly asks for technical design.
- Push back on scope creep with concise product reasoning.
- If the next artifact type has no local template, route to `writing-requirements` or `creating-diagrams` and use the research fallback defined there.
