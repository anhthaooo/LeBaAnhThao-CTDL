class _Node:
    # Tạo lớp _Node để đại diện cho các nút trong danh sách liên kết.
    __slots__ = '_element', '_next'  # Chỉ định các thuộc tính _element và _next của lớp.

    def __init__(self, element, next):
        # Phương thức khởi tạo cho lớp _Node với các tham số element (giá trị của nút) và next (tham chiếu đến nút tiếp theo).
        self._element = element  # Gán giá trị của tham số element cho thuộc tính _element.
        self._next = next  # Gán giá trị của tham số next cho thuộc tính _next.

class CircularLinkedList:
    # Tạo lớp CircularLinkedList để đại diện cho danh sách liên kết vòng.
    def __init__(self):
        # Phương thức khởi tạo của lớp CircularLinkedList.
        self._head = None  # Gán giá trị đầu của danh sách liên kết là None.
        self._tail = None  # Tạo một biến tail để tham chiếu đến nút cuối cùng.
        self._size = 0  # Khởi tạo biến _size để đếm số phần tử trong danh sách liên kết vòng.

    def __len__(self):
        # Phương thức để lấy độ dài của danh sách liên kết.
        return self._size  # Trả về giá trị của biến _size.

    def isempty(self):
        # Phương thức để kiểm tra xem danh sách liên kết có rỗng không.
        return self._size == 0  # Trả về True nếu danh sách rỗng, ngược lại là False.

    def addlast(self, e):
        # Phương thức để thêm một phần tử e vào cuối danh sách liên kết vòng.
        newest = _Node(e, None)  # Tạo một nút mới với giá trị là e và tham chiếu next là None.
        if self.isempty():
            # Nếu danh sách liên kết đang rỗng, gán next của nút mới là chính nó và đặt nút mới là đầu danh sách.
            newest._next = newest
            self._head = newest
        else:
            # Nếu không rỗng, cập nhật tham chiếu next của nút mới để trỏ đến nút đầu tiên hiện tại,
            # sau đó cập nhật tham chiếu next của nút cuối cùng hiện tại để trỏ đến nút mới,
            # làm nút mới trở thành nút cuối cùng của danh sách liên kết vòng.
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest  # Cập nhật nút cuối cùng của danh sách liên kết là nút mới.
        self._size += 1  # Tăng kích thước danh sách liên kết.

    def addfirst(self, e):
        # Phương thức để thêm một phần tử e vào đầu danh sách liên kết vòng.
        newest = _Node(e, None)  # Tạo một nút mới với giá trị là e và tham chiếu next là None.
        if self.isempty():
            # Nếu danh sách rỗng, gán next của nút mới là chính nó và đặt nút mới là đầu danh sách.
            newest._next = newest
            self._head = newest
        else:
            # Nếu không rỗng, cập nhật tham chiếu next của nút mới để trỏ đến nút đầu tiên hiện tại của danh sách,
            # sau đó cập nhật tham chiếu next của nút cuối cùng hiện tại để trỏ đến nút mới, làm nút mới trở thành
            # nút cuối cùng của danh sách liên kết vòng.
            self._tail._next = newest
            newest._next = self._head
        self._head = newest  # Cập nhật nút đầu của danh sách liên kết là nút mới.
        self._size += 1  # Tăng kích thước danh sách liên kết.

    def display(self):
        # Phương thức để hiển thị các phần tử trong danh sách liên kết.
        p = self._head  # Bắt đầu từ đầu danh sách liên kết.
        i = 0
        while i < len(self):
            # Sử dụng vòng lặp để duyệt và in giá trị của các nút.
            print(p._element, end='-->')
            p = p._next
            i += 1
        print()

C = CircularLinkedList()  # Khởi tạo một danh sách liên kết vòng C.
C.addlast(7)  # Thêm 7 vào cuối danh sách.
C.addlast(4)  # Thêm 4 vào cuối danh sách.
C.addlast(12)  # Thêm 12 vào cuối danh sách.
C.display()  # In danh sách.
print("Size", len(C))  # In ra kích thước của danh sách.
C.addlast(8)  # Thêm 8 vào cuối danh sách.
C.addlast(3)  # Thêm 3 vào cuối danh sách.
C.display()  # In danh sách.
print("Size", len(C))  # In ra kích thước của danh sách.
C.addfirst(25)  # Thêm 25 vào đầu danh sách.
C.display()  # In danh sách.
print("Size", len(C))  # In ra kích thước của danh sách.
