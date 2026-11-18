# Day 08 — trạng thái của Trần Xuân Bắc

Cập nhật ngày 2026-11-18: **review lại đạt 12/12 bẫy = 100%**; bản nhãn cuối của [job 23](http://localhost:8080/tasks/23/jobs/23) có **24 ảnh/492 annotation**. Mẫu QC sau sửa có **0/100 đối tượng lỗi, 0/5 ảnh lỗi**; script gợi ý **Release** khi dùng số đo vòng sau sửa. Đã có gold **4 ảnh/76 annotation**, **3/3 mask SAM** và **3 ca calibration v1.1**. Lượt review đầu 30 phút, 6/12 bẫy và các giới hạn của lượt tái kiểm được giữ trong hồ sơ từng vòng.

## 1. Mở nhãn trong CVAT

| Bộ ảnh | File COCO | Số ảnh | Annotation | Job |
|---|---|---:|---:|---|
| Gold đã xuất | [gold_manual.json](submission/labels/gold_manual.json) | 4 | 76 | [Mở job 21](http://localhost:8080/tasks/21/jobs/21) |
| Batch draft | [batch_draft.json](submission/labels/batch_draft.json) | 24 | 385 | [Mở job 22](http://localhost:8080/tasks/22/jobs/22) |
| Batch để review, từ Colab | [pre_traps_import.coco.json](submission/prelabel/pre_traps_import.coco.json) | 24 | 532 | [Mở job 23](http://localhost:8080/tasks/23/jobs/23) |
| Batch sau lượt review đầu | [batch_reviewed.json](submission/labels/batch_reviewed.json) | 24 | 500 | [Mở job 23](http://localhost:8080/tasks/23/jobs/23) |
| Batch hiện tại sau sửa bổ sung | [corrected.coco.json](submission/qc/reviews/batch-02/corrected.coco.json) | 24 | 490 | [Mở job 23](http://localhost:8080/tasks/23/jobs/23) |
| Batch hiện tại sau sửa QC | [final_det.coco.json](submission/release/final_det.coco.json) | 24 | 492 | [Mở job 23](http://localhost:8080/tasks/23/jobs/23) |

Project: [day08-2A202603132](http://localhost:8080/projects/3). Task 21 hiện tên `gold-draft`; task 22 tên `batch-review`. Mỗi task có một job. Lần nhập nháp ban đầu được lưu tại [kết quả nhập nhãn](cvat/annotation_drafts.json). Bản gold hiện tại: [hồ sơ review và export](submission/qc/reviews/gold-01/README.md).

## 2. Phần đã thực hiện

- Đã chạy bốn lượt tour Part 2 bằng **CPU trên Colab**: YOLO26m conf 0.25 và 0.5, YOLOE, YOLO26m + SAM 2.1 base. Có nhật ký, thông số và ảnh so sánh trong [hồ sơ tour model](submission/qc/model_tour/README.md). Các lượt local với YOLO26 nano và SAM tiny trước đó được giữ để đối chiếu.
- Có hai lượt nguồn trên toàn bộ 36 ảnh ở conf 0.05 cho Part 3; đã chạy quét ngưỡng bằng gold đã xuất, tạo [threshold_sweep.md](submission/qc/threshold_sweep.md), CSV và PNG.
- Gộp kết quả cho 4 ảnh gold và 24 ảnh batch ở ngưỡng khởi đầu 0.25; chưa xem đây là ngưỡng được calibration bằng gold độc lập.
- Xem các ảnh tổng quan, sửa một số lỗi nhầm lớp, box trùng và đối tượng không thuộc taxonomy; bổ sung một số người/xe bị sót.
- Bỏ box đối tượng thấp hơn 20 px. Giữ `can_review` ở các ca chưa chắc quy tắc.
- Kiểm tra hai file bằng `validate_labels.py`, đủ 4/24 ảnh và không có lỗi cấu trúc. Việc này chưa xác nhận mọi box đều đúng hoặc đã tìm hết vật.
- Lần nhập nháp ban đầu: 58 + 385 = 443 annotation. Sau lượt chỉnh sửa, job 21 có 83 annotation; review bỏ 7 box dưới 20 px và xuất bản 76 annotation. Đã kiểm tra file khớp với CVAT; validator không còn lỗi hoặc cảnh báo kích thước.
- Thời gian chỉnh sửa gold được ghi là 25 phút trong `submission/time_log.csv`. Bản nháp gốc và bản 83 annotation trước review được giữ để đối chiếu.
- Đã xuất lượt review batch đầu từ job 23, kiểm tra đủ 24 ảnh/500 annotation và đối chiếu với annotation hiện lưu trong CVAT. Thời gian review lượt đầu là 30 phút; [hồ sơ export và số đo](submission/qc/reviews/batch-01/README.md). Validator không có lỗi cấu trúc; còn 10 cảnh báo box nhỏ.
- Sau đó đã sửa bẫy và bỏ 10 box dưới 20 px, tạo bản 490 annotation ở [batch-02](submission/qc/reviews/batch-02/README.md). Sau lượt QC đã sửa thêm 8 lỗi, tạo bản hiện tại 492 annotation và `qc_fixed.json` cho 12 ảnh. Xem [QC sau sửa](submission/qc/reviews/qc-02/README.md). Số đo review đầu 6/12 vẫn giữ nguyên.

Ảnh overlay dùng để kiểm tra nằm trong `work/gold-refined-viz/` và `work/batch-refined-viz/` trên máy này.

## 3. Trạng thái nộp bài

1. Part 5 đã có đủ ba vật: img_013 (SAM base, Colab), img_004 và img_009 (SAM tiny, local CPU). Xem `submission/masks/` và `submission/qc/sam_clicks/`; các nhận xét tập trung vào phần người hoặc hàng hóa bị lẫn trong mask.
2. Đã chốt CAL-01–03 và cập nhật taxonomy v1.1, giữ nguyên mục rules. Nội dung cụ thể nằm trong guideline và báo cáo.
3. QC trước sửa ghi 8/98 lỗi sau đính chính, 4/5 ảnh có lỗi; đã xử lý 8 lỗi theo yêu cầu. Tái kiểm cùng 5 ảnh/100 đối tượng không ghi nhận lỗi rõ mới. Review lại đạt 12/12 bẫy; script gợi ý Release khi đọc `submission/qc/reviews/qc-02/review_stats_after_rework.json`. Đây chưa phải kiểm độc lập hoặc chứng minh toàn bộ 24 ảnh sạch lỗi.
4. Đã có `gold_manual.json`, `batch_reviewed.json`, bản sửa QC và `traps_key.json` theo cấu trúc nộp. Gold có nhãn nháp trước lượt chỉnh sửa; giới hạn này được giữ trong báo cáo.
5. Trạng thái sau review lại: **Release theo mẫu QC sau sửa**. Quyết định Rework ngày 2026-11-17 thuộc vòng trước. Sau khi kiểm tra và push bản cập nhật, nộp link repo lên LMS theo hướng dẫn trong `SUBMISSION.md`.

## 4. Môi trường và repo

Repo public: https://github.com/trxuanbac/K5-L2-DAY08-2A202603132-TranXuanBac-AIPrelabel. Nhánh `main`, `origin` trỏ repo này; `upstream` là repo đề.

Máy Apple M1 arm64, RAM 8 GB, macOS 26.3, CVAT Docker 2.82.1. `.venv` Python 3.12.16 dùng thư viện nhẹ cho đo số/QC. Có tour local CPU trong `work/model-env` (Python 3.13.17); sau đó đã nhận thêm kết quả Colab CPU từ `colab_stage1.zip`. Part 3–4 hiện dùng YOLO26m + YOLOE-26s của Colab; [hồ sơ nguồn](submission/qc/colab_stage1/manifest.json). Trọng số và thư mục `work/` được loại khỏi Git. Xem [cấu hình và lệnh kiểm tra](SETUP_MAC_M1_8GB.md).

Kiểm tra gold và batch đã xuất:

```bash
cd /Users/chuoi/tool/K5-L23-DAY08-2A202603132-TranXuanBac-AIPrelabel
source .venv/bin/activate
python scripts/validate_labels.py submission/labels/gold_manual.json --expect gold
python scripts/validate_labels.py submission/labels/batch_reviewed.json --expect batch
```
