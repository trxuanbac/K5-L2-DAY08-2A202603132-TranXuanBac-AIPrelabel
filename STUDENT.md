# Thông tin cá nhân

- Họ và tên: Trần Xuân Bắc
- MSHV: 2A202603132
- Lớp: L2
- Tài khoản GitHub: trxuanbac
- Repo bài nộp (public): https://github.com/trxuanbac/K5-L2-DAY08-2A202603132-TranXuanBac-AIPrelabel
- Commit chốt bài (hash): [d8586f7b7616b4ebd9d57b57d427a685841bf6dd](https://github.com/trxuanbac/K5-L2-DAY08-2A202603132-TranXuanBac-AIPrelabel/commit/d8586f7b7616b4ebd9d57b57d427a685841bf6dd). Đây là commit chốt nội dung; commit kế tiếp chỉ cập nhật dòng tham chiếu này.
- Cập nhật kết quả: 2026-11-18
- Trạng thái: **Release theo mẫu QC sau sửa**; review lại đạt **12/12 bẫy = 100%**.

## Môi trường đã sử dụng

- **Chạy model: CPU trên Google Colab.** Nhật ký có sáu lượt: bốn lượt tour Part 2 và hai lượt tạo nguồn nhãn cho Part 3–4. Model gồm YOLO26m, YOLOE small và SAM 2.1 base (`sam2.1_b.pt`). Xem [nhật ký Colab](submission/qc/colab_stage1/runs.csv).
- **Máy cá nhân:** Apple M1 arm64, RAM 8 GB, macOS 26.3; chạy CVAT Docker 2.82.1 tại http://localhost:8080 và các script đo số/QC bằng `.venv` Python 3.12.16.
- **Các lượt local bổ sung:** `work/model-env` Python 3.13.17 dùng cho tour đối chiếu trước đó và hai ảnh mask SAM tiny (`sam2.1_t.pt`). Chi tiết tại [hồ sơ tour model](submission/qc/model_tour/README.md).

## Kết quả tóm tắt

| Hạng mục | Kết quả | File đối chiếu |
|---|---|---|
| Gold | 4 ảnh, 76 annotation: 75 đối tượng và 1 ignore region | [gold_manual.json](submission/labels/gold_manual.json) |
| Batch cuối | 24 ảnh, 492 annotation; không còn cảnh báo box cao dưới 20 px | [final_det.coco.json](submission/release/final_det.coco.json) |
| Bẫy sau review lại | **12/12 = 100%**; loose, missing, wrong_class và extra đều 3/3; ngưỡng đạt 80% | [review_stats_after_rework.md](submission/qc/reviews/qc-02/review_stats_after_rework.md) |
| Mask SAM | 3 ảnh: img_013 dùng SAM base trên Colab; img_004 và img_009 dùng SAM tiny local CPU | [hồ sơ ba mask](submission/qc/sam_clicks/README.md) |
| Calibration | Đã chốt CAL-01–03 và cập nhật guideline v1.1; giữ nguyên mục rules của taxonomy | [calibration_decisions.csv](submission/qc/calibration_decisions.csv), [guideline v1.1](submission/guidelines/guideline_v1.1_calibrated.md) |
| QC sau sửa | Không ghi nhận lỗi mới trên mẫu tái kiểm: **0/100 đối tượng, 0/5 ảnh** | [qc_report_auto.md](submission/qc/qc_report_auto.md) |

- **Số đo sau review lại:** accepted 452/520 = 86,9%; edited 12/520 = 2,3%; deleted 56/520 = 10,8%; added 16/480 = 3,3%. Script loại các đối tượng quanh bẫy khỏi bảng trạng thái nên mẫu số khác tổng 492 annotation của bản cuối.
- **Máy so với gold:** precision 47/72 = 65,3%; recall 47/75 = 62,7%.
- **Thời gian đã ghi:** chỉnh sửa 4 ảnh gold trong 25 phút, trung bình 6,25 phút/ảnh; review 24 ảnh batch lượt đầu trong 30 phút, trung bình 1,25 phút/ảnh. Xem [time_log.csv](submission/time_log.csv).
- **QC trước sửa:** 8/98 = 8,2% lỗi, 4/5 ảnh có lỗi sau đính chính. Đã xử lý 8 lỗi; các lượt xuất và số đo trước sửa được lưu tại [hồ sơ review](submission/qc/reviews/qc-02/README.md).

## Quyết định và giới hạn

**Release theo mẫu QC sau sửa**, dựa trên kết quả hiện tại: 12/12 bẫy, 0/100 đối tượng lỗi, 0/5 ảnh lỗi và ba ca calibration đã chốt. Script QC dùng số đo vòng sau review lại; quyết định Rework ngày 2026-11-17 thuộc vòng trước. Phân tích đầy đủ tại [REPORT.md](submission/REPORT.md).

Đã xác nhận chốt bản nộp ngày 2026-11-18 theo kết quả QC hỗ trợ hiện có; [hồ sơ xác nhận](submission/qc/qc_review_provenance.json) đã cập nhật trạng thái. Đây là xác nhận sử dụng kết quả đã lưu để nộp bài, không phải một lượt QC độc lập mới.

- Gold đã có nhãn gợi ý trước lượt chỉnh sửa; chọn và chấm ngưỡng trên cùng 4 ảnh nên số đo máy chưa độc lập.
- Kết quả 12/12 thuộc lượt kiểm sau sửa, đã biết bẫy. QC tái kiểm cùng 5 ảnh và cùng reviewer; cận trên Wilson 95% của tỉ lệ ảnh lỗi vẫn là 43%, chưa chứng minh toàn lô dưới 2% lỗi.
- Thời gian 30 phút chỉ tính lượt review đầu; chưa có số đo thời gian các vòng sửa bổ sung.
