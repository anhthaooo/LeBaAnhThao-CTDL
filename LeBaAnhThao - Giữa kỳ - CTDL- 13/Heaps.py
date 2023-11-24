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

    def deletemax(self):
        # Kiểm tra xem heap có trống không
        if self._csize == 0:
            print('Heap is Empty')
            return 
        e = self._data[1]
        # Thay thế phần tử gốc bằng phần tử cuối cùng của heap
       # Thay thế giá trị của phần tử gốc (lớn nhất) bằng giá trị của phần tử cuối cùng của heap
        self._data[1] = self._data[self._csize]
        # Gán giá trị -1 cho phần tử cuối cùng của heap, đánh dấu vùng nhớ đã bị xóa
        self._data[self._csize] = -1
        # Giảm kích thước hiện tại của heap đi 1
        self._csize = self._csize - 1
        # Thiết lập chỉ số i bằng 1 để bắt đầu quá trình điều chỉnh heap từ đỉnh (gốc) của heap
        i = 1
        # Thiết lập chỉ số j bằng 2, đại diện cho con trái của gốc. 
        # Quá trình điều chỉnh heap sẽ bắt đầu từ gốc và di chuyển xuống các nút con để đảm bảo tính chất heap
        j = i * 2

        # Thực hiện phép heapify từ gốc xuống để duy trì tính chất của heap
        while j <= self._csize:
    # Kiểm tra xem có tồn tại con phải và con phải lớn hơn con trái hay không
            if j < self._csize and self._data[j] < self._data[j+1]:
                j = j + 1  # Nếu có, di chuyển đến con phải
            # So sánh giá trị của phần tử hiện tại với giá trị của con lớn hơn
            if self._data[i] < self._data[j]:
                # Nếu phần tử hiện tại nhỏ hơn con lớn hơn, thực hiện swap
                temp = self._data[i]
                self._data[i] = self._data[j]
                self._data[j] = temp
                i = j  # Cập nhật chỉ số i để tiếp tục kiểm tra xuống cây heap
                j = i * 2  # Cập nhật chỉ số j để kiểm tra con tiếp theo
            else: 
                break  # Nếu không thỏa mãn, thoát khỏi vòng lặp while
        return e  # Trả về giá trị của phần tử đã xoá (phần tử lớn nhất)

