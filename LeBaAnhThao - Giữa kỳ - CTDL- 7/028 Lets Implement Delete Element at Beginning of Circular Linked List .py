class _Node:  # Định nghĩa lớp _Node để tạo nút cho danh sách liên kết vòng
    __slots__ = '_element', '_next'  # Mỗi nút chứa hai thuộc tính là _element (giá trị của nút) và _next (tham chiếu đến nút tiếp theo)

    def __init__(self, element, next):  # Phương thức khởi tạo của lớp _Node, được gọi khi một nút mới được tạo
        self._element = element  # Gán giá trị của tham số element cho thuộc tính _element của nút
        self._next = next  # Gán giá trị của tham số next cho thuộc tính _next của nút

class CircularLinkedList:  # Định nghĩa lớp CircularLinkedList để tạo danh sách liên kết vòng
    def __init__(self):  # Phương thức khởi tạo của lớp CircularLinkedList
        self._head = None  # Gán giá trị đầu (_head) của danh sách là None (rỗng)
        self._tail = None  # Tạo một biến tail để tham chiếu đến nút cuối cùng (ban đầu là None)
        self._size = 0  # Tạo một biến _size để đếm số phần tử của danh sách liên kết vòng

    def __len__(self):  # Định nghĩa phương thức __len__ để kiểm tra số phần tử của danh sách liên kết
        return self._size  # Trả về độ dài (số phần tử) của danh sách liên kết

    def isempty(self):  # Định nghĩa phương thức isempty để kiểm tra xem danh sách liên kết có rỗng không
        return self._size == 0  # Trả về giá trị True nếu danh sách rỗng (size = 0), False nếu danh sách có phần tử

    def addlast(self, e):  # Định nghĩa phương thức addlast để thêm phần tử e vào cuối danh sách liên kết vòng
        newest = _Node(e, None)  # Tạo một nút mới (newest) với giá trị e và tham chiếu _next ban đầu là None
        if self.isempty():  # Nếu danh sách đang rỗng
            newest._next = newest  # Tham chiếu _next của newest trỏ vào chính nó (tạo danh sách vòng)
            self._head = newest  # Gán giá trị _head của danh sách liên kết là newest, tạo danh sách chỉ chứa một phần tử trỏ vào chính nó
        else:  # Nếu danh sách không rỗng
            newest._next = self._tail._next  # Tham chiếu _next của newest trỏ vào nút đầu tiên hiện tại (vì self._tail._next trỏ vào đầu danh sách)
            self._tail._next = newest  # Tham chiếu _next của nút cuối cùng hiện tại trỏ vào newest (thay vì đầu danh sách), tạo newest thành phần tử cuối cùng của danh sách liên kết
        self._tail = newest  # Tham chiếu _tail của danh sách liên kết trỏ vào nút newest, newest trở thành phần tử cuối cùng của danh sách
        self._size += 1  # Tăng giá trị kích thước (size) của danh sách liên kết

    def addfirst(self, e):  # Định nghĩa phương thức addfirst để thêm phần tử e vào đầu danh sách liên kết vòng
        newest = _Node(e, None)  # Tạo một nút mới (newest) với giá trị e và tham chiếu _next ban đầu là None
        if self.isempty():  # Nếu danh sách rỗng
            newest._next = newest  # Tham chiếu _next của newest trỏ vào chính nó (tạo danh sách vòng)
            self._head = newest  # Tham chiếu đến nút đầu (_head) của danh sách liên kết là newest
        else:  # Nếu danh sách không rỗng
            self._tail._next = newest  # Tham chiếu _next của nút cuối cùng hiện tại trỏ vào newest (thay vì đầu danh sách), tạo newest thành phần tử cuối cùng của danh sách liên kết
            newest._next = self._head  # Tham chiếu _next của nút newest trỏ vào nút đầu tiên hiện tại của danh sách, tạo newest thành nút đầu tiên của danh sách
        self._head = newest  # Tham chiếu đến nút đầu (_head) của danh sách liên kết trỏ vào newest, newest trở thành nút đầu tiên của danh sách
        self._size += 1  # Tăng giá trị kích thước (size) của danh sách liên kết

    def addany(self, e, position):  # Định nghĩa phương thức addany để thêm phần tử e vào vị trí position
        newest = _Node(e, None)  # Tạo một nút mới (newest) với giá trị e và tham chiếu _next ban đầu là None
        p = self._head  # Tham chiếu p trỏ vào nút đầu tiên của danh sách liên kết
        i = 1
        while i < position - 1:  # Duyệt qua danh sách để đến phần tử cần chèn (position - 1)
            p = p._next  # Duyệt tới nút tiếp theo
            i = i + 1
        newest._next = p._next  # Tham chiếu _next của nút newest trỏ vào tham chiếu của nút kế tiếp của p
        p._next = newest  # Tham chiếu _next của nút p trỏ vào newest, tạo thành p --> newest --> p.next
        self._size += 1  # Tăng giá trị kích thước (size) của danh sách liên kết vòng

    def removefirst(self):  # Định nghĩa phương thức removefirst để xóa phần tử đầu tiên của danh sách liên kết vòng
        if self.isempty():  # Nếu danh sách rỗng
            print("Circular List is Empty")  # In ra thông báo
            return
        e = self._head._element  # Lưu giá trị của phần tử đầu tiên
        self._tail_next = self._head._next  # Cập nhật tham chiếu của phần tử cuối cùng, là tham chiếu đến phần tử kế tiếp của phần tử đầu tiên
        self._head = self._head._next  # Cập nhật tham chiếu đến phần tử đầu tiên
        self._size -= 1  # Giảm kích thước đi 1
        if self.isempty():  # Nếu danh sách rỗng sau khi xóa
            self._head = None  # Gán tham chiếu đến phần tử đầu tiên là None
            self._tail = None  # Gán tham chiếu đến phần tử cuối cùng là None
        return e  # Trả về giá trị phần tử bị xóa

    def display(self):  # Định nghĩa phương thức display để hiển thị phần tử của danh sách liên kết vòng
        p = self._head  # Tham chiếu p trỏ vào nút đầu tiên của danh sách liên kết
        i = 0  # Gán i = 0
        while i < len(self):  # Sử dụng vòng lặp để duyệt qua tất cả phần tử
            print(p._element, end=' --> ')  # In ra giá trị của phần tử p
            p = p._next  # Tham chiếu p trỏ vào phần tử tiếp theo
            i = i + 1  # Tăng biến đếm
        print()  # In xuống dòng

