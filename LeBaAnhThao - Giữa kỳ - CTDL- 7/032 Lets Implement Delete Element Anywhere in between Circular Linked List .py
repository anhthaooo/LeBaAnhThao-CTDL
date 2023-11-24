class _Node:
    # Định nghĩa lớp _Node để tạo nút trong danh sách liên kết.
    __slots__ = '_element', '_next'
    # Giới hạn danh sách các thuộc tính của đối tượng _Node chỉ cho '_element' và '_next'.

    def __init__(self, element, next):
        # Phương thức khởi tạo của lớp _Node với 2 tham số là 'element' và 'next'.
        self._element = element
        # Gán giá trị của tham số 'element' cho thuộc tính '_element'.
        self._next = next
        # Gán giá trị của tham số 'next' cho thuộc tính '_next'.

class CircularLinkedList:
    # Định nghĩa lớp CircularLinkedList để tạo danh sách liên kết vòng.
    def __init__(self):
        # Phương thức khởi tạo của lớp CircularLinkedList.
        self._head = None
        # Tham chiếu đến phần tử đầu tiên, ban đầu là None.
        self._tail = None
        # Tham chiếu đến phần tử cuối cùng, ban đầu là None.
        self._size = 0
        # Số lượng phần tử trong danh sách, ban đầu là 0.

    def __len__(self):
        # Phương thức trả về kích thước của danh sách liên kết.
        return self._size

    def isempty(self):
        # Kiểm tra xem danh sách liên kết có rỗng không.
        return self._size == 0

    def addlast(self, e):
        # Thêm một phần tử mới vào cuối danh sách liên kết vòng.
        newest = _Node(e, None)
        # Tạo một nút mới với giá trị e và tham chiếu ban đầu là None.

        if self.isempty():
            # Nếu danh sách liên kết đang rỗng.
            newest._next = newest
            # Nút mới trỏ vào chính nó.
            self._head = newest
            # Nút mới trở thành nút đầu tiên của danh sách (tạo danh sách liên kết vòng).
        else:
            # Nếu danh sách không rỗng.
            newest._next = self._tail._next
            # Nút mới trỏ vào nút đầu tiên hiện tại.
            self._tail._next = newest
            # Nút cuối cùng hiện tại trỏ vào nút mới.
        self._tail = newest
        # Cập nhật nút cuối cùng là nút mới.
        self._size += 1
        # Tăng kích thước danh sách liên kết.

    def addfirst(self, e):
        # Thêm một phần tử mới vào đầu danh sách liên kết vòng.
        newest = _Node(e, None)
        # Tạo một nút mới với giá trị e và tham chiếu ban đầu là None.

        if self.isempty():
            # Nếu danh sách rỗng.
            newest._next = newest
            # Nút mới trỏ vào chính nó.
            self._head = newest
            # Nút mới trở thành nút đầu tiên của danh sách.
        else:
            # Nếu danh sách không rỗng.
            self._tail._next = newest
            # Nút cuối cùng hiện tại trỏ vào nút mới.
            newest._next = self._head
            # Nút mới trỏ vào nút đầu tiên hiện tại, biến đầu thành thứ hai.
        self._head = newest
        # Nút mới trở thành nút đầu tiên của danh sách.
        self._size += 1
        # Tăng kích thước danh sách liên kết.

    def addany(self, e, position):
        # Thêm một phần tử mới vào vị trí position trong danh sách liên kết vòng.
        newest = _Node(e, None)
        # Tạo một nút mới với giá trị e và tham chiếu ban đầu là None.

        p = self._head
        # Tham chiếu đến phần tử đầu tiên của danh sách.
        i = 1

        while i < position - 1:
            # Di chuyển đến phần tử cạnh phần tử cần chèn.
            p = p._next
            # Di chuyển đến phần tử kế tiếp.
            i += 1
        newest._next = p._next
        # Tham chiếu của nút mới trỏ vào tham chiếu của phần tử kế tiếp của p.
        p._next = newest
        # Tham chiếu của p trỏ vào nút mới, kết nối như (p -->newest--> p.next).
        self._size += 1
        # Tăng kích thước danh sách liên kết vòng.

    def removefirst(self):
        # Xóa phần tử đầu tiên khỏi danh sách liên kết vòng.
        if self.isempty():
            print("Circular List is Empty")
            # In ra thông báo nếu danh sách rỗng.
            return

        e = self._head._element
        # Lưu giá trị của phần tử đầu tiên.
        self._tail._next = self._head._next
        # Cập nhật tham chiếu của phần tử cuối cùng là phần tử kế tiếp của phần tử đầu tiên (bỏ qua phần tử đầu tiên).
        self._head = self._head._next
        # Cập nhật nút đầu tiên là phần tử kế tiếp.
        self._size -= 1
        # Giảm kích thước đi 1.

        if self.isempty():
            # Kiểm tra lại nếu danh sách rỗng.
            self._head = None
            # Tham chiếu đến phần tử đầu tiên là None.
            self._tail = None
            # Tham chiếu đến phần tử cuối cùng là None.

        return e

    def removelast(self):
        # Xóa phần tử cuối cùng khỏi danh sách liên kết vòng.
        if self.isempty():
            print("Circular List is Empty")
            # In ra thông báo nếu danh sách rỗng.
            return

        p = self._head
        # Tham chiếu đến phần tử đầu tiên của danh sách liên kết.
        i = 1

        while i < len(self) - 1:
            # Di chuyển đến phần tử cuối cùng trừ 1.
            p = p._next
            # Di chuyển đến phần tử kế tiếp.
            i += 1

        e = p._next._element
        # Lưu giá trị của phần tử bị xóa.
        p._next = self._head
        # Cập nhật tham chiếu của phần tử gần cuối là nút đầu tiên của danh sách liên kết (bỏ qua phần tử cuối cùng).
        self._size -= 1

        return e

    def removeany(self, position):
        # Xóa phần tử ở vị trí position.
        p = self._head
        # Tham chiếu đến phần tử đầu tiên của danh sách liên kết.
        i = 1

        while i < position - 1:
            # Di chuyển đến phần tử cạnh phần tử cần xóa.
            p = p._next
            # Di chuyển đến phần tử kế tiếp.
            i += 1

        e = p._next._element
        # Lưu giá trị của phần tử cần xóa.
        p._next = p._next._next
        # Tham chiếu của phần tử cạnh phần tử cần xóa trỏ vào phần tử sau phần tử cần xóa (bỏ qua phần tử cần xóa).
        self._size -= 1
        # Giảm kích thước danh sách liên kết.

        return e

    def display(self):
        # Hiển thị danh sách liên kết.
        p = self._head
        # Tham chiếu đến phần tử đầu tiên của danh sách.
        i = 0

        while i < len(self):
            # Sử dụng vòng lặp để duyệt qua danh sách.
            print(p._element, end=' --> ')
            # In ra giá trị của phần tử.
            p = p._next
            # Di chuyển đến phần tử kế tiếp.
            i += 1

        print()
        # Xuống dòng.

