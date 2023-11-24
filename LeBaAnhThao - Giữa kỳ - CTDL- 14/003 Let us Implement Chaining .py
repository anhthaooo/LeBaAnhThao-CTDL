# Import LinkedList class từ file LinkedList
from LinkedList import LinkedList

# Định nghĩa class HashChain
class HashChain:
    # Hàm khởi tạo, tạo bảng băm (hash table) với kích thước mặc định là 10
    def __init__(self):
        self.hashtable_size = 10  # Kích thước của bảng băm
        self.hashtable = [0] * self.hashtable_size  # Tạo một danh sách các đối tượng LinkedList
        # Khởi tạo mỗi đối tượng LinkedList trong danh sách
        for i in range(self.hashtable_size):
            self.hashtable[i] = LinkedList()

    # Hàm băm, trả về mã băm của khóa
    def hashcode(self, key):
        return key % self.hashtable_size
    
    # Hàm chèn phần tử vào bảng băm
    def insert(self, element):
        i = self.hashcode(element)  # Tính mã băm của phần tử
        self.hashtable[i].insertsorted(element)  # Chèn phần tử vào danh sách liên kết ở vị trí mã băm tương ứng
    
    # Hàm tìm kiếm phần tử trong bảng băm
    def search(self, key):
        i = self.hashcode(key)  # Tính mã băm của khóa
        # Kiểm tra xem khóa có tồn tại trong danh sách liên kết tại vị trí mã băm không
        return self.hashtable[i].search(key) != -1

    # Hàm hiển thị nội dung của bảng băm
    def display(self):
        for i in range(self.hashtable_size):
            print('[', i, ']', end=' ')
            self.hashtable[i].display()
        print()

# Tạo một đối tượng HashChain
H = HashChain()
# Chèn các phần tử vào bảng băm
H.insert(54)
H.insert(78)
H.insert(64)
H.insert(92)
H.insert(34)
H.insert(86)
H.insert(28)
# Hiển thị nội dung của bảng băm
H.display()
# Tìm kiếm phần tử có khóa là 74 trong bảng băm và in kết quả
print('Result:', H.search(74))
