def quicksort(A, low, high):
    # Hàm quicksort nhận một danh sách A, và khoảng giới hạn từ low đến high.

    if low < high:
        # Kiểm tra điều kiện dừng của đệ quy (khi low < high)
        pi = partition(A, low, high)  # Tìm phần tử pivot và chia danh sách thành hai nửa

        # Gọi quicksort đệ quy cho nửa bên trái và nửa bên phải của pivot
        quicksort(A, low, pi - 1)
        quicksort(A, pi + 1, high)

def partition(A, low, high):
    # Hàm partition nhận danh sách A, và khoảng giới hạn từ low đến high.

    pivot = A[low]  # Chọn phần tử pivot, thường là phần tử đầu tiên
    i = low + 1
    j = high

    while True:
        while i <= j and A[i] <= pivot:
            i = i + 1  # Di chuyển i sang phải để tìm phần tử lớn hơn pivot
        while i <= j and A[j] > pivot:
            j = j - 1  # Di chuyển j sang trái để tìm phần tử nhỏ hơn hoặc bằng pivot
        if i <= j:
            # Nếu i và j gặp nhau, đổi chỗ hai phần tử
            A[i], A[j] = A[j], A[i]
        else:
            break  # Khi i > j, thoát khỏi vòng lặp

    # Đổi chỗ pivot với phần tử A[j]
    A[low], A[j] = A[j], A[low]

    return j  # Trả về chỉ mục của pivot sau khi đã sắp xếp

A = [3, 5, 8, 9, 6, 2]
print('Original Array:', A)

# Gọi hàm quicksort để sắp xếp danh sách
quicksort(A, 0, len(A) - 1)

print('Sorted Array:', A)  # In danh sách sau khi sắp xếp
