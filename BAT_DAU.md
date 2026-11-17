# Day 08 — trạng thái của Trần Xuân Bắc

Ngày 2026-11-17: đã có **443 annotation cho 28 ảnh** và đã nhập vào CVAT. Bộ nhãn đang ở trạng thái nháp, chưa qua QC cuối.

## 1. Mở nhãn trong CVAT

| Bộ ảnh | File COCO | Số ảnh | Annotation | Job |
|---|---|---:|---:|---|
| Gold draft | [gold_draft.json](submission/labels/gold_draft.json) | 4 | 58 | [Mở job 21](http://localhost:8080/tasks/21/jobs/21) |
| Batch draft | [batch_draft.json](submission/labels/batch_draft.json) | 24 | 385 | [Mở job 22](http://localhost:8080/tasks/22/jobs/22) |

Project: [day08-2A202603132](http://localhost:8080/projects/3). Task 21 hiện tên `gold-draft`; task 22 tên `batch-review`. Mỗi task có một job. Đã đọc lại dữ liệu sau khi nhập để kiểm tra lớp, tọa độ, frame và thuộc tính khớp file COCO: [kết quả nhập nhãn](cvat/annotation_drafts.json).

## 2. Phần đã thực hiện

- Chạy detector trên 36 ảnh để có dữ liệu nhãn cho các tập; chạy thêm một lượt pilot ở ngưỡng 0.25. Nhật ký thực tế ở `work/runs.csv` trên máy này.
- Gộp kết quả cho 4 ảnh gold và 24 ảnh batch ở ngưỡng khởi đầu 0.25; chưa xem đây là ngưỡng được calibration bằng gold độc lập.
- Xem các ảnh tổng quan, sửa một số lỗi nhầm lớp, box trùng và đối tượng không thuộc taxonomy; bổ sung một số người/xe bị sót.
- Bỏ box đối tượng thấp hơn 20 px. Giữ `can_review` ở các ca chưa chắc quy tắc.
- Kiểm tra hai file bằng `validate_labels.py`, đủ 4/24 ảnh và không có lỗi cấu trúc. Việc này chưa xác nhận mọi box đều đúng hoặc đã tìm hết vật.
- Nhập nhãn vào CVAT và đối chiếu dữ liệu đọc lại: 58 + 385 = 443 annotation.

Ảnh overlay dùng để kiểm tra nằm trong `work/gold-refined-viz/` và `work/batch-refined-viz/` trên máy này.

## 3. Việc tiếp theo

1. Review từng ảnh trong CVAT: tìm vật sót, bỏ box thừa, sửa lớp và ôm sát phần nhìn thấy. Lưu sau mỗi ảnh.
2. Ghi thời gian review thực tế; ghi các ca chưa chắc quy tắc để calibration.
3. Hoàn thành các phần còn lại của lab theo [GUIDE.md](GUIDE.md): tour model, SAM, ngưỡng, bẫy, calibration và QC. Chưa có kết quả đo bẫy hoặc quyết định chất lượng.
4. Các file hiện có tên `*_draft.json`; chưa thay bằng các file cuối `gold_manual.json` hoặc `batch_reviewed.json`. Báo cáo và kết quả tóm tắt còn các mục chưa hoàn thành.
5. Khi hoàn tất bài, chạy `validate_labels.py --all` và `check_submission.py` trước khi nộp.

## 4. Môi trường và repo

Repo public: https://github.com/trxuanbac/K5-L23-DAY08-2A202603132-TranXuanBac-AIPrelabel. Nhánh `main`, `origin` trỏ repo này; `upstream` là repo đề.

Máy macOS arm64, RAM 8 GB, Python 3.13.17, CVAT Docker 2.82.1. Đã chuẩn bị bộ model nhỏ để chạy tuần tự bằng CPU. Môi trường model ở `work/model-env`, môi trường kiểm nhãn/QC nhẹ ở `.venv`. Trọng số và thư mục `work/` được loại khỏi Git.

Kiểm tra hai file nháp:

```bash
cd /Users/chuoi/tool/K5-L23-DAY08-2A202603132-TranXuanBac-AIPrelabel
source .venv/bin/activate
python scripts/validate_labels.py submission/labels/gold_draft.json --expect gold
python scripts/validate_labels.py submission/labels/batch_draft.json --expect batch
```
