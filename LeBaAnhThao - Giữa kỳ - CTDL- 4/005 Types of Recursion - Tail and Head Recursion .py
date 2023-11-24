# Định nghĩa hàm calculate với tham số n
def calculate(n):
    # Kiểm tra nếu n > 0 (điều kiện dừng của đệ quy)
    if n > 0:
        # Gọi đệ quy bằng cách giảm giá trị của n đi 1
        calculate(n - 1)
        
        # Tính bình phương của n và lưu vào biến k
        k = n ** 2

        # In giá trị k ra màn hình
        print(k)
        calculate(n - 1)

# Gọi hàm calculate với đối số 4
calculate(4)
