# User Story Quality Checklist

Run this checklist before showing a User Story to the user when detailed review is needed. Fix all blocking issues silently first.

## Blocking Gate

A User Story is not ready to show if any item below fails.

- [ ] Story statement has a specific persona, one clear goal, and distinct business/user value.
- [ ] **[Single-Persona]** Every AC and Scenario describes behavior observable from the persona named in the Story Statement. ACs about a different persona must be split into a separate US or moved into `Given` (precondition).
- [ ] Acceptance Criteria include happy path behavior.
- [ ] Acceptance Criteria include alternative or edge behavior, or explicitly say `N/A` with a reason.
- [ ] Acceptance Criteria include exception or negative behavior, or explicitly say `N/A` with a reason.
- [ ] Usage Scenarios include Happy Path, Alternative/Edge, and Exception/Negative scenarios.
- [ ] Unknown business rules are listed as open questions, not invented as facts.
- [ ] **[Negotiable]** No implementation-binding term appears in any section (story statement, Acceptance Criteria, Scenarios). See the **Negotiable Blocklist** below for a concrete keyword reference.

## Story Statement

- [ ] Persona is specific and relevant to the product context.
- [ ] Goal describes one clear action or outcome.
- [ ] Business value is distinct from the goal.
- [ ] The statement avoids implementation details.
- [ ] The story does not combine unrelated goals.
- [ ] The story does not embed a second persona's behavior (even as a note or parenthetical).

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
- An AC or Scenario describes behavior of a persona not named in the Story Statement.

## Negotiable Blocklist (UI/Tech terms to rephrase)

If any of the following terms appear in Story Statement, AC, or Scenario, rephrase them as behavioral descriptions.

### UI State Terms
`Read-only`, `Disabled`, `Hidden`, `Visible`, `Enabled`, `Checked`, `Unchecked`, `Selected`, `Active`, `Inactive` (when describing component state)

### UI Component Names
`Dropdown`, `Modal`, `Dialog`, `Combobox`, `Checkbox`, `RadioButton`, `Toggle`, `Tab`, `DataGrid`, `Tooltip`, `Popover`, `Sidebar`, `Navbar`, `Breadcrumb`

### Tech / Protocol Terms
`HTTP 403`, `HTTP 404`, `HTTP 500`, `API`, `REST`, `GraphQL`, `endpoint`, `query`, `JOIN`, `SQL`, `CRUD`

### Cloud / Framework Names
`AWS Lambda`, `S3`, `Firebase`, `Kafka`, `Redis`, `React`, `Vue`, `Spring Boot`, `FastAPI`, `PostgreSQL`, `MongoDB`

### Replacement Examples

| ❌ Do not use | ✅ Rephrase to |
|---|---|
| Trường X hiển thị dạng `Read-only` | Người dùng có thể xem trường X nhưng không thể chỉnh sửa |
| Trường X bị `Disabled` | Trường X không cho phép tương tác |
| Hệ thống trả về `HTTP 403 Forbidden` | Hệ thống thông báo không tìm thấy nội dung |
| Store Admin có quyền `CRUD` Memo | Store Admin có thể tạo, chỉnh sửa và xóa Memo |
| Dữ liệu `JOIN` bảng `t_worker` | Dữ liệu được lấy từ hồ sơ Worker liên quan |
| Hiển thị bằng `Modal` | Hiển thị trong một cửa sổ phụ |
