def tim_ucln(a, b):
    if b == 0:
        return a
    else:
        return tim_ucln(b, a % b)

# Nhập hai số từ người dùng
so1 = int(input("Nhập số thứ nhất: "))
so2 = int(input("Nhập số thứ hai: "))

# Gọi hàm tìm ước chung lớn nhất và in kết quả
ucln = tim_ucln(so1, so2)
print(f"Ước chung lớn nhất của {so1} và {so2} là: {ucln}")
