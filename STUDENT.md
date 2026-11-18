# Thông tin cá nhân

- Họ và tên: Trần Xuân Bắc
- MSHV: 2A202603132
- Lớp: L2
- Tài khoản GitHub: trxuanbac
- Repo bài nộp (URL): https://github.com/trxuanbac/K5-L2-DAY08-2A202603132-TranXuanBac-AIPrelabel (public; cập nhật sau review lại).
- Commit chốt bài (hash): [2c0630d99ed0c89b76f1e34ae9eff245f8532963](https://github.com/trxuanbac/K5-L2-DAY08-2A202603132-TranXuanBac-AIPrelabel/commit/2c0630d99ed0c89b76f1e34ae9eff245f8532963). Commit tiếp theo chỉ cập nhật thông tin commit này.
- Trạng thái bản nộp: **Release theo mẫu QC sau sửa**, ngày 2026-11-18. Review lại đạt **12/12 bẫy = 100%**. Gold 4 ảnh/76 annotation; batch sau sửa QC 24 ảnh/492 annotation; đủ ba mask SAM và ba ca calibration v1.1.
- Máy: macOS 26.3, Apple M1 arm64, RAM 8 GB. `.venv` dùng Python 3.12.16 và thư viện nhẹ cho chế độ Colab; `work/model-env` dùng Python 3.13.17, đã kiểm tra model local bằng CPU. Đã nhận kết quả Colab stage1; nhật ký ghi `cpu`. GPU T4 Colab chưa được xác nhận.
- CVAT (Docker): 2.82.1, bản local đang có tại http://localhost:8080 (đề minh họa bản 2.81.0).

## Kết quả tóm tắt (điền cuối bài; số lấy từ `submission/qc/*`, kèm mẫu số)

- Sau review lại: accepted 452/520 = 86,9%; edited 12/520 = 2,3%; deleted 56/520 = 10,8%; added 16/480 = 3,3%. Script loại đối tượng quanh bẫy khỏi các mẫu số này; file batch cuối có 492 annotation. Số đo ở `submission/qc/reviews/qc-02/review_stats_after_rework.json`.
- So với gold: precision của **máy** 47/72 = 65,3%; recall 47/75 = 62,7%. Gold đã có nhãn nháp trước lượt chỉnh sửa; ngưỡng cũng được chọn trên cùng 4 ảnh này.
- Bắt bẫy sau review lại: **12/12 = 100%**, đạt ngưỡng 80%. Mỗi loại loose, missing, wrong_class và extra đều đạt 3/3. Đây là lượt kiểm sau sửa, đã biết bẫy.
- Lịch sử: lượt đầu có 500 annotation, 6/12 bẫy; bản sau sửa bẫy có 490 annotation; sau sửa tiếp 8 lỗi QC có 492 annotation. Hồ sơ lượt đầu được giữ riêng tại `submission/qc/reviews/batch-01/`. Bản cuối không còn cảnh báo box cao dưới 20 px.
- Thời gian: chỉnh sửa 4 ảnh gold trong 25 phút, trung bình 6,25 phút/ảnh; review 24 ảnh batch trong 30 phút, trung bình 1,25 phút/ảnh.
- QC trước sửa: 8/98 = 8,2% lỗi, 4/5 ảnh có lỗi; đã đính chính một nhận xét nhầm trong số sơ bộ 9 lỗi. Sau sửa, tái kiểm cùng 5 ảnh/100 đối tượng: chưa ghi nhận lỗi rõ mới (0/100, 0/5). Cùng reviewer và cùng ảnh nên không xem là QC độc lập. Cận trên Wilson 95% của tỉ lệ ảnh lỗi sau sửa vẫn là 43%.
- **Quyết định sau review lại: Release theo mẫu QC sau sửa** — 12/12 bẫy, 0/100 đối tượng lỗi và 0/5 ảnh lỗi trong lượt tái kiểm. Script được chạy với số đo vòng sau sửa; quyết định Rework ngày 2026-11-17 thuộc vòng trước. Mẫu nhỏ và việc tái kiểm cùng ảnh chưa chứng minh chất lượng toàn lô.
