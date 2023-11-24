# Định nghĩa lớp _Node để tạo các nút của danh sách liên kết
class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element  # Gán giá trị của phần tử cho nút
        self._next = next  # Gán con trỏ next cho nút tiếp theo

# Định nghĩa lớp StacksLinked để triển khai ngăn xếp sử dụng danh sách liên kết
class StacksLinked:
    def __init__(self):
        self._top = None  # Khởi tạo đỉnh của ngăn xếp là None
        self._size = 0     # Khởi tạo độ dài của ngăn xếp là 0

    def __len__(self):
        return self._size  # Trả về độ dài của ngăn xếp

    def isempty(self):
        return self._size == 0  # Kiểm tra xem ngăn xếp có trống không

    def push(self, e):
        newest = _Node(e, None)  # Tạo một nút mới với giá trị là e và con trỏ next là None
        if self.isempty():
            self._top = newest  # Nếu ngăn xếp trống, nút mới là đỉnh ngăn xếp
        else:
            newest._next = self._top  # Ngược lại, con trỏ next của nút mới trỏ đến nút hiện tại là đỉnh ngăn xếp
            self._top = newest  # Cập nhật đỉnh ngăn xếp là nút mới
        self._size += 1  # Tăng kích thước ngăn xếp

    def pop(self):
        if self.isempty():
            print('Stack is Empty')  # Nếu ngăn xếp trống, in ra thông báo và thoát khỏi phương thức
            return
        e = self._top._element  # Lấy giá trị của phần tử ở đỉnh ngăn xếp
        self._top = self._top._next  # Cập nhật đỉnh ngăn xếp là nút tiếp theo
        self._size -= 1  # Giảm kích thước ngăn xếp
        return e  # Trả về giá trị của phần tử ở đỉnh ngăn xếp

    def top(self):
        if self.isempty():
            print('Stack is Empty')  # Nếu ngăn xếp trống, in ra thông báo và thoát khỏi phương thức
            return
        return self._top._element  # Trả về giá trị của phần tử ở đỉnh ngăn xếp

    def display(self):
        p = self._top  # Bắt đầu từ đỉnh ngăn xếp
        while p:
            print(p._element, end='-->')  # In giá trị của từng phần tử trong ngăn xếp
            p = p._next  # Di chuyển đến nút tiếp theo
        print()


# Tạo một đối tượng ngăn xếp
S = StacksLinked()

# Thêm phần tử 5 và 3 vào ngăn xếp, in ra độ dài của ngăn xếp và hiển thị ngăn xếp
S.push(5)
S.push(3)
print('Length:', len(S))
S.display()

# Lấy và in ra giá trị của phần tử ở đỉnh ngăn xếp, kiểm tra xem ngăn xếp có trống không, và hiển thị ngăn xếp
print(S.pop())
print(S.isempty())
S.display()

# Thêm phần tử 7, 9, 12 vào ngăn xếp, hiển thị ngăn xếp
S.push(7)
S.push(9)
S.push(12)
S.display()

# In ra giá trị của phần tử ở đỉnh ngăn xếp, hiển thị ngăn xếp
print(S.top())
S.display()
