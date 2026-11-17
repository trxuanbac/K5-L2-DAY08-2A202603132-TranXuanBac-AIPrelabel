# Báo cáo Day 08 — 2A202603132 - Trần Xuân Bắc

> Bản báo cáo kỹ thuật để học viên đọc và chốt trước khi nộp. Mọi số đo có mẫu số và nguồn. Ba quy tắc calibration đã được học viên xác nhận; phần phân tích và đề xuất cải thiện dưới đây cần học viên đối chiếu với trải nghiệm thực tế. Không ghi một bước thao tác cá nhân là đã làm khi chưa có thông tin.

## 1. Model và recipe (Part 2–3)

| Lớp | Model + cỡ | Ngưỡng | Nguồn lần chạy và quét ngưỡng |
|---|---|---|---|
| person / bicycle / motorbike / car / bus / truck | YOLO26m, Colab CPU | 0.3 mặc định theo script | `qc/colab_stage1/runs.csv`, r05; script quét không chọn ngưỡng riêng cho person, bicycle, motorbike, car vì không đạt recall 90%; bus chỉ 1 vật, truck 0 vật gold. |
| three_wheeler | YOLOE-26s, prompt tuk-tuk / cyclo / cargo tricycle | 0.15 | `qc/colab_stage1/runs.csv`, r06; script quét ghi recall 7/7, precision 78% trên gold ở ngưỡng này. |

- Lệnh `merge_prelabels.py` đã dùng: `.venv/bin/python scripts/merge_prelabels.py work/colab-stage1-20261117/work/prelabel/yoloe_all/pre.coco.json work/colab-stage1-20261117/work/prelabel/y26_all/pre.coco.json --thr three_wheeler=0.15 --conf 0.3 --iou 0.6 --split batch,gold --out work/prelabel/merged_review/pre.coco.json`
- **SAM đã chạy:** SAM 2.1 tiny (`sam2.1_t.pt`), CPU, cỡ nhỏ cho cấu hình RAM 8 GB. Lượt `r06` có 2 ảnh và 8 mask; xem ảnh kết quả trong `qc/model_tour/`.
- Part 5 có ba vật: img_013 dùng SAM 2.1 base theo ô lệnh Colab; img_004 và img_009 dùng SAM 2.1 tiny local CPU, cấu hình và checksum ở `qc/sam_clicks/completion_manifest.json`.
- Lỗi không sửa được chỉ bằng đổi ngưỡng: trong tour local, tuk-tuk xanh ở img_002 bị YOLO26n gọi `truck` với conf 0,3712; nâng conf 0,5 làm box biến mất, không tạo ra nhãn `three_wheeler`. Dùng model/prompt phù hợp cho lớp địa phương và kiểm lại nhãn; ảnh tour ở `qc/model_tour/`.
- Box điểm cao vẫn cần sửa: img_003, box xe ba bánh #11 của bản trước sửa QC có conf 0,90 nhưng cắt mất phần mui. Lỗi hình học này được sửa trong `qc/reviews/qc-02/`; điểm của model không thay thế việc kiểm biên box.
- Giới hạn: chọn và chấm ngưỡng trên cùng 4 ảnh gold; gold cũng đã có nhãn nháp trước lượt học viên chỉnh sửa. Các số đo này không phải kiểm định trên gold độc lập. Lớp ít mẫu hoặc không đạt recall mục tiêu được script giữ ở ngưỡng mặc định.

## 2. AI error profile (từ `qc/review_stats.md`)

| Trạng thái | Số | Tỉ lệ | Mẫu số |
|---|---|---|---|
| accepted | 467 | 89,8% | 520 box máy |
| edited | 10 | 1,9% | 520 box máy |
| deleted | 43 | 8,3% | 520 box máy |
| added | 12 | 2,5% | 489 đối tượng sau duyệt |

Nguồn: `qc/review_stats.json`, lượt review đầu của job 23. File COCO xuất có 24 ảnh/500 annotation; script loại 23 đối tượng nằm quanh các bẫy (tổng cả trước và sau duyệt) khỏi bảng trạng thái. Số đếm trong bảng không phải toàn bộ số box trong file xuất.

