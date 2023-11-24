class _Node:  # Tạo một lớp _Node để đại diện cho các nút trong danh sách liên kết đôi
    __slots__ = '_element', '_next', '_prev'  # Định nghĩa các thuộc tính của _Node: _element, _next, _prev

    def __init__(self, element, next, prev):  # Khởi tạo một đối tượng _Node với các thuộc tính _element, _next, _prev
        self._element = element  # Gán giá trị của tham số 'element' cho thuộc tính '_element' của nút
        self._next = next  # Gán giá trị của tham số 'next' cho thuộc tính '_next' của nút
        self._prev = prev  # Gán giá trị của tham số 'prev' cho thuộc tính '_prev' của nút

class DoublyLinkedList:  # Tạo một lớp DoublyLinkedList để đại diện cho danh sách liên kết đôi
    def __init__(self):  # Khởi tạo danh sách liên kết đôi với các thuộc tính ban đầu
        self._head = None  # Trỏ vào phần tử đầu tiên của danh sách (ban đầu là None, vì danh sách đang trống)
        self._tail = None  # Trỏ vào phần tử cuối của danh sách (ban đầu là None, vì danh sách đang trống)
        self._size = 0  # Số lượng phần tử ban đầu trong danh sách (ban đầu là 0, vì danh sách đang trống)

    def __len__(self):  # Phương thức trả về kích thước (số lượng phần tử) của danh sách liên kết đôi
        return self._size

    def isempty(self):  # Phương thức kiểm tra xem danh sách liên kết đôi có rỗng không
        return self._size == 0

    def addlast(self, e):  # Phương thức thêm phần tử 'e' vào cuối danh sách liên kết đôi
        newest = _Node(e, None, None)  # Tạo một nút mới chứa giá trị 'e', không trỏ tới nút nào phía trước và sau đó
        if self.isempty():  # Kiểm tra xem danh sách có rỗng không
            self._head = newest  # Nếu rỗng, thì nút đầu và nút cuối của danh sách trỏ tới nút mới này
            self._tail = newest
        else:  # Nếu danh sách không rỗng
            self._tail._next = newest  # Thay đổi nút kế tiếp của nút cuối hiện tại để trỏ tới nút mới này
            newest._prev = self._tail  # Cập nhật trỏ phía trước của nút mới để trỏ tới nút cuối hiện tại
            self._tail = newest  # Cập nhật nút cuối của danh sách để trỏ tới nút mới
        self._size += 1  # Tăng kích thước của danh sách liên kết

    def addfirst(self, e):  # Phương thức thêm phần tử 'e' vào đầu danh sách liên kết đôi
        newest = _Node(e, None, None)  # Tạo một nút mới chứa giá trị 'e', không trỏ tới nút nào phía trước và sau đó
        if self.isempty():  # Kiểm tra xem danh sách có rỗng không
            self._head = newest  # Nếu rỗng, thì nút đầu và nút cuối của danh sách trỏ tới nút mới này
            self._tail = newest
        else:  # Nếu danh sách không rỗng
            newest._next = self._head  # Thay đổi nút kế tiếp của nút mới để trỏ tới nút đầu hiện tại
            self._head._prev = newest  # Cập nhật trỏ phía trước của nút đầu hiện tại để trỏ tới nút mới này
            self._head = newest  # Cập nhật nút đầu của danh sách để trỏ tới nút mới
        self._size += 1  # Tăng kích thước của danh sách liên kết

    def display(self):  # Phương thức hiển thị danh sách liên kết đôi theo chiều từ đầu tới cuối
        p = self._head  # Gán nút 'p' để trỏ tới nút đầu của danh sách liên kết
        while p:  # Vòng lặp chạy cho đến khi nút 'p' trỏ tới một nút có giá trị
            print(p._element, end="-->")  # In ra giá trị của nút đó, kết thúc bằng dấu mũi tên
            p = p._next  # Di chuyển đến nút tiếp theo
        print()  # In một dòng trống sau khi hiển thị xong danh sách

    def addany(self, e, position):  # Phương thức thêm phần tử 'e' vào vị trí 'position'
        newest = _Node(e, None, None)  # Tạo một nút mới chứa giá trị 'e', không trỏ tới nút nào phía trước và sau đó
        p = self._head  # Gán nút 'p' để trỏ tới nút đầu của danh sách
        i = 1  # Biến đếm
        while i < position - 1:  # Vòng lặp để di chuyển tới nút cần chèn trừ 1
            p = p._next  # Di chuyển tới nút kế tiếp
            i = i + 1  # Tăng biến đếm
        newest._next = p._next  # Thay đổi trỏ tới của nút mới để trỏ tới nút cần chèn, đẩy nút cần chèn lên sau nút mới
        p._next._prev = newest  # Cập nhật trỏ phía trước của nút cần chèn để trỏ tới nút mới, hoàn thành việc nối nút mới với nút tại vị trí chèn
        p._next = newest  # Cập nhật trỏ tới của nút trước nút cần chèn để trỏ tới nút mới
        newest._prev = p  # Cập nhật trỏ phía trước của nút mới để trỏ tới nút trước nút cần chèn, hoàn thành việc nối nút trước nó với nút mới
        self._size += 1  # Tăng kích thước của danh sách liên kết

    def removefirst(self):  # Phương thức xóa phần tử ở vị trí đầu
        if self.isempty():  # Kiểm tra xem danh sách có rỗng không
            print("Circular List is Empty")  # In ra thông báo rằng danh sách rỗng
            return
        e = self._head._element  # Gán giá trị của phần tử đầu vào biến 'e'
        self._head = self._head._next  # Đặt nút thứ hai làm phần tử đầu của danh sách liên kết
        self._head._prev = None  # Cập nhật trỏ phía trước của nút thứ hai (nút đầu mới) để trỏ vào None
        self._size -= 1  # Giảm kích thước của danh sách liên kết
        if self.isempty():  # Kiểm tra lại xem sau khi xóa, danh sách có rỗng không
            self._tail = None  # Nếu rỗng, đặt nút cuối thành None
        return e  # Trả về giá trị đã xóa

    def removelast(self):  # Phương thức xóa phần tử ở vị trí cuối
        if self.isempty():  # Kiểm tra xem danh sách có rỗng không
            print("Circular List is Empty")  # In ra thông báo rằng danh sách rỗng
            return
        e = self._tail._element  # Gán giá trị của phần tử cuối vào biến 'e'
        self._tail = self._tail._prev  # Đặt nút trước cuối làm phần tử cuối của danh sách liên kết
        self._tail._next = None  # Cập nhật trỏ tới của phần tử cuối sau khi xóa để trỏ vào None
        self._size -= 1  # Giảm kích thước của danh sách liên kết
        return e  # Trả về giá trị đã xóa

    def removeany(self, position):  # Phương thức xóa phần tử tại vị trí 'position'
        p = self._head  # Gán nút 'p' để trỏ tới nút đầu của danh sách
        i = 1  # Biến đếm
        while i < position - 1:  # Vòng lặp để di chuyển tới phần tử (position - 1)
            p = p._next  # Di chuyển trỏ 'p' tới địa chỉ phần tử kế tiếp
            i = i + 1  # Tăng biến đếm
        e = p._next._element  # Gán giá trị của phần tử tại vị trí 'position' vào biến 'e'
        p._next = p._next._next  # Cập nhật trỏ tới của vị trí (position - 1) để trỏ tới vị trí (position + 1)
        p._next._prev = p  # Cập nhật trỏ phía trước của nút (position + 1) để trỏ tới nút (position - 1)
        self._size -= 1  # Giảm kích thước của danh sách liên kết
        return e  # Trả về giá trị đã xóa

    def displayrev(self):  # Phương thức hiển thị danh sách liên kết đôi theo chiều từ cuối về đầu
        p = self._tail  # Gán nút 'p' để trỏ tới phần tử cuối
        while p:  # Vòng lặp chạy cho đến khi nút 'p' trỏ tới một nút có giá trị
            print(p._element, end="-->")  # In ra giá trị của nút đó, kết thúc bằng dấu mũi tên
            p = p._prev  # Di chuyển đến nút trước đó
        print()  # In một dòng trống sau khi hiển thị xong danh sách

