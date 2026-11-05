# Lab 03 - Câu trả lời thảo luận

## 1. Merge base là gì?
- Merge base là điểm tổ tiên chung gần nhất (common ancestor commit) giữa hai nhánh Git trước khi chúng rẽ nhánh. Git sử dụng điểm này làm gốc để tính toán sự khác biệt và thực hiện gộp (merge/rebase) code.

## 2. Vì sao nhánh `master` và `release/*` bắt buộc phải dùng `revert` thay vì `reset`?
- `master` và `release/*` là các nhánh công khai / nhánh baseline đã được chia sẻ và đưa vào sử dụng chung. 
- Dùng `reset` sẽ làm thay đổi và xóa bỏ lịch sử commit chung (viết lại lịch sử - rewrite history), gây lệch lịch sử với máy của người khác và làm mất dấu vết kiểm toán (audit trail).
- Dùng `revert` tạo ra một commit mới hoàn toàn có tác dụng đảo ngược lại thay đổi cũ mà **không làm mất lịch sử cũ**, đảm bảo an toàn tuyệt đối cho các nhánh chính.
