# API and NFR Authoring Reference

Read this reference only when drafting or reviewing an API Spec or Non-functional Requirement.

## API Spec Decisions

### Use tables as the primary review surface

- Put the operation inventory, parameters, request fields, response fields, business rules, errors, permissions, and compatibility decisions in Markdown tables.
- Keep one field or rule per row so Product, Development, and QA can scan and comment without interpreting a large YAML block.
- Treat examples as evidence of the contract, not as a replacement for field rules.

### Keep OpenAPI supplementary

OpenAPI is a language-neutral description format that supports paths, operations, parameters, request bodies, responses, security schemes, and reusable components. It can also drive documentation, client/server generation, and testing tools.

Use it as an appendix because:

- Developers can turn the approved contract into tooling quickly.
- Reviewers can still work from concise tables.
- Business rules, decision history, and unresolved questions remain visible outside machine-oriented syntax.

Follow these rules:

- Use the OpenAPI version supported by the target project.
- Keep `operationId`, method, path, schemas, security, and responses aligned with the primary tables.
- Validate YAML syntax and OpenAPI conformance when project tooling exists.
- Flag conflicts between tables and YAML. Do not silently overwrite either representation.
- Do not include secrets, credentials, or real personal data in servers, examples, or security definitions.

### Document HTTP semantics explicitly

- Record whether an operation is safe, idempotent, cacheable, or retryable when it affects client behavior.
- Do not assume every failed state-changing request can be retried safely.
- Document status codes based on the actual operation semantics.
- If using RFC 9457 Problem Details, define stable problem types and safe, actionable client-facing details. Do not leak implementation internals.

### Sources

- [OpenAPI Specification](https://spec.openapis.org/oas/), latest and previous specification versions.
- [OpenAPI 3.1.2](https://spec.openapis.org/oas/v3.1.2.html), including paths, parameters, request bodies, responses, components, and security.
- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110), including methods, safety, idempotency, caching, authentication, and status semantics.
- [RFC 9457: Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457), including the problem detail model and requirements for custom problem types.

## NFR Decisions

### Use a categorized and measurable catalog

ISO/IEC 25010:2023 provides nine product-quality characteristics that can be used as a baseline taxonomy:

1. Functional Suitability
2. Performance Efficiency
3. Compatibility
4. Interaction Capability
5. Reliability
6. Security
7. Maintainability
8. Flexibility
9. Safety

Do not force every project concern into this list. Use the project's taxonomy when it exists. Add clearly labeled categories such as Privacy and Compliance or Observability and Operability when stakeholder, regulatory, or operational needs require them.

### Separate tracking concepts

- `Priority` indicates business or delivery importance.
- `Status` indicates the requirement lifecycle.
- `Verification Result` indicates whether evidence meets the requirement.

Never use one field as a substitute for another.

### Make each NFR verifiable

For each NFR, capture:

- a stable ID;
- category and item;
- condition and affected scope;
- metric and target or threshold;
- operating conditions;
- verification method and expected evidence;
- priority, lifecycle status, and owner;
- source and traceability;
- exceptions or accepted risk when applicable.

Replace vague adjectives with measures. A useful target normally identifies:

- metric;
- comparator;
- value and unit;
- percentile, ratio, or time window when relevant;
- workload, environment, user group, device, geography, or dependency conditions.

If no approved target exists, use `TBD` and record the decision as an Open Question. Do not invent a number to make the requirement appear complete.

### Elaborate Feature Spec quality concerns

When a Feature Spec mentions performance, availability, security, accessibility, audit, recovery, compatibility, privacy, or another quality concern:

1. Preserve the source intent.
2. Add a traceability row linking the source statement to an NFR ID.
3. Elaborate scope, target, operating conditions, ownership, and verification.
4. Mark missing decisions as `TBD`.
5. Keep the NFR spec more detailed than the Feature Spec.
6. Feed approved target changes back into the Feature Spec only if the project workflow requires that synchronization.

### Sources

- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) defines a nine-characteristic product quality model for specifying, measuring, and evaluating ICT product quality.
- [ISO/IEC 25030:2019](https://www.iso.org/standard/72116.html) provides a framework to elicit, define, use, and govern quality requirements, and uses quality models to categorize and quantify them.
- [ISO/IEC 25023:2016](https://www.iso.org/standard/35747.html) provides quality measures and explains their application. It does not prescribe universal passing ranges because targets depend on the product and user context.
