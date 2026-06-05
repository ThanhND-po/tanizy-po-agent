# [UC-XXX] - [Use Case Name]

## Overview

| Field | Value |
|---|---|
| Description | [Business goal and user outcome of this use case.] |
| Primary Actor | [Specific actor or role.] |
| Supporting Actors / Systems | [External actors or systems, if any.] |
| Preconditions | [Conditions that must be true before the use case starts.] |
| Trigger | [Event or actor action that starts the use case.] |
| Postconditions | [Expected state after success and after handled failure.] |
| Related Requirements | [Epic, User Story, Spec, or other reference.] |

## Basic Flow

| Step | Actor | Action | System Response |
|---:|---|---|---|
| 1 | [Actor] | [Starts the use case.] | [Validates context or shows the first response.] |
| 2 | [Actor] | [Continues the workflow.] | [Processes, retrieves, updates, or displays data.] |
| 3 | [Actor] | [Completes the intended action.] | [Confirms completion or shows final state.] |

## Alternate Flows

| ID | Trigger | Actor | Action | System Response |
|---|---|---|---|---|
| A1 | [Valid variation from a basic-flow step.] | [Actor] | [Alternate action.] | [Successful alternate outcome.] |

## Exception Flows

| ID | Trigger | Actor / System | System Response |
|---|---|---|---|
| E1 | [Invalid input, missing permission, unavailable dependency, or conflicting state.] | [Actor/System] | [Error handling, recovery option, and data consistency behavior.] |

## Business Rules

- [Rule name]: [Rule detail.]

## Scenarios

**Scenario 1 - Happy Path** *(Basic Flow)*

```gherkin
Given [precondition]
When [actor performs the primary action]
Then [system completes the expected outcome]
```

**Scenario 2 - Alternate Path** *(A1)*

```gherkin
Given [precondition]
When [actor performs an alternate valid action]
Then [system completes the alternate outcome]
```

**Scenario 3 - Exception Path** *(E1)*

```gherkin
Given [exception condition]
When [actor attempts the action]
Then [system handles the exception safely]
```
