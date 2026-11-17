# Lượt review batch đầu — job 23

Bản sửa bổ sung hiện có ở [batch-02](../batch-02/README.md). Số đo và nhãn trong thư mục `batch-01` giữ nguyên lượt review đầu.

Lượt review 24 ảnh kéo dài **30 phút**, trung bình **1,25 phút/ảnh**. Bản export COCO 1.0 có **500 annotation**, so với 532 box trước review. Bản export được đối chiếu với dữ liệu lưu trong CVAT tại thời điểm xuất.

- [Bản COCO lưu riêng cho lượt đầu](batch_reviewed.coco.json).
- [Hồ sơ export và checksum](export_summary.json).
- [Kết quả script đo](review_stats.md), [JSON](review_stats.json).
- [Danh sách 10 cảnh báo kích thước](size_warnings.csv).
- Job: http://localhost:8080/tasks/23/jobs/23.

## Số đo

| Trạng thái | Số | Mẫu số | Tỉ lệ |
|---|---:|---:|---:|
| accepted | 467 | 520 box máy | 89,8% |
| edited | 10 | 520 box máy | 1,9% |
| deleted | 43 | 520 box máy | 8,3% |
| added | 12 | 489 đối tượng sau duyệt | 2,5% |

Script loại vùng quanh bẫy khỏi bảng trạng thái: tổng cộng 23 đối tượng ở cả hai phía. Vì vậy mẫu số không bằng số annotation trong file COCO. Đổi lớp được script tính là deleted + added; script ghi 4 trường hợp như vậy.

Máy so với gold: precision **47/72 = 65,3%**, recall **47/75 = 62,7%**. Gold có 75 đối tượng và 1 ignore region, đã có nhãn nháp trước lượt chỉnh sửa. Ngưỡng được chọn và chấm trên cùng 4 ảnh này nên số đo chưa phải đánh giá độc lập.

## Các mục cần kiểm tra lại

Script ghi **6/12 bẫy được bắt (50%)**, ngưỡng trong taxonomy là 80%. Theo loại: loose 1/3, missing 1/3, wrong_class 2/3, extra 2/3.

| Ảnh | Loại bẫy còn lọt theo script |
|---|---|
| img_006.jpg | wrong_class — sai lớp |
| img_013.jpg | missing — thiếu vật |
| img_021.jpg | loose — box lỏng/lệch |
| img_024.jpg | loose — box lỏng/lệch |
| img_034.jpg | missing — thiếu vật |
| img_035.jpg | extra — box thừa |

`validate_labels.py --all` không báo lỗi cấu trúc, nhưng còn 10 box cao dưới 20 px trên `img_018`, `img_025`, `img_027`, `img_033`, `img_034`. Đây là cảnh báo theo guideline, chưa phải kết quả QC hình ảnh. Xem ID trong `size_warnings.csv`.

Các vòng sửa tiếp được lưu riêng để đối chiếu. Bản review đầu và kết quả 50% trong thư mục này được giữ nguyên; kết quả sau khi biết bẫy không thay thế số đo ban đầu.

## Phần còn lại

Hồ sơ này ghi lại thời điểm kết thúc lượt review đầu. Các bước bổ sung mask, calibration và sửa QC được lưu ở những vòng sau; bản cập nhật nằm tại [qc-02](../qc-02/README.md). File đáp án bẫy được script đọc sau khi xuất bản review đầu và vẫn giữ local.
