# Định nghĩa hàm calculate_itr với tham số n
def calculate_itr(n):
    # Bắt đầu một vòng lặp while, với điều kiện n > 0
    while n > 0:
        # Tính bình phương của n và lưu vào biến k
        k = n ** 2

        # In giá trị k ra màn hình
        print(k)

        # Giảm giá trị của n đi 1 để chuẩn bị cho vòng lặp tiếp theo
        n = n - 1

# Gọi hàm calculate_itr với đối số 4
calculate_itr(4)
