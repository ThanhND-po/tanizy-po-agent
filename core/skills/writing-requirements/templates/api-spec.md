# API Specification: [API-XXX] - [API Name]

> The Markdown tables are the primary review contract. The OpenAPI YAML in Appendix A is supplementary and must not replace business rules, field definitions, or error conditions in the tables.

## 1. Metadata

| Field | Value |
|---|---|
| API Spec ID | [API-XXX] |
| Module / Domain | [Owning module or business domain] |
| Version | [v1 / semantic version / date-based version] |
| Status | Draft / In Review / Approved / Deprecated |
| Owner | [Team or role] |
| Last Updated | [YYYY-MM-DD] |
| Related Feature Spec | [ID and relative link] |
| Related Requirements | [Epic, User Story, Use Case, or NFR links] |
| Intended Consumers | [Internal service, web app, partner, public client] |
| OpenAPI Appendix | Included / Not Included / TBD |

## 2. Purpose and Scope

| Topic | Description |
|---|---|
| Purpose | [Business capability enabled by this API.] |
| In Scope | [Operations and use cases covered by this document.] |
| Out of Scope | [Explicit exclusions.] |
| Assumptions | [Confirmed assumptions only.] |
| Dependencies | [External systems, upstream data, or related contracts.] |

## 3. Operation Summary

> List every operation before adding details. Keep this table synchronized with Section 5 and Appendix A.

| Operation ID | Method | Path | Summary | Authentication | Idempotency | Success Status | Status |
|---|---|---|---|---|---|---:|---|
| [operationId] | GET / POST / PUT / PATCH / DELETE | [/resource/{id}] | [One-line outcome.] | [Scheme / None / TBD] | Yes / No / Conditional | [200] | Draft / In Review / Approved / Deprecated |

## 4. Shared Contract

### 4.1 Servers and Environments

