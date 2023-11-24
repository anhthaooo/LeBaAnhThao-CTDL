def mergesort(A, left, right):
    # Kiểm tra điều kiện dừng của đệ quy: Nếu chỉ còn một phần tử hoặc không có phần tử nào để sắp xếp (left >= right), thoát.
    if left < right:
        mid = (left + right) // 2  # Tìm chỉ số giữa của mảng.
        mergesort(A, left, mid)     # Sắp xếp nửa đầu mảng từ left đến mid.
        mergesort(A, mid + 1, right)  # Sắp xếp nửa sau mảng từ mid+1 đến right.
        merge(A, left, mid, right)   # Kết hợp hai nửa đã sắp xếp lại với nhau.

def merge(A, left, mid, right):
    i = left           # Chỉ số bắt đầu của mảng con trái.
    j = mid + 1        # Chỉ số bắt đầu của mảng con phải.
    k = left           # Chỉ số bắt đầu của mảng kết quả.
    B = [0] * (right + 1)  # Tạo mảng B để lưu trữ mảng kết quả.

    # So sánh và kết hợp các phần tử của hai mảng con.
    while i <= mid and j <= right:
        if A[i] < A[j]:
            B[k] = A[i]  # Phần tử của mảng con trái nhỏ hơn, thêm vào mảng kết quả.
            i += 1
        else:
            B[k] = A[j]  # Phần tử của mảng con phải nhỏ hơn hoặc bằng, thêm vào mảng kết quả.
            j += 1
        k += 1

    # Sao chép các phần tử còn lại của mảng con trái (nếu còn).
    while i <= mid:
        B[k] = A[i]
        i += 1
        k += 1

    # Sao chép các phần tử còn lại của mảng con phải (nếu còn).
    while j <= right:
        B[k] = A[j]
        j += 1
        k += 1

    # Sao chép mảng kết quả B vào mảng ban đầu A từ left đến right.
    for x in range(left, right + 1):
        A[x] = B[x]

A = [5, 6, 8, 9, 6, 2]
print("Original Array", A)
mergesort(A, 0, len(A) - 1)  # Gọi hàm sắp xếp mảng.
print("Sorted Array ", A)   # In mảng đã sắp xếp.
