# Non-functional Requirements: [NFR-XXX] - [Product / Feature / Module]

> This document elaborates quality requirements mentioned in Feature Specs. Do not copy vague statements unchanged. Add measurable targets and verification details, or mark them `TBD` and raise an Open Question.

## 1. Metadata

| Field | Value |
|---|---|
| NFR Spec ID | [NFR-XXX] |
| Scope | [Product, feature, module, service, or release.] |
| Version | [Version.] |
| Status | Draft / In Review / Approved / Superseded |
| Owner | [Accountable team or role.] |
| Last Updated | [YYYY-MM-DD] |
| Related Feature Specs | [IDs and relative links.] |
| Related API Specs / Designs | [IDs and relative links.] |

## 2. Scope and Quality Context

| Topic | Description |
|---|---|
| Business Context | [Why these quality requirements matter.] |
| In Scope | [Components, workflows, users, data, and environments covered.] |
| Out of Scope | [Explicit exclusions.] |
| Critical User Journeys | [Journeys whose quality must be protected.] |
| Critical Data | [Sensitive, regulated, or business-critical data.] |
| Operating Conditions | [Expected load, geography, device, network, or dependency conditions.] |
| Assumptions | [Confirmed assumptions only.] |

## 3. Feature Spec Traceability

> Create one row for every quality concern stated or implied as a constraint in a related Feature Spec.

| Source | Source Statement / Concern | NFR ID | Elaboration | Traceability Status |
|---|---|---|---|---|
| [FS-XXX, section or relative link] | [Original quality concern, summarized without changing intent.] | [NFR-PERF-001] | [Detailed target and verification reference.] | Covered / Partial / TBD / Not Applicable |

## 4. Category Coverage

> Use the project taxonomy when defined. Otherwise review the ISO/IEC 25010:2023 baseline categories below. Add project-specific categories such as Privacy and Compliance or Observability and Operability only when relevant.

| Category | Applicability | Reason / Scope | Requirement IDs |
|---|---|---|---|
| Functional Suitability | In Scope / Not Applicable / TBD | [Usually covered by functional specs; include only quality-related completeness or correctness concerns.] | [NFR-FUNC-...] |
| Performance Efficiency | In Scope / Not Applicable / TBD | [Response time, throughput, capacity, resource utilization.] | [NFR-PERF-...] |
| Compatibility | In Scope / Not Applicable / TBD | [Interoperability and coexistence.] | [NFR-COMP-...] |
| Interaction Capability | In Scope / Not Applicable / TBD | [Learnability, operability, error protection, inclusivity, accessibility, self-descriptiveness.] | [NFR-UX-...] |
| Reliability | In Scope / Not Applicable / TBD | [Availability, fault tolerance, recoverability, continuity.] | [NFR-REL-...] |
| Security | In Scope / Not Applicable / TBD | [Confidentiality, integrity, accountability, authenticity, resistance.] | [NFR-SEC-...] |
| Maintainability | In Scope / Not Applicable / TBD | [Modularity, analyzability, modifiability, testability.] | [NFR-MAIN-...] |
| Flexibility | In Scope / Not Applicable / TBD | [Adaptability, scalability, installability, replaceability.] | [NFR-FLEX-...] |
| Safety | In Scope / Not Applicable / TBD | [Risk identification, operational constraints, fail-safe behavior, hazard warning.] | [NFR-SAFE-...] |
| [Project-specific Category] | In Scope / Not Applicable / TBD | [Why the additional category is needed.] | [NFR-...] |

## 5. NFR Catalog

> Keep one requirement per row. Use measurable targets. If a value is not approved, write `TBD` and link it to an Open Question.

| ID | Category | Item | Description | Target / Threshold | Priority | Status | Verification | Source |
|---|---|---|---|---|---|---|---|---|
| [NFR-PERF-001] | Performance Efficiency | [API response time] | [Condition, system behavior, and affected scope.] | [p95 <= 500 ms under approved workload / TBD] | Critical / High / Medium / Low | Proposed / Accepted / Implemented / Verified / Deferred / Rejected | [Load test, monitoring query, audit, inspection.] | [FS-XXX section / stakeholder decision / regulation.] |

### Field Rules

