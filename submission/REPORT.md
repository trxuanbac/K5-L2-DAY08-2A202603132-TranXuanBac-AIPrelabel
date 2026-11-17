# Báo cáo Day 08 — 2A202603132 - Trần Xuân Bắc

> Một file duy nhất cho cả bài (đã gộp recipe, QC và ghi chú cá nhân). Mọi con số kèm **mẫu số** và nguồn (file nào). Viết bằng lời của bạn.

## 1. Model và recipe (Part 2–3)

| Lớp | Model + cỡ | Ngưỡng | Vì sao (dẫn `run_id` trong `model_log.csv`) |
|---|---|---|---|
| person / bicycle / motorbike / bus / truck | YOLO26n | 0.3 mặc định theo script | r02/r04; person, bicycle, motorbike không đạt recall mục tiêu 90% ở bất kỳ ngưỡng thử <= 0.5; bus chỉ 1 vật, truck 0 vật gold nên không chọn ngưỡng riêng. |
| car | YOLO26n | 0.45 | Script quét đề xuất; 8 vật car trong gold. |
| three_wheeler | YOLOE-26s, prompt tuk-tuk / cyclo / cargo tricycle | 0.15 | Script quét đề xuất; 7 vật three_wheeler trong gold. |

- Lệnh `merge_prelabels.py` đã dùng (dán nguyên): <<>>
- **SAM đã chạy:** SAM 2.1 tiny (`sam2.1_t.pt`), CPU, cỡ nhỏ cho cấu hình RAM 8 GB. Lượt `r06` có 2 ảnh và 8 mask; xem ảnh kết quả trong `qc/model_tour/`.
- Lỗi nào **không sửa được bằng đổi ngưỡng** (ví dụ tuk-tuk bị gọi `car`)? Sửa thế nào? <<>>
- Box **điểm cao mà sai** hoặc **điểm thấp mà đúng** (ảnh nào): <<>>
- Giới hạn: chọn và chấm ngưỡng trên cùng 4 ảnh gold; gold cũng đã có nhãn nháp trước lượt học viên chỉnh sửa. Các số đo này không phải kiểm định trên gold độc lập. Lớp ít mẫu hoặc không đạt recall mục tiêu được script giữ ở ngưỡng mặc định.

## 2. AI error profile (từ `qc/review_stats.md`)

| Trạng thái | Số | Tỉ lệ | Mẫu số |
|---|---|---|---|
| accepted | <<>> | <<>> | <<box máy>> |
| edited | <<>> | <<>> | <<>> |
| deleted | <<>> | <<>> | <<>> |
| added | <<>> | <<>> | <<đối tượng sau duyệt>> |

- Lớp nào máy tệ nhất? Vì sao (dẫn ảnh)? <<>>
- So với gold: precision / recall của **máy** <<>> (mẫu số: <<đối tượng gold>>)

## 3. Thiên kiến tự động hóa và ảnh bẫy

- Bắt bẫy: <<.../12>>; loại nào lọt: <<>>; vì sao (bạn đã bỏ bước nào của checklist)? <<>>
- Accepted cao mà bắt bẫy thấp (hoặc ngược lại) nói gì về cách bạn duyệt? <<>>

## 4. Máy có đáng dùng không?

- Thời gian (từ `time_log.csv`): gán tay/chỉnh sửa gold **6,25 phút/ảnh** (25 phút/4 ảnh, học viên cung cấp) vs duyệt <<... phút/ảnh>>. Thiên lệch (bạn gán gold trước nên đã quen cảnh): <<>>
- Kết luận: <<có / không / chỉ cho lớp nào>>, dựa trên <<số liệu>>
- **Ba quy tắc giảm thiên kiến của bạn** (mỗi quy tắc kiểm tra được bằng số hoặc việc làm):
  1. <<>>
  2. <<>>
  3. <<>>

## 5. Mask SAM cho 3 vật (Part 5)

