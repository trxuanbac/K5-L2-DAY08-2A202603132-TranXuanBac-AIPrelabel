# Thông tin học viên

- Họ và tên: Trần Xuân Bắc
- MSHV: 2A202603132
- Lớp: L2
- Tài khoản GitHub: trxuanbac
- Repo bài nộp (URL): https://github.com/trxuanbac/K5-L2-DAY08-2A202603132-TranXuanBac-AIPrelabel (public; đã xuất lượt review batch đầu, chưa chốt bài).
- Commit chốt bài (hash): Chưa chốt nộp; đã xuất gold 4 ảnh/76 annotation, batch đầu 24 ảnh/500 annotation và bản sau sửa QC 24 ảnh/492 annotation. Đủ ba mask SAM; học viên đã xác nhận ba ca calibration v1.1. Báo cáo kỹ thuật và kết quả QC cần học viên đọc lại trước khi chốt.
- Máy: macOS 26.3, Apple M1 arm64, RAM 8 GB. `.venv` dùng Python 3.12.16 và thư viện nhẹ cho chế độ Colab; `work/model-env` dùng Python 3.13.17, đã kiểm tra model local bằng CPU. Đã nhận kết quả Colab stage1; nhật ký ghi `cpu`. GPU T4 Colab chưa được xác nhận.
- CVAT (Docker): 2.82.1, bản local đang có tại http://localhost:8080 (đề minh họa bản 2.81.0).

## Kết quả tóm tắt (điền cuối bài; số lấy từ `submission/qc/*`, kèm mẫu số)

- Máy: accepted 467/520 = 89,8%; edited 10/520 = 1,9%; deleted 43/520 = 8,3%; added 12/489 = 2,5%. Script loại đối tượng quanh bẫy khỏi các mẫu số này; file batch thực tế có 500 annotation.
- So với gold: precision của **máy** 47/72 = 65,3%; recall 47/75 = 62,7%. Gold có nhãn nháp trước lượt học viên chỉnh sửa; ngưỡng cũng được chọn trên cùng 4 ảnh này.
- Bắt bẫy lượt review đầu: 6/12 = 50%; ngưỡng trong taxonomy là 80%.
- Bản sửa bổ sung: script đối chiếu 12/12 bẫy sau khi đã biết kết quả; không thay kết quả review đầu. Bản sau sửa bẫy có 490 annotation; sau sửa tiếp 8 lỗi QC có 492 annotation. Không còn cảnh báo box cao dưới 20 px.
- Thời gian: gán tay/chỉnh sửa gold 25 phút/4 ảnh = 6,25 phút/ảnh; review batch 30 phút/24 ảnh = 1,25 phút/ảnh. Cả hai thời gian do học viên cung cấp.
- QC hỗ trợ trước sửa: 8/98 = 8,2% lỗi, 4/5 ảnh có lỗi; đã đính chính một nhận xét nhầm trong số sơ bộ 9 lỗi. Sau sửa, tái kiểm cùng 5 ảnh/100 đối tượng: chưa ghi nhận lỗi rõ mới (0/100, 0/5). Cùng reviewer và cùng ảnh nên không xem là QC độc lập. Cận trên Wilson 95% của tỉ lệ ảnh lỗi sau sửa vẫn là 43%.
- **Gợi ý của script: Rework** — lượt review đầu bắt 6/12 bẫy (50%), dưới 80%; không thay bằng kết quả sau biết đáp án. Học viên chưa xác nhận quyết định chốt nộp cuối cùng.
