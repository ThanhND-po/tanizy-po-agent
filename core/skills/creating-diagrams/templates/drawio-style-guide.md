# Draw.io Style Guide — Adaptive Theme (Light & Dark Mode)

> **⚡ AI Agent: Đọc file này trước khi tạo hoặc chỉnh sửa bất kỳ file `.drawio` nào.**
>
> Mục đích: Đảm bảo mọi diagram hiển thị hoàn hảo trên cả **Light Mode** và **Dark Mode** trong draw.io desktop, app.diagrams.net, và VS Code extension.

---

## 1. Nguyên tắc cốt lõi: Adaptive Theme First

Draw.io tự động chuyển đổi màu Text và Stroke (đen ↔ trắng) khi người dùng đổi theme **nếu và chỉ nếu** những thuộc tính đó không bị hardcode.

| Vị trí phần tử | Quy tắc `fontColor` | Quy tắc `strokeColor` | Lý do |
|---|---|---|---|
| **Trên Canvas** (Arrow label, Edge label, UML Actor label, floating text) | ❌ KHÔNG khai báo | ❌ KHÔNG khai báo | Draw.io tự đổi theo theme |
| **Trong Box** (Actor, Phase Header, Note, Database box) | ✅ BẮT BUỘC `#333333` | ✅ Dùng màu semantic của zone | Nền pastel cố định, cần chữ tối để có contrast |
| **Semantic Line** (mũi tên có màu ngữ nghĩa: đỏ/xanh) | ❌ KHÔNG khai báo | ✅ Dùng màu semantic | Label vẫn tự đổi màu theo theme |

**Quy tắc vàng**: Nếu phần tử nằm TRÊN nền canvas → bỏ trống fontColor/strokeColor. Nếu phần tử nằm TRONG box có nền màu → hardcode fontColor=#333333.

---

## 2. Color Palette

### 2.1 Fill Colors — Actor Zones / Semantic Groups

| Token | fillColor | strokeColor (border của box) | Ý nghĩa |
|---|---|---|---|
| 🟢 User / Client Side | `#d5e8d4` | `#82b366` | Xanh lá nhạt — phía người dùng, client app |
| 🔵 Core System / CMS | `#dae8fc` | `#6c8ebf` | Xanh dương nhạt — core system, shared data |
| 🟣 Backend Services | `#e1d5e7` | `#9673a6` | Tím nhạt — service layer, backend |
| 🟡 Batch / External | `#fff2cc` | `#d6b656` | Vàng nhạt — batch jobs, external services |
| 🔴 Critical / Error | `#f8cecc` | `#b85450` | Đỏ nhạt — security-critical, error states |
| ⬜ Infra / Database | `#F5F5F5` | `#999999` | Xám nhạt — infrastructure, DB |
| 🔷 Title Background | `#f5f5f5` | `#CCCCCC` | Xám nhạt — title bar, section header |

### 2.2 Connection / Edge Colors

| Loại | strokeColor | fontColor (label) | strokeWidth | Ghi chú |
|---|---|---|---|---|
| Request (plain solid) | *(bỏ trống)* | *(bỏ trống)* | 1 | Tự adaptive |
| Response (plain dashed) | *(bỏ trống)* | *(bỏ trống)* | 1 | dashed=1 |
| Critical / Error path | `#b85450` | *(bỏ trống)* | 2 | Đỏ semantic, label vẫn adaptive |
| Success path | `#82b366` | *(bỏ trống)* | 2 | Xanh semantic, label vẫn adaptive |
| Lifeline (Sequence) | *(bỏ trống)* | — | 1 | dashed=1 dashPattern=5 5 |

---

## 3. XML Style Snippets

> **Lưu ý**: Để "bỏ trống" một thuộc tính, không viết nó vào chuỗi `style=""` — **không phải** viết `fontColor=none` hay `strokeColor=default`.

### 3.1 Title / Section Header

```xml
style="text;html=1;align=center;fontSize=14;fontStyle=1;fillColor=#f5f5f5;strokeColor=#CCCCCC;rounded=1;fontColor=#333333;"
```

### 3.2 Actor Box (Rounded, nền pastel)

```xml
style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontStyle=1;fontSize=11;fontColor=#333333;"
```

### 3.3 UML Actor Icon (Label ngoài canvas — adaptive)

```xml
style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;fontStyle=1;"
```
*(Không có `fontColor` — label tự đổi theo theme)*