C = CircularLinkedList()
# Khởi tạo danh sách liên kết vòng C.
C.addlast(7)
# Thêm phần tử 7 vào cuối danh sách.
C.addlast(4)
# Thêm phần tử 4 vào cuối danh sách.
C.addlast(12)
# Thêm phần tử 12 vào cuối danh sách.
C.display()
# Hiển thị danh sách.

print("Size", len(C))
# In ra kích thước của danh sách liên kết.
C.addlast(8)
# Thêm phần tử 8 vào cuối danh sách.
C.addlast(3)
# Thêm phần tử 3 vào cuối danh sách.
C.display()
# Hiển thị danh sách.

print("Size", len(C))
# In ra kích thước của danh sách liên kết.
C.addfirst(25)
# Thêm phần tử 25 vào đầu danh sách.
C.display()
# Hiển thị danh sách.

print("Size", len(C))
# In ra kích thước của danh sách liên kết.

C.addany(20, 3)
# Thêm phần tử 20 vào vị trí thứ 3 trong danh sách.
C.display()
# Hiển thị danh sách.

print("Size", len(C))
# In ra kích thước của danh sách liên kết.

ele = C.removefirst()
# Xóa phần tử đầu tiên và lưu giá trị.
C.display()
# Hiển thị danh sách.
print("Size", len(C))
# In ra kích thước của danh sách.
print("removed element: ", ele)
# In ra giá trị đã xóa.

elelast = C.removelast()
# Xóa phần tử cuối cùng và lưu giá trị.
C.display()
# Hiển thị danh sách.
print("Size", len(C))
# In ra kích thước của danh sách.
print("removed element: ", elelast)
# In ra giá trị đã xóa.

eleany = C.removeany(2)
# Xóa phần tử ở vị trí thứ 2 và lưu giá trị.
C.display()
# Hiển thị danh sách.
print("Size", len(C))
# In ra kích thước của danh sách.
print("removed element: ", eleany)
# In ra giá trị đã xóa.
