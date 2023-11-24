# Định nghĩa lớp DEQueArray để tạo một deque sử dụng danh sách trong Python
class DEQueArray:
    # Phương thức khởi tạo, tạo ra một deque mới với danh sách rỗng
    def __init__(self):
        self._data = []

    # Phương thức trả về độ dài (số lượng phần tử) của deque
    def __len__(self):
        return len(self._data)
    
    # Phương thức kiểm tra xem deque có rỗng không
    def isempty(self):
        return len(self._data) == 0
    
    # Phương thức thêm phần tử vào đầu deque
    def addfirst(self, e):
        self._data.insert(0, e)

    # Phương thức thêm phần tử vào cuối deque
    def addlast(self, e):
        self._data.append(e)
    
    # Phương thức loại bỏ và trả về phần tử ở đầu deque
    def removefirst(self):
        if self.isempty():
            print('DEQue is Empty')
            return
        return self._data.pop(0)
    
    # Phương thức loại bỏ và trả về phần tử ở cuối deque
    def removelast(self):
        if self.isempty():
            print('DEQue is empty ')
            return
        return self._data.pop()
    
    # Phương thức trả về phần tử ở đầu deque
    def first(self):
        if self.isempty():
            print('DEQue is Empty')
            return
        return self._data[-1]

# Tạo một đối tượng DEQueArray mới
D = DEQueArray()

# Thêm các phần tử vào đầu deque
D.addfirst(5)   
D.addfirst(3)  
D.addfirst(7)  
D.addfirst(12) 

# In ra nội dung của deque
print(D._data)

# In ra độ dài của deque sử dụng phương thức __len__
print('Length:', len(D))

# Gọi phương thức removefirst để loại bỏ phần tử ở đầu deque và in ra giá trị đã loại bỏ
print(D.removefirst())

# Gọi phương thức removelast để loại bỏ phần tử ở cuối deque và in ra giá trị đã loại bỏ
print(D.removelast())

# In ra nội dung của deque sau các thay đổi
print(D._data)

# Gọi phương thức first để in ra phần tử ở đầu deque
print('First Element:', D.first())

# Sử dụng phương thức first để in ra phần tử ở cuối deque
print('Last Element:', D.first())
