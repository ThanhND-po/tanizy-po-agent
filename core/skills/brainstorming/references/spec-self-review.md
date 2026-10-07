# Spec Self-Review Checklist

Use this lightweight checklist after drafting a feature spec and before asking the user to confirm it.

Apply the [shared Feature Spec quality gate](../../writing-requirements/references/feature-spec-authoring.md#quality-gate) in addition to the checks below.

## Check

- **Completeness:** No accidental placeholders, incomplete sections, or unresolved decisions hidden as requirements.
- **Consistency:** Scope, actors, flows, rules, and success metrics do not contradict each other.
- **Clarity:** A PO, designer, developer, or QA can understand the behavior without guessing.
- **Scope:** The spec describes one coherent feature or a clearly decomposed set of sub-features.
- **YAGNI:** The spec does not add unrequested capabilities without clear business value.

## Result

Return one of:

- `Ready for review` - self-review passed; user approval is still required.
- `Issues Found` - list only issues that would materially affect downstream requirements, diagrams, or implementation planning.
