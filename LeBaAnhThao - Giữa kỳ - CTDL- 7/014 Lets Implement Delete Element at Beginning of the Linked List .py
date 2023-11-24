class _Node:
    """Định nghĩa một lớp _Node để tạo Node trong danh sách liên kết."""
    __slots__ = '_element', '_next'  # Sử dụng __slots__ để tối ưu hóa việc quản lý bộ nhớ

    def __init__(self, element, next):
        """Phương thức khởi tạo của lớp _Node với tham số element và next."""
        self._element = element  # Gán giá trị của tham số element cho thuộc tính _element
        self._next = next  # Gán giá trị của tham số next cho thuộc tính _next

class LinkedList:
    """Định nghĩa một lớp LinkedList để tạo danh sách liên kết."""
    def __init__(self):
        """Phương thức khởi tạo của lớp LinkedList."""
        self._head = None  # Gán giá trị đầu của danh sách liên kết là None
        self._tail = None  # Gán giá trị đuôi của danh sách liên kết là None
        self._size = 0  # Khởi tạo biến _size để đếm số phần tử trong danh sách liên kết

    def __len__(self):
        """Phương thức để lấy độ dài của danh sách liên kết."""
        return self._size  # Trả về giá trị của biến _size

    def isempty(self):
        """Phương thức để kiểm tra xem danh sách liên kết có rỗng không."""
        return self._size == 0  # Trả về True nếu danh sách rỗng, ngược lại là False

    def addlast(self, e):
        """Phương thức để thêm một phần tử e vào cuối danh sách liên kết."""
        newest = _Node(e, None)  # Tạo một Node mới có giá trị là e và next trỏ đến None
        if self.isempty():
            self._head = newest  # Nếu rỗng, gán phần đầu danh sách là newest
        else:
            self._tail._next = newest  # Nếu không rỗng, cập nhật con trỏ next của Node cuối cùng đến newest
        self._tail = newest  # Cập nhật Node cuối danh sách là newest
        self._size += 1  # Tăng giá trị của _size lên 1 để đếm số phần tử trong danh sách

    def addfirst(self, e):
        """Phương thức để thêm một phần tử e vào đầu danh sách liên kết."""
        newest = _Node(e, None)  # Tạo một Node mới `newest` với giá trị `e` và con trỏ `next` trỏ đến `None`.
        if self.isempty():  # Kiểm tra xem danh sách liên kết có rỗng không.
            self._head = newest  # Nếu rỗng, gán phần tử đầu của danh sách liên kết là `newest`.
            self._tail = newest  # Vì danh sách rỗng, nên phần tử cuối cũng là `newest`.
        else:
            newest._next = self._head  # Cập nhật con trỏ `next` của `newest` để trỏ đến phần tử đầu tiên của danh sách liên kết hiện tại. Điều này làm cho `newest` trở thành phần tử đầu tiên của danh sách.
            self._head = newest  # Cập nhật con trỏ `head` để trỏ đến `newest`, làm cho `newest` trở thành phần tử đầu tiên của danh sách.
        self._size += 1  # Tăng kích thước của danh sách liên kết lên 1 (nếu bạn đang theo dõi kích thước).

    def addany(self,e,position):
        """Phương thức để thêm một phần tử e vào vị trí position trong danh sách liên kết."""
        newest = _Node(e, None)  # Tạo một Node mới có giá trị là e và next trỏ đến None
        p = self._head  # Gán p là phần tử đầu tiên của danh sách liên kết
        i = 1  # Gán i = 1
        while i < position - 1:  # Kiểm tra vị trí của i có phải là vị trí cần chèn vào chưa
            p = p._next  # Trỏ tới phần tử kế tiếp trong danh sách liên kết
            i = i + 1  # Tăng biến đếm i
        newest._next = p._next  # Trỏ giá trị của biến cần chèn vào đến phần tử danh sách liên kết kế tiếp
        p._next = newest  # Trỏ giá trị tiếp theo của p là biến cần chèn vào
        self._size += 1  # Tăng kích thước của danh sách liên kết

    def removefirst(self):  # tạo hàm xóa phần tử đầu tiên của danh sách liên kết
        if self.isempty():   # kiểm tra nếu danh sách trống
            print("List is empty") #nếu danh sách trống thì in ra list trống
            return
        e= self._head._element # gán e là giá trị của phần tử đầu tiên danh sách liên kết
        self._head=self._head._next # chúng ta sẽ trỏ head đến phần tử thứ 2, coi như phần tử thứ 2 là phần tử đầu, bỏ qua phần tử đầu tiên
        self._size-=1 # sau khi xóa thì giảm kích thước danh sách liên kết đi 1
        if self.isempty(): # kiểm tra lại nếu sau khi xóa danh sách liên kết trống
            self._tail=None # nếu linkedlist trống thì gán phần tử cuối cùng là None
        return e # trả về giá trị e để in ra giá trị của phần tử đã xóa nêu cần

    def search(self, key):
        """Phương thức để tìm kiếm giá trị key trong danh sách liên kết đơn."""
        p = self._head  # Gán giá trị đầu là p
        index = 0  # Biến index để lưu số thứ tự của phần tử cần tìm
        while p:  # Tạo vòng lặp while
            if p._element == key:  # Nếu giá trị của phần tử hiện tại bằng key cần tìm
                return index  # Trả về giá trị index
            p = p._next  # Duyệt tới phần tử kế tiếp
            index += 1  # Tăng giá trị của index
        return -1  # Nếu không tìm thấy, trả về -1

    def display(self):
        """Phương thức để hiển thị các phần tử trong danh sách liên kết."""
        p = self._head  # Gán p là giá trị đầu của danh sách liên kết
        while p:  # Sử dụng vòng lặp while để duyệt qua danh sách
            print(p._element, end=' --> ')  # In ra giá trị của Node hiện tại, end=' --> ' để tạo dấu nối
            p = p._next  # Di chuyển con trỏ p đến phần tử tiếp theo trong danh sách
        print()  # In một dòng mới để kết thúc danh sách