| Field | Rule |
|---|---|
| ID | Use a stable ID. Do not reuse an ID for a different requirement. |
| Category | Use the approved project taxonomy or the category coverage in Section 4. |
| Item | Name one quality concern, for example `Availability`, `Recovery time`, or `Audit retention`. |
| Description | State the condition, affected scope, and required behavior without vague adjectives. |
| Target / Threshold | Include metric, comparator, value, unit, percentile or time window, and operating conditions when relevant. |
| Priority | Use the project scale. If none exists, use `Critical / High / Medium / Low`. |
| Status | Track lifecycle only: `Proposed / Accepted / Implemented / Verified / Deferred / Rejected`. |
| Verification | State how evidence will be produced and evaluated. |
| Source | Link to the Feature Spec, regulation, architecture decision, stakeholder decision, or other authority. |

## 6. Detailed Requirement Records

> Add one record for each high-risk NFR or any NFR whose catalog row cannot hold enough verification detail. Do not duplicate the catalog text without adding detail.

### [NFR-ID] [Item]

| Field | Detail |
|---|---|
| Category | [Category.] |
| Description | [Condition, affected scope, and required behavior.] |
| Rationale | [Business, user, regulatory, or operational reason.] |
| Scope | [Component, workflow, tenant, geography, role, or data class.] |
| Operating Conditions | [Workload, duration, data volume, dependency state, network, device, or environment.] |
| Measure | [Metric name and calculation.] |
| Target / Threshold | [Comparator, value, unit, percentile or time window.] |
| Baseline | [Current measured value / Not measured / N/A.] |
| Verification Method | Test / Monitoring / Audit / Inspection - [Procedure and evidence.] |
| Verification Environment | [Production-like, staging, production monitoring, device/browser matrix, or other.] |
| Verification Frequency | [Per release, continuous, quarterly, on demand, or event-driven.] |
| Owner | [Accountable role or team.] |
| Dependencies | [Related service, control, tool, vendor, or decision.] |
| Priority | Critical / High / Medium / Low |
| Status | Proposed / Accepted / Implemented / Verified / Deferred / Rejected |
| Verification Result | Not Run / Pass / Fail / Accepted Exception |
| Source | [Feature Spec section, regulation, decision, or stakeholder.] |

## 7. Exceptions and Trade-offs

| ID | Related NFR | Exception / Trade-off | Rationale | Risk | Approver | Expiry / Review Date | Status |
|---|---|---|---|---|---|---|---|
| [EX-01] | [NFR-XXX-001] | [Approved deviation.] | [Why it is necessary.] | [Impact and mitigation.] | [Role or name.] | [YYYY-MM-DD] | Proposed / Approved / Expired / Closed |

## 8. Verification Summary

| NFR ID | Evidence | Environment / Period | Result | Verified By | Verified Date | Notes |
|---|---|---|---|---|---|---|
| [NFR-XXX-001] | [Test report, dashboard, audit record, or link.] | [Environment and time window.] | Not Run / Pass / Fail / Accepted Exception | [Role or name.] | [YYYY-MM-DD] | [Relevant constraint.] |

## 9. Quality Checklist

- [ ] Every NFR concern in each related Feature Spec is traced in Section 3.
- [ ] Every applicable category has at least one requirement or an explicit reason why no requirement is needed.
- [ ] Each NFR catalog row contains Category, Item, Description, Priority, Status, Verification, and Source.
- [ ] Targets include measurable values and operating conditions, or are marked `TBD` with an Open Question.
- [ ] Priority, Status, and Verification Result are not conflated.
- [ ] High-risk requirements contain detailed verification records.
- [ ] No unapproved service level, compliance rule, or numeric threshold has been invented.
- [ ] Exceptions have an owner, risk statement, approval state, and review or expiry date.

## 10. Open Questions

| ID | Question | Related NFR / Category | Impact | Owner | Due Date | Status |
|---|---|---|---|---|---|---|
| [OQ-01] | [Missing target, scope, verification method, or stakeholder decision.] | [NFR-ID / Category] | [What cannot be approved or verified.] | [Role or team.] | [YYYY-MM-DD / TBD] | Open / Answered / Deferred |

## References

- [ISO/IEC 25010:2023 Product quality model](https://www.iso.org/standard/78176.html)
- [ISO/IEC 25030:2019 Quality requirements framework](https://www.iso.org/standard/72116.html)
- [ISO/IEC 25023:2016 Measurement of system and software product quality](https://www.iso.org/standard/35747.html)
