# User Story Quality Checklist

Run this checklist before showing a User Story to the user. Fix all blocking issues silently first.

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
- [ ] Includes at least one relevant edge or alternate path when applicable.
- [ ] Includes negative, validation, permission, or failure behavior when applicable.
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
