# Day 08 — bước tiếp theo của Trần Xuân Bắc

Trạng thái ngày 2026-11-17: đã chuẩn bị Part 0 trên máy local. Bài chưa hoàn thành; cần học viên gán tay gold trước khi chạy AI. Tài khoản GitHub đã xác nhận: `trxuanbac`.

## 1. Việc cần làm ngay: gán tay 4 ảnh gold

1. Đọc [label contract v1.0](guideline/guideline_v1.0_label_contract.md).
2. Mở [job gold-manual trong CVAT](http://localhost:8080/tasks/21/jobs/21), đăng nhập tài khoản local đang dùng. Project là [day08-2A202603132](http://localhost:8080/projects/3).
3. Bắt đầu bấm giờ khi thực sự bắt đầu gán; dừng khi hoàn tất. Nếu nghỉ, trừ thời gian nghỉ. Ghi số phút thực tế vào `submission/time_log.csv`, dòng `gold_manual`, `images = 4`.
4. Tự gán toàn bộ 4 ảnh: `img_001.jpg`, `img_012.jpg`, `img_020.jpg`, `img_036.jpg`. Dùng Rectangle, để trống `conf`; chỉ tick `can_review` khi không chắc quy tắc. Lưu sau mỗi ảnh bằng `Ctrl+S` hoặc nút Save.
5. Khi đã lưu đủ 4 ảnh, nhắn **“xong gold”** để Codex xuất COCO và kiểm tra cấu trúc. Nếu tự export: Task 21 → Actions → Export task dataset → COCO 1.0 → tắt Save images; lấy `annotations/instances_default.json` trong ZIP, lưu thành `submission/labels/gold_manual.json`.

Theo [RULES.md](RULES.md), “Part 1 làm trước mọi thứ có AI”. Chưa chạy model, xem cache/pre-label hay dùng AI Interactor trên gold. Không nhờ AI nhận diện đối tượng trong gold. Các phần minh họa có nhãn gold trong tài liệu HTML nên để sau khi đã export gold.

Sau khi có file export:

```bash
cd /Users/chuoi/tool/K5-L23-DAY08-2A202603132-TranXuanBac-AIPrelabel
source .venv/bin/activate
python scripts/validate_labels.py submission/labels/gold_manual.json --expect gold
```

Validator kiểm định dạng và phạm vi ảnh; học viên chịu trách nhiệm độ đúng của nhãn.

## 2. Những gì đã chuẩn bị và kiểm tra

| Hạng mục | Trạng thái thực tế |
|---|---|
| Repo local | Tên đúng mẫu; README, thông tin học viên và ghi chú dùng AI đã cập nhật |
| Python | `.venv`, Python 3.13.17; cài `requirements-local.txt`, `pip check` đạt |
| Môi trường nhẹ + CVAT | `python docs/day08_setup.py check --light` báo **SẴN SÀNG cho buổi học**; log tại `work/logs/setup-light.txt` |
| CVAT | Bản Docker 2.82.1 đang chạy; dùng lại bản hiện có |
| Project Day 08 | Project 3, đủ 8 lớp; kiểm đúng loại hình và thuộc tính `conf`, `can_review` theo taxonomy |
| Gold | Task 21 / Job 21, đúng 4 ảnh, chưa có annotation tại lúc chuẩn bị |
| Batch | [Task 22 / Job 22](http://localhost:8080/tasks/22/jobs/22), đúng 24 ảnh, chưa có annotation tại lúc chuẩn bị; chưa import pre-label |
| Ảnh local | `work/tasks/gold/`, `work/tasks/review/`; ZIP dự phòng trong `work/gold-manual-images.zip`, `work/batch-review-images.zip` |
| Notebook | `notebooks/day08_colab.ipynb` đã chuẩn bị, chưa chạy; có bước xác nhận hoàn tất gold và yêu cầu tự điền ngưỡng Part 3 |
| Dữ liệu và quy tắc | Giữ nguyên ảnh, split, attribution, taxonomy và label contract v1.0 |

Chi tiết task local: [cvat/local_tasks.json](cvat/local_tasks.json). Phiên bản thư viện đã cài: [requirements-local.lock.txt](requirements-local.lock.txt).

## 3. Sau khi gold đã được export

Máy có RAM 8 GB nên dùng Colab cho model và giữ CVAT/đo số trên máy local:

1. Mở [Google Colab](https://colab.research.google.com/), chọn **Upload notebook**, tải `notebooks/day08_colab.ipynb` trong repo này lên. Chọn Runtime → Change runtime type → T4 GPU nếu còn hạn mức.
2. Chạy lần lượt các ô setup. Mã nguồn model được ghim ở commit `e2e9a5d32d9d9238416f98ab6e6fad55ed653f66` của repo đề đã cung cấp. Không chạy các ô model trước khi hoàn tất gold.
3. Khi bắt đầu Part 2, notebook yêu cầu gõ `DA_EXPORT_GOLD_2A202603132`. Đây là xác nhận của học viên, không phải kiểm định chất lượng gold.
4. Quan sát kết quả từng model và tự ghi nhận xét vào `submission/model_log.csv`. Không chép số hoặc nhận xét chưa quan sát.
5. Sau khi chạy nguồn dự đoán, tải `colab_stage1.zip` về và giải nén vào thư mục repo. Chạy threshold sweep local, rồi dán chuỗi ngưỡng thực vào ô `THR` của notebook; không dùng ngưỡng ví dụ.
6. Tạo bẫy local bằng MSHV `2A202603132`, import **`pre_traps_import.coco.json`** vào task batch-review. Không mở đáp án bẫy trước khi export nhãn đã review.
7. Thực hiện SAM, calibration và QC theo [GUIDE.md](GUIDE.md); kết luận và quy tắc guideline do học viên tự quyết từ bằng chứng thực tế.

`requirements-local.lock.txt` ghi lại môi trường macOS arm64 trong phiên này; notebook Colab dùng dependencies riêng của notebook, không cài lock local lên Colab.

## 4. Trạng thái bài nộp và Git

- Repo public: https://github.com/trxuanbac/K5-L23-DAY08-2A202603132-TranXuanBac-AIPrelabel. Fork từ repo đề vào tài khoản `trxuanbac`, tên đúng mẫu; `origin` trỏ repo này, nhánh làm việc là `main`. Nội dung công bố là phần chuẩn bị Part 0, chưa phải bài hoàn thành.
- `upstream` trỏ repo đề bạn cung cấp. Không push bài vào upstream.
- Chưa có nhãn gold/batch, dòng log model/thời gian, mask, số đo QC hoặc quyết định chất lượng. Các chỗ chưa làm trong mẫu báo cáo được giữ nguyên.
- Lần chạy `check_submission.py` trong bước chuẩn bị báo **24 lỗi, 1 cảnh báo** do chưa có kết quả các Part và khi đó mới có lịch sử clone rút gọn. Log local: `work/logs/submission-preparation.txt`. Lịch sử Git đầy đủ đã được tải trước khi xuất bản; bài vẫn chưa đủ điều kiện nộp.
- Commit tiếp theo theo từng phần thực sự hoàn thành; không tạo commit rỗng để đủ số lượng.
- Khi hoàn tất, chạy lại `validate_labels.py --all` và `check_submission.py`, sửa hết lỗi trước khi nộp.

