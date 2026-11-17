# Sửa bổ sung sau lượt review đầu

Đây là bản 490 annotation trước vòng sửa QC. Bản mới nhất 492 annotation nằm tại [qc-02](../qc-02/README.md); hồ sơ và số đo trong thư mục này được giữ nguyên để đối chiếu.

Đã đối chiếu ảnh gốc và lưu các sửa đổi trong CVAT job 23. Bản hiện tại có **24 ảnh/490 annotation**, xuất tại [corrected.coco.json](corrected.coco.json). Bản sửa cho 10 ảnh nằm trong `submission/labels/qc_fixed.json`; các ảnh còn lại dùng bản review đầu khi chạy `build_release.py`.

## Thay đổi

| Ảnh | Sửa đổi |
|---|---|
| img_006.jpg | Giữ nhãn `car` học viên vừa sửa cho ô tô trắng phía cuối đường. |
| img_013.jpg | Thêm box `person` cho người mặc áo trắng đứng phía sau tuk-tuk. |
| img_021.jpg | Chỉnh box xe máy ở giữa ảnh để ôm sát phần xe nhìn thấy. |
| img_024.jpg | Chỉnh box ô tô tối màu ở giữa giao lộ. |
| img_034.jpg | Thêm box xe máy phía xa; bỏ 1 box khác cao dưới 20 px. |
| img_035.jpg | Xóa box `truck` ở vùng biển hiệu/dây điện; giữ nguyên box xe máy học viên đã xóa trước đó. |
| img_018.jpg | Bỏ 5 box cao dưới 20 px. |
| img_025.jpg | Bỏ 1 box cao dưới 20 px. |
| img_027.jpg | Bỏ 2 box cao dưới 20 px. |
| img_033.jpg | Bỏ 1 box cao dưới 20 px. |

Ngay trước khi áp dụng có 499 annotation. Đợt sửa áp dụng 2 lần chỉnh tọa độ, thêm 2 box và xóa 11 box; sau đó có 490 annotation. Đã kiểm tra **486 annotation ngoài phạm vi sửa không thay đổi**. Xem [change_log.json](change_log.json), [export_summary.json](export_summary.json).

## Kiểm tra sau sửa

- `validate_labels.py` kiểm bản export 24 ảnh và `qc_fixed.json`: không lỗi, không còn cảnh báo kích thước dưới 20 px.
- Script đối chiếu bẫy ghi **12/12** sau sửa: [kết quả kiểm sau sửa](review_stats_after_corrections.md).
- Đây là kết quả sửa bổ sung **sau khi đã biết các bẫy**, không phải kết quả review mù ban đầu.
- Bản review đầu vẫn giữ nguyên: 24 ảnh/500 annotation, **6/12 bẫy**, 30 phút; xem `../batch-01/`. Không thay số đo đầu bằng kết quả 12/12 sau sửa.
- Không thêm thời gian gán tay cho đợt sửa này khi học viên chưa cung cấp.

## Bản ứng viên và QC còn lại

Đã chạy `build_release.py`: `submission/release/final_det.coco.json` có 24 ảnh/490 annotation và khớp nhãn/tọa độ với bản CVAT đã sửa. Đây là **bản ứng viên**, chưa có quyết định Release.

Đã tạo mẫu QC 5 ảnh ngẫu nhiên, seed 42, tổng 98 đối tượng, tại `submission/qc/qc_sample.csv`; phiếu `qc_review.csv` chưa được điền. Ảnh có ID để kiểm ở `work/qc/review/`. Calibration, mask SAM cho 3 vật và QC hình ảnh vẫn cần hoàn tất.