### 3.4 Phase Header / Swimlane Header (nền xám nhạt)

```xml
style="rounded=0;whiteSpace=wrap;html=1;fillColor=#F0F4F8;strokeColor=#CCCCCC;fontSize=11;fontStyle=1;fontColor=#333333;"
```

### 3.5 Lifeline (Sequence Diagram)

```xml
style="endArrow=none;dashed=1;dashPattern=5 5;"
```
*(Không có `strokeColor` — tự adaptive)*

### 3.6 Request Arrow (Solid)

```xml
style="html=1;endArrow=block;endFill=1;fontSize=10;"
```
*(Không có `strokeColor`, không có `fontColor`)*

### 3.7 Response Arrow (Dashed)

```xml
style="html=1;endArrow=open;dashed=1;fontSize=10;"
```
*(Không có `strokeColor`, không có `fontColor`)*

### 3.8 Note Box

```xml
style="shape=note;whiteSpace=wrap;html=1;size=14;fillColor=#FFF2CC;strokeColor=#D6B656;fontSize=9;align=left;fontColor=#333333;"
```

### 3.9 Database / Storage

```xml
style="shape=mxgraph.flowchart.database;fillColor=#F5F5F5;strokeColor=#999999;fontColor=#333333;fontSize=10;"
```

### 3.10 Decision Gateway (Diamond)

```xml
style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontColor=#333333;fontSize=10;"
```

---

## 4. Layout & Spacing Rules (Chống Overlap)

### 4.1 Kích thước tối thiểu

| Element | Width (px) | Height (px) | Ghi chú |
|---|---|---|---|
| Actor Box | 120 | 40 | Tăng nếu label > 15 ký tự |
| Phase Header | 160 | 30 | — |
| Note Box | 140 | 50 | Tăng nếu text dài |
| UML Actor Icon | 30 | 60 | Cộng thêm ~20px cho label phía dưới |
| Decision Gateway | 60 | 60 | — |
| Swimlane Lane | ≥ 120 | Variable | — |

### 4.2 Khoảng cách

- **Giữa các box liền kề trên cùng hàng**: tối thiểu **30px** horizontal gap
- **Giữa các row liên tiếp (top-to-bottom)**: tối thiểu **40px** vertical gap
- **Edge label** không được chồng lên box: dùng `align=center` và `labelBackgroundColor=#ffffff` khi label bị che

### 4.3 Tự động phát hiện overlap

Trước khi save, kiểm tra:
- Có bất kỳ hai box nào có toạ độ `(x, y, width, height)` giao nhau không?
- Arrow label có nằm trong vùng box khác không?
- Nếu có → điều chỉnh `x`, `y` để tách ra, ưu tiên tăng spacing theo chiều dọc.

---

## 5. Pre-Save Checklist (Bắt buộc trước khi xuất XML)

- [ ] Mũi tên thông thường (Request/Response): **KHÔNG** có `strokeColor` trong style
- [ ] Label của mũi tên và text trên canvas: **KHÔNG** có `fontColor` trong style
- [ ] Text bên trong box (Actor, Phase, Note, DB): có `fontColor=#333333`
- [ ] Lifelines: **KHÔNG** có `strokeColor`
- [ ] UML Actor label (ngoài box): **KHÔNG** có `fontColor`
- [ ] Không có hai phần tử nào bị overlap (giao nhau về toạ độ)
- [ ] Mọi box có kích thước đủ để hiển thị text bên trong (không bị cắt)
- [ ] File XML bắt đầu bằng `<mxGraphModel>` và có cấu trúc hợp lệ

---

## 6. File XML Template (Skeleton)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxGraphModel dx="1422" dy="762" grid="1" gridSize="10" guides="1" tooltips="1"
  connect="1" arrows="1" fold="1" page="1" pageScale="1"
  pageWidth="1169" pageHeight="827" math="0" shadow="0">
  <root>
    <mxCell id="0" />
    <mxCell id="1" parent="0" />
    <!-- Elements go here with id="2", id="3", etc. -->
  </root>
</mxGraphModel>
```

**Quy tắc ID**:
- `id="0"` và `id="1"` là bắt buộc, không được xoá
- Các element bắt đầu từ `id="2"` trở đi, tăng dần, không trùng lặp
- Edge (mũi tên) dùng `source="X"` và `target="Y"` tham chiếu id của node

---

*Version: 1.0 | Dựa trên draft/guidelines/DIAGRAM_STYLE_GUIDE.md*
