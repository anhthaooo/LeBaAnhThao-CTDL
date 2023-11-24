class _Node:  # Định nghĩa lớp _Node (nút)
    __slots__ = '_element', '_next'  # Xác định thuộc tính của lớp _Node: _element và _next

    def __init__(self, element, next):  # Phương thức khởi tạo của lớp _Node với tham số element và next
        self._element = element    # Gán giá trị của tham số element cho thuộc tính _element
        self._next = next          # Gán giá trị của tham số next cho thuộc tính _next

class CircularLinkedList:  # Định nghĩa lớp CircularLinkedList (danh sách liên kết vòng)
    def __init__(self):  # Phương thức khởi tạo của lớp CircularLinkedList
        self._head = None  # Khởi tạo giá trị _head là None (không có nút nào ban đầu)
        self._tail = None  # Khởi tạo giá trị _tail là None (không có nút nào ban đầu)
        self._size = 0     # Khởi tạo biến _size để đếm số phần tử của danh sách liên kết vòng (ban đầu bằng 0)

    def __len__(self):  # Định nghĩa phương thức __len__ để kiểm tra số phần tử của danh sách liên kết
        return self._size  # Trả về độ dài (số phần tử) của danh sách liên kết

    def isempty(self):  # Định nghĩa phương thức kiểm tra xem danh sách liên kết có rỗng không
        return self._size == 0  # Trả về giá trị True nếu danh sách rỗng (size = 0), ngược lại trả về False

    def addlast(self, e):  # Định nghĩa phương thức thêm phần tử e vào cuối danh sách liên kết vòng
        newest = _Node(e, None)  # Tạo một nút mới có giá trị e và tham chiếu _next ban đầu là None
        if self.isempty():  # Kiểm tra nếu danh sách liên kết đang rỗng
            newest._next = newest  # Gán tham chiếu _next của nút mới vào chính nó, tạo thành danh sách liên kết vòng với một nút
            self._head = newest  # Gán nút mới làm đầu của danh sách liên kết
        else:  # Nếu danh sách không rỗng
            newest._next = self._tail._next  # Nút mới trỏ vào nút đầu tiên hiện tại của danh sách liên kết
            self._tail._next = newest  # Nút cuối cùng hiện tại trỏ vào nút mới, tạo nút mới thành phần tử cuối cùng của danh sách liên kết
        self._tail = newest  # Cập nhật tham chiếu của _tail để trỏ vào nút mới, nút mới trở thành phần tử cuối cùng của danh sách
        self._size += 1  # Tăng kích thước danh sách liên kết lên 1

    def addfirst(self, e):  # Định nghĩa phương thức thêm phần tử e vào phần tử đầu của danh sách liên kết
        newest = _Node(e, None)  # Tạo một nút mới có giá trị e và tham chiếu _next ban đầu là None
        if self.isempty():  # Kiểm tra nếu danh sách rỗng
            newest._next = newest  # Gán tham chiếu _next của nút mới vào chính nó, tạo thành danh sách liên kết vòng với một nút
            self._head = newest  # Gán nút mới làm đầu của danh sách liên kết
            self._tail = newest  # Gán nút mới làm cuối của danh sách liên kết
        else:  # Nếu danh sách không rỗng
            self._tail._next = newest  # Tham chiếu _next của nút cuối cùng hiện tại trỏ vào nút mới
            newest._next = self._head  # Tham chiếu _next của nút mới trỏ vào nút đầu tiên hiện tại của danh sách, tạo nút mới thành nút thứ hai của danh sách
            self._head = newest  # Cập nhật tham chiếu _head để trỏ vào nút mới, nút mới trở thành phần tử đầu tiên của danh sách
        self._size += 1  # Tăng kích thước danh sách liên kết lên 1

    def addany(self, e, position):  # Định nghĩa phương thức thêm phần tử e vào vị trí position trong danh sách liên kết
        newest = _Node(e, None)  # Tạo một nút mới có giá trị e và tham chiếu _next ban đầu là None
        p = self._head  # Gán p để trỏ vào phần tử đầu tiên của danh sách liên kết
        i = 1
        while i < position - 1:  # Vòng lặp để duyệt đến phần tử cần chèn (position - 1)
            p = p._next  # Di chuyển p để tham chiếu tới phần tử kế tiếp
            i = i + 1  # Tăng biến đếm i lên 1
        newest._next = p._next  # Tham chiếu của nút mới trỏ vào tham chiếu của nút kế tiếp của p
        p._next = newest  # Tham chiếu của nút p trỏ vào nút mới, tạo thành liên kết (p --> newest --> p.next)
        self._size += 1  # Tăng kích thước danh sách liên kết lên 1

    def removefirst(self):  # Định nghĩa phương thức xóa phần tử đầu tiên khỏi danh sách liên kết vòng
        if self.isempty():  # Kiểm tra nếu danh sách rỗng
            print("Circular List is Empty")  # In ra thông báo rằng danh sách vòng rỗng
            return
        e = self._head._element  # Lấy giá trị của phần tử đầu tiên
        self._tail_next = self._head._next  # Cập nhật tham chiếu của phần tử cuối cùng để trỏ vào phần tử kế tiếp của phần tử đầu tiên, tương đương việc bỏ qua phần tử đầu tiên
        self._head = self._head._next  # Cập nhật _head để trỏ vào phần tử kế tiếp, loại bỏ phần tử đầu tiên
        self._size -= 1  # Giảm kích thước danh sách đi 1
        if self.isempty():  # Kiểm tra lại nếu danh sách rỗng
            self._head = None  # Cập nhật _head thành None
            self._tail = None  # Cập nhật _tail thành None
        return e  # Trả về giá trị e của phần tử đầu tiên đã bị xóa

    def removelast(self):  # Định nghĩa phương thức xóa phần tử cuối cùng khỏi danh sách liên kết vòng
        if self.isempty():  # Kiểm tra nếu danh sách rỗng
            print("Circular List is Empty")  # In ra thông báo rằng danh sách vòng rỗng
            return
        p = self._head  # Gán p để trỏ vào phần tử đầu tiên của danh sách liên kết
        i = 1
        while i < len(self) - 1:  # Sử dụng vòng lặp để chạy đến phần tử gần cuối trừ 1
            p = p._next  # Di chuyển p để tham chiếu tới phần tử kế tiếp
            i = i + 1  # Tăng biến đếm i lên 1
        e = p._next._element  # Lấy giá trị của phần tử bị xóa (phần tử cuối cùng)
        p._next = self._head  # Cập nhật tham chiếu của phần tử gần cuối là phần tử đầu tiên của danh sách liên kết, tương tự việc bỏ qua phần tử cuối cùng
        self._size -= 1  # Giảm kích thước danh sách đi 1
        return e  # Trả về giá trị e của phần tử cuối cùng đã bị xóa

    def display(self):  # Định nghĩa phương thức để hiển thị các phần tử trong danh sách liên kết vòng
        p = self._head  # Gán p để trỏ vào phần tử đầu tiên của danh sách liên kết
        i = 0  # Khởi tạo biến đếm i
        while i < len(self):  # Sử dụng vòng lặp để chạy đến phần tử cuối cùng
            print(p._element, end='-->')  # In ra giá trị của p, kết thúc bằng dấu mũi tên
            p = p._next  # Di chuyển p để tham chiếu tới phần tử kế tiếp
            i = i + 1  # Tăng biến đếm i lên 1
        print()  # In xuống dòng

