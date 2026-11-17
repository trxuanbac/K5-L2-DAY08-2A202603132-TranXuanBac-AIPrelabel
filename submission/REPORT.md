# Báo cáo Day 08 — 2A202603132 - Trần Xuân Bắc

> Một file duy nhất cho cả bài (đã gộp recipe, QC và ghi chú cá nhân). Mọi con số kèm **mẫu số** và nguồn (file nào). Viết bằng lời của bạn.

## 1. Model và recipe (Part 2–3)

| Lớp | Model + cỡ | Ngưỡng | Nguồn lần chạy và quét ngưỡng |
|---|---|---|---|
| person / bicycle / motorbike / car / bus / truck | YOLO26m, Colab CPU | 0.3 mặc định theo script | `qc/colab_stage1/runs.csv`, r05; script quét không chọn ngưỡng riêng cho person, bicycle, motorbike, car vì không đạt recall 90%; bus chỉ 1 vật, truck 0 vật gold. |
| three_wheeler | YOLOE-26s, prompt tuk-tuk / cyclo / cargo tricycle | 0.15 | `qc/colab_stage1/runs.csv`, r06; script quét ghi recall 7/7, precision 78% trên gold ở ngưỡng này. |

- Lệnh `merge_prelabels.py` đã dùng: `.venv/bin/python scripts/merge_prelabels.py work/colab-stage1-20261117/work/prelabel/yoloe_all/pre.coco.json work/colab-stage1-20261117/work/prelabel/y26_all/pre.coco.json --thr three_wheeler=0.15 --conf 0.3 --iou 0.6 --split batch,gold --out work/prelabel/merged_review/pre.coco.json`
- **SAM đã chạy:** SAM 2.1 tiny (`sam2.1_t.pt`), CPU, cỡ nhỏ cho cấu hình RAM 8 GB. Lượt `r06` có 2 ảnh và 8 mask; xem ảnh kết quả trong `qc/model_tour/`.
- Lỗi nào **không sửa được bằng đổi ngưỡng** (ví dụ tuk-tuk bị gọi `car`)? Sửa thế nào? <<>>
- Box **điểm cao mà sai** hoặc **điểm thấp mà đúng** (ảnh nào): <<>>
- Giới hạn: chọn và chấm ngưỡng trên cùng 4 ảnh gold; gold cũng đã có nhãn nháp trước lượt học viên chỉnh sửa. Các số đo này không phải kiểm định trên gold độc lập. Lớp ít mẫu hoặc không đạt recall mục tiêu được script giữ ở ngưỡng mặc định.

## 2. AI error profile (từ `qc/review_stats.md`)

| Trạng thái | Số | Tỉ lệ | Mẫu số |
|---|---|---|---|
| accepted | 467 | 89,8% | 520 box máy |
| edited | 10 | 1,9% | 520 box máy |
| deleted | 43 | 8,3% | 520 box máy |
| added | 12 | 2,5% | 489 đối tượng sau duyệt |

Nguồn: `qc/review_stats.json`, lượt review đầu của job 23. File COCO xuất có 24 ảnh/500 annotation; script loại 23 đối tượng nằm quanh các bẫy (tổng cả trước và sau duyệt) khỏi bảng trạng thái. Số đếm trong bảng không phải toàn bộ số box trong file xuất.

- Lớp nào máy tệ nhất? Vì sao (dẫn ảnh)? <<>>
- So với gold: precision của **máy** 47/(47 + 25) = 65,3%; recall 47/(47 + 28) = 62,7% (75 đối tượng gold, không tính 1 ignore region). Chỉ đo trên 4 ảnh gold đã dùng để chọn ngưỡng và đã có nhãn nháp trước lượt học viên chỉnh sửa; chưa phải đánh giá độc lập.

## 3. Thiên kiến tự động hóa và ảnh bẫy

- Bắt bẫy lượt review đầu: 6/12 = 50%; ngưỡng trong taxonomy là 80%. Theo loại: loose 1/3, missing 1/3, wrong_class 2/3, extra 2/3. Script ghi lọt ở `img_013` (missing), `img_021` và `img_024` (loose), `img_035` (extra), `img_006` (wrong_class), `img_034` (missing). Vì sao (bạn đã bỏ bước nào của checklist)? <<>>
- Sau sửa bổ sung: script ghi 12/12; bản CVAT hiện có 24 ảnh/490 annotation. Đây là kiểm sau khi đã biết các bẫy; số đo lượt review đầu vẫn là 6/12 và được giữ nguyên. Hồ sơ ở `qc/reviews/batch-02/`.
- Accepted cao mà bắt bẫy thấp (hoặc ngược lại) nói gì về cách bạn duyệt? <<>>