| Ảnh | SAM (phiên bản) | Số click | Mask gồm người lái / hàng hoá? | Lỗi quan sát | File trong `masks/` |
|---|---|---|---|---|---|
| <<img_0xx>> | <<>> | <<>> | <<>> | <<>> | <<>> |

- Đối chiếu guideline mục 4.2: quy tắc nào giúp, quy tắc nào thiếu? <<>>
- *(Tuỳ chọn)* Interactor SAM trong CVAT: làm được / không (lỗi gì, đã thử gì); khác gì offline: <<>>

## 6. Calibration (Part 6)

- Số quyết định: <<>> (`calibration_decisions.csv`); quan trọng nhất (dẫn `CAL-xx`): <<>>
- Quy tắc mới đã vào `guideline_v1.1_calibrated.md`: <<>>
- Nguyên nhân gốc: <<guideline mơ hồ / chưa nắm quy tắc / máy>>

## 7. QC và quyết định (Part 6)

- Mẫu: <<n>> ảnh (<<m>> ảnh `can_review` + <<k>> ngẫu nhiên, seed 42); người kiểm: bạn (**hạn chế**: bạn vừa là người duyệt).
- Lỗi theo **đối tượng**: <<.../... = ...%>> · theo **ảnh**: <<.../... = ...%>> (ngưỡng Release ≤ 2%)
- Top lỗi (trong: bỏ sót, thừa, sai lớp, sai vị trí/kích thước, sai thuộc tính, sai mask) + một ảnh ví dụ mỗi loại: <<>>
- **Giới hạn mẫu nhỏ** (cận trên 95% trong `qc_report_auto.md`): <<>>
- Script kiểm được / không kiểm được (ví dụ ôm sát, cùng bỏ sót với máy, theo checklist thật): <<>>

**Quyết định: <<Release / Hold / Rework>>**, ngày <<YYYY-MM-DD>>. Lý do (đi theo Hold → Rework → Release): <<>>
Nếu Rework / Hold, việc cần làm tiếp: <<>>

## 8. Ghi chú cá nhân

- **Dùng AI để làm bài:** Codex hỗ trợ đọc yêu cầu, tạo repo local, cài thư viện nhẹ và chuẩn bị project/task CVAT. Đối chiếu cấu hình với `submission/taxonomy.json`, `data/split.csv` và chạy kiểm tra môi trường. Học viên cần kiểm tra bộ nhãn và task trong CVAT. Phần này ghi nhận công việc chuẩn bị; các kết quả review và QC chưa hoàn tất.
- Gold có bị nhiễm không (bạn có nhìn pre-label hay hỏi AI trước khi gán xong)? Có: task 21 đã có bản nháp 58 annotation trước lượt gán tay/chỉnh sửa 25 phút do học viên báo. Bản học viên lưu có 83 annotation; review bỏ 7 box dưới 20 px, xuất `labels/gold_manual.json` với 76 annotation. Bộ này không phải gold được tạo độc lập trước khi thấy nhãn gợi ý.
- Máy / GPU / CVAT dùng; vướng mắc cài đặt: macOS 26.3, Apple M1, RAM 8 GB; CVAT Docker 2.82.1 đã có sẵn. Môi trường QC nhẹ `.venv` dùng Python 3.12.16; môi trường model `work/model-env` dùng Python 3.13.17, đã chạy local bằng CPU. Cấu hình chuẩn bị 8 GB theo trang hướng dẫn là chạy model trên Colab; Colab báo phần phụ trợ không có sẵn; dùng kết quả chạy local CPU, chưa có lượt chạy GPU T4 Colab.
- Dùng cache `data/cache/` thay vì tự chạy? Không. Đã dùng kết quả chạy local CPU trong `work/prelabel/`; các lượt tour được lưu ở `model_log.csv` và `qc/model_tour/runs.json`.
- Lỗi / bug script đã gặp (nếu có): <<>>
- Một điều bạn làm khác lần sau: <<>>
