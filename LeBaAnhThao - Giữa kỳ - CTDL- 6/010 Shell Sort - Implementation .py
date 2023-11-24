def shellsort(A):
    # Định nghĩa hàm shellsort với đối số là danh sách A

    n = len(A)  # Lấy độ dài của danh sách
    gap = n // 2  # Khởi tạo khoảng cách ban đầu

    while gap > 0:  # Bắt đầu vòng lặp chính với khoảng cách giảm dần
        i = gap  # Bắt đầu từ vị trí cách gap phần tử

        while i < n:  # Lặp qua danh sách từ vị trí i đến cuối danh sách
            temp = A[i]  # Lưu trữ giá trị của phần tử hiện tại

            j = i - gap  # Bắt đầu tìm vị trí thích hợp trong danh sách con

            while j >= 0 and A[j] > temp:
                # Di chuyển phần tử lớn hơn giá trị hiện tại về phía sau khoảng cách gap
                A[j + gap] = A[j]
                j = j - gap

            A[j + gap] = temp  # Gán giá trị hiện tại vào vị trí thích hợp sau khi di chuyển
            i = i + 1  # Di chuyển đến phần tử tiếp theo

        gap = gap // 2  # Giảm khoảng cách

# Danh sách đầu vào
A = [3, 5, 8, 9, 6, 2]

# In danh sách ban đầu
print('Original Array:', A)

# Gọi hàm shellsort để sắp xếp danh sách
shellsort(A)

# In danh sách sau khi sắp xếp
print('Sorted Array:', A)
