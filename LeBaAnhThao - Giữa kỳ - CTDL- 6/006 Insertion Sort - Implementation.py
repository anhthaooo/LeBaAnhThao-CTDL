def insertionsort(A):
    # Định nghĩa hàm sắp xếp chèn với đối số là danh sách A

    n = len(A)  # Lấy độ dài của danh sách
    for i in range(1, n):
        # Lặp qua từng phần tử của danh sách, bắt đầu từ phần tử thứ 2 (index 1)
        
        cvalue = A[i]  # Lưu trữ giá trị của phần tử hiện tại
        position = i  # Lưu trữ vị trí của phần tử hiện tại

        # Sử dụng vòng lặp while để so sánh và dịch chỗ các phần tử để tìm vị trí thích hợp
        while position > 0 and A[position - 1] > cvalue:
            # Kiểm tra nếu phần tử tại vị trí trước đó (position - 1) lớn hơn giá trị hiện tại (cvalue)
            
            A[position] = A[position - 1]  # Di chuyển phần tử trước đó lên một vị trí
            position = position - 1  # Di chuyển vị trí hiện tại lên một vị trí

        # Khi vòng lặp while kết thúc, vị trí 'position' là vị trí thích hợp cho giá trị hiện tại (cvalue)
        A[position] = cvalue  # Gán giá trị hiện tại vào vị trí thích hợp
        
# Danh sách đầu vào
A = [3, 5, 8, 9, 6, 2]

# In danh sách ban đầu
print('Original Array:', A)

# Gọi hàm insertionsort để sắp xếp danh sách
insertionsort(A)

# In danh sách sau khi sắp xếp
print('Sorted Array:', A)
