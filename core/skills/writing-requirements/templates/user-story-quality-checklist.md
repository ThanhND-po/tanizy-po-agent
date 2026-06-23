# User Story Quality Checklist

Run this checklist before showing a User Story to the user when detailed review is needed. Fix all blocking issues silently first.

## Blocking Gate

A User Story is not ready to show if any item below fails.

- [ ] Story statement has a specific persona, one clear goal, and distinct business/user value.
- [ ] Acceptance Criteria include happy path behavior.
- [ ] Acceptance Criteria include alternative or edge behavior, or explicitly say `N/A` with a reason.
- [ ] Acceptance Criteria include exception or negative behavior, or explicitly say `N/A` with a reason.
- [ ] Usage Scenarios include Happy Path, Alternative/Edge, and Exception/Negative scenarios.
- [ ] Unknown business rules are listed as open questions, not invented as facts.
- [ ] **[Negotiable]** No implementation-binding term appears in any section (story statement, Acceptance Criteria, Scenarios). Examples of terms that must be rephrased: UI component names (Combobox, Modal, Dropdown), cloud services (AWS Lambda, S3, Firebase), frameworks (React, Spring Boot), database technologies (PostgreSQL, MongoDB), specific API endpoints or HTTP verbs.

## Story Statement

- [ ] Persona is specific and relevant to the product context.
- [ ] Goal describes one clear action or outcome.
- [ ] Business value is distinct from the goal.
- [ ] The statement avoids implementation details.
- [ ] The story does not combine unrelated goals.

## INVEST

| Criterion | Pass? | Notes |
|---|---|---|
| Independent | [ ] | |
| Negotiable | [ ] | |
| Valuable | [ ] | |
| Estimable | [ ] | |
| Small | [ ] | |
| Testable | [ ] | |

If `Small` fails, propose a split. If `Estimable` fails, ask for missing context or propose a Spike only when appropriate.

## Acceptance Criteria

- [ ] Includes happy path behavior.
- [ ] Includes at least one relevant edge or alternate path, or explicitly marks it `N/A` with a reason.
- [ ] Includes negative, validation, permission, or failure behavior, or explicitly marks it `N/A` with a reason.
- [ ] Uses measurable, observable language.
- [ ] Avoids vague terms such as `fast`, `easy`, `nice`, `user-friendly`, or `etc.`.
- [ ] Avoids UI pixel details, framework names, API names, or database schema unless explicitly requested.

## Scenarios

- [ ] Scenarios use Given-When-Then.
- [ ] Scenarios map to the Acceptance Criteria.
- [ ] QA can derive test cases from the scenarios.

## Red Flags

- Persona is `user`, `everyone`, or another generic role without explanation.
- `So that` repeats `I want`.
- Acceptance Criteria are missing or not testable.
- One story contains multiple independent workflows.
- Unknown business rules are presented as facts instead of open questions.
- Any section contains a UI component name, cloud service, framework, or database technology sourced from user discussion context (these must be converted to behavioral descriptions).
