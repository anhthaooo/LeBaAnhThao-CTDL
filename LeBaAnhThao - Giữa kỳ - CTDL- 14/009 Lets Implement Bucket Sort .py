# Định nghĩa hàm sắp xếp chèn
def insertionsort(A):
    # Thuật toán Insertion Sort để sắp xếp một danh sách
    n = len(A)
    for i in range(1, n):
        cvalue = A[i]
        position = i 
        while position > 0 and A[position - 1] > cvalue:
            # Di chuyển các phần tử lớn hơn giá trị hiện tại về phía sau
            A[position] = A[position - 1]
            position = position - 1 
        # Đặt giá trị hiện tại vào đúng vị trí đã sắp xếp
        A[position] = cvalue

# Định nghĩa hàm sắp xếp theo bucket
def bucketsort(A):
    # Lấy số phần tử trong mảng
    n = len(A)
    # Tìm giá trị lớn nhất trong mảng
    maxelement = max(A)
    
    # Khởi tạo danh sách rỗng và một mảng buckets có 10 phần tử, mỗi phần tử là một danh sách
    l = []
    buckets = [l] * 10 

    # Phân phối các phần tử của mảng vào các bucket
    for i in range(n):
        # Tính chỉ số của bucket dựa trên giá trị của phần tử
        j = int(n * A[i] / (maxelement + 1))
        
        # Kiểm tra xem bucket có rỗng không
        if len(buckets[j]) == 0:
            buckets[j] = [A[i]]
        else:
            buckets[j].append(A[i])

    # Sắp xếp từng bucket bằng thuật toán Insertion Sort
    for i in range(10):
        insertionsort(buckets[i])

    # Gộp các bucket lại thành mảng đã sắp xếp
    k = 0 
    for i in range(10):
        for j in range(len(buckets[i])):
            A[k] = buckets[i].pop(0)
            k = k + 1 

# Mảng đầu vào
A = [63, 250, 835, 947, 651, 28]

# In ra mảng ban đầu
print('Original Array:', A)

# Gọi hàm bucketsort để sắp xếp mảng
bucketsort(A)

# In ra mảng đã sắp xếp
print('Sorted Array:', A)
