> **Ticket title**: [MODULE] Sort description about the feature, limit 120 characters

# User Story: [US-XXX-XX] - [Story Name]

## Metadata

| Field | Value |
|---|---|
| Related Epic | [EPIC-XXX - Epic Name] |
| Priority | [High / Medium / Low] |
| Story Points | [1 / 2 / 3 / 5 / 8 / To be estimated] |
| Status | Draft |

## Story Statement

As a **[specific persona]**, I want to **[perform one clear goal/action]** so that **[business or user outcome]**.

> **Single-Persona Rule:** All Acceptance Criteria and Scenarios below must describe behavior observable from this persona only. If another persona's behavior is relevant, express it as a `Given` precondition or create a separate User Story.

## Acceptance Criteria

### Happy Path

- [Observable condition that must be true when the primary workflow succeeds.]

### Business Rules / Validation

- [Rule, validation, limit, state transition, or data condition that constrains the story.]

### Alternative / Edge Cases

- [Relevant valid variation, boundary condition, empty state, duplicate action, timeout, retry, or edge behavior.]
- `N/A` only if there is truly no meaningful alternative or edge behavior; include the reason.

### Exception / Negative Cases

- [Invalid input, unauthorized access, unavailable dependency, conflicting state, or failure behavior.]
- `N/A` only if there is truly no meaningful exception or negative behavior; include the reason.

### Permission / Security

- [Actor permission, privacy, audit, visibility, or access rule if relevant.]
- `N/A` only if there is no permission or security implication; include the reason.

## Usage Scenarios

**Scenario 1 - Happy Path**

```gherkin
Given [precondition or system state]
When [actor performs the primary action]
Then [expected result]
And [additional expected result if needed]
```

**Scenario 2 - Alternate or Edge Case**

```gherkin
Given [variation in state or input]
When [actor performs the action]
Then [expected alternate result]
```

**Scenario 3 - Exception or Negative Path**

```gherkin
Given [invalid, unauthorized, unavailable, or failure condition]
When [actor attempts the action]
Then [system handles the condition clearly and safely]
```

## Open Questions

- [Question that must be resolved before implementation or acceptance.]

## References

- Feature Spec: [Link]
- Related Use Case: [UC-XXX]
- Design / Flow: [Link]
