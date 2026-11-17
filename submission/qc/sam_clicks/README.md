# Mask SAM nhận từ Colab

Đã kiểm tra `colab_outputs.zip` tải về ngày 2026-11-17: ZIP không lỗi, có **1/3 ảnh mask** dự kiến. Chỉ đưa ảnh mask vào `submission/masks/`; kết quả model và nhãn máy còn lại trong ZIP được giữ riêng ở `work/colab-outputs-20261117/`, không ghi đè nhãn đã sửa hoặc bản ứng viên 490 annotation.

| File | Tình trạng |
|---|---|
| `submission/masks/tuktuk_img013.jpg` | Có, ảnh JPEG 1024 × 682, xem checksum trong `import_manifest.json`. |
| `submission/masks/tuktuk_img004.jpg` | Chưa có trong ZIP đã nhận. |
| `submission/masks/motorbike_img009.jpg` | Chưa có trong ZIP đã nhận. |

## Quan sát ảnh 013

Ô lệnh đã hướng dẫn dùng `sam2.1_b.pt`, hai click dương `(400,480)`, `(600,110)` và một click âm `(720,300)`. Ảnh nhận về thể hiện đúng ba vị trí này.

Vùng tô phủ phần lớn mui, thân và bánh xe tuk-tuk. Tuy nhiên còn tô lên một phần người lái áo xanh, người mặc áo sọc ở phía sau và một phần xe máy bên phải. Click âm hiện tại chưa loại hết các vùng này; đây là quan sát trên ảnh overlay, không phải phép chấm IoU mask.

Script click không ghi nhật ký riêng vào `work/runs.csv`, nên không có thời gian chạy hoặc thiết bị được xác nhận cho lượt click này. Không dùng thời gian của lượt tour box → mask để thay thế.

## Việc còn lại

Chạy thêm hai lệnh click cho ảnh 004 và 009 trong Colab, kiểm tra chúng tạo ra file, rồi đóng gói thư mục `submission/masks/` để tải về. Part 5 chưa đủ ba vật để đánh dấu hoàn tất.
