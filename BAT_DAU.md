# Day 08 — trạng thái của Trần Xuân Bắc

Ngày 2026-11-17: đã xuất `gold_manual.json` cho **4 ảnh / 76 annotation** từ job 21 sau review. Thời gian học viên báo là **25 phút / 4 ảnh = 6,25 phút/ảnh**. Batch còn file nháp local, chưa xuất kết quả review cuối.

## 1. Mở nhãn trong CVAT

| Bộ ảnh | File COCO | Số ảnh | Annotation | Job |
|---|---|---:|---:|---|
| Gold đã xuất | [gold_manual.json](submission/labels/gold_manual.json) | 4 | 76 | [Mở job 21](http://localhost:8080/tasks/21/jobs/21) |
| Batch draft | [batch_draft.json](submission/labels/batch_draft.json) | 24 | 385 | [Mở job 22](http://localhost:8080/tasks/22/jobs/22) |

Project: [day08-2A202603132](http://localhost:8080/projects/3). Task 21 hiện tên `gold-draft`; task 22 tên `batch-review`. Mỗi task có một job. Lần nhập nháp ban đầu được lưu tại [kết quả nhập nhãn](cvat/annotation_drafts.json). Bản gold hiện tại: [hồ sơ review và export](submission/qc/reviews/gold-01/README.md).

## 2. Phần đã thực hiện

- Chạy detector trên 36 ảnh để có dữ liệu nhãn cho các tập; chạy thêm một lượt pilot ở ngưỡng 0.25. Nhật ký thực tế ở `work/runs.csv` trên máy này.
- Gộp kết quả cho 4 ảnh gold và 24 ảnh batch ở ngưỡng khởi đầu 0.25; chưa xem đây là ngưỡng được calibration bằng gold độc lập.
- Xem các ảnh tổng quan, sửa một số lỗi nhầm lớp, box trùng và đối tượng không thuộc taxonomy; bổ sung một số người/xe bị sót.
- Bỏ box đối tượng thấp hơn 20 px. Giữ `can_review` ở các ca chưa chắc quy tắc.
- Kiểm tra hai file bằng `validate_labels.py`, đủ 4/24 ảnh và không có lỗi cấu trúc. Việc này chưa xác nhận mọi box đều đúng hoặc đã tìm hết vật.
- Lần nhập nháp ban đầu: 58 + 385 = 443 annotation. Sau lượt học viên chỉnh sửa, job 21 có 83 annotation; review bỏ 7 box dưới 20 px và xuất bản 76 annotation. Đã kiểm tra file khớp với CVAT; validator không còn lỗi hoặc cảnh báo kích thước.
- Đã ghi 25 phút do học viên cung cấp vào `submission/time_log.csv`. Bản nháp gốc và bản 83 annotation trước review được giữ để đối chiếu.

Ảnh overlay dùng để kiểm tra nằm trong `work/gold-refined-viz/` và `work/batch-refined-viz/` trên máy này.

## 3. Việc tiếp theo

1. Tiếp tục các phần còn lại theo [GUIDE.md](GUIDE.md). Với batch, review từng ảnh trong CVAT: tìm vật sót, bỏ box thừa, sửa lớp và ôm sát phần nhìn thấy. Lưu sau mỗi ảnh.
2. Ghi thời gian review thực tế; ghi các ca chưa chắc quy tắc để calibration.
3. Hoàn thành các phần còn lại của lab theo [GUIDE.md](GUIDE.md): tour model, SAM, ngưỡng, bẫy, calibration và QC. Chưa có kết quả đo bẫy hoặc quyết định chất lượng.
4. Đã có `gold_manual.json`; chưa có `batch_reviewed.json`. Gold đã có bản nháp trước lượt chỉnh sửa, nên cần giữ giới hạn này khi diễn giải số đo. Báo cáo và kết quả tóm tắt còn các mục chưa hoàn thành.
5. Khi hoàn tất bài, chạy `validate_labels.py --all` và `check_submission.py` trước khi nộp.

## 4. Môi trường và repo

Repo public: https://github.com/trxuanbac/K5-L23-DAY08-2A202603132-TranXuanBac-AIPrelabel. Nhánh `main`, `origin` trỏ repo này; `upstream` là repo đề.

Máy Apple M1 arm64, RAM 8 GB, macOS 26.3, CVAT Docker 2.82.1. Đã đối chiếu hướng dẫn Mac 8 GB: model trên Colab, `.venv` Python 3.12.16 dùng thư viện nhẹ và chạy kiểm tra đạt. Bộ model local nhỏ và môi trường Python 3.13.17 ở `work/model-env` vẫn có sẵn làm dự phòng, đã chạy thử bằng CPU. Trọng số và thư mục `work/` được loại khỏi Git. Xem [cấu hình và lệnh kiểm tra](SETUP_MAC_M1_8GB.md).

Kiểm tra gold đã xuất và batch nháp:

```bash
cd /Users/chuoi/tool/K5-L23-DAY08-2A202603132-TranXuanBac-AIPrelabel
source .venv/bin/activate
python scripts/validate_labels.py submission/labels/gold_manual.json --expect gold
python scripts/validate_labels.py submission/labels/batch_draft.json --expect batch
```
