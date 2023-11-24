# Import thư viện heapq với tên viết tắt là heap
import heapq as heap

# Tạo danh sách (list) L1 với các giá trị là 20, 14, 2, 15, 10, và 21
L1 = [20, 14, 2, 15, 10, 21]
print("Danh sách ban đầu:", L1)

# Thực hiện heapify để biến danh sách L1 thành một heap
heap.heapify(L1)
print("Heap sau khi heapify:", L1)

# In ra 3 phần tử nhỏ nhất của heap L1 sử dụng hàm nsmallest
print("3 phần tử nhỏ nhất:", heap.nsmallest(3, L1))

# In ra 3 phần tử lớn nhất của heap L1 sử dụng hàm nlargest
print("3 phần tử lớn nhất:", heap.nlargest(3, L1))
