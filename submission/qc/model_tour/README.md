# Part 2 — kết quả chạy local bằng CPU

Đã có đủ bốn lượt tour cho YOLO26, YOLOE và SAM. Mac M1, RAM 8 GB; môi trường `work/model-env`, Python 3.13.17. Colab báo phần phụ trợ không có sẵn nên dùng kết quả local, không ghi các lượt này là chạy trên GPU Colab.

| Run | Model | Tập ảnh | Ngưỡng | Box | Mask | Giây/ảnh |
|---|---|---|---:|---:|---:|---:|
| r02 | YOLO26 nano | pilot, 8 ảnh | 0.25 | 148 | 0 | 0.22 |
| r04 | YOLO26 nano | pilot, 8 ảnh | 0.5 | 81 | 0 | 0.24 |
| r05 | YOLOE small | pilot, 8 ảnh | 0.25 | 8 | 0 | 0.34 |
| r06 | YOLO26 nano → SAM 2.1 tiny | img_004, img_013 | 0.3 | 8 | 8 | 2.98 |

Số liệu sao từ các lần chạy thực tế; thời gian không gồm thời gian nạp model. [Manifest lần chạy](runs.json) · [model_log.csv](../../model_log.csv).

## Ảnh so sánh

- [YOLO26, conf 0.25, img_002](yolo26_conf025_img002.jpg): tuk-tuk xanh bị gọi `truck`, điểm 0.3712.
- [YOLO26, conf 0.5, img_002](yolo26_conf050_img002.jpg): box `truck` đó biến mất; chưa có box `three_wheeler` thay thế.
- [YOLOE, img_002](yoloe_img002.jpg): có `three_wheeler` trên tuk-tuk xanh, điểm 0.9265; xe bán tải trắng bên phải cũng bị gán `three_wheeler` khoảng 0.37.
- [SAM, img_004](sam_img004.jpg): có 3 mask `person`; không có box xe được đưa sang SAM với cấu hình này, nên chưa có mask tuk-tuk.
- [SAM, img_013](sam_img013.jpg): 4 mask người và 1 mask xe phía sau; không tự sinh mask cho tuk-tuk lớn khi detector không cung cấp box của nó.

Đây là các quan sát trên ảnh kết quả, chưa thay thế review toàn bộ batch hoặc quyết định QC cuối.

## Dữ liệu cho Part 3

Hai lượt nguồn ngưỡng thấp đã có trên máy:

- `r01`: YOLO26 nano, toàn bộ 36 ảnh, conf 0.05, 1.525 box.
- `r03`: YOLOE small cho `three_wheeler`, toàn bộ 36 ảnh, conf 0.05, 125 box.

Tệp nguồn ở `work/prelabel/y26_all/pre.coco.json` và `work/prelabel/yoloe_all/pre.coco.json`. Đã chạy `threshold_sweep.py` với `submission/labels/gold_manual.json`; xem [kết quả quét](../threshold_sweep.md). Gold đã có nhãn nháp trước lượt học viên chỉnh sửa, cần giữ giới hạn đó khi đọc số đo.