- Trên lượt review đầu đã loại vùng quanh bẫy, `three_wheeler` có 7 box edited + 20 deleted trên 43 box máy của lớp này, tức 27/43 = 62,8% cần sửa/xóa. Đây là mô tả lượt này, không phải so sánh model trên test độc lập. Ví dụ img_003 có xe tải bị gán three_wheeler và nhãn khác lớp trên cùng vùng xe; xem CAL-01 và `qc/evidence/`.
- So với gold: precision của **máy** 47/(47 + 25) = 65,3%; recall 47/(47 + 28) = 62,7% (75 đối tượng gold, không tính 1 ignore region). Chỉ đo trên 4 ảnh gold đã dùng để chọn ngưỡng và đã có nhãn nháp trước lượt học viên chỉnh sửa; chưa phải đánh giá độc lập.

## 3. Thiên kiến tự động hóa và ảnh bẫy

- Bắt bẫy lượt review đầu: 6/12 = 50%; ngưỡng trong taxonomy là 80%. Theo loại: loose 1/3, missing 1/3, wrong_class 2/3, extra 2/3. Script ghi lọt ở img_013 (missing), img_021 và img_024 (loose), img_035 (extra), img_006 (wrong_class), img_034 (missing). Học viên chưa cung cấp nhật ký thao tác từng bước, nên chưa quy kết việc bỏ bước nào của checklist.
- Sau sửa bẫy: script ghi 12/12 trên bản 490 annotation, hồ sơ ở `qc/reviews/batch-02/`. Sau sửa tiếp 8 lỗi QC, bản hiện tại có 24 ảnh/492 annotation. Kết quả 12/12 là kiểm sau khi đã biết bẫy; không thay kết quả review đầu 6/12.
- Diễn giải kỹ thuật để học viên đối chiếu: accepted 89,8% chỉ mô tả box ít thay đổi; bắt bẫy 50% cho thấy vẫn có lỗi đã biết không được xử lý ở lượt đầu. Hai số không chứng minh nguyên nhân tâm lý hoặc việc đã/không làm một bước cụ thể.

## 4. Máy có đáng dùng không?

- Thời gian (từ `time_log.csv`): gán tay/chỉnh sửa gold **6,25 phút/ảnh** (25 phút/4 ảnh) vs review batch **1,25 phút/ảnh** (30 phút/24 ảnh), đều do học viên cung cấp. Tốc độ lượt đầu chênh 5 lần; 30 phút chưa gồm sửa bẫy, sửa QC và hoàn thiện mask. Hai tập ảnh khác nhau, gold có nhãn nháp và học viên đã quen cảnh nên không xem đây là thí nghiệm thời gian có kiểm soát.
- Nhận định kỹ thuật đề nghị học viên xem lại: pre-label rút ngắn thao tác ở lượt đầu, nhưng chưa có thời gian toàn bộ các vòng sửa để kết luận tiết kiệm tổng công sức. Cần dùng cùng số đo chất lượng; tốc độ riêng không chứng minh bộ nhãn đã đủ tốt.
- **Ba quy tắc đề nghị áp dụng ở lượt sau**, chưa ghi là đã thực hiện trong lượt 30 phút:
  1. Mỗi ảnh ẩn toàn bộ nhãn 5–10 giây, quét người và phương tiện trước khi hiện nhãn máy.
  2. Kiểm lần lượt bỏ sót → box thừa → sai lớp → biên box; đối chiếu mọi box chồng khác lớp và không chấp nhận chỉ vì conf cao.
  3. Giữ pre-label gốc, bấm giờ riêng mỗi vòng sửa và lưu kết quả trước/sau; QC lại sau sửa, ghi rõ khi dùng cùng ảnh hoặc đã biết bẫy.

## 5. Mask SAM cho 3 vật (Part 5)

| Ảnh | SAM (phiên bản) | Số click | Mask gồm người lái / hàng hoá? | Lỗi quan sát | File trong `masks/` |
|---|---|---|---|---|---|
| img_013 | SAM 2.1 base, `sam2.1_b.pt` theo ô lệnh Colab | 3: 2 dương + 1 âm | Còn gồm một phần người lái và người mặc áo sọc ở phía sau | Vùng tô còn dính người và một phần xe máy bên phải; click âm chưa loại hết | `tuktuk_img013.jpg` |
| img_004 | SAM 2.1 tiny, `sam2.1_t.pt`, local CPU | 3: 2 dương + 1 âm | Người áo xanh tại click âm nằm ngoài mask; đồ trong xe còn cần phân biệt với phần xe | Mask phủ phần lớn tuk-tuk trước; biên kính/đồ trong xe cần kiểm. Model trả 94.656 px, 1 polygon | `tuktuk_img004.jpg` |
| img_009 | SAM 2.1 tiny, `sam2.1_t.pt`, local CPU | 3: 2 dương + 1 âm | Vùng chuối tại click âm không được tô | Mới phủ bánh và khung dưới, còn thiếu tay lái/giỏ gắn xe. Model trả 20.739 px, 1 polygon | `motorbike_img009.jpg` |

