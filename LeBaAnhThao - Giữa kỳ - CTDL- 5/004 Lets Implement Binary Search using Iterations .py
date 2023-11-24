def binarysearch_iterative(A, key):
    # Khởi tạo biến l và r để theo dõi phạm vi tìm kiếm trong danh sách A
    l = 0
    r = len(A) - 1
    
    # Sử dụng vòng lặp while cho đến khi phạm vi tìm kiếm hết
    while l <= r:
        # Tính toán giữa danh sách
        mid = (l + r) // 2
        
        # Kiểm tra giá trị tại vị trí giữa với giá trị cần tìm
        if key == A[mid]:
            return mid  # Trả về vị trí nếu tìm thấy giá trị
        
        elif key < A[mid]:
            r = mid - 1  # Giảm phạm vi tìm kiếm về bên trái
        
        elif key > A[mid]:
            l = mid + 1  # Tăng phạm vi tìm kiếm về bên phải
        
    return -1  # Trả về -1 nếu không tìm thấy giá trị

# Danh sách đã sắp xếp
A = [15, 21, 47, 84, 96]

# Gọi hàm binarysearch_iterative để tìm giá trị 84 trong danh sách A
found = binarysearch_iterative(A, 84)

# In kết quả
print('Result:', found)
