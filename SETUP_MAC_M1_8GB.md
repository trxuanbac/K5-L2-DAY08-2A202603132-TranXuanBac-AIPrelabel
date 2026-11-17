# Cài đặt đã kiểm tra — Mac M1, RAM 8 GB

Kiểm tra ngày 2026-11-17 trên Apple M1, macOS 26.3, arm64. Đối chiếu với phần hướng dẫn Mac 8 GB học viên đã cung cấp từ trang Claude.

## Chế độ theo hướng dẫn: Colab + CVAT local

Máy 8 GB dùng Colab để chạy model; máy local chạy CVAT và các script kiểm nhãn/đo số. Đã tạo `.venv` bằng **Python 3.12.16 ARM64**, cài numpy, pillow, opencv-python-headless, matplotlib và pyyaml. Môi trường này không cài PyTorch.

Python 3.12 được cài riêng trong `work/python-managed` bằng uv từ [Python Build Standalone của Astral](https://github.com/astral-sh/python-build-standalone). Máy chưa có Homebrew; cách cài này cung cấp Python 3.12 cho repo mà không thay Python hệ thống. Command Line Tools và Git đã có sẵn.

Chạy trong Terminal:

```bash
cd /Users/chuoi/tool/K5-L23-DAY08-2A202603132-TranXuanBac-AIPrelabel
source .venv/bin/activate
python --version
python day08_setup.py check --light
```

Đã kiểm tra: Python 3.12.16, các thư viện nhẹ và CVAT đều `[ OK ]`; kết thúc bằng **SẴN SÀNG cho buổi học.** Xem [log thực tế](docs/setup_checks/mac_m1_8gb_light.txt).

## Model local đã có sẵn

| File trong `models/` | Dung lượng MB | Xác minh |
|---|---:|---|
| yolo26n.pt | 5,5 | Có; checksum đúng; chạy detector được |
| yoloe-26s-seg.pt | 31,1 | Có; checksum đúng; chạy text prompt được |
| mobileclip2_b.ts | 253,8 | Có; checksum đúng; YOLOE nạp encoder được |
| mobile_sam.pt | 40,7 | Có; checksum đúng; tạo mask được |
| sam2.1_t.pt | 78,1 | Có; checksum đúng; tạo mask được |

Tổng khoảng 409,2 MB. Cấu hình Colab không yêu cầu tải các file này về máy, nhưng bộ local đã có sẵn làm dự phòng. [Kết quả kiểm checksum](docs/setup_checks/model_assets.json).

Môi trường model ở `work/model-env`, Python 3.13.17, PyTorch 2.15.0, Ultralytics 8.4.215, CLIP 1.0 và timm 1.0.31. Đã bổ sung timm để MobileSAM chạy được. Checker trong repo hỗ trợ Python 3.13 cho môi trường này; `.venv` chuẩn bị theo trang web dùng Python 3.12.

Khi cần kiểm tra model local:

```bash
source work/model-env/bin/activate
python day08_setup.py check
```

Đã chạy thử tuần tự bằng CPU trên ảnh mẫu có sẵn:

- YOLO26 nano: 5 box.
- YOLOE với prompt `bus`, `person`: 5 box.
- MobileSAM: mask 260.872 px.
- SAM 2.1 tiny: mask 262.278 px trong lượt kiểm tra bổ sung.

[Log model local](docs/setup_checks/mac_m1_local_models.txt) · [Kết quả SAM 2.1](docs/setup_checks/sam2_1_tiny.json). Đây là kiểm tra chạy được, không phải đánh giá độ chính xác của model.

## Docker và CVAT

Docker 29.1.3, Docker Compose 5.0.1 đã có sẵn. CVAT đang chạy ở http://localhost:8080, phiên bản **2.82.1**; trang hướng dẫn minh họa 2.81.0. Đã giữ nguyên CVAT và các job hiện có.

Docker VM hiện có khoảng 4,11 GB RAM; hướng dẫn gợi ý khoảng 5 GB. CVAT đã phản hồi đạt trong cả kiểm tra nhẹ và kiểm tra model local. Chưa thay đổi tài nguyên hoặc khởi động lại Docker trong lần kiểm tra này.

## Trạng thái Colab và cách tiếp tục

Đã mở [notebook Colab của bài](https://colab.research.google.com/github/trxuanbac/K5-L23-DAY08-2A202603132-TranXuanBac-AIPrelabel/blob/main/notebooks/day08_colab.ipynb). Trong Colab, chọn **Runtime → Change runtime type → T4 GPU → Save**, rồi chạy:

```python
!nvidia-smi -L
```

Học viên đã thử kết nối và nhận thông báo **phần phụ trợ không có sẵn**. Chưa có lượt chạy Colab hoặc GPU T4 để ghi nhận; không đánh dấu bước này hoàn thành. Hiện dùng kết quả local CPU đã có, xem [bốn lượt tour và ảnh so sánh](submission/qc/model_tour/README.md).

Khi chạy model local, kích hoạt `work/model-env`; khi chạy script đo số/QC, kích hoạt `.venv`. Kết quả local được ghi đúng thiết bị `cpu`.

[Bản kiểm tra tổng hợp](docs/setup_checks/setup_audit.json). Trọng số, Python cài riêng và môi trường ảo nằm ngoài các file được commit.
