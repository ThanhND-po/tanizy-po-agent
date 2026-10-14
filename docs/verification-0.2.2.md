# Verification: 0.2.2

Ngày kiểm tra: 2026-10-14.

## Kết luận

**PASS cho metadata contract, tính đầy đủ của resource, installer và packaging trong phạm vi kiểm tra dưới đây.** Đã bump package từ `0.2.1` lên `0.2.2`; ba package theo target lấy version từ package gốc.

Đánh giá cấu trúc: phù hợp với gói skill portable cho nhiều agent, có thể release. Chưa thể khẳng định mọi workflow đã tối ưu hoặc mọi model sẽ luôn sinh metadata đúng. Tests kiểm tra file và hành vi installer, không thay thế model eval hay validator của project.

## Metadata contract

- `writing-requirements/references/document-metadata.md` là contract dùng chung; enum, schema và phạm vi áp dụng thuộc project đích.
- Delivery `status`, document approval và verification được tách riêng. Sửa nội dung không tự thay delivery state; approval evidence phải gắn với revision thực sự được duyệt.
- Áp dụng delivery metadata theo cả document type và owning path. Không tự thêm status cho standards, entities, roles, indexes hoặc references chỉ vì sửa file.
- Đồng bộ Metadata và catalog hiện tại bằng exact path/link hoặc ID; giữ history, scope notes, HTTP/product statuses và Decision Log.
- Bảy template có frontmatter minh họa nhất quán. `draft`, IDs và dates là sample cần thay theo project; Use Case standalone phải resolve schema trước, Use Case embedded dùng metadata của artifact chứa nó.
- API/NFR tách implementation, approval và verification; không còn dùng một mixed lifecycle enum cho ba ý nghĩa này.
- Policy chưa có, mapping mâu thuẫn hoặc delivery state chưa được xác nhận phải được làm rõ trước khi gán giá trị; không tự tạo enum.

## Các điểm audit đã sửa

| Điểm phát hiện | Thay đổi |
|---|---|
| Cài lẻ artifact update có thể thiếu shared metadata contract | Thêm required dependency `artifact-update-process -> writing-requirements`; manual-copy và tool guides được đồng bộ. |
| Cài lẻ mockup có thể thiếu resource của các mode được hỗ trợ | Thêm dependencies `web-design-guidelines`, `creating-diagrams`, `shadcn-ui`. |
| Package check bỏ qua thư mục ẩn `.agents` của adapter | Kiểm tra cả rule Antigravity; có negative test khi rule bị loại khỏi tarball. |
| Guard dùng `existsSync` bỏ qua dangling symlink | Kiểm tra symlink bằng `lstatSync`, trước khi ghi, cho cả symlink tồn tại và dangling. |
| Hướng dẫn Basic Design luôn bị nạp khi làm artifact khác | Đưa chi tiết sang `references/basic-design-authoring.md`, đọc theo artifact type. |
| Metadata rules lặp trong adapters | Adapter giữ nguyên tắc project ownership và route đến contract của skill. |
| Một số description quá dài hoặc trigger quá rộng | Rút gọn mockup/meeting descriptions; shadcn không được chọn chỉ vì project có `components.json`. |
| Approval có thể bị hỏi lại dù cùng write set đã được duyệt | Writing/update skills tái sử dụng approval cho cùng content, scope và paths. |

Selective install không thay adapter. Full install/update chỉ thay Tanizy-managed skills, block và rule; project policy và artifact hiện có không được migrate tự động. `--force` thay cả dependency đã resolve; người dùng cần review plan khi dependency có local edits.

## Bằng chứng kiểm tra

| Kiểm tra | Kết quả |
|---|---|
| `quick_validate.py` của skill-creator | 9/9 skills hợp lệ |
| `npm run test:installer` | 24/24 tests pass |
| `npm run test:diagrams` | 31/31 tests pass |
| `npm run test:packages` | 5/5 tests pass |
| Universal `npm pack` dry run | 49 published files |
| Codex target package dry run | 46 published files |
| Claude Code target package dry run | 46 published files |
| Antigravity target package dry run | 47 published files |
| `git diff --check` | Pass |

Tarball tests pack và giải nén bốn package, chạy installer từ package đã giải nén bên ngoài repository, kiểm tra full/selective install, dry-run và force update. Universal được kiểm tra trên cả ba target; package theo target được kiểm tra trên target tương ứng và từ chối target khác. Resource được so sánh theo bytes, gồm cả icon catalog nén. Fixtures dùng enum riêng, artifact đã released theo enum đó, numbered Metadata, approval evidence và scope notes; các nội dung này giữ nguyên sau installation/update.

CI đã thêm tarball tests. Các fixture được tạo trong temporary directories và dọn sau test. Không mở test server hoặc sửa project đích thật.

## Best-practice và giới hạn

- Giữ `core/skills/` làm single source of truth, adapters mỏng, references đọc theo nhu cầu và scripts cho thao tác deterministic là hướng phù hợp. Không cần thêm một tầng workflow engine để bắt agent chạy quy trình cố định.
- `five-whys-rca/SKILL.md` còn dài, chứa nhiều chi tiết của General RCA và Incident Report. Có thể tách mode-specific instructions sang references trong một đợt tối ưu riêng, sau khi có behavioral eval để bảo toàn interview/approval semantics.
- Brainstorming và mockup còn nhiều confirmation gates. Đây là lựa chọn workflow hiện tại; đánh giá và rút gọn dựa trên cách dùng thực tế, tránh bỏ các gate có ý nghĩa chỉ để giảm số dòng.
- Gói npm là lựa chọn phân phối portable hiện tại. Với phân phối dành riêng cho Codex/ChatGPT, tài liệu hiện tại khuyến nghị plugin; có thể bổ sung sau, không bắt buộc đổi toàn bộ installer đa target của release này.
- Skill instructions không chặn được người dùng sửa metadata trực tiếp. Nếu cần bảo đảm tự động, project phải kiểm tra enum, applicability và catalog consistency bằng validator trong save/CI workflow.
- Chưa chạy behavioral eval với model hoặc kiểm tra discovery trong phiên Codex, Claude Code và Antigravity thật. Không có bằng chứng để tuyên bố mọi model/host đã runtime-verified.
- Installer preflights các collision/path lỗi đã kiểm tra; không có transaction rollback cho mọi lỗi filesystem hoặc thay đổi đồng thời từ process khác.
- npm publish dành cho maintainer thực hiện sau bước này.

## Tài liệu đối chiếu

- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills): discovery locations, concise descriptions, progressive disclosure, optional UI metadata và plugin distribution.
- [OpenAI: Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): giảm context thừa, tránh quy trình quá cứng và giữ decision boundaries tương xứng với task.