C = CircularLinkedList()  # Khởi tạo đối tượng CircularLinkedList có tên C
C.addlast(7)  # Thêm phần tử 7 vào cuối danh sách
C.addlast(4)  # Thêm phần tử 4 vào cuối danh sách
C.addlast(12)  # Thêm phần tử 12 vào cuối danh sách
C.display()  # Hiển thị danh sách

print("Size", len(C))  # In ra kích thước (số phần tử) của danh sách liên kết

C.addlast(8)  # Thêm phần tử 8 vào cuối danh sách
C.addlast(3)  # Thêm phần tử 3 vào cuối danh sách
C.display()  # Hiển thị danh sách
print("Size", len(C))  # In ra kích thước (số phần tử) của danh sách

C.addfirst(25)  # Thêm phần tử 25 vào đầu danh sách
C.display()  # Hiển thị danh sách
print("Size", len(C))  # In ra kích thước (số phần tử) của danh sách

C.addany(20, 3)  # Thêm phần tử 20 vào vị trí thứ 3 trong danh sách
C.display()  # Hiển thị danh sách
print("Size", len(C))  # In ra kích thước (số phần tử) của danh sách

ele = C.removefirst()  # Xóa phần tử đầu tiên
C.display()  # Hiển thị danh sách
print("Size", len(C))  # In ra kích thước (số phần tử) của danh sách
print("Removed element:", ele)  # In ra phần tử đã bị xóa

elelast = C.removelast()  # Xóa phần tử cuối cùng
C.display()  # Hiển thị danh sách
print("Size", len(C))  # In ra kích thước (số phần tử) của danh sách
print("Removed element:", elelast)  # In ra phần tử đã bị xóa
