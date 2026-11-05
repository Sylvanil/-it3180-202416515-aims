# Lab 04 - Câu trả lời thảo luận

## 1. Vì sao chuẩn bị phát hành trên `master` trước mà không sửa trực tiếp trên nhánh `release/*`?
- Nhánh `release/*` đóng vai trò là dòng đóng băng baseline (chỉ dành riêng cho việc kiểm thử chốt phiên bản và vá lỗi khẩn cấp - hotfix)[cite: 46, 48]. Mọi tính năng hay chuẩn bị cấu hình, cập nhật version/changelog phải được tích hợp qua quy trình chuẩn trên `master` trước khi tạo nhánh release để đảm bảo tính nhất quán của mã nguồn phát triển[cite: 47].

## 2. Vì sao lên phiên bản `1.0.0` mà không phải `0.4.0`?
- Theo chuẩn định danh SemVer (Semantic Versioning), phiên bản `1.0.0` đánh dấu mốc sản phẩm phần mềm chính thức đạt độ ổn định, hoàn thành các tính năng cốt lõi và sẵn sàng bàn giao cho người dùng sử dụng thực tế (release baseline)[cite: 46].
