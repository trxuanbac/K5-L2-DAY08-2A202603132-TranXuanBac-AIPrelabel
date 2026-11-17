# Mask SAM cho ba vật

Hiện đã có **3/3 ảnh mask cho ba vật**: một ảnh dùng SAM 2.1 base trên Colab và hai ảnh bổ sung dùng SAM 2.1 tiny chạy local CPU. Cấu hình, diện tích do model trả và checksum tại `completion_manifest.json`.

| Vật | Model/nguồn | Click | Quan sát |
|---|---|---|---|
| Tuk-tuk img_013 | `sam2.1_b.pt` theo ô lệnh Colab | 2 dương + 1 âm | Còn dính người lái/người áo sọc và một phần xe máy bên phải. |
| Tuk-tuk img_004 | `sam2.1_t.pt`, local CPU | 2 dương + 1 âm | Tạo mask 94.656 px, 1 polygon; người áo xanh ở click âm nằm ngoài vùng tô. Còn cần kiểm biên kính và đồ trong xe. |
| Xe máy chở hàng img_009 | `sam2.1_t.pt`, local CPU | 2 dương + 1 âm | Tạo mask 20.739 px, 1 polygon; loại vùng chuối ở click âm, nhưng còn thiếu tay lái/giỏ gắn xe. |

Thời gian toàn lệnh của hai lượt local lần lượt 5,776 và 2,997 giây, gồm khởi động Python/nạp model; không ghi các số này thành `sec_per_img` inference. Không có mask ground truth để chấm IoU; ảnh overlay dùng để quan sát lỗi theo yêu cầu Part 5.

## ZIP Colab ban đầu

Đã kiểm tra `colab_outputs.zip` tải về ngày 2026-11-17: ZIP không lỗi, có **1/3 ảnh mask** dự kiến. Chỉ đưa ảnh mask vào `submission/masks/`; kết quả model và nhãn máy còn lại trong ZIP được giữ riêng ở `work/colab-outputs-20261117/`, không ghi đè nhãn đã sửa hoặc bản ứng viên 490 annotation.

| File | Tình trạng |
|---|---|
| `submission/masks/tuktuk_img013.jpg` | Có, ảnh JPEG 1024 × 682, xem checksum trong `import_manifest.json`. |
| `submission/masks/tuktuk_img004.jpg` | Không có trong ZIP; sau đó đã tạo bằng SAM tiny local CPU. |
| `submission/masks/motorbike_img009.jpg` | Không có trong ZIP; sau đó đã tạo bằng SAM tiny local CPU. |

## Quan sát ảnh 013

Ô lệnh đã hướng dẫn dùng `sam2.1_b.pt`, hai click dương `(400,480)`, `(600,110)` và một click âm `(720,300)`. Ảnh nhận về thể hiện đúng ba vị trí này.

Vùng tô phủ phần lớn mui, thân và bánh xe tuk-tuk. Tuy nhiên còn tô lên một phần người lái áo xanh, người mặc áo sọc ở phía sau và một phần xe máy bên phải. Click âm hiện tại chưa loại hết các vùng này; đây là quan sát trên ảnh overlay, không phải phép chấm IoU mask.

Script click không ghi nhật ký riêng vào `work/runs.csv`, nên không có thời gian chạy hoặc thiết bị được xác nhận cho lượt click này. Không dùng thời gian của lượt tour box → mask để thay thế.

## Đối chiếu trước khi nộp

Đã có đủ ba vật và ba ảnh kết quả. Các ảnh cho thấy rõ giới hạn khi người lẫn trong xe hoặc hàng rời che xe. Những nhận xét này dựa trên overlay, chưa có mask ground truth để chấm độc lập.
