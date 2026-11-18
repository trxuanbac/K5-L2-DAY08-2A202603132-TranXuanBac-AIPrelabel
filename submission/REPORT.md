# Báo cáo Day 08 — 2A202603132 - Trần Xuân Bắc

Bài lab gồm thử model để tạo nhãn gợi ý, duyệt lại trên CVAT, chọn ngưỡng theo lớp và kiểm tra chất lượng sau sửa. Kết quả từng vòng được lưu riêng để đối chiếu các thay đổi.

## 1. Model và recipe (Part 2–3)

| Lớp | Model + cỡ | Ngưỡng | Lần chạy và căn cứ chọn ngưỡng |
|---|---|---|---|
| person / bicycle / motorbike / car / bus / truck | YOLO26m, Colab CPU | 0.3 mặc định theo script | `qc/colab_stage1/runs.csv`, r05; script quét không chọn ngưỡng riêng cho person, bicycle, motorbike, car vì không đạt recall 90%; bus chỉ 1 vật, truck 0 vật gold. |
| three_wheeler | YOLOE-26s, Colab CPU, prompt tuk-tuk / cyclo / cargo tricycle | 0.15 | `qc/colab_stage1/runs.csv`, r06; script quét ghi recall 7/7, precision 78% trên gold ở ngưỡng này. |

- Lệnh `merge_prelabels.py` đã dùng: `.venv/bin/python scripts/merge_prelabels.py work/colab-stage1-20261117/work/prelabel/yoloe_all/pre.coco.json work/colab-stage1-20261117/work/prelabel/y26_all/pre.coco.json --thr three_wheeler=0.15 --conf 0.3 --iou 0.6 --split batch,gold --out work/prelabel/merged_review/pre.coco.json`
- **Tour Part 2 đã chạy trên Colab CPU:** YOLO26m conf 0.25 cho 215 box/8 ảnh, conf 0.5 cho 139 box/8 ảnh; YOLOE cho 8 box/8 ảnh; YOLO26m + SAM 2.1 base (`sam2.1_b.pt`) cho 16 mask/2 ảnh. Nhật ký gốc ở `qc/colab_stage1/runs.csv`, các dòng tổng hợp là `colab-r01` đến `colab-r04` trong `model_log.csv`. Ảnh đối chiếu và checksum ở `qc/colab_stage1/tour/` và `tour_manifest.json`.
- Trước đó cũng có tour local CPU trên Mac với YOLO26 nano và SAM 2.1 tiny, gồm lượt 8 mask/2 ảnh. Hồ sơ và ảnh local được giữ riêng trong `qc/model_tour/` để đối chiếu.
- Part 5 có ba vật: img_013 dùng SAM 2.1 base theo ô lệnh Colab; img_004 và img_009 dùng SAM 2.1 tiny local CPU, cấu hình và checksum ở `qc/sam_clicks/completion_manifest.json`.
- Lỗi không sửa được chỉ bằng đổi ngưỡng: trong tour Colab, YOLO26m gán tuk-tuk xanh ở img_004 là `car` với conf 0,3735. SAM nhận box này và tạo mask nhưng giữ lớp `car`; cần model/prompt phù hợp và kiểm lại lớp. Ở img_002, tăng conf từ 0.25 lên 0.5 vẫn chưa tìm được tuk-tuk giữa ảnh, trong khi YOLOE tìm đúng `three_wheeler` với conf 0,9265.
- Box điểm cao vẫn cần sửa: img_003, box xe ba bánh #11 của bản trước sửa QC có conf 0,90 nhưng cắt mất phần mui. Lỗi hình học này được sửa trong `qc/reviews/qc-02/`; điểm của model không thay thế việc kiểm biên box.
- Ngưỡng được chọn và đo trên cùng 4 ảnh gold. Các ảnh này đã có nhãn nháp trước lượt chỉnh sửa, nên số đo có thể lạc quan hơn khi đánh giá trên một bộ ảnh độc lập. Lớp ít mẫu hoặc không đạt recall mục tiêu được giữ ở ngưỡng mặc định theo script.

## 2. AI error profile (sau review lại)

| Trạng thái | Số | Tỉ lệ | Mẫu số |
|---|---|---|---|
| accepted | 452 | 86,9% | 520 box máy |
| edited | 12 | 2,3% | 520 box máy |
| deleted | 56 | 10,8% | 520 box máy |
| added | 16 | 3,3% | 480 đối tượng sau duyệt |

Nguồn hiện tại: `qc/reviews/qc-02/review_stats_after_rework.json`, được tính lại từ `release/final_det.coco.json` sau review lại. File cuối có 24 ảnh/492 annotation; script loại 24 đối tượng nằm quanh các bẫy (tổng cả trước và sau duyệt) khỏi bảng trạng thái. Số đếm trong bảng không phải toàn bộ số box trong file xuất. Số đo lượt đầu vẫn được lưu riêng tại `qc/review_stats.json` và `qc/reviews/batch-01/`.

