# Thông tin cá nhân

- Họ và tên: Trần Xuân Bắc
- MSHV: 2A202603132
- Lớp: L2
- Tài khoản GitHub: trxuanbac
- Repo bài nộp (URL): https://github.com/trxuanbac/K5-L2-DAY08-2A202603132-TranXuanBac-AIPrelabel (public; chốt trạng thái Rework).
- Commit chốt bài (hash): [2c0630d99ed0c89b76f1e34ae9eff245f8532963](https://github.com/trxuanbac/K5-L2-DAY08-2A202603132-TranXuanBac-AIPrelabel/commit/2c0630d99ed0c89b76f1e34ae9eff245f8532963). Commit tiếp theo chỉ cập nhật thông tin commit này.
- Trạng thái bản nộp: **Rework**. Gold 4 ảnh/76 annotation; batch sau sửa QC 24 ảnh/492 annotation; đủ ba mask SAM và ba ca calibration v1.1.
- Máy: macOS 26.3, Apple M1 arm64, RAM 8 GB. `.venv` dùng Python 3.12.16 và thư viện nhẹ cho chế độ Colab; `work/model-env` dùng Python 3.13.17, đã kiểm tra model local bằng CPU. Đã nhận kết quả Colab stage1; nhật ký ghi `cpu`. GPU T4 Colab chưa được xác nhận.
- CVAT (Docker): 2.82.1, bản local đang có tại http://localhost:8080 (đề minh họa bản 2.81.0).

## Kết quả tóm tắt (điền cuối bài; số lấy từ `submission/qc/*`, kèm mẫu số)

- Máy: accepted 467/520 = 89,8%; edited 10/520 = 1,9%; deleted 43/520 = 8,3%; added 12/489 = 2,5%. Script loại đối tượng quanh bẫy khỏi các mẫu số này; file batch thực tế có 500 annotation.
- So với gold: precision của **máy** 47/72 = 65,3%; recall 47/75 = 62,7%. Gold đã có nhãn nháp trước lượt chỉnh sửa; ngưỡng cũng được chọn trên cùng 4 ảnh này.
- Bắt bẫy lượt review đầu: 6/12 = 50%; ngưỡng trong taxonomy là 80%.
- Bản sửa bổ sung: script đối chiếu 12/12 bẫy sau khi đã biết kết quả; không thay kết quả review đầu. Bản sau sửa bẫy có 490 annotation; sau sửa tiếp 8 lỗi QC có 492 annotation. Không còn cảnh báo box cao dưới 20 px.
- Thời gian: chỉnh sửa 4 ảnh gold trong 25 phút, trung bình 6,25 phút/ảnh; review 24 ảnh batch trong 30 phút, trung bình 1,25 phút/ảnh.
- QC trước sửa: 8/98 = 8,2% lỗi, 4/5 ảnh có lỗi; đã đính chính một nhận xét nhầm trong số sơ bộ 9 lỗi. Sau sửa, tái kiểm cùng 5 ảnh/100 đối tượng: chưa ghi nhận lỗi rõ mới (0/100, 0/5). Cùng reviewer và cùng ảnh nên không xem là QC độc lập. Cận trên Wilson 95% của tỉ lệ ảnh lỗi sau sửa vẫn là 43%.
- **Quyết định: Rework** — lượt review đầu bắt 6/12 bẫy (50%), dưới 80%. Kết quả sau sửa được giữ riêng, không thay số đo ban đầu. Tái kiểm cùng mẫu ảnh chưa chứng minh chất lượng toàn lô.
