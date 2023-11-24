class _Node:  # Định nghĩa lớp _Node để tạo một nút trong danh sách liên kết.
    __slots__ = '_element', '_next'  # Sử dụng __slots__ để tối ưu hóa việc quản lý bộ nhớ.

    def __init__(self, element, next):  # Phương thức khởi tạo của lớp _Node với tham số element và next.
        self._element = element  # Gán giá trị của tham số element cho thuộc tính _element.
        self._next = next  # Gán giá trị của tham số next cho thuộc tính _next.

class CircularLinkedList:  # Định nghĩa lớp CircularLinkedList để tạo danh sách liên kết vòng.
    def __init__(self):  # Phương thức khởi tạo của lớp CircularLinkedList.
        self._head = None  # Gán giá trị đầu của danh sách liên kết là None.
        self._tail = None  # Tạo một biến _tail để tham chiếu đến nút cuối cùng.
        self._size = 0  # Khởi tạo biến _size để đếm số phần tử trong danh sách liên kết vòng.

    def __len__(self):  # Phương thức để lấy độ dài của danh sách liên kết.
        return self._size  # Trả về giá trị của biến _size.

    def isempty(self):  # Phương thức để kiểm tra xem danh sách liên kết có rỗng không.
        return self._size == 0  # Trả về True nếu danh sách rỗng, ngược lại là False.

    def addlast(self, e):  # Phương thức để thêm một phần tử e vào cuối danh sách liên kết vòng.
        newest = _Node(e, None)  # Tạo một nút mới có giá trị là e và tham chiếu next là None.
        if self.isempty():  # Kiểm tra nếu danh sách liên kết đang rỗng.
            newest._next = newest  # Gán tham chiếu next của nút mới vào chính nó, tạo danh sách liên kết vòng.
            self._head = newest  # Gán nút đầu của danh sách liên kết là nút mới, tạo danh sách vòng.
        else:  # Nếu danh sách không rỗng.
            newest._next = self._tail._next  # Nút mới trỏ vào nút đầu tiên hiện tại của danh sách liên kết (vì _tail._next trỏ vào đầu danh sách).
            self._tail._next = newest  # Nút cuối cùng hiện tại trỏ vào nút mới, biến nút mới thành nút cuối cùng của danh sách liên kết.
        self._tail = newest  # Thay đổi tham chiếu _tail để trỏ vào nút mới, biến nút mới thành nút cuối cùng của danh sách liên kết.
        self._size += 1  # Tăng giá trị _size để đếm số phần tử.

    def display(self):  # Phương thức để hiển thị các phần tử trong danh sách liên kết vòng.
        p = self._head  # Gán p để trỏ vào nút đầu của danh sách liên kết.
        i = 0  # Khởi tạo biến đếm i.
        while i < len(self):  # Sử dụng vòng lặp để duyệt qua danh sách đến phần tử cuối cùng.
            print(p._element, end=' --> ')  # In giá trị của nút hiện tại, kết thúc bằng dấu ' --> ' để tạo kết nối.
            p = p._next  # Di chuyển con trỏ p đến nút tiếp theo trong danh sách liên kết.
            i += 1  # Tăng biến đếm i.
        print()  # In xuống dòng.

C = CircularLinkedList()  # Khởi tạo danh sách liên kết vòng C.
C.addlast(7)  # Thêm phần tử 7 vào cuối danh sách.
C.addlast(4)  # Thêm phần tử 4 vào cuối danh sách.
C.addlast(12)  # Thêm phần tử 12 vào cuối danh sách.
C.display()  # Hiển thị danh sách.
print("Size", len(C))  # In ra kích thước của danh sách liên kết.
C.addlast(8)  # Thêm phần tử 8 vào cuối danh sách.
C.addlast(3)  # Thêm phần tử 3 vào cuối danh sách.
C.display()  # Hiển thị danh sách sau khi thêm.
print("Size", len(C))  # In ra kích thước của danh sách liên kết.
