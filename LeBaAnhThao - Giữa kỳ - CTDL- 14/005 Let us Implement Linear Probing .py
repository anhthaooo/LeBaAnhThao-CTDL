# Định nghĩa lớp HashLinearProbe
class HashLinearProbe:
    # Hàm khởi tạo, thiết lập kích thước bảng băm và tạo danh sách băm với giá trị mặc định là 0
    def __init__(self):
        self.hashtable_size = 10  # Kích thước của bảng băm
        self.hashtable = [0] * self.hashtable_size  # Danh sách băm với các giá trị mặc định là 0

    # Hàm băm đơn giản, trả về phần dư khi chia key cho kích thước bảng băm
    def hashcode(self, key):
        return key % self.hashtable_size

    # Hàm thực hiện tìm kiếm tuyến tính để xác định vị trí trống tiếp theo trong bảng băm
    def Iprobe(self, element):
        i = self.hashcode(element)  # Băm phần tử để lấy vị trí ban đầu
        j = 0
        while self.hashtable[(i + j) % self.hashtable_size] != 0:
            # Tìm vị trí trống tiếp theo trong bảng băm
            j = j + 1
        return (i + j) % self.hashtable_size

    # Hàm chèn phần tử vào bảng băm, sử dụng tìm kiếm tuyến tính nếu cần
    def insert(self, element):
        i = self.hashcode(element)  # Băm phần tử để lấy vị trí ban đầu
        if self.hashtable[i] == 0:
            # Nếu vị trí ban đầu trống, chèn phần tử vào đó
            self.hashtable[i] = element
        else:
            # Nếu không, sử dụng tìm kiếm tuyến tính để tìm vị trí tiếp theo và chèn phần tử vào đó
            i = self.Iprobe(element)
            self.hashtable[i] = element

    # Hàm tìm kiếm phần tử trong bảng băm
    def search(self, key):
        i = self.hashcode(key)  # Băm khóa để lấy vị trí ban đầu
        j = 0
        while self.hashtable[(i + j) % self.hashtable_size] != key:
            # Sử dụng tìm kiếm tuyến tính để duyệt qua bảng băm cho đến khi tìm thấy khóa hoặc một ô trống
            if self.hashtable[(i + j) % self.hashtable_size] == 0:
                return False
            j = j + 1
        return True

    # Hàm hiển thị trạng thái của bảng băm
    def display(self):
        print(self.hashtable)

# Tạo một đối tượng của lớp HashLinearProbe
H = HashLinearProbe()

# Chèn các phần tử vào bảng băm
H.insert(54)
H.insert(78)
H.insert(64)
H.insert(92)
H.insert(34)
H.insert(86)
H.insert(28)

# Hiển thị trạng thái của bảng băm
H.display()

# Tìm kiếm khóa 74 trong bảng băm và in kết quả
print('Result:', H.search(74))
