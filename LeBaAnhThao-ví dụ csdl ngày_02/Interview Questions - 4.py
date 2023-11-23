def chuyen_thap_phan_sang_nhi_phan(n):
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * chuyen_thap_phan_sang_nhi_phan(n // 2)

# Nhập số từ người dùng
so_thap_phan = int(input("Nhập số thập phân: "))

# Gọi hàm chuyển đổi và in kết quả
so_nhi_phan = chuyen_thap_phan_sang_nhi_phan(so_thap_phan)
print(f"Số nhị phân tương ứng với {so_thap_phan} là: {so_nhi_phan}")
