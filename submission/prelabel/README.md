# Part 4 — bộ nhãn đầu vào để review

- Bài làm: Trần Xuân Bắc, `2A202603132`.
- Nguồn: `colab_stage1.zip`; log và checksum ở `../qc/colab_stage1/`.
- YOLO26m + YOLOE-26s, chạy trên Colab bằng CPU theo nhật ký.
- Gộp: ưu tiên YOLOE; `three_wheeler=0.15`, các lớp khác `0.3`, IoU `0.6`.
- `inject_traps.py --student 2A202603132`, seed mặc định 0: đã cài đủ 12 bẫy.
- `pre_traps.coco.json`: 28 ảnh batch + gold, dùng khi đo sau review.
- `pre_traps_import.coco.json`: 24 ảnh batch / 532 box, đã nạp bằng COCO 1.0 vào task `batch-review-colab`.
- Job: http://localhost:8080/tasks/23/jobs/23. Ảnh đầu `img_003.jpg` có 26 box lúc nhập.
- Hồ sơ nhập và đối chiếu tọa độ/nhãn: `../../cvat/colab_review.json`.

Đã xuất lượt review đầu thành `submission/labels/batch_reviewed.json`: 24 ảnh/500 annotation. Lượt review đầu hoàn thành trong 30 phút. Số đo được tạo sau export: bắt 6/12 bẫy; xem `submission/qc/reviews/batch-01/README.md`. Chưa hoàn tất QC nội dung hoặc quyết định chất lượng cuối.

Đã có bản sửa bổ sung 24 ảnh/490 annotation ở `submission/qc/reviews/batch-02/`, cùng `submission/labels/qc_fixed.json` cho 10 ảnh thay đổi. Job 23 hiện dùng bản đã sửa; `batch_reviewed.json` và số đo lượt đầu giữ nguyên. Script kiểm bẫy sau sửa ghi 12/12; đây là kiểm sau khi đã biết kết quả bẫy.

Giữ nguyên các file đầu vào. `traps_key.json` đã được script đọc sau khi export lượt review đầu; file đáp án vẫn chỉ lưu local và được loại khỏi Git.
