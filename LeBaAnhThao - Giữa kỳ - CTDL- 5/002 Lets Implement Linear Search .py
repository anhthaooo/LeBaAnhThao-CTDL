# Định nghĩa hàm tìm kiếm tuyến tính
def linearsearch(A,key):
    # Khởi tạo chỉ số ban đầu là 0
    index = 0
    # Lặp qua từng phần tử trong danh sách A
    while index < len(A):
        # Nếu phần tử tại vị trí index bằng với key
        if A[index] == key:
            # Trả về chỉ số index
            return index 
        # Tăng index lên 1
        index = index + 1 
    # Nếu không tìm thấy key trong danh sách, trả về -1
    return -1

# Khởi tạo danh sách A
A = [84,21,47,96,15]
# Gọi hàm tìm kiếm tuyến tính với danh sách A và key là 21
found = linearsearch(A,21)
# In kết quả ra màn hình
print('Result:',found)
