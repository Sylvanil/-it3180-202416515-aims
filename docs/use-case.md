# Sơ đồ và Đặc tả Use Case - AIMS-mini

## 1. Tác nhân (Actor)
- **Customer (Khách hàng / Người dùng):** Người sử dụng ứng dụng AIMS-mini để tìm kiếm đĩa DVD và quản lý giỏ hàng.

## 2. Sơ đồ Use Case (Text Diagram)
[Customer] ---> (UC1: Thêm DVD vào giỏ hàng - Cart.add_dvd)
[Customer] ---> (UC2: Xem chi tiết giỏ hàng - Cart.print_cart)
[Customer] ---> (UC3: Tính tổng chi phí - Cart.total_cost)
[Customer] ---> (UC4: Tìm kiếm DVD theo tiêu đề - search_by_title)

## 3. Mô tả ngắn các Use Case chính
1. **Thêm DVD vào giỏ hàng (`Cart.add_dvd`):** Cho phép người dùng thêm một đĩa `DigitalVideoDisc` vào giỏ hàng hiện tại (tối đa 20 đĩa).
2. **Xem chi tiết giỏ hàng (`Cart.print_cart`):** Hiển thị danh sách các đĩa DVD đang có trong giỏ kèm số thứ tự, tiêu đề, thể loại, giá tiền và tổng chi phí. Nếu giỏ trống, thông báo "The cart is empty".
3. **Tính tổng chi phí (`Cart.total_cost`):** Tính và trả về tổng giá tiền của toàn bộ các đĩa DVD trong giỏ hàng.
4. **Tìm kiếm DVD theo tiêu đề (`search_by_title`):** Lọc và trả về danh sách các đĩa DVD có tiêu đề chứa từ khóa do người dùng nhập vào.
