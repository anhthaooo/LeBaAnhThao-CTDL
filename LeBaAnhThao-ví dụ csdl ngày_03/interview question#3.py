def are_lists_equivalent(list1, list2):
    # Sắp xếp cả hai danh sách
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    
    # So sánh danh sách đã sắp xếp
    return sorted_list1 == sorted_list2

# Kiểm tra hàm với ví dụ
list1 = [1, 2, 3]
list2 = [3, 2, 1]

if are_lists_equivalent(list1, list2):
    print("Hai danh sách tương đương.")
else:
    print("Hai danh sách không tương đương.")
