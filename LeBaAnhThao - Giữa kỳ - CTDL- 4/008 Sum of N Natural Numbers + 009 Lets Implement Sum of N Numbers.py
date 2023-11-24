# Định nghĩa hàm sum_of_natural_numbers với tham số N
def sum_of_natural_numbers(N):
    total = 0  # Khởi tạo biến total để lưu tổng
    for i in range(1, N + 1):  # Duyệt qua các số từ 1 đến N
        total += i  # Cộng giá trị i vào tổng
    return total  # Trả về tổng

N = 5  # Ví dụ, tính tổng của 5 số tự nhiên đầu tiên
result = sum_of_natural_numbers(N)  # Gọi hàm để tính tổng
print(f"Tổng của {N} số tự nhiên đầu tiên là {result}")  # In kết quả ra màn hình
