# Kết quả Colab stage1

Nhận ngày 2026-11-17 từ `colab_stage1.zip`; kiểm tra ZIP không lỗi và xác minh checksum trong `manifest.json`. `runs.csv` được sao nguyên từ ZIP; các run ID ở đây thuộc phiên Colab, độc lập với ID của tour local trong `submission/model_log.csv`.

- `r05`: YOLO26m, toàn bộ 36 ảnh, conf 0.05, 1.669 box, 1,62 giây/ảnh.
- `r06`: YOLOE-26s, toàn bộ 36 ảnh, conf 0.05, 125 box, 0,83 giây/ảnh.
- Nhật ký ghi `device=cpu`; không ghi các lượt này là GPU T4.
- Đã quét bằng `gold_manual.json`: 4 ảnh, 76 annotation, gồm 1 ignore region.
- Ngưỡng script đề xuất: `three_wheeler=0.15`; các lớp khác dùng mặc định 0.3.
- `threshold_sweep.csv/.md/.png` được tạo bởi script; bản dùng hiện tại ở thư mục QC cấp trên có cùng nội dung.
- Quét nano local trước đây được giữ ở `../model_tour/local_threshold_sweep.*`.

Gold đã có nhãn nháp trước lượt chỉnh sửa; chọn và chấm ngưỡng trên cùng gold nên số đo có giới hạn. Chưa có kết quả review batch hoặc QC cuối.
