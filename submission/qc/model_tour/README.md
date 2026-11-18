# Part 2 — tour model bằng CPU trên Colab và máy local

Đã chạy đủ bốn lượt tour trên **Google Colab bằng CPU**. Nhật ký Colab có `device=cpu` cho YOLO26m, YOLOE và SAM 2.1 base. Kết quả Colab được bổ sung vào hồ sơ ngày 2026-11-18; các lượt local trước đó được giữ để đối chiếu.

## Kết quả Colab CPU

| Run trong model_log | Model | Tập ảnh | Ngưỡng | Box | Mask | Giây/ảnh |
|---|---|---|---:|---:|---:|---:|
| colab-r01 | YOLO26 medium | pilot, 8 ảnh | 0.25 | 215 | 0 | 2.29 |
| colab-r02 | YOLO26 medium | pilot, 8 ảnh | 0.5 | 139 | 0 | 1.63 |
| colab-r03 | YOLOE small | pilot, 8 ảnh | 0.25 | 8 | 0 | 0.84 |
| colab-r04 | YOLO26 medium → SAM 2.1 base | img_004, img_013 | 0.3 | 16 | 16 | 13.1 |

Nhật ký gốc: [runs.csv](../colab_stage1/runs.csv). Thông số, checksum và ảnh lấy nguyên từ ZIP: [tour_manifest.json](../colab_stage1/tour_manifest.json). ID thêm tiền tố `colab-` trong `model_log.csv` để phân biệt với run local.

- [YOLO26m conf 0.25, img_002](../colab_stage1/tour/yolo26_conf025_img002.jpg): nhận diện người, xe máy và xe bán tải; chưa có box xe cho tuk-tuk xanh ở giữa.
- [YOLO26m conf 0.5, img_002](../colab_stage1/tour/yolo26_conf050_img002.jpg): mất thêm một số người điểm thấp; tuk-tuk vẫn bị sót. Trên 8 ảnh, số box giảm từ 215 xuống 139.
- [YOLOE, img_002](../colab_stage1/tour/yoloe_img002.jpg): tìm tuk-tuk đúng lớp `three_wheeler` với conf 0.9265; xe bán tải trắng bị gán nhầm cùng lớp với conf 0.3658.
- [SAM base, img_004](../colab_stage1/tour/sam_img004.jpg): có mask xe từ các box detector mang nhãn `car`.
- [SAM base, img_013](../colab_stage1/tour/sam_img013.jpg): mask tuk-tuk còn gồm người lái và thiếu phần xe bên trái; SAM không sửa nhãn `car` do detector đưa vào.

## Kết quả local CPU trước đó

Mac M1, RAM 8 GB; môi trường `work/model-env`, Python 3.13.17. Các lượt này được chạy khi Colab chưa kết nối được và được lưu riêng với model/cỡ khác các lượt Colab.

| Run | Model | Tập ảnh | Ngưỡng | Box | Mask | Giây/ảnh |
|---|---|---|---:|---:|---:|---:|
| r02 | YOLO26 nano | pilot, 8 ảnh | 0.25 | 148 | 0 | 0.22 |
| r04 | YOLO26 nano | pilot, 8 ảnh | 0.5 | 81 | 0 | 0.24 |
| r05 | YOLOE small | pilot, 8 ảnh | 0.25 | 8 | 0 | 0.34 |
| r06 | YOLO26 nano → SAM 2.1 tiny | img_004, img_013 | 0.3 | 8 | 8 | 2.98 |

Số liệu sao từ các lần chạy thực tế; thời gian không gồm thời gian nạp model. [Manifest lần chạy](runs.json) · [model_log.csv](../../model_log.csv).

## Ảnh so sánh local

- [YOLO26, conf 0.25, img_002](yolo26_conf025_img002.jpg): tuk-tuk xanh bị gọi `truck`, điểm 0.3712.
- [YOLO26, conf 0.5, img_002](yolo26_conf050_img002.jpg): box `truck` đó biến mất; chưa có box `three_wheeler` thay thế.
- [YOLOE, img_002](yoloe_img002.jpg): có `three_wheeler` trên tuk-tuk xanh, điểm 0.9265; xe bán tải trắng bên phải cũng bị gán `three_wheeler` khoảng 0.37.
- [SAM, img_004](sam_img004.jpg): có 3 mask `person`; không có box xe được đưa sang SAM với cấu hình này, nên chưa có mask tuk-tuk.
- [SAM, img_013](sam_img013.jpg): 4 mask người và 1 mask xe phía sau; không tự sinh mask cho tuk-tuk lớn khi detector không cung cấp box của nó.

Đây là các quan sát trên ảnh kết quả, chưa thay thế review toàn bộ batch hoặc quyết định QC cuối.

## Dữ liệu cho Part 3

Part 3–4 hiện dùng nguồn **Colab CPU**: YOLO26m 1.669 box và YOLOE 125 box trên 36 ảnh. Xem [hồ sơ Colab](../colab_stage1/README.md) và [kết quả quét hiện tại](../threshold_sweep.md).

Hai lượt nguồn local ngưỡng thấp trước đó được giữ để đối chiếu:

- `r01`: YOLO26 nano, toàn bộ 36 ảnh, conf 0.05, 1.525 box.
- `r03`: YOLOE small cho `three_wheeler`, toàn bộ 36 ảnh, conf 0.05, 125 box.

Tệp nguồn local ở `work/prelabel/y26_all/pre.coco.json` và `work/prelabel/yoloe_all/pre.coco.json`; [kết quả quét local](local_threshold_sweep.md) được giữ riêng. Gold đã có nhãn nháp trước lượt chỉnh sửa, cần giữ giới hạn đó khi đọc số đo.
