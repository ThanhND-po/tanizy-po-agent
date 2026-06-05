# Use Case: [UC-XXX] - [Use Case Name]

## 1. Description

[Briefly describe the business goal and expected user outcome.]

## 2. Actors

- **Primary Actor:** [Specific user role]
- **Supporting Actor(s):** [External system or secondary role, if any]

Do not list the internal application as an actor. Use **System** inside flow steps to describe application responses.

## 3. Preconditions

- [Condition that must be true before the use case starts.]
- [Permission, configuration, or data prerequisite.]

## 4. Main Flow

1. **[Actor]** [performs the action that starts the use case].
2. **System** [validates the context and responds].
3. **[Actor]** [continues the workflow].
4. **System** [processes, retrieves, updates, or displays required data].
5. **System** [confirms successful completion or final state].

## 5. Alternative Flows

### Alternative A: [Alternative Flow Name]

1. At Step [N] of the Main Flow, **[Actor]** [takes a valid alternative action].
2. **System** [processes the alternative action].
3. **System** [returns the actor to the appropriate state or completes the alternate outcome].

## 6. Exception Flows

### Exception E1: [Exception Name]

1. At Step [N] of the Main Flow, [exception condition occurs].
2. **System** [blocks the action, shows an error, redirects, retries, or provides a recovery option].
3. **System** [preserves data consistency and avoids duplicate or partial updates when relevant].

## 7. Postconditions

- **Success:** [State after successful completion.]
- **Failure:** [State after handled exception.]

## 8. Business Rules

- **[Rule Name]:** [Business rule that constrains the flow.]

## 9. Scenarios

**Scenario 1 - Happy Path** *(Main Flow)*

```gherkin
Given [precondition]
When [actor performs primary action]
Then [system shows or applies expected result]
```

**Scenario 2 - Alternative: [Alternative Name]** *(Alternative Flow A)*

```gherkin
Given [precondition]
When [actor performs alternative action]
Then [system completes the alternative outcome]
```

**Scenario 3 - Exception: [Exception Name]** *(Exception Flow E1)*

```gherkin
Given [exception condition]
When [actor attempts the action]
Then [system handles the exception safely]
```

## 10. Notes

- [Optional dependency, open question, or important assumption.]
