# Lab 01 - Câu trả lời thảo luận

## 1. Cấu hình --global được lưu ở đâu? Khác gì so với --local?

Cấu hình `--global` được lưu trong file `~/.gitconfig` (trên Windows là
`C:\Users\<tên>\.gitconfig`) và áp dụng cho mọi repo của người dùng hiện tại.
Cấu hình `--local` được lưu trong file `.git/config` của riêng repo đó và chỉ
có tác dụng với repo này. Khi cùng một khóa (ví dụ `user.email`) được đặt ở cả
hai nơi thì `--local` được ưu tiên. Lệnh `git config --list --show-origin` cho
biết mỗi giá trị đến từ file nào.

## 2. Vì sao dùng git mv?

`git mv` tương đương với đổi tên file rồi `git add` cho cả đường dẫn cũ lẫn đường
dẫn mới, nên thay đổi được đưa vào staging ngay trong một bước. Git không lưu
"đổi tên" như một thao tác riêng mà nhận ra đổi tên vì nội dung file giống nhau.
Nhờ vậy `git log --follow` vẫn theo dõi được lịch sử của `aims/cart.py` từ trước
khi chuyển, và trang Files changed của PR hiện `renamed` thay vì xóa rồi thêm file
mới, giúp người review dễ thấy chỉ có vị trí thay đổi.

## 3. release/lab01 có phải baseline không?

Có, theo nghĩa của quản lý cấu hình. Baseline là một phiên bản đã được thống
nhất và đóng lại, từ đó chỉ được thay đổi thông qua quy trình có kiểm soát.
Nhánh `release/lab01` được tạo từ `master` sau khi PR refactor đã được merge và
kiểm tra, và đây chính là phiên bản nộp bài. Mọi sửa đổi về sau phải đi qua quy
trình (PR, hotfix), không được commit trực tiếp. Ở Lab 04, phiên bản này còn được
gắn tag `v0.1.0` để định danh chính xác, vì tag không bao giờ di chuyển.

## 4. Vì sao không commit thẳng master dù làm một mình?

- Mỗi thay đổi đi qua nhánh riêng và Pull Request nên có mô tả mục đích, nội dung
  thay đổi và cách kiểm thử, giúp truy vết được thay đổi nào sinh ra vì lý do gì.
- `master` luôn ở trạng thái ổn định; việc đang làm dở nằm trên nhánh riêng và
  không làm hỏng `master`.
- Có thể tự xem lại toàn bộ thay đổi ở tab Files changed trước khi merge, và nếu
  cần có thể hoàn tác cả PR bằng một lệnh revert.
- Tập thói quen làm việc nhóm: khi có người cùng làm hoặc khi bật branch
  protection ở Lab 02, quy trình vẫn y nguyên.
