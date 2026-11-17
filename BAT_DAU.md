# Day 08 — trạng thái của Trần Xuân Bắc

Ngày 2026-11-17: đã xuất gold **4 ảnh/76 annotation**, thời gian học viên báo **25 phút**. Đã xuất lượt review đầu của [job 23 — batch-review-colab](http://localhost:8080/tasks/23/jobs/23): **24 ảnh/500 annotation**, **30 phút = 1,25 phút/ảnh**. Số đo: bắt **6/12 bẫy (50%)**, còn 10 cảnh báo box cao dưới 20 px. Chưa có QC hoặc quyết định chất lượng cuối.

## 1. Mở nhãn trong CVAT

| Bộ ảnh | File COCO | Số ảnh | Annotation | Job |
|---|---|---:|---:|---|
| Gold đã xuất | [gold_manual.json](submission/labels/gold_manual.json) | 4 | 76 | [Mở job 21](http://localhost:8080/tasks/21/jobs/21) |
| Batch draft | [batch_draft.json](submission/labels/batch_draft.json) | 24 | 385 | [Mở job 22](http://localhost:8080/tasks/22/jobs/22) |
| Batch để review, từ Colab | [pre_traps_import.coco.json](submission/prelabel/pre_traps_import.coco.json) | 24 | 532 | [Mở job 23](http://localhost:8080/tasks/23/jobs/23) |
| Batch sau lượt review đầu | [batch_reviewed.json](submission/labels/batch_reviewed.json) | 24 | 500 | [Mở job 23](http://localhost:8080/tasks/23/jobs/23) |

Project: [day08-2A202603132](http://localhost:8080/projects/3). Task 21 hiện tên `gold-draft`; task 22 tên `batch-review`. Mỗi task có một job. Lần nhập nháp ban đầu được lưu tại [kết quả nhập nhãn](cvat/annotation_drafts.json). Bản gold hiện tại: [hồ sơ review và export](submission/qc/reviews/gold-01/README.md).

## 2. Phần đã thực hiện

- Đã lưu bốn lượt tour Part 2: YOLO26 conf 0.25 và 0.5, YOLOE, SAM 2.1 tiny. Có số đo thực tế và ảnh so sánh trong [hồ sơ tour model](submission/qc/model_tour/README.md).
- Có hai lượt nguồn trên toàn bộ 36 ảnh ở conf 0.05 cho Part 3; đã chạy quét ngưỡng bằng gold đã xuất, tạo [threshold_sweep.md](submission/qc/threshold_sweep.md), CSV và PNG.
- Gộp kết quả cho 4 ảnh gold và 24 ảnh batch ở ngưỡng khởi đầu 0.25; chưa xem đây là ngưỡng được calibration bằng gold độc lập.
- Xem các ảnh tổng quan, sửa một số lỗi nhầm lớp, box trùng và đối tượng không thuộc taxonomy; bổ sung một số người/xe bị sót.
- Bỏ box đối tượng thấp hơn 20 px. Giữ `can_review` ở các ca chưa chắc quy tắc.
- Kiểm tra hai file bằng `validate_labels.py`, đủ 4/24 ảnh và không có lỗi cấu trúc. Việc này chưa xác nhận mọi box đều đúng hoặc đã tìm hết vật.
- Lần nhập nháp ban đầu: 58 + 385 = 443 annotation. Sau lượt học viên chỉnh sửa, job 21 có 83 annotation; review bỏ 7 box dưới 20 px và xuất bản 76 annotation. Đã kiểm tra file khớp với CVAT; validator không còn lỗi hoặc cảnh báo kích thước.
- Đã ghi 25 phút do học viên cung cấp vào `submission/time_log.csv`. Bản nháp gốc và bản 83 annotation trước review được giữ để đối chiếu.
- Đã xuất lượt review batch đầu từ job 23, kiểm tra đủ 24 ảnh/500 annotation và đối chiếu với annotation hiện lưu trong CVAT. Ghi 30 phút do học viên cung cấp; [hồ sơ export và số đo](submission/qc/reviews/batch-01/README.md). Validator không có lỗi cấu trúc; còn 10 cảnh báo box nhỏ.

Ảnh overlay dùng để kiểm tra nằm trong `work/gold-refined-viz/` và `work/batch-refined-viz/` trên máy này.

## 3. Việc tiếp theo

1. Kiểm tra lại [job 23](http://localhost:8080/tasks/23/jobs/23) theo checklist: lượt đầu bắt 6/12 bẫy, dưới ngưỡng 80%. Các ảnh bẫy lọt và box nhỏ được liệt kê tại [hồ sơ lượt đầu](submission/qc/reviews/batch-01/README.md). Không nạp lại pre-label vì sẽ mất phần học viên đã sửa.
2. Nếu sửa tiếp, bấm giờ riêng và lưu thành lượt sửa bổ sung. Bản review đầu và kết quả 6/12 được giữ nguyên để đối chiếu; sửa sau khi biết kết quả không phải lượt review mù ban đầu.
3. Còn Part 5 (mask click cho 3 vật), calibration và QC. Chưa có quyết định chất lượng cuối; học viên cần tự viết kết luận và quy tắc bổ sung theo RULES.md.
4. Đã có `gold_manual.json` và `batch_reviewed.json`. Gold đã có bản nháp trước lượt chỉnh sửa, nên cần giữ giới hạn này khi diễn giải số đo. Báo cáo và kết quả tóm tắt còn các mục cần học viên phân tích.
5. Khi hoàn tất bài, chạy `validate_labels.py --all` và `check_submission.py` trước khi nộp.

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
