# User Story INVEST Guide

Use INVEST as the quality bar for every User Story.

| Criterion | Meaning | Check |
|---|---|---|
| Independent | Can deliver meaningful value without requiring another story to be completed first. | Dependencies are minimized or explicitly called out. |
| Negotiable | Describes the need, not a fixed implementation contract. Avoids UI component names (e.g., Combobox, Modal), cloud service names (e.g., AWS Lambda, S3), framework names, database technologies, or specific API endpoints. | No implementation-binding term appears in any section. Rephrase: `select from a list` not `use a Combobox`; `automated background processing` not `AWS Lambda`. |
| Valuable | Creates value for a user, customer, business, or operational role. | The `so that` clause explains an outcome, not a repeated feature. |
| Estimable | Clear enough for the delivery team to size. | Scope, actor, and acceptance boundaries are understandable. |
| Small | Fits inside a normal delivery iteration. | Split if the story combines multiple goals or workflows. |
| Testable | QA can verify completion with concrete tests. | Acceptance criteria and scenarios are observable and measurable. |

## Writing Rules

- Use the format: `As a [specific persona], I want [goal/action], so that [value/outcome].`
- Avoid generic personas such as `user` unless the product truly has one undifferentiated user type.
- Keep implementation details out of every section of the story (statement, Acceptance Criteria, Scenarios). If the user mentioned specific UI components, services, or technology during discussion, convert them to behavioral descriptions in the artifact.
- Put business rules and acceptance boundaries in Acceptance Criteria.
- Put concrete examples in Given-When-Then scenarios.
- If a story is too large, propose a split before finalizing it.
