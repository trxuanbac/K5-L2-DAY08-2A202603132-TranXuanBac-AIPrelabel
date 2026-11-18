# Kết quả chạy model bằng CPU trên Colab

Nhận ngày 2026-11-17 từ `colab_stage1.zip`; kiểm tra ZIP không lỗi và xác minh checksum trong `manifest.json`. `runs.csv` được sao nguyên từ ZIP; các run ID ở đây thuộc phiên Colab, độc lập với ID của tour local trong `submission/model_log.csv`.

Đã có đủ bốn lượt tour Part 2 trên Colab CPU:

| Run gốc | Model | Số ảnh | Conf | Box | Mask | Giây/ảnh |
|---|---|---:|---:|---:|---:|---:|
| r01 | YOLO26m | 8 pilot | 0.25 | 215 | 0 | 2.29 |
| r02 | YOLO26m | 8 pilot | 0.5 | 139 | 0 | 1.63 |
| r03 | YOLOE small | 8 pilot | 0.25 | 8 | 0 | 0.84 |
| r04 | YOLO26m + SAM 2.1 base | 2 | 0.3 | 16 | 16 | 13.1 |

Ảnh tour và `run.json` được đối chiếu từ `colab_outputs.zip`; năm ảnh overlay được bổ sung nguyên bản vào `tour/`. Xem [manifest](tour_manifest.json), [quan sát và so sánh](../model_tour/README.md). `model_log.csv` ghi các lượt này dưới ID `colab-r01` đến `colab-r04`.

Hai lượt nguồn dùng cho Part 3–4:

- `r05`: YOLO26m, toàn bộ 36 ảnh, conf 0.05, 1.669 box, 1,62 giây/ảnh.
- `r06`: YOLOE-26s, toàn bộ 36 ảnh, conf 0.05, 125 box, 0,83 giây/ảnh.
- Cả sáu lượt trong nhật ký đều ghi `device=cpu`.
- Đã quét bằng `gold_manual.json`: 4 ảnh, 76 annotation, gồm 1 ignore region.
- Ngưỡng script đề xuất: `three_wheeler=0.15`; các lớp khác dùng mặc định 0.3.
- `threshold_sweep.csv/.md/.png` được tạo bởi script; bản dùng hiện tại ở thư mục QC cấp trên có cùng nội dung.
- Quét nano local trước đây được giữ ở `../model_tour/local_threshold_sweep.*`.

Gold đã có nhãn nháp trước lượt chỉnh sửa; chọn và chấm ngưỡng trên cùng gold nên số đo có giới hạn. Kết quả review batch và QC cuối nằm tại [qc-02](../reviews/qc-02/README.md).
