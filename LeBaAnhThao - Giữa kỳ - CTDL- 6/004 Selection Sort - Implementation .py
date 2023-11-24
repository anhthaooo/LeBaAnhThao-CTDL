def selection_sort(A):
    # Hàm sắp xếp danh sách A bằng thuật toán Selection Sort
    
    # Độ dài của danh sách
    n = len(A)
    
    # Vòng lặp ngoài để duyệt từng phần tử
    for i in range(n - 1):
        # Gán i là vị trí hiện tại là phần tử nhỏ nhất
        
        # Vòng lặp bên trong để tìm phần tử nhỏ nhất trong phần còn lại
        position = i
        for j in range(i + 1, n):
            # So sánh phần tử tại vị trí j với phần tử nhỏ nhất hiện tại
            if A[j] < A[position]:
                # Nếu phần tử tại vị trí j nhỏ hơn, cập nhật vị trí của phần tử nhỏ nhất
                position = j
        
        # Hoán đổi phần tử nhỏ nhất với phần tử hiện tại (tại vị trí i)
        temp = A[i]        # Lưu trữ giá trị của phần tử hiện tại vào biến tạm thời temp
        A[i] = A[position]  # Gán giá trị của phần tử nhỏ nhất vào vị trí hiện tại
        A[position] = temp  # Gán giá trị ban đầu của phần tử hiện tại vào vị trí của phần tử nhỏ nhất


# Danh sách đầu vào
A = [3, 5, 8, 9, 6, 2]

# In danh sách ban đầu
print('Original Array:', A)

# Gọi hàm selection_sort để sắp xếp danh sách
selection_sort(A)

# In danh sách sau khi sắp xếp
print('Sorted Array:', A)
