# Nhập lớp Heap từ module Heaps
from Heaps import Heap

# Định nghĩa hàm heapsort
def heapsort(A):
    # Tạo một đối tượng Heap mới
    H = Heap()
    # Lấy độ dài của mảng
    n = len(A)
    # Chèn từng phần tử của mảng vào heap
    for i in range(n):
        H.insert(A[i])
    # Khởi tạo k là chỉ số cuối cùng của mảng
    k = n - 1 
    # Đối với mỗi phần tử trong heap
    for i in range (H._csize):
        # Xóa phần tử lớn nhất từ heap và gán nó vào vị trí k trong mảng
        A[k] = H.deletemax()
        # Giảm k đi 1
        k = k - 1 

# Định nghĩa một mảng
A = [63,250,835,947,651,28]
# In mảng ban đầu
print('Mảng ban đầu:',A)
# Sắp xếp mảng bằng heapsort
heapsort(A)
# In mảng đã sắp xếp
print('Mảng đã sắp xếp:',A)
