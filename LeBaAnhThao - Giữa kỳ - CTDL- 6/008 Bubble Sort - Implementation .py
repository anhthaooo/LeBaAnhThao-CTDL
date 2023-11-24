def bubblesort(A):
    # Định nghĩa hàm bubblesort với đối số là danh sách A

    n = len(A)  # Lấy độ dài của danh sách
    for passes in range(n - 1, 0, -1):
        # Vòng lặp ngoài để điều chỉnh vị trí cuối cùng sau mỗi lượt lặp
        for i in range(passes):
            # Vòng lặp bên trong để so sánh và đổi chỗ các phần tử

            if A[i] > A[i + 1]:
                # So sánh phần tử hiện tại với phần tử kế bên
                # Nếu phần tử hiện tại lớn hơn phần tử kế bên, đổi chỗ chúng

                temp = A[i]     # Sử dụng biến tạm thời để lưu trữ giá trị của phần tử hiện tại
                A[i] = A[i + 1]  # Gán phần tử kế bên vào vị trí hiện tại
                A[i + 1] = temp  # Gán giá trị từ biến tạm thời vào vị trí kế bên

# Danh sách đầu vào
A = [3, 5, 8, 9, 6, 2]

# In danh sách ban đầu
print('Original Array:', A)

# Gọi hàm bubblesort để sắp xếp danh sách
bubblesort(A)

# In danh sách sau khi sắp xếp
print('Sorted Array:', A)
