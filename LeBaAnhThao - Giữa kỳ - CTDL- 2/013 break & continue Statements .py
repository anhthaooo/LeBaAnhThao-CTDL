# Tạo một danh sách chứa các số nguyên
L = [10, 54, 2, 61, 15]

# Nhập giá trị mà bạn muốn tìm trong danh sách từ người dùng
n = int(input('Nhập giá trị cần tìm: '))

# Lặp qua từng phần tử trong danh sách L
for i in L:
    # In ra giá trị của từng phần tử trong danh sách và giá trị n mà bạn muốn tìm
    print(i, n)
    
    # Kiểm tra nếu giá trị của phần tử hiện tại bằng giá trị n
    if i == n:
        # Nếu tìm thấy, in ra thông báo và dừng vòng lặp bằng lệnh break
        print('Đã tìm thấy')
        break