Đã có **3/3 ảnh mask cho ba vật**. ZIP Colab chỉ chứa ảnh 013; hai ảnh còn lại được tạo local bằng SAM tiny. Hồ sơ nhập ZIP ở `qc/sam_clicks/import_manifest.json`, hồ sơ đủ ba vật ở `qc/sam_clicks/completion_manifest.json`. Thời gian toàn lệnh local có ghi riêng, không thay cho thời gian inference; lượt click Colab không có số đo thời gian/thiết bị riêng.

- Đối chiếu kỹ thuật với mục 4.2: vùng tô chạm người ở img_013 cần kiểm theo quy tắc mỗi vật một mask; phân biệt hàng rời và giỏ cố định ở img_009 đã được học viên chốt trong CAL-02. Các giới hạn mask trong bảng là quan sát hỗ trợ trên overlay, chưa phải phép chấm mask bằng ground truth.
- Interactor SAM trực tiếp trong CVAT chưa được thử ở Part 5; các kết quả ở đây được tạo offline bằng `sam2_points.py`.

## 6. Calibration (Part 6)

- Học viên đã xác nhận **3 quyết định CAL-01–03** tại `qc/calibration_decisions.csv`: CAL-01 và CAL-03 từ `loi_may`; CAL-02 từ `cau_hoi_mo`. Hồ sơ xác nhận ở `qc/calibration_confirmation.json`.
- `guideline_v1.1_calibrated.md` có ba ca kèm ảnh: kiểm cấu trúc và box trùng ở img_003; phân biệt hàng rời/giỏ cố định ở img_031 và img_009; kiểm vùng người trong mask xe ở img_013. Taxonomy cập nhật version v1.1, toàn bộ mục rules giữ nguyên.
- Căn cứ kỹ thuật: CAL-02 làm rõ câu hỏi mở 3 của v1.0; CAL-01 và CAL-03 áp dụng lại quy tắc lớp, vùng mask đã có. Chưa có mô tả trải nghiệm đủ để quy các lỗi ban đầu cho một thói quen duyệt cụ thể của học viên.

## 7. QC và quyết định (Part 6)

