# Lab 02 - Câu trả lời thảo luận

## 1. Vì sao phải đồng bộ master trước khi gửi Pull Request?
- Trong quá trình phát triển song song, nhánh master có thể đã nhận thêm các commit mới từ những PR khác (ví dụ: PR feature/cart-print đã được merge trước khi feature/search-by-title hoàn tất).
- Việc đồng bộ (git fetch origin và git merge origin/master) vào nhánh tính năng trước khi gửi PR giúp:
  - Phát hiện và giải quyết sớm các xung đột (merge conflicts) ngay trên nhánh cá nhân thay vì để kẹt trên PR.
  - Kiểm thử tích hợp (chạy lại chương trình/test) để đảm bảo mã của nhánh mình hoạt động đúng khi kết hợp với các thay đổi mới nhất trên master.
  - Đảm bảo nguyên tắc SCM: phiên bản được đem ra review và kiểm thử trên PR phản ánh sát nhất kết quả sau khi tích hợp vào master.

## 2. Khi nào không được dùng rebase?
- Quy tắc vàng: Không bao giờ dùng git rebase trên các nhánh công khai/dùng chung (như master, release/*) hoặc trên các commit đã được chia sẻ (push) mà có người khác đang cùng làm việc dựa trên các commit đó.
- Lý do: rebase viết lại lịch sử bằng cách tạo ra các commit mới với mã băm (SHA) mới. Nếu rebase các commit đã chia sẻ cho người khác, lịch sử giữa máy các thành viên sẽ bị lệch nhau, buộc phải push --force và dễ dẫn đến mất commit của đồng đội hoặc tạo ra các commit trùng lặp khi merge lại.

## 3. Nhánh feature/* khác nhánh topic/* ra sao?
- feature/<tên>: Dùng để phát triển các tính năng nghiệp vụ mới của sản phẩm phần mềm, trực tiếp bổ sung hành vi hoặc chức năng cho người dùng (ví dụ: feature/cart-print, feature/search-by-title).
- topic/<mô-tả>: Dùng cho các công việc theo chủ đề hỗ trợ dự án nhưng không phải là tính năng nghiệp vụ trong mã nguồn sản phẩm, chẳng hạn như thêm tài liệu, sơ đồ thiết kế, biểu mẫu cấu hình kho chứa, hoặc thiết lập CI (ví dụ: topic/pr-template, topic/use-case-diagram, topic/ci-unit-tests).