- Sau review lại và loại vùng quanh bẫy, `three_wheeler` có 8 box edited + 23 deleted trên 43 box máy của lớp này, tức 31/43 = 72,1% cần sửa/xóa. Đây là mô tả lượt này, không phải so sánh model trên test độc lập. Ví dụ img_003 có xe tải bị gán three_wheeler và nhãn khác lớp trên cùng vùng xe; xem CAL-01 và `qc/evidence/`.
- So với gold: precision của **máy** là 47/(47 + 25) = 65,3%; recall là 47/(47 + 28) = 62,7%, với 75 đối tượng và 1 ignore region. Các giá trị được đo trên 4 ảnh gold đã dùng để chọn ngưỡng, nên chưa phải đánh giá độc lập.

## 3. Thiên kiến tự động hóa và ảnh bẫy

- **Kết quả sau review lại: 12/12 bẫy = 100%, đạt ngưỡng 80% trong taxonomy.** Theo loại: loose 3/3, missing 3/3, wrong_class 3/3, extra 3/3. Script đã được chạy lại trên bản cuối 24 ảnh/492 annotation; xem `qc/reviews/qc-02/review_stats_after_rework.md`.
- Lịch sử lượt đầu: 6/12 bẫy = 50%; loose 1/3, missing 1/3, wrong_class 2/3, extra 2/3. Những ca cần sửa khi đó nằm ở img_013 (missing), img_021 và img_024 (loose), img_035 (extra), img_006 (wrong_class), img_034 (missing). Hồ sơ lượt đầu được giữ tại `qc/reviews/batch-01/`; kết quả hiện tại thuộc vòng review lại sau khi đã biết bẫy.
- Ở lượt đầu, accepted 89,8% đi cùng kết quả bắt bẫy 50%, cho thấy giữ nguyên nhiều box chưa đủ để đánh giá chất lượng duyệt. Sau các vòng kiểm và sửa, accepted là 86,9% và toàn bộ 12 bẫy đã được xử lý. Cần đọc cả kết quả bẫy, lỗi thực tế và phạm vi QC của từng vòng.

## 4. Máy có đáng dùng không?

- Thời gian chỉnh sửa là **25 phút cho 4 ảnh gold**, tương đương **6,25 phút/ảnh**, và **30 phút duyệt 24 ảnh batch**, tương đương **1,25 phút/ảnh** (`time_log.csv`). Thời gian trung bình ở lượt đầu chênh 5 lần. Tuy nhiên, 30 phút chưa gồm sửa bẫy, sửa QC và hoàn thiện mask. Hai nhóm ảnh khác nhau về nội dung và độ khó, nên đây chưa phải phép so sánh thời gian có kiểm soát.
- Pre-label giúp rút ngắn thao tác ở lượt đầu, nhưng chưa có tổng thời gian của tất cả các vòng sửa để kết luận mức tiết kiệm công sức. Kết quả bắt bẫy cho thấy vẫn cần kiểm tra chất lượng cùng với tốc độ.
- **Ba quy tắc cần áp dụng ở những lần duyệt sau:**
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

- Đối chiếu với mục 4.2 cho thấy mask ở img_013 còn lấn vào người, chưa đúng yêu cầu tách từng vật. CAL-02 được dùng để phân biệt phần xe, giỏ cố định và hàng rời ở img_009. Các nhận xét dựa trên ảnh overlay; chưa có mask ground truth để chấm IoU.
- Interactor SAM trực tiếp trong CVAT chưa được thử ở Part 5. Các ảnh kết quả được tạo offline bằng `sam2_points.py`.

## 6. Calibration (Part 6)

- Đã chốt **3 ca CAL-01–03** trong `qc/calibration_decisions.csv`: CAL-01 và CAL-03 từ `loi_may`, CAL-02 từ `cau_hoi_mo`. Nội dung xác nhận được lưu tại `qc/calibration_confirmation.json`.
- `guideline_v1.1_calibrated.md` có ba ca kèm ảnh: kiểm cấu trúc và box trùng ở img_003; phân biệt hàng rời/giỏ cố định ở img_031 và img_009; kiểm vùng người trong mask xe ở img_013. Taxonomy cập nhật version v1.1, toàn bộ mục rules giữ nguyên.
- CAL-02 làm rõ câu hỏi mở số 3 của v1.0. CAL-01 và CAL-03 nhắc lại cách chọn lớp và tách vùng mask đã có trong guideline, đồng thời bổ sung bước kiểm sau khi chạy model. Những ca này giúp chỉ ra chỗ cần làm rõ quy tắc và chỗ cần kiểm lại nhãn.

## 7. QC và quyết định (Part 6)