## 4. Máy có đáng dùng không?

- Thời gian (từ `time_log.csv`): gán tay/chỉnh sửa gold **6,25 phút/ảnh** (25 phút/4 ảnh) vs review batch **1,25 phút/ảnh** (30 phút/24 ảnh). Cả hai do học viên cung cấp; 30 phút chỉ là lượt review đầu, chưa gồm sửa lỗi sau đo. Thiên lệch (bạn gán gold trước nên đã quen cảnh): <<>>
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

- Mẫu đã tạo: 5 ảnh (0 ảnh `can_review` + 5 ngẫu nhiên, seed 42), 98 đối tượng. Phiếu `qc_review.csv` chưa điền, chưa có lượt QC hình ảnh. Người kiểm khi thực hiện: <<>>.
- Bản ứng viên: `release/final_det.coco.json` gồm 24 ảnh/490 annotation, khớp bản export sau sửa. Còn mask SAM, calibration và QC; chưa có quyết định Release.
- Lỗi theo **đối tượng**: <<.../... = ...%>> · theo **ảnh**: <<.../... = ...%>> (ngưỡng Release ≤ 2%)
- Top lỗi (trong: bỏ sót, thừa, sai lớp, sai vị trí/kích thước, sai thuộc tính, sai mask) + một ảnh ví dụ mỗi loại: <<>>
- **Giới hạn mẫu nhỏ** (cận trên 95% trong `qc_report_auto.md`): <<>>
- Script kiểm được / không kiểm được (ví dụ ôm sát, cùng bỏ sót với máy, theo checklist thật): <<>>

**Quyết định: <<Release / Hold / Rework>>**, ngày <<YYYY-MM-DD>>. Lý do (đi theo Hold → Rework → Release): <<>>
Nếu Rework / Hold, việc cần làm tiếp: <<>>

## 8. Ghi chú cá nhân

- **Dùng AI để làm bài:** Codex hỗ trợ đọc yêu cầu, tạo repo local, cài thư viện nhẹ, chuẩn bị project/task CVAT, xuất COCO và chạy script đo. Học viên báo đã review job 23 trong 30 phút; đã xuất lượt đầu 24 ảnh/500 annotation, không lỗi cấu trúc nhưng còn 10 cảnh báo box cao dưới 20 px. Bản này và số đo được giữ tại `qc/reviews/batch-01/`. Bản sửa bổ sung ở `qc/reviews/batch-02/` có 24 ảnh/490 annotation, không còn cảnh báo kích thước; không ghi thêm thời gian review của học viên cho đợt sửa này. QC nội dung, mask 3 vật và calibration chưa hoàn tất.
- Gold có bị nhiễm không (bạn có nhìn pre-label hay hỏi AI trước khi gán xong)? Có: task 21 đã có bản nháp 58 annotation trước lượt gán tay/chỉnh sửa 25 phút do học viên báo. Bản học viên lưu có 83 annotation; review bỏ 7 box dưới 20 px, xuất `labels/gold_manual.json` với 76 annotation. Bộ này không phải gold được tạo độc lập trước khi thấy nhãn gợi ý.
- Máy / GPU / CVAT dùng; vướng mắc cài đặt: macOS 26.3, Apple M1, RAM 8 GB; CVAT Docker 2.82.1 đã có sẵn. Môi trường QC nhẹ `.venv` dùng Python 3.12.16; môi trường model `work/model-env` dùng Python 3.13.17, đã chạy local bằng CPU. Colab ban đầu báo phần phụ trợ không có sẵn; sau đó học viên chạy được và tải `colab_stage1.zip`. Nhật ký trong ZIP ghi thiết bị `cpu`, chưa có lượt chạy GPU T4 để xác nhận.
- Dùng cache `data/cache/` thay vì tự chạy? Không. Các lượt tour local được lưu ở `model_log.csv` và `qc/model_tour/runs.json`. Part 3–4 hiện dùng kết quả Colab CPU: YOLO26m và YOLOE-26s, có nhật ký gốc và checksum tại `qc/colab_stage1/`. Kết quả quét YOLO26 nano cũ được giữ tại `qc/model_tour/local_threshold_sweep.*`.
- Lỗi / bug script đã gặp (nếu có): <<>>
- Một điều bạn làm khác lần sau: <<>>
