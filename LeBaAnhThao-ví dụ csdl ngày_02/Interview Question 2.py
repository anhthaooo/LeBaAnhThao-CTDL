def tinh_luy_thua(x, n):
    # Trường hợp cơ bản: n = 0, lũy thừa bằng 1
    if n == 0:
        return 1
    # Trường hợp đệ quy: xn = x * xn-1
    else:
        return x ** n

# Nhập số cơ số và số mũ từ người dùng
x = float(input("Nhập số cơ số (x): "))
n = float(input("Nhập số mũ (n): "))

# Gọi hàm để tính lũy thừa và in kết quả
ket_qua = tinh_luy_thua(x, n)
print(f"{x}^{n} = {ket_qua}")
