# Định nghĩa một lớp Heap để biểu diễn cấu trúc dữ liệu Heap (cây nhị phân đầy đủ với tính chất heap)
class Heap:
    def __init__(self):
        # Khởi tạo kích thước tối đa của heap là 10
        self.maxsize = 10 
        # Tạo một mảng để lưu trữ các phần tử của heap, ban đầu được khởi tạo với giá trị -1
        self._data = [-1] * self.maxsize 
        # Biến lưu trữ kích thước hiện tại của heap, ban đầu là 0
        self._csize = 0 

    # Phương thức này trả về độ dài của heap, được gọi khi sử dụng hàm len()
    def __len__(self):
        return len(self._data)
    
    # Phương thức kiểm tra xem heap có trống rỗng hay không
    def isempty(self):
        return len(self._data) == 0 
    
    # Phương thức chèn một phần tử vào heap
    def insert(self, e):
        # Kiểm tra xem còn không gian trong heap không
        if self._csize == self.maxsize:
            print('No Space in Heap')
            return 
        # Tăng kích thước hiện tại của heap
        self._csize = self._csize + 1 
        # Vị trí hiện tại của phần tử trong heap
        hi = self._csize 
        # Thực hiện phép heapify để duy trì tính chất của heap
        while hi > 1 and e > self._data[hi // 2]:
            # Di chuyển phần tử lớn hơn từ vị trí hi//2 xuống vị trí hi
            self._data[hi] = self._data[hi // 2]
            hi = hi // 2 
        # Đặt phần tử mới vào vị trí thích hợp trong heap
        self._data[hi] =  e

    # Phương thức trả về phần tử lớn nhất trong heap (gốc)
    def max(self):
        # Kiểm tra xem heap có trống không
        if self._csize == 0 :
            print('Heap is Empty')
            return 
        # Trả về phần tử lớn nhất trong heap
        return self._data[1]


# Tạo một đối tượng Heap
S = Heap()
# Chèn các phần tử vào heap
S.insert(25)
S.insert(14)
S.insert(2)
S.insert(20)
S.insert(10)
# In trạng thái của heap sau mỗi lần chèn
print(S._data)
# Chèn thêm một phần tử vào heap
S.insert(40)
# In trạng thái của heap sau khi chèn phần tử mới
print(S._data)