L = DoublyLinkedList()  # Khởi tạo một danh sách liên kết đôi 'L'
L.addlast(7)  # Thêm phần tử 7 vào cuối danh sách
L.addlast(4)  # Thêm phần tử 4 vào cuối danh sách
L.addlast(12)  # Thêm phần tử 12 vào cuối danh sách
L.display()  # Hiển thị danh sách theo chiều từ đầu đến cuối
print('Size', len(L))  # In ra kích thước của danh sách
L.displayrev()  # Hiển thị danh sách theo chiều từ cuối về đầu
L.addlast(8)  # Thêm phần tử 8 vào cuối danh sách
L.addlast(3)  # Thêm phần tử 3 vào cuối danh sách
L.display()  # Hiển thị danh sách theo chiều từ đầu đến cuối
print('Size', len(L))  # In ra kích thước của danh sách

L.addfirst(25)  # Thêm phần tử 25 vào đầu danh sách
L.display()

L.addany(25, 3)  # Thêm phần tử 25 vào vị trí 3
L.display()

L.removefirst()  # Xóa phần tử ở vị trí đầu
L.display()

L.removelast()  # Xóa phần tử ở vị trí cuối
L.display()
L.addlast(25)
L.display()

ele = L.removeany(3)  # Xóa phần tử ở vị trí 3
L.display()
print(ele)  # In ra giá trị đã xóa
