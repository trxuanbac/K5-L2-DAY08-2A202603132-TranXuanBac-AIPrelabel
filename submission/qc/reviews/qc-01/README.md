# QC — lượt 1

**Đã đính chính:** một nhận xét về box #69 img_006 trong số sơ bộ 9 lỗi là nhầm. Phóng lại ảnh cho thấy box này đúng; đã giữ nguyên nhãn và rút nhận xét. Số lỗi xác nhận trước sửa là **8/98 = 8,2%**, trên 4/5 ảnh. Xem [erratum.json](erratum.json), [phiếu đã hiệu chỉnh](qc_review_corrected.csv), [báo cáo trước sửa](qc_report_corrected_before_rework.md). Bản sơ bộ bên dưới được giữ làm lịch sử.

Sau đó đã sửa 8 lỗi theo yêu cầu học viên; bản hiện tại và kết quả tái kiểm ở [qc-02](../qc-02/README.md).

Đã xem ảnh gốc và ảnh nhãn có ID của 5 ảnh trong mẫu seed 42: `img_003`, `img_006`, `img_014`, `img_031`, `img_035`. Bản ứng viên có 98 đối tượng trong mẫu. Thông tin lượt kiểm được lưu trong phiếu và nhật ký QC; chưa có lượt kiểm độc lập.

## Kết quả quan sát sơ bộ trước đính chính

- 9 dòng lỗi, 9 đối tượng/ca lỗi theo cách đếm của script: **9/98 = 9,2%**.
- Có lỗi trên **4/5 ảnh = 80%**.
- Sai vị trí/kích thước: 3; sai lớp: 3; bỏ sót: 3.
- `img_014` không ghi nhận lỗi rõ trong lượt này; điều đó không bảo đảm không có lỗi bị cùng bỏ qua.
- Xem [phiếu kiểm](qc_review.csv), [báo cáo do script tạo](qc_report_auto.md), [summary](summary.json) và [ảnh đối chiếu](../../evidence/README.md).

Phần bỏ sót có `object_id` trống và mô tả vị trí trong `note`, đúng định dạng hướng dẫn. Script lấy mẫu số 98 từ các đối tượng đang có trong nhãn nguồn; những vật bị bỏ sót được ghi như các ca lỗi theo quy ước của script.

## Trạng thái guideline và quyết định

Ở thời điểm ghi bản sơ bộ, ba đề xuất CAL-01–03 chưa chốt; script chạy `--guideline-gap 1` và gợi ý HOLD. Sau đó học viên đã xác nhận cả ba, taxonomy chuyển v1.1 và script chạy `--guideline-gap 0`, gợi ý REWORK. Các báo cáo lịch sử giữ riêng, không sửa tay đầu ra script.

Quyết định cuối Release/Hold/Rework do học viên xác nhận. Chưa sửa nhãn CVAT hoặc bản ứng viên trong lượt QC này, chưa có thời gian QC của học viên để ghi thêm. ZIP Colab chỉ chứa một mask; sau đó đã bổ sung hai mask local CPU, hiện đủ ba vật ở `submission/masks/`.

## Giới hạn

Lượt QC dùng 5 ảnh; chưa có kiểm tra độc lập bởi người thứ hai. Cận trên Wilson 95% do script tính với 4 ảnh lỗi/5 ảnh là 96%; mẫu nhỏ không chứng minh được chất lượng toàn lô ở ngưỡng 2%. Giữ nguyên lượt review đầu 6/12; kết quả 12/12 sau sửa bẫy nằm riêng ở `../batch-02/`.
