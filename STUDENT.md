# Thông tin học viên

- Họ và tên: Trần Xuân Bắc
- MSHV: 2A202603132
- Lớp: L2
- Tài khoản GitHub: trxuanbac
- Repo bài nộp (URL): https://github.com/trxuanbac/K5-L2-DAY08-2A202603132-TranXuanBac-AIPrelabel (public; đã xuất lượt review batch đầu, chưa chốt bài).
- Commit chốt bài (hash): Chưa chốt; đã xuất gold 4 ảnh/76 annotation và batch 24 ảnh/500 annotation; còn kiểm tra lại lỗi, mask SAM, calibration và QC.
- Máy: macOS 26.3, Apple M1 arm64, RAM 8 GB. `.venv` dùng Python 3.12.16 và thư viện nhẹ cho chế độ Colab; `work/model-env` dùng Python 3.13.17, đã kiểm tra model local bằng CPU. Đã nhận kết quả Colab stage1; nhật ký ghi `cpu`. GPU T4 Colab chưa được xác nhận.
- CVAT (Docker): 2.82.1, bản local đang có tại http://localhost:8080 (đề minh họa bản 2.81.0).

## Kết quả tóm tắt (điền cuối bài; số lấy từ `submission/qc/*`, kèm mẫu số)

- Máy: accepted 467/520 = 89,8%; edited 10/520 = 1,9%; deleted 43/520 = 8,3%; added 12/489 = 2,5%. Script loại đối tượng quanh bẫy khỏi các mẫu số này; file batch thực tế có 500 annotation.
- So với gold: precision của **máy** 47/72 = 65,3%; recall 47/75 = 62,7%. Gold có nhãn nháp trước lượt học viên chỉnh sửa; ngưỡng cũng được chọn trên cùng 4 ảnh này.
- Bắt bẫy lượt review đầu: 6/12 = 50%; ngưỡng trong taxonomy là 80%.
- Thời gian: gán tay/chỉnh sửa gold 25 phút/4 ảnh = 6,25 phút/ảnh; review batch 30 phút/24 ảnh = 1,25 phút/ảnh. Cả hai thời gian do học viên cung cấp.
- Lỗi QC: <<...% theo ảnh (.../...)>>, <<...% theo đối tượng (.../...)>>
- **Quyết định:** <<Release / Hold / Rework>> — lý do một dòng: <<...>>