- Mẫu ban đầu: 5 ảnh (0 ảnh `can_review` + 5 ngẫu nhiên, seed 42), 98 đối tượng. Codex kiểm hỗ trợ; số sơ bộ 9 lỗi có một nhận xét nhầm về box #69 ở img_006. Đã rút nhận xét đó sau khi phóng ảnh: trước sửa có **8/98 = 8,2%**, **4/5 ảnh = 80%**. Giữ nguyên bản sơ bộ và đính chính tại `qc/reviews/qc-01/`.
- Sau khi học viên yêu cầu sửa tiếp, đã chỉnh 4 box/nhãn, bỏ 1 box sai/trùng và thêm 3 vật thiếu: giải quyết 8 lỗi đã ghi, giữ 485 annotation ngoài phạm vi sửa. Bản hiện tại `release/final_det.coco.json` có **24 ảnh/492 annotation**, khớp export CVAT; `qc_fixed.json` thay 12 ảnh.
- Tái kiểm **cùng 5 ảnh** sau sửa: 100 đối tượng, không ghi nhận lỗi rõ mới trong lượt này (**0/100 đối tượng, 0/5 ảnh**). Đây là kiểm hỗ trợ sau sửa, không phải mẫu mới hoặc QC độc lập. Hồ sơ tại `qc/reviews/qc-02/`.
- Loại lỗi trước sửa: sai vị trí/kích thước **2** (img_003 box #11 thiếu mui, img_031 box #419 cắt giỏ); sai lớp **3** (img_003 box #12, #13, #14); bỏ sót **3** (xe đạp img_003, người img_006, xe máy img_035). Ảnh đối chiếu tại `qc/evidence/`.
- **Giới hạn mẫu nhỏ:** sau sửa 0 ảnh lỗi/5 ảnh, cận trên Wilson 95% do script tính vẫn **43%**. Không dùng mẫu này để chứng minh toàn lô đạt ngưỡng 2%; cùng reviewer và cùng ảnh có thể cùng bỏ sót.
- Script kiểm định dạng, đếm lỗi trong phiếu và tính tỉ lệ/khoảng tin cậy. Nó không xác minh nhận xét hình ảnh, không tìm lỗi cả người và model cùng bỏ qua, không thay cho học viên hoặc người kiểm độc lập đối chiếu lại.

**Gợi ý kỹ thuật hiện tại: Rework**, ngày 2026-11-17. `qc_report.py --guideline-gap 0` vẫn gợi ý REWORK do lượt review đầu bắt 6/12 bẫy, dưới 80%. Kết quả 12/12 sau sửa không được thay vào số đo ban đầu. **Quyết định chốt nộp của học viên: chưa xác nhận.**

Việc tiếp theo đề nghị học viên xem lại: kiểm độc lập hoặc mở rộng kiểm toàn lô theo v1.1, kiểm biên mask và ghi thời gian thực tế của các vòng bổ sung; sau đó chốt quyết định chất lượng. Không có bước sửa số đo để đổi gợi ý thành Release.

## 8. Ghi chú cá nhân

- **Dùng AI để làm bài:** Codex hỗ trợ chuẩn bị repo/môi trường/CVAT, xuất và kiểm nhãn, chạy script đo, quan sát QC và sửa các lỗi đã ghi theo yêu cầu học viên. Học viên báo review đầu 30 phút; số đo và file 24 ảnh/500 annotation giữ ở `qc/reviews/batch-01/`. Sửa bẫy có bản 490 annotation; sau sửa QC có bản 492 annotation ở `qc/reviews/qc-02/`. Đã tạo hai mask SAM tiny local cùng một mask SAM base từ Colab. Ba quy tắc calibration đã được học viên xác nhận; phần phân tích báo cáo là bản kỹ thuật để học viên đọc lại. Không ghi thêm thời gian thao tác học viên cho các vòng hỗ trợ này.
- Gold có bị nhiễm không (bạn có nhìn pre-label hay hỏi AI trước khi gán xong)? Có: task 21 đã có bản nháp 58 annotation trước lượt gán tay/chỉnh sửa 25 phút do học viên báo. Bản học viên lưu có 83 annotation; review bỏ 7 box dưới 20 px, xuất `labels/gold_manual.json` với 76 annotation. Bộ này không phải gold được tạo độc lập trước khi thấy nhãn gợi ý.
- Máy / GPU / CVAT dùng; vướng mắc cài đặt: macOS 26.3, Apple M1, RAM 8 GB; CVAT Docker 2.82.1 đã có sẵn. Môi trường QC nhẹ `.venv` dùng Python 3.12.16; môi trường model `work/model-env` dùng Python 3.13.17, đã chạy local bằng CPU. Colab ban đầu báo phần phụ trợ không có sẵn; sau đó học viên chạy được và tải `colab_stage1.zip`. Nhật ký trong ZIP ghi thiết bị `cpu`, chưa có lượt chạy GPU T4 để xác nhận.
- Dùng cache `data/cache/` thay vì tự chạy? Không. Các lượt tour local được lưu ở `model_log.csv` và `qc/model_tour/runs.json`. Part 3–4 hiện dùng kết quả Colab CPU: YOLO26m và YOLOE-26s, có nhật ký gốc và checksum tại `qc/colab_stage1/`. Kết quả quét YOLO26 nano cũ được giữ tại `qc/model_tour/local_threshold_sweep.*`.
- Lỗi đã gặp: Colab từng không cấp runtime và có lỗi gửi lệnh `Load failed`; sau đó nhận được ZIP kết quả. Chưa xác nhận bug của script gán nhãn. Một nhận xét QC về box #69 img_006 của lượt hỗ trợ đã được đính chính bằng ảnh phóng, không sửa box đúng để khớp nhận xét sai; xem `qc/reviews/qc-01/erratum.json`.
- Đề nghị cho lượt sau để học viên cân nhắc: giữ gold độc lập từ đầu, lưu log từng vòng và thực hiện QC độc lập sau sửa. Chưa ghi đây là hành động cá nhân đã được thực hiện.
