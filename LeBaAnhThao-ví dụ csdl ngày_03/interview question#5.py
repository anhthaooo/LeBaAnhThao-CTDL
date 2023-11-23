def find_duplicates(arr):
    # Tạo một danh sách để lưu trữ các giá trị đã kiểm tra
    checked_values = []
    
    # Tạo một danh sách để lưu trữ các giá trị trùng lặp
    duplicates = []
    
    # Lặp qua từng phần tử trong mảng
    for num in arr:
        # Kiểm tra xem phần tử đã tồn tại trong danh sách đã kiểm tra hay chưa
        if num in checked_values:
            # Nếu đã tồn tại, thêm nó vào danh sách các giá trị trùng lặp
            if num not in duplicates:
                duplicates.append(num)
        else:
            # Nếu chưa tồn tại, thêm nó vào danh sách để kiểm tra tiếp
            checked_values.append(num)
    
    return duplicates

# Kiểm tra hàm với một ví dụ
arr = [1, 3, 3, 5]
result = find_duplicates(arr)
print(result)  