L = LinkedList()           # Khởi tạo một danh sách liên kết rỗng có tên L
L.addlast(7)               # Thêm phần tử 7 vào cuối danh sách liên kết
L.addlast(4)               # Thêm phần tử 4 vào cuối danh sách liên kết
L.addlast(12)              # Thêm phần tử 12 vào cuối danh sách liên kết
L.display()                # In ra các phần tử trong danh sách liên kết
print('Size:', len(L))     # In ra độ dài của danh sách liên kết
L.addlast(8)               # Thêm phần tử 8 vào danh sách liên kết
L.addlast(3)               # Thêm phần tử 3 vào danh sách liên kết
L.display()                # In ra các phần tử của danh sách liên kết sau khi thêm
print('Size:', len(L))     # In ra độ dài của danh sách liên kết
result = L.search(8)       # Tìm kiếm phần tử có giá trị 8 trong danh sách liên kết
print('Result:', result)   # In kết quả tìm kiếm
L.addfirst(15)             # Chèn phần tử 15 vào đầu danh sách liên kết
L.display()                # In ra danh sách liên kết sau khi chèn
print('Size:', len(L))     # In ra độ dài của danh sách liên kết
L.addany(20,3)             # chèn 20 vào vị trí thứ 3 của danh sách liên kết
L.display()
print('Size:',len(L))      # in ra độ dài của danh sách liên kết
ele = L.removefirst()  # Gọi phương thức removefirst để xóa phần tử đầu tiên và lưu giá trị vào biến 'ele'
L.display()  # Hiển thị danh sách liên kết sau khi xóa phần tử đầu tiên
print('Size:', len(L))  # In ra độ dài của danh sách liên kết
print('Element Removed:', ele)  # In ra giá trị của phần tử đã bị xóa từ đầu danh sách liên kết
