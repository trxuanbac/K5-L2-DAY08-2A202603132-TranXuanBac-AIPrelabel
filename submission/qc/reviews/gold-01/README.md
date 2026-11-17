# Review và export gold — job 21

Ngày 2026-11-17, tôi dành 25 phút chỉnh sửa 4 ảnh trong job 21, tương đương 6,25 phút/ảnh. Thời gian được ghi trong `submission/time_log.csv`.

## Kết quả

| Ảnh | Annotation sau review |
|---|---:|
| img_001.jpg | 23 |
| img_012.jpg | 13 |
| img_020.jpg | 12 |
| img_036.jpg | 28 |
| Tổng | 76 |

76 annotation gồm 75 đối tượng và 1 `ignore_region`. Đã xuất COCO 1.0, không kèm ảnh, vào [gold_manual.json](../../../labels/gold_manual.json).

## Chỉnh sửa khi review

Bản lưu trước review có 83 annotation, được giữ nguyên ở [before_review.coco.json](before_review.coco.json). Đã bỏ đúng 7 box dưới ngưỡng `min_box_height_px = 20`; không nới box để vượt ngưỡng và không thay đổi 76 annotation còn lại.

| Ảnh | Lớp | Số box bỏ | Chiều cao (px) |
|---|---|---:|---|
| img_001.jpg | person | 2 | 18,59; 19,83 |
| img_001.jpg | bicycle | 1 | 18,37 |
| img_036.jpg | car | 1 | 14,87 |
| img_036.jpg | motorbike | 3 | 12,26; 15,62; 12,60 |

ID và tọa độ CVAT của các box đã bỏ nằm trong [size_review.json](size_review.json).

## Kiểm tra

- Xem overlay của 4 ảnh, kiểm tra phạm vi ảnh, lớp và hình chữ nhật.
- Xác nhận nhãn không thay đổi trong lúc export; đối chiếu 76 box COCO với snapshot CVAT theo ảnh, lớp và tọa độ.
- `validate_labels.py submission/labels/gold_manual.json --expect gold`: đủ 4 ảnh, 76 annotation, không lỗi và không cảnh báo.
- `validate_labels.py --all`: đạt với các file chuẩn hiện có. Batch cuối chưa được xuất.
- Tóm tắt số lượng và checksum: [export_summary.json](export_summary.json).

Đây là kiểm tra cho bước export gold, chưa phải QC cuối của toàn bộ batch. Task đã có nhãn nháp trước khi tôi chỉnh sửa; cần giữ giới hạn đó khi sử dụng gold để đo model.
