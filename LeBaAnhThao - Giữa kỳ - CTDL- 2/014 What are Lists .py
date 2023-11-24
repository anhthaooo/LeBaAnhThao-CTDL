# Tạo một danh sách gồm các số nguyên
numbers = [1, 2, 3, 4, 5]

# Thêm một số mới vào danh sách
numbers.append(6)

# Truy cập và in ra phần tử đầu tiên trong danh sách
first_number = numbers[0]
print("First number:", first_number)

# Sắp xếp danh sách theo thứ tự giảm dần
numbers.sort(reverse=True)

# In danh sách đã sắp xếp
print("Sorted numbers:", numbers)

# Xóa phần tử thứ hai trong danh sách
removed_number = numbers.pop(1)
print("Removed number:", removed_number)

# Kiểm tra xem số 3 có tồn tại trong danh sách không
is_three_in_list = 3 in numbers
print("Is 3 in the list?", is_three_in_list)

# Tạo một danh sách chứa các loại hoa quả
fruits = [" táo ", "chuối", "cherry"]

# Kết hợp danh sách số và danh sách hoa quả vào một danh sách lớn
mixed_list = numbers + fruits

# In danh sách kết hợp
print("Mixed list:", mixed_list)

# In chiều dài của danh sách kết hợp
mixed_list_length = len(mixed_list)
print("Length of mixed list:", mixed_list_length)