- Mẫu ban đầu: 5 ảnh (0 ảnh `can_review` + 5 ngẫu nhiên, seed 42), 98 đối tượng. Số sơ bộ 9 lỗi có một nhận xét nhầm về box #69 ở img_006. Đã rút nhận xét đó sau khi phóng ảnh: trước sửa có **8/98 = 8,2%**, **4/5 ảnh = 80%**. Giữ nguyên bản sơ bộ và đính chính tại `qc/reviews/qc-01/`.
- Ở vòng sửa tiếp theo, 4 box/nhãn được cập nhật, 1 box sai/trùng bị xóa và 3 vật thiếu được bổ sung. Như vậy đã xử lý 8 lỗi được ghi nhận và giữ nguyên 485 annotation khác. Bản hiện tại `release/final_det.coco.json` có **24 ảnh/492 annotation**, khớp với bản export CVAT; `qc_fixed.json` thay thế nhãn của 12 ảnh.
- Tái kiểm **cùng 5 ảnh** sau sửa: 100 đối tượng, không ghi nhận lỗi rõ mới trong lượt này (**0/100 đối tượng, 0/5 ảnh**). Đây là tái kiểm sau sửa trên cùng mẫu ảnh; chưa có lượt QC độc lập. Hồ sơ tại `qc/reviews/qc-02/`.
- Loại lỗi trước sửa: sai vị trí/kích thước **2** (img_003 box #11 thiếu mui, img_031 box #419 cắt giỏ); sai lớp **3** (img_003 box #12, #13, #14); bỏ sót **3** (xe đạp img_003, người img_006, xe máy img_035). Ảnh đối chiếu tại `qc/evidence/`.
- **Giới hạn mẫu nhỏ:** sau sửa 0 ảnh lỗi/5 ảnh, cận trên Wilson 95% do script tính vẫn **43%**. Không dùng mẫu này để chứng minh toàn lô đạt ngưỡng 2%; cùng reviewer và cùng ảnh có thể cùng bỏ sót.
- Script giúp kiểm định dạng, đếm lỗi trong phiếu và tính tỉ lệ cùng khoảng tin cậy. Việc box có ôm sát vật hay còn vật bị bỏ sót vẫn cần đối chiếu với ảnh gốc. Những lỗi cùng bị bỏ qua ở cả lượt duyệt và lượt QC sẽ không xuất hiện trong số đếm này.

**Quyết định sau review lại: Release theo mẫu QC sau sửa**, cập nhật ngày 2026-11-18. Bản cuối đạt **12/12 bẫy = 100%**, mẫu tái kiểm ghi **0/100 đối tượng lỗi, 0/5 ảnh lỗi**, không còn ca guideline chưa chốt. Báo cáo QC được tính lại bằng `python scripts/qc_report.py --guideline-gap 0 --review-stats submission/qc/reviews/qc-02/review_stats_after_rework.json` và gợi ý **RELEASE**. Quyết định Rework ngày 2026-11-17 thuộc vòng trước, khi script còn dùng số đo lượt đầu.

Phạm vi quyết định dựa trên 12 bẫy và mẫu QC hiện có. Kết quả 12/12 là kiểm sau sửa khi đã biết bẫy; tái kiểm cùng 5 ảnh chưa phải đánh giá độc lập hoặc chứng minh toàn lô dưới 2% lỗi. Kiểm thêm mẫu mới, xem kỹ biên mask và ghi thời gian các vòng bổ sung vẫn là hướng cải thiện tiếp theo.

## 8. Ghi chú cá nhân

- **Công cụ sử dụng:** Codex hỗ trợ chuẩn bị môi trường, kiểm/sửa nhãn, tạo mask và tổng hợp báo cáo. Kết quả được đối chiếu bằng script và ảnh gốc.
- **Cập nhật script QC:** thêm `--review-stats FILE` vào `scripts/qc_report.py` để chọn đúng vòng review khi tái kiểm. Mặc định vẫn đọc `qc/review_stats.json` của lượt đầu. Không đổi công thức hoặc ngưỡng; báo cáo hiện tại dùng số đo được script tính từ nhãn cuối. Bản QC trước cập nhật được giữ tại `qc/reviews/qc-02/qc_report_before_round_update.md`.
- **Giới hạn gold:** 4 ảnh đã có nhãn gợi ý trước lượt chỉnh sửa 25 phút. Bản lưu có 83 annotation; sau khi bỏ 7 box dưới 20 px, bản xuất còn 76 annotation. Vì vậy, bộ gold này chưa độc lập với nhãn gợi ý.
- **Môi trường:** chạy model bằng CPU trên Google Colab, đã có nhật ký sáu lượt YOLO26m, YOLOE và SAM 2.1 base. Máy Mac M1, RAM 8 GB chạy CVAT Docker 2.82.1 và Python QC 3.12.16; môi trường model local Python 3.13.17 được dùng cho các lượt đối chiếu và hai mask bổ sung.
- **Dữ liệu chạy model:** không dùng kết quả có sẵn trong `data/cache/`. Tour local và kết quả Colab được lưu tại `model_log.csv`, `qc/model_tour/`, `qc/colab_stage1/`; hồ sơ mask tại `qc/sam_clicks/`.
- **Vướng mắc:** Đã gặp lỗi Colab không cấp runtime và báo `Load failed`. Trong QC, một nhận xét về box #69 img_006 đã được rút sau khi phóng ảnh kiểm lại; box đúng được giữ nguyên, có đính chính tại `qc/reviews/qc-01/erratum.json`.
- **Điều rút ra:** Cần tạo gold độc lập từ đầu, ghi thời gian từng vòng và dùng thêm mẫu mới để kiểm tra sau sửa.
