# Part 4 — bộ nhãn đầu vào để review

- Học viên: Trần Xuân Bắc, `2A202603132`.
- Nguồn: `colab_stage1.zip`; log và checksum ở `../qc/colab_stage1/`.
- YOLO26m + YOLOE-26s, chạy trên Colab bằng CPU theo nhật ký.
- Gộp: ưu tiên YOLOE; `three_wheeler=0.15`, các lớp khác `0.3`, IoU `0.6`.
- `inject_traps.py --student 2A202603132`, seed mặc định 0: đã cài đủ 12 bẫy.
- `pre_traps.coco.json`: 28 ảnh batch + gold, dùng khi đo sau review.
- `pre_traps_import.coco.json`: 24 ảnh batch / 532 box, đã nạp bằng COCO 1.0 vào task `batch-review-colab`.
- Job: http://localhost:8080/tasks/23/jobs/23. Ảnh đầu `img_003.jpg` có 26 box lúc nhập.
- Hồ sơ nhập và đối chiếu tọa độ/nhãn: `../../cvat/colab_review.json`.

Chưa có lượt review cuối hoặc thời gian batch. Người học cần bấm giờ, duyệt từng ảnh theo `docs/REVIEW_CHECKLIST.md`, lưu và export thành `submission/labels/batch_reviewed.json`.

Giữ nguyên các file đầu vào. Không mở `traps_key.json` đến khi review và export xong.
