# Định nghĩa hàm tìm kiếm tuyến tính
def linear_search(arr, target):
    """
    Tìm kiếm tuyến tính trong danh sách arr để tìm giá trị target.
    
    Parameters:
    - arr: Danh sách cần tìm kiếm.
    - target: Giá trị cần tìm.
    
    Returns:
    - Nếu tìm thấy, trả về vị trí của giá trị target.
    - Nếu không tìm thấy, trả về -1.
    """
    # Duyệt qua từng phần tử trong danh sách
    for i in range(len(arr)):
        # Kiểm tra nếu giá trị của phần tử hiện tại bằng với giá trị cần tìm
        if arr[i] == target:
            return i  # Trả về vị trí của giá trị nếu tìm thấy
    
    return -1  # Trả về -1 nếu không tìm thấy

# Ví dụ sử dụng
my_list = [4, 2, 8, 1, 7, 3, 9, 5]  # Danh sách để tìm kiếm
target_value = 7  # Giá trị cần tìm kiếm

# Gọi hàm tìm kiếm tuyến tính
result = linear_search(my_list, target_value)

# Kiểm tra và in kết quả
if result != -1:
    print(f"Giá trị {target_value} được tìm thấy tại vị trí {result}.")
else:
    print(f"Giá trị {target_value} không có trong danh sách.")
