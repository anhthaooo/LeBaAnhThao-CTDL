class QueuesArray:
    def __init__(self):
        # Khởi tạo một queue rỗng bằng cách sử dụng một danh sách (list) trong self._data
        self._data = []

    def __len__(self):
        # Phương thức này trả về độ dài của queue (số lượng phần tử)
        return len(self._data)
    
    def isempty(self):
        # Phương thức này trả về True nếu queue trống, ngược lại trả về False
        return len(self._data) == 0
    
    def enqueue(self, e):
        # Thêm phần tử e vào cuối queue
        self._data.append(e)
    
    def dequeue(self):
        # Loại bỏ và trả về phần tử đầu tiên của queue (nếu có)
        if self.isempty():
            print('Queue is Empty')
            return
        return self._data.pop(0)

    def first(self):
        # Trả về phần tử đầu tiên của queue (nếu có)
        if self.isempty():
            print('Queue is Empty')
            return
        return self._data[0]

# Tạo một đối tượng queue
Q = QueuesArray()

# Thêm các phần tử vào queue
Q.enqueue(5)
Q.enqueue(3)

# In ra nội dung của queue
print(Q._data)  # Output: [5, 3]

# In ra độ dài của queue
print('Length:', len(Q))  # Output: Length: 2

# Thêm thêm phần tử vào queue
Q.enqueue(7)
Q.enqueue(12)

# Loại bỏ phần tử đầu tiên và in ra giá trị đã loại bỏ
print(Q.dequeue())  # Output: 5

# In ra nội dung của queue sau khi loại bỏ phần tử
print(Q._data)  # Output: [3, 7, 12]

# In ra phần tử đầu tiên của queue
print(Q.first())  # Output: 3
