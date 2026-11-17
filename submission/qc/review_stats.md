# Số đo review (det)

- Ảnh tính: 24 (batch,gold); box máy: 520; đối tượng sau duyệt: 489; ngưỡng accepted: IoU >= 0.9
- Đã **loại 23 đối tượng nằm quanh các bẫy** khỏi bảng này: lỗi nhân tạo không phản ánh chất lượng máy.

## 1. Bốn trạng thái (AI error profile)
| Trạng thái | Số | Tỉ lệ | Mẫu số |
|---|---|---|---|
| accepted (giữ nguyên) | 467 | 467/520 = 89.8% | 520 box máy |
| edited (sửa) | 10 | 10/520 = 1.9% | 520 box máy |
| deleted (xoá) | 43 | 43/520 = 8.3% | 520 box máy |
| added (vẽ thêm) | 12 | 12/489 = 2.5% | 489 đối tượng sau duyệt |

Trong số deleted + added, **4 trường hợp là đổi lớp** (máy gán sai lớp, box đúng chỗ): đó không phải máy bỏ sót. Số vật máy **sót thật** ≈ added − đổi lớp = 8.

### Theo lớp
| Lớp | accepted | edited | deleted | added |
|---|---|---|---|---|
| person | 261 | 0 | 10 | 1 |
| bicycle | 5 | 0 | 2 | 1 |
| motorbike | 133 | 3 | 2 | 4 |
| car | 45 | 0 | 7 | 1 |
| bus | 3 | 0 | 0 | 1 |
| truck | 4 | 0 | 2 | 1 |
| three_wheeler | 16 | 7 | 20 | 3 |

## 2. So với gold (nhãn gán tay từ đầu)
Ảnh gold: 4; đối tượng gold: 75 (mẫu số của recall)
| | TP | FP | FN | Precision | Recall |
|---|---|---|---|---|---|
| Máy (pre-label) | 47 | 25 | 28 | 65.3% (KTC 95%: 54–75%) | 62.7% (KTC 95%: 51–73%) |

*Lạc quan: ngưỡng được chọn trên chính các ảnh gold này (in-sample), và chỉ có 4 ảnh. Đọc khoảng tin cậy, đừng đọc con số đơn.*


(Ảnh gold không nằm trong nhãn sau duyệt: không tính residual / new error. Đó là chủ ý: duyệt lại ảnh bạn vừa tự gán tay sẽ đo trí nhớ, không đo thiên kiến.)

## 3. Ảnh bẫy
- Bắt được 6/12 = 50.0% (KTC 95%: 25–75%) (ngưỡng đạt: 80%). Chỉ 12 bẫy nên khoảng tin cậy rất rộng: đọc cùng danh sách bẫy lọt, đừng kết luận chỉ từ %.
  - loose: 1/3
  - missing: 1/3
  - wrong_class: 2/3
  - extra: 2/3
  - lọt: img_013.jpg (missing), img_021.jpg (loose), img_024.jpg (loose), img_035.jpg (extra), img_006.jpg (wrong_class), img_034.jpg (missing)

## Gợi ý đọc số
- `deleted` cao → ngưỡng thấp hoặc ánh xạ nhãn sai; `added` cao → máy bỏ sót (xem lớp nào);
- `accepted` thấp (< 50%) → sửa mỗi box lâu hơn vẽ mới: đổi model/ngưỡng hoặc vẽ tay;
- bắt bẫy < 80% → duyệt lại lô, siết checklist (quét ảnh TRƯỚC khi nhìn nhãn máy).
