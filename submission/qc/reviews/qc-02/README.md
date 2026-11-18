# Sửa và tái kiểm QC — lượt 2

Sau khi chốt ba ca calibration, bộ nhãn được sửa tiếp để xử lý **8 lỗi đã xác nhận** trong job 23. Bản xuất hiện tại có **24 ảnh/492 annotation**, lưu tại [corrected.coco.json](corrected.coco.json).

## Thay đổi

- img_003: mở box xe ba bánh để bao đủ mui; đổi hai xe nền từ three_wheeler sang truck; xóa box three_wheeler sai/trùng trên vùng xe hai bánh; thêm xe đạp bị thiếu.
- img_006: thêm người quay lưng áo họa tiết cạnh bàn. **Giữ nguyên box trẻ áo xanh #69** vì nhận xét ban đầu về box đó đã được đính chính.
- img_031: chỉnh box xe đạp để tính phần giỏ/khung gắn xe bên trái theo CAL-02.
- img_035: thêm xe máy màu sáng ở xa bên phải.

Tổng: 4 cập nhật box/nhãn, 1 xóa, 3 thêm. **485 annotation khác giữ nguyên**, được đối chiếu sau ghi API. Xem [change_log.json](change_log.json), [summary.json](summary.json). `qc_fixed.json` hiện gồm 12 ảnh/297 annotation, ghép với phần còn lại thành bản ứng viên 492 annotation, taxonomy v1.1.

## Tái kiểm

Giữ cùng 5 ảnh seed 42 như lượt đầu: img_003, img_006, img_014, img_031, img_035. Sau sửa có 100 đối tượng trong mẫu. Đã xem lại các ảnh có nhãn sau sửa và giữ nguyên img_014 không có lỗi rõ ở lượt trước.

- Không ghi nhận lỗi rõ mới trong lượt tái kiểm: **0/100 đối tượng, 0/5 ảnh**.
- Tái kiểm **cùng reviewer/cùng ảnh sau khi đã biết lỗi**; chưa có QC độc lập hoặc mẫu mới. Thông tin lượt kiểm nằm trong phiếu và nhật ký QC.
- Cận trên Wilson 95% với 0 ảnh lỗi/5 ảnh vẫn là **43%**; không chứng minh toàn lô đạt ngưỡng 2%.
- [Phiếu hiện tại](qc_review.csv), [báo cáo script](qc_report_auto.md), [nguồn kiểm](qc_review_provenance.json).

## Kết quả sau review lại — 2026-11-18

Script `review_stats.py` được chạy lại trên `submission/release/final_det.coco.json`: **12/12 bẫy = 100%**, mỗi loại loose, missing, wrong_class và extra đều 3/3. Xem [số đo hiện tại](review_stats_after_rework.md).

Script QC đã được bổ sung tham số chọn vòng review và chạy bằng:

```bash
python scripts/qc_report.py --guideline-gap 0 --review-stats submission/qc/reviews/qc-02/review_stats_after_rework.json
```

Kết quả hiện tại gợi ý **Release theo mẫu QC sau sửa**, dựa trên 12/12 bẫy và 0/5 ảnh lỗi. Quyết định Rework trước đó dùng số đo lượt đầu 6/12; giữ [báo cáo trước cập nhật](qc_report_before_round_update.md) để đối chiếu. Lượt đầu và bản export 500 annotation vẫn được giữ nguyên ở `../batch-01/`.

Kết quả sau review lại thuộc vòng sửa đã biết bẫy và mẫu QC cùng ảnh. Thời gian của vòng sửa bổ sung chưa có trong `time_log.csv`; quyết định hiện tại không chứng minh toàn lô dưới 2% lỗi.

Đã xác nhận chốt bản nộp ngày 2026-11-18 theo kết quả QC hỗ trợ hiện có. Hồ sơ xác nhận được lưu tại [qc_review_provenance.json](qc_review_provenance.json), đồng bộ với bản ở thư mục QC cấp trên. Reviewer, phiếu kiểm và số đo giữ nguyên; không ghi nhận thêm một lượt QC độc lập.
