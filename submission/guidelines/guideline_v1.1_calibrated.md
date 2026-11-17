# Label contract — Phố châu Á — BỔ SUNG v1.1 — 2A202603132 - Trần Xuân Bắc

> **Học viên đã xác nhận cả ba ca CAL-01–03 trong phiên làm bài.** Bản này chỉ ghi phần bổ sung so với v1.0; taxonomy cập nhật version v1.1 và giữ nguyên toàn bộ mục rules.

## 1. Câu hỏi mở đã chốt

| Case | Câu hỏi | Quy tắc đã chốt | Ảnh ví dụ |
|---|---|---|---|
| CAL-02 | Box/mask xe chở hàng có gồm hàng rời và giỏ không? | Box gồm phần nhìn thấy của xe và giỏ/khung gắn cố định. Không nới theo hàng rời nhô quá 20% chiều dài xe. Mask gồm bề mặt xe/giỏ cố định nhìn thấy, loại trái cây, bao và hàng rời; không đoán phần xe bị hàng che. | [img_031](../../data/images/img_031.jpg), [img_009](../../data/images/img_009.jpg) |

Nguồn: câu hỏi mở 3, v1.0 mục 6; làm rõ mục 4.1.5 và 4.2. Học viên đã chốt ca này; báo cáo QC hiện được chạy với `--guideline-gap 0`. Báo cáo trước khi chốt được giữ riêng trong hồ sơ QC lượt đầu.

## 2. Ca khó và bước kiểm đã chốt

| Case | Quan sát có bằng chứng | Cách xử lý đã chốt | Liên hệ v1.0 |
|---|---|---|---|
| CAL-01 | `img_003`: nhãn `three_wheeler` xuất hiện trên xe tải ở nền và xe hai bánh đỗ cạnh lề; cùng vùng xe còn có box khác lớp. [Ảnh nền](../qc/evidence/003-background.jpg), [xe đỗ](../qc/evidence/003-parked-bike.jpg). | Dùng cấu trúc xe nhìn thấy để chọn lớp. Mỗi vật giữ một nhãn đúng; không chắc thì bật `can_review` và kiểm lại. Khi gộp nhiều model, đối chiếu box chồng nhau trước khi giữ. | Áp dụng mục 2 và 4.3; không tạo thêm lớp và không đổi ngưỡng số đo. |
| CAL-02 | `img_031`: box xe đạp cắt phần khung/giỏ bên trái; `img_009` có hàng rời che xe. [Giỏ và khung](../qc/evidence/031-basket.jpg). | Áp dụng quy tắc box/mask ở mục 1. | Làm rõ mục 4.1.5, 4.2 và ca xe đạp chở hàng ở mục 5. |
| CAL-03 | `img_013`: mask SAM còn dính người lái và người mặc áo sọc sau một click âm. [Mask đã nhận](../masks/tuktuk_img013.jpg). | Người là instance riêng. Kiểm đầu/thân/chân sau click âm; chỉnh tiếp khi mask xe còn lấn người nhìn thấy qua cạnh hở. | Áp dụng mục 4.2.4; thêm bước kiểm sau prompt. |

Mỗi ca có một dòng tại `../qc/calibration_decisions.csv`, trạng thái `da_xac_nhan_boi_hoc_vien`. Những lỗi phát hiện trong mẫu QC vẫn được giữ trên phiếu để xử lý; việc chốt guideline không tự sửa nhãn.

## 3. Lịch sử thay đổi

| Phiên bản | Trạng thái/thay đổi | Bằng chứng |
|---|---|---|
| v1.0 | Bản giảng viên, giữ nguyên | `guideline/guideline_v1.0_label_contract.md` |
| v1.1 đã xác nhận | Phân biệt hàng rời và giỏ cố định; kiểm nhãn/box trùng; kiểm vùng người trong mask xe | CAL-01, CAL-02, CAL-03; ảnh img_003, img_009, img_013, img_031 |
