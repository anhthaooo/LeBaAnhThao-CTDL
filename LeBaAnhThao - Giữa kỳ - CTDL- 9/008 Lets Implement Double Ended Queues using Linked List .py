class _Node:
    # Định nghĩa một lớp _Node đại diện cho một nút trong danh sách liên kết.
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        # Hàm khởi tạo của lớp _Node, tạo một nút với phần tử và nút kế tiếp.
        self._element = element
        self._next = next 

class DEQueLinked:
    # Định nghĩa lớp DEQueLinked đại diện cho deque được triển khai bằng danh sách liên kết.
    def __init__(self):
        # Hàm khởi tạo của deque, khởi tạo front, rear và size.
        self._front = None
        self._rear = None 
        self._size = 0 

    def __len__(self):
        # Trả về kích thước của deque khi len() được gọi.
        return self._size 
    
    def isempty(self):
        # Kiểm tra xem deque có rỗng không.
        return self._size == 0 
    
    def addlast(self, e):
        # Thêm một phần tử vào cuối deque.
        newest = _Node(e, None)
        if self.isempty():
            # Nếu deque rỗng, đặt cả hai con trỏ _front và _rear vào newest.
            self._front = newest 
        else: 
            # Ngược lại, cập nhật next của rear để trỏ đến newest.
            self._rear._next = newest 
        # Cập nhật con trỏ _rear để trỏ đến newest.
        self._rear = newest 
        # Tăng kích thước của deque.
        self._size += 1

    def addfirst(self, e):
        # Thêm một phần tử vào đầu deque.
        newest = _Node(e, None)
        if self.isempty():
            # Nếu deque rỗng, đặt cả hai con trỏ _front và _rear vào newest.
            self._front = newest 
            self._rear = newest
        else:
            # Ngược lại, cập nhật next của newest để trỏ đến _front, sau đó di chuyển _front đến newest.
            newest._next = self._front
            self._front = newest 
        # Tăng kích thước của deque.
        self._size += 1

    def removefirst(self):
        # Loại bỏ và trả về phần tử từ đầu deque.
        if self.isempty():
            # In thông báo nếu deque rỗng và trả về None.
            print('List is empty')
            return 
        # Lấy phần tử tại _front.
        e = self._front._element
        # Cập nhật _front để trỏ đến phần tử tiếp theo.
        self._front = self._front._next
        # Giảm kích thước của deque.
        self._size -= 1 
        # Nếu deque trở nên rỗng, cập nhật _rear thành None.
        if self.isempty():
            self._rear = None
        # Trả về phần tử đã loại bỏ.
        return e 
    
    def removelast(self):
        # Loại bỏ và trả về phần tử từ cuối deque.
        if self.isempty():
            # In thông báo nếu deque rỗng và trả về None.
            print('List is empty')
            return 
        # Duyệt deque để đến phần tử trước phần tử cuối cùng.
        p = self._front
        i = 1 
        while i < len(self) - 1:
            p = p._next
            i = i + 1 
        # Cập nhật _rear để trỏ đến phần tử trước phần tử cuối cùng.
        self._rear = p 
        # Di chuyển p đến phần tử cuối cùng.
        p = p._next
        # Lấy phần tử cuối cùng.
        e = p._element 
        # Cắt liên kết với phần tử cuối cùng.
        self._rear._next = None 
        # Giảm kích thước của deque.
        self._size -= 1 
        # Trả về phần tử đã loại bỏ.
        return e 
        
    def display(self):
        # Duyệt deque và in các phần tử.
        p = self._front
        while p: 
            print(p._element, end='-->')
            p = p._next
        print()

    def search(self, key):
        # Tìm kiếm phần tử trong deque và trả về chỉ số nếu tìm thấy, ngược lại trả về -1.
        p = self._front
        index = 0 
        while p:
            if p._element == key:
                return index 
            p = p._next
            index = index + 1 
        return -1 

# Tạo một đối tượng DEQueLinked.
D = DEQueLinked()
# Thêm các phần tử vào deque.
D.addfirst(5)
D.addfirst(3)
D.addfirst(7)
D.addlast(12)
# Hiển thị các phần tử của deque.
D.display()
# In độ dài của deque.
print('Length:', len(D))
# Loại bỏ phần tử từ đầu deque và in nó.
print(D.removefirst())
# Loại bỏ phần tử từ cuối deque và in nó.
print(D.removelast())
# Hiển thị các phần tử của deque sau khi loại bỏ.
D.display()

