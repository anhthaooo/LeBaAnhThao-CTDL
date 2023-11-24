class _Node:  # Định nghĩa một lớp _Node để tạo Node trong danh sách liên kết
    __slots__ = '_element', '_next'  # Sử dụng __slots__ để tối ưu hóa việc quản lý bộ nhớ

    def __init__(self, element, next):  # Phương thức khởi tạo của lớp _Node với tham số element và next
        self._element = element  # Gán giá trị của tham số element cho thuộc tính _element
        self._next = next  # Gán giá trị của tham số next cho thuộc tính _next

class LinkedList:  # Định nghĩa một lớp LinkedList để tạo danh sách liên kết
    def __init__(self):  # Phương thức khởi tạo của lớp LinkedList
        self._head = None  # Gán giá trị đầu của danh sách liên kết là None
        self._tail = None  # Gán giá trị đuôi của danh sách liên kết là None
        self._size = 0  # Khởi tạo biến _size để đếm số phần tử trong danh sách liên kết

    def __len__(self):  # Phương thức để lấy độ dài của danh sách liên kết
        return self._size  # Trả về giá trị của biến _size

    def isempty(self):  # Phương thức để kiểm tra xem danh sách liên kết có rỗng không
        return self._size == 0  # Trả về True nếu danh sách rỗng, ngược lại là False

    def addlast(self, e):  # Phương thức để thêm một phần tử e vào cuối danh sách liên kết
        newest = _Node(e, None)  # Tạo một Node mới có giá trị là e và next trỏ đến None
        if self.isempty():  # Kiểm tra xem danh sách có rỗng không
            self._head = newest  # Nếu rỗng, gán phần đầu danh sách là newest
        else:               
            self._tail._next = newest  # Nếu không rỗng, cập nhật con trỏ next của Node cuối cùng đến newest
        self._tail = newest  # Cập nhật Node cuối danh sách là newest
        self._size += 1  # Tăng giá trị của _size lên 1 để đếm số phần tử trong danh sách

    def display(self):  # Phương thức để hiển thị các phần tử trong danh sách liên kết
        p = self._head  # Gán p là giá trị đầu của danh sách liên kết
        while p:  # Sử dụng vòng lặp while để duyệt qua danh sách
            print(p._element, end=' --> ')  # In ra giá trị của Node hiện tại, end=' --> ' để tạo dấu nối
            p = p._next  # Di chuyển con trỏ p đến phần tử tiếp theo trong danh sách
        print()  # In một dòng mới để kết thúc danh sách

L = LinkedList()  # Khởi tạo một danh sách liên kết rỗng có tên L
L.addlast(7)  # Thêm phần tử 7 vào cuối danh sách liên kết
L.addlast(4)  # Thêm phần tử 4 vào cuối danh sách liên kết
L.addlast(12)  # Thêm phần tử 12 vào cuối danh sách liên kết
L.display()  # In ra các phần tử trong danh sách liên kết
print('Size:', len(L))  # In ra độ dài của danh sách liên kết
L.addlast(8)            # thêm phần tử 8 vào danh sách liên kết
L.addlast(3)            # thêm phần tử 3 vào danh sách liên kết
L.display()             # in ra màn hình các phần tử của danh sách liên kết
print('Size:',len(L))   # in ra độ dài của danh sách liên kết