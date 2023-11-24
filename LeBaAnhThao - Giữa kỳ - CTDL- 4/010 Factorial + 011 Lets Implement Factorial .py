# Tính giai thừa bằng phương pháp đệ quy
def factorial_recursive(n):
    if n == 0:  # Trường hợp cơ sở: nếu n bằng 0
        return 1  # Trả về 1 (0! = 1)
    else:
        return n * factorial_recursive(n - 1)  # Sử dụng đệ quy để tính giai thừa

# Tính giai thừa bằng phương pháp vòng lặp
def factorial_iterative(n):
    result = 1  # Khởi tạo biến result để lưu kết quả
    for i in range(1, n + 1):  # Duyệt qua các số từ 1 đến n
        result *= i  # Nhân i vào kết quả (tích tụ giai thừa)
    return result  # Trả về kết quả giai thừa

# Số nguyên cần tính giai thừa
n = int(input("Nhập một số nguyên n: "))  # Nhập số nguyên từ người dùng và chuyển sang kiểu int

# Tính giai thừa sử dụng cả hai phương pháp
result_recursive = factorial_recursive(n)  # Tính giai thừa bằng phương pháp đệ quy
result_iterative = factorial_iterative(n)  # Tính giai thừa bằng phương pháp vòng lặp

# In kết quả
print(f"Giai thừa của {n} là {result_recursive} (đệ quy)")  # In kết quả giai thừa bằng đệ quy
print(f"Giai thừa của {n} là {result_iterative} (vòng lặp)")  # In kết quả giai thừa bằng vòng lặp
