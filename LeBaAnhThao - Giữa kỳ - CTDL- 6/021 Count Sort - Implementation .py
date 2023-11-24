def countsort(A):
    # Hàm Counting Sort nhận một danh sách A.

    n = len(A)  # Số lượng phần tử trong danh sách
    maxsize = max(A)  # Tìm giá trị lớn nhất trong danh sách

    carray = [0] * (maxsize + 1)  # Tạo một mảng carray có kích thước maxsize + 1 để đếm số lần xuất hiện của mỗi giá trị

    for i in range(n):
        carray[A[i]] = carray[A[i]] + 1  # Đếm số lần xuất hiện của mỗi giá trị trong danh sách

    i = 0 # Biến i được sử dụng để duyệt qua các giá trị từ 0 đến maxsize.
    j = 0 # Biến j theo dõi vị trí của danh sách đã sắp xếp.

    while i < maxsize + 1:
        # Duyệt qua các giá trị từ 0 đến maxsize
        if carray[i] > 0:
            # Nếu có ít nhất một phần tử có giá trị i
            A[j] = i  # Đặt giá trị i vào danh sách A
            j = j + 1  # Tăng chỉ mục j
            carray[i] = carray[i] - 1  # Giảm số lần xuất hiện của giá trị i
        else:
            i = i + 1  # Nếu không, tăng i lên 1

A = [3, 5, 8, 9, 6, 2, 3, 5, 5]
print('Original Array:', A)

# Gọi hàm countsort để sắp xếp danh sách
countsort(A)

print('Sorted Array:', A)  # In danh sách sau khi sắp xếp