C = CircularLinkedList()  # Khởi tạo danh sách liên kết vòng C
C.addlast(7)  # Thêm phần tử 7 vào cuối danh sách
C.addlast(4)  # Thêm phần tử 4 vào cuối danh sách
C.addlast(12)  # Thêm phần tử 12 vào cuối danh sách
C.display()  # Hiển thị danh sách
print("Size", len(C))  # In ra kích thước của danh sách

C.addlast(8)  # Thêm phần tử 8 vào cuối danh sách
C.addlast(3)  # Thêm phần tử 3 vào cuối danh sách
C.display()  # Hiển thị danh sách
print("Size", len(C))  # In ra kích thước của danh sách

C.addfirst(25)  # Thêm phần tử 25 vào đầu danh sách
C.display()  # Hiển thị danh sách
print("Size", len(C))  # In ra kích thước của danh sách

C.addany(20, 3)  # Thêm phần tử 20 vào vị trí thứ 3 trong danh sách
C.display()  # Hiển thị danh sách
print("Size", len(C))  # In ra kích thước của danh sách

ele = C.removefirst()  # Xóa phần tử đầu tiên
C.display()  # Hiển thị danh sách sau khi xóa
print("Size", len(C))  # In ra kích thước của danh sách
print("Removed element:", ele)  # In ra giá trị của phần tử bị xóa
