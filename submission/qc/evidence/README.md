# Ảnh đối chiếu QC và calibration

Các ảnh ở đây là crop từ ảnh gốc, phóng 3 lần để xem chi tiết. Ảnh gốc trong `data/images/` không thay đổi. Nguồn và giấy phép giữ tại [ATTRIBUTION.csv](../../../data/ATTRIBUTION.csv).

| File | Ảnh gốc và vùng crop `(x1,y1,x2,y2)` | Nội dung đối chiếu |
|---|---|---|
| 003-background.jpg | img_003, `(35,157,147,245)` | Xe có cabin ở nền bị gán three_wheeler, gồm box #12 và #13 của bản ứng viên. |
| 003-parked-bike.jpg | img_003, `(650,230,825,370)` | Xe hai bánh đỗ bên phải bị gán three_wheeler #14; cùng vùng có box motorbike #19. |
| 006-people.jpg | img_006, `(810,420,1024,682)` | Người ngồi bên phải, gồm trẻ áo xanh bị box #69 cắt và người quay lưng áo họa tiết chưa có box. |
| 031-basket.jpg | img_031, `(125,318,513,540)` | Giỏ/khung hàng gắn với xe đạp bị box #419 cắt ở mép trái. |
| 035-distant-bike.jpg | img_035, `(898,423,980,500)` | Xe máy màu sáng ở xa chưa có box trong bản ứng viên đang kiểm. |

ID box tham chiếu `submission/release/final_det.coco.json` tại thời điểm tạo phiếu QC; checksum nguồn nằm ở `../qc_review_provenance.json`. Các ảnh dùng để đối chiếu khi kiểm nhãn.
