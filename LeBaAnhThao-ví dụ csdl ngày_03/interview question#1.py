def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        # Hoán đổi phần tử tại vị trí start và end
        arr[start], arr[end] = arr[end], arr[start]

        # Di chuyển con trỏ
        start += 1
        end -= 1

# Kiểm tra hàm với một mảng
arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print(arr)  