| Environment | Base URL Pattern | Purpose | Notes |
|---|---|---|---|
| [Development] | [https://api-dev.example.com/v1] | [Development and integration testing.] | [Do not include credentials.] |

### 4.2 Authentication and Authorization

| Topic | Requirement |
|---|---|
| Authentication Scheme | [OAuth 2.0 / bearer token / API key / mTLS / None / TBD] |
| Required Scopes / Roles | [Scope or role rules.] |
| Resource-level Authorization | [Ownership, tenant, organization, or record-level rule.] |
| Unauthenticated Response | [Expected status and error code.] |
| Unauthorized Response | [Expected status and error code.] |

### 4.3 Common Headers

| Header | Direction | Required | Type / Format | Description | Example |
|---|---|---|---|---|---|
| [X-Correlation-ID] | Request / Response | Yes / No / Conditional | string | [Tracing or contract purpose.] | [safe-example-id] |

### 4.4 Common Conventions

| Concern | Contract |
|---|---|
| Content Type | [application/json] |
| Character Encoding | [UTF-8] |
| Date and Time | [ISO 8601 profile, timezone handling, precision.] |
| Pagination | [Cursor / offset / none, defaults and limits.] |
| Filtering and Sorting | [Supported fields, operators, defaults, invalid-input handling.] |
| Idempotency and Retry | [Safe retry rules, idempotency key behavior, retention period.] |
| Rate Limits | [Limit, window, headers, and exceeded response, or N/A.] |
| Caching | [Cacheability, validators, TTL, or N/A.] |
| Localization | [Language selection and localized fields, or N/A.] |
| Compatibility | [Versioning and backward-compatibility policy.] |

## 5. Operation Details

> Repeat Section 5 for each operation in Section 3.

### 5.1 [METHOD] [PATH] - [Operation Name]

#### Overview

| Field | Value |
|---|---|
| Operation ID | [operationId] |
| Purpose | [Business outcome.] |
| Actor / Consumer | [Caller.] |
| Preconditions | [Required state, permission, or configuration.] |
| Authentication | [Scheme and scopes.] |
| Authorization | [Role, ownership, tenant, or resource-level rule.] |
| Idempotency | Yes / No / Conditional - [Details.] |
| Side Effects | [Created, updated, deleted, notification emitted, or None.] |

#### Path, Query, and Header Parameters

| Name | In | Type / Format | Required | Description | Validation / Rules | Example |
|---|---|---|---|---|---|---|
| [id] | path / query / header | [string / uuid] | Yes / No / Conditional | [Meaning.] | [Allowed values, range, pattern, dependency.] | [safe-example] |

#### Request Body

| Field | Type / Format | Required | Nullable | Description | Validation / Business Rules | Example |
|---|---|---|---|---|---|---|
| [fieldName] | [string / date] | Yes / No / Conditional | Yes / No | [Business meaning.] | [Length, range, enum, cross-field rule.] | [safe value] |

Use dot notation for nested fields and `[]` for arrays, for example `items[].productId`.

```json
{
  "fieldName": "safe-example"
}
```

#### Processing and Business Rules

| Rule ID | Condition / Trigger | Rule | Result |
|---|---|---|---|
| [BR-01] | [When the request meets a condition.] | [Business or processing rule.] | [State change or response behavior.] |

#### Success Response

| Status | Meaning | Headers | Body Schema |
|---:|---|---|---|
| [200] | [Successful outcome.] | [Location, ETag, or N/A.] | [Schema name or description.] |

| Field | Type / Format | Nullable | Description | Rules | Example |
|---|---|---|---|---|---|
| [data.id] | [string / uuid] | No | [Business meaning.] | [Visibility, derivation, or formatting rule.] | [safe-example-id] |

```json
{
  "data": {
    "id": "safe-example-id"
  }
}
```

#### Error Responses

| HTTP Status | Error Code / Problem Type | Condition | Client Action / Retry | Response Notes |
|---:|---|---|---|---|
| [400] | [VALIDATION_ERROR or stable type URI] | [Exact failure condition.] | [Correct request / Do not retry / Retry later.] | [Safe, actionable detail without internal leakage.] |

#### Operation Notes

- [Concurrency, ordering, timeout, partial success, asynchronous processing, or other operation-specific note.]

## 6. Shared Error Model

| Field | Type / Format | Required | Description |
|---|---|---|---|
| type | string / URI | [Yes / No] | [Stable problem type identifier.] |
| title | string | [Yes / No] | [Short problem summary.] |
| status | integer | [Yes / No] | [HTTP status reflected in the response.] |
| detail | string | [Yes / No] | [Actionable occurrence-specific explanation.] |
| instance | string / URI reference | [Yes / No] | [Occurrence identifier.] |
| code | string | [Yes / No] | [Stable application error code, if used.] |
| errors[] | array | [Yes / No] | [Field-level validation errors, if used.] |

> If the API adopts RFC 9457, use `application/problem+json` and document each custom problem type with a stable type URI, title, and HTTP status. Do not expose stack traces, queries, credentials, or internal implementation details.

## 7. Security, Privacy, and Audit

| Concern | Requirement |
|---|---|
| Sensitive Data | [Fields classified as personal, confidential, regulated, or None.] |
| Data Minimization | [Only required fields exposed and accepted.] |
| Transport Protection | [Requirement or reference to NFR/security standard.] |
| Logging and Masking | [What is logged, masked, or prohibited.] |
| Audit Events | [Actor, action, target, result, timestamp, correlation ID.] |
| Abuse Protection | [Rate limiting, replay prevention, fraud controls, or N/A.] |

## 8. Compatibility and Lifecycle

| Version / Date | Change | Compatibility | Consumer Action | Status |
|---|---|---|---|---|
| [v1] | [Initial contract.] | Backward compatible / Breaking / N/A | [Required migration action.] | Planned / Active / Deprecated / Retired |

## 9. Verification Checklist

- [ ] Every operation in Section 3 has one matching detailed section.
- [ ] Every request and response field occupies one table row.
- [ ] Required, nullable, validation, and conditional rules are explicit.
- [ ] Authentication and resource-level authorization are documented.
- [ ] Success, validation, permission, conflict, dependency, and server failure responses are covered when relevant.
- [ ] Retry and idempotency behavior are explicit for state-changing operations.
- [ ] Examples contain no real secrets, tokens, personal data, or production-only values.
- [ ] OpenAPI Appendix A is marked supplementary and matches the approved tables.
- [ ] Unknown rules remain `TBD` and appear in Open Questions.

## 10. Open Questions

| ID | Question | Impact | Owner | Due Date | Status |
|---|---|---|---|---|---|
| [OQ-01] | [Decision or missing information.] | [Blocked operation, schema, or rule.] | [Role or team] | [YYYY-MM-DD / TBD] | Open / Answered / Deferred |

## Appendix A. Supplementary OpenAPI YAML

> Use the OpenAPI version supported by the project. The example below uses OpenAPI 3.1.2. Keep this appendix aligned with the approved tables. Do not treat it as the sole source for business rules or unresolved decisions.

```yaml
openapi: 3.1.2
info:
  title: Example API
  version: 1.0.0
servers:
  - url: https://api.example.com/v1
paths:
  /resources/{id}:
    get:
      operationId: getResource
      summary: Get one resource
      security:
        - bearerAuth: []
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        "200":
          description: Resource returned
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Resource"
        "404":
          description: Resource not found
          content:
            application/problem+json:
              schema:
                $ref: "#/components/schemas/Problem"
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
  schemas:
    Resource:
      type: object
      required:
        - id
      properties:
        id:
          type: string
          format: uuid
    Problem:
      type: object
      properties:
        type:
          type: string
          format: uri-reference
        title:
          type: string
        status:
          type: integer
        detail:
          type: string
        instance:
          type: string
          format: uri-reference
```

## References

- [OpenAPI Specification](https://spec.openapis.org/oas/)
- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [RFC 9457: Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457)
