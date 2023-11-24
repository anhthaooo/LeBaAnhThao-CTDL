class _Node:
    # Định nghĩa một lớp _Node để tạo nút cho danh sách liên kết
    __slots__ = '_element', '_next'  # Danh sách thuộc tính của lớp _Node

    def __init__(self, element, next):
        # Khởi tạo một nút _Node với giá trị (element) và tham chiếu đến nút tiếp theo (next)
        self._element = element  # Gán giá trị của tham số element cho thuộc tính _element
        self._next = next  # Gán giá trị của tham số next cho thuộc tính _next

class CircularLinkedList:
    # Định nghĩa lớp CircularLinkedList để tạo danh sách liên kết vòng
    def __init__(self):
        # Phương thức khởi tạo của lớp CircularLinkedList
        self._head = None  # Gán tham chiếu đầu danh sách (head) là None (danh sách rỗng)
        self._tail = None  # Khởi tạo biến tail để theo dõi tham chiếu đến nút cuối cùng
        self._size = 0  # Khởi tạo biến size để đếm số phần tử của danh sách liên kết vòng

    def __len__(self):
        # Phương thức để kiểm tra kích thước của danh sách liên kết
        return self._size  # Trả về độ dài (số phần tử) của danh sách liên kết

    def isempty(self):
        # Hàm kiểm tra xem danh sách liên kết có rỗng không
        return self._size == 0  # Trả về True nếu danh sách rỗng, ngược lại là False

    def addlast(self, e):
        # Hàm thêm một phần tử e vào cuối danh sách liên kết vòng
        newest = _Node(e, None)  # Tạo một nút mới có giá trị e và tham chiếu ban đầu là None

        if self.isempty():
            # Nếu danh sách liên kết rỗng, thêm phần tử vào danh sách với tham chiếu đến chính nó
            newest._next = newest
            self._head = newest
        else:
            # Nếu danh sách không rỗng, cập nhật tham chiếu cuối cùng của danh sách để trỏ đến nút mới
            newest._next = self._tail._next  # Tham chiếu của nút mới trỏ vào nút đầu tiên hiện tại của danh sách
            self._tail._next = newest  # Tham chiếu của nút cuối cùng hiện tại trỏ đến nút mới

        self._tail = newest  # Cập nhật tham chiếu cuối cùng của danh sách để trỏ đến nút mới
        self._size += 1  # Tăng kích thước của danh sách

    def addfirst(self, e):
        # Hàm thêm một phần tử e vào đầu danh sách liên kết vòng
        newest = _Node(e, None)  # Tạo một nút mới có giá trị e và tham chiếu ban đầu là None

        if self.isempty():
            # Nếu danh sách liên kết rỗng, thêm phần tử vào danh sách với tham chiếu đến chính nó
            newest._next = newest
        else:
            # Nếu danh sách không rỗng, cập nhật tham chiếu cuối cùng của danh sách để trỏ đến nút mới
            newest._next = self._tail._next  # Tham chiếu của nút mới trỏ vào nút đầu tiên hiện tại của danh sách

        self._head = newest  # Cập nhật tham chiếu đầu của danh sách để trỏ đến nút mới
        self._tail._next = newest  # Cập nhật tham chiếu của nút cuối cùng hiện tại để trỏ đến nút mới
        self._size += 1  # Tăng kích thước của danh sách

    def addany(self, e, position):
        # Hàm thêm một phần tử e vào vị trí position trong danh sách liên kết vòng
        newest = _Node(e, None)  # Tạo một nút mới có giá trị e và tham chiếu ban đầu là None
        p = self._head  # p trỏ tới giá trị đầu của danh sách liên kết
        i = 1

        while i < position - 1:
            # Di chuyển p đến nút trước vị trí cần chèn (position-1)
            p = p._next
            i += 1

        newest._next = p._next  # Tham chiếu của nút mới trỏ vào tham chiếu của nút kế tiếp của p
        p._next = newest  # Tham chiếu của nút p trỏ đến nút mới
        self._size += 1  # Tăng kích thước của danh sách

    def display(self):
        # Hàm để hiển thị giá trị phần tử trong danh sách liên kết vòng
        p = self._head  # p trỏ tới giá trị đầu của danh sách liên kết
        i = 0

        while i < len(self):
            # Sử dụng vòng lặp để duyệt qua các phần tử trong danh sách và hiển thị chúng
            print(p._element, end=' --> ')
            p = p._next
            i += 1

        print()  # In xuống dòng

# Tạo một danh sách liên kết vòng và thực hiện thêm và hiển thị các phần tử
C = CircularLinkedList()  # Khởi tạo danh sách liên kết vòng C
C.addlast(7)  # Thêm 7 vào cuối danh sách
C.addlast(4)  # Thêm 4 vào cuối danh sách
C.addlast(12)  # Thêm 12 vào cuối danh sách
C.display()  # Hiển thị danh sách
print("Size", len(C))  # Hiển thị kích thước của danh sách

C.addlast(8)  # Thêm 8 vào cuối danh sách
C.addlast(3)  # Thêm 3 vào cuối danh sách
C.display()  # Hiển thị danh sách
print("Size", len(C))  # Hiển thị kích thước của danh sách

C.addfirst(25)  # Thêm 25 vào đầu danh sách
C.display()  # Hiển thị danh sách
print("Size", len(C))  # Hiển thị kích thước của danh sách

C.addany(20, 3)  # Thêm 20 vào vị trí thứ 3 trong danh sách
C.display()  # Hiển thị danh sách
print("Size", len(C))  # Hiển thị kích thước của danh sách
