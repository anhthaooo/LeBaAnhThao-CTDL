def binarysearch_recursive(A, key, l, r):
    # Nếu biến bắt đầu (l) vượt qua biến kết thúc (r), không tìm thấy giá trị. Điều kiện dừng của đệ quy.
    if l > r:
        return -1
    else:
        mid = (l + r) // 2  # Tính giữa danh sách
        if key == A[mid]:
            return mid  # Trả về vị trí nếu tìm thấy giá trị
        elif key < A[mid]:
            # Nếu giá trị cần tìm nhỏ hơn giá trị tại vị trí giữa, thực hiện đệ quy trên phạm vi bên trái của danh sách.
            return binarysearch_recursive(A, key, l, mid - 1)
        elif key > A[mid]:
            # Nếu giá trị cần tìm lớn hơn giá trị tại vị trí giữa, thực hiện đệ quy trên phạm vi bên phải của danh sách.
            return binarysearch_recursive(A, key, mid + 1, r)

# Danh sách đã sắp xếp
A = [15, 21, 47, 84, 96]

# Gọi hàm binarysearch_recursive để tìm giá trị 84 trong danh sách A từ vị trí 0 đến 4
found = binarysearch_recursive(A, 84, 0, 4)

# In kết quả
print('Result:', found)
