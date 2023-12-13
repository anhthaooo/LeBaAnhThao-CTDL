# Định nghĩa lớp HashTable để biểu diễn một bảng băm.
class HashTable:

    # Hàm khởi tạo của HashTable.
    def __init__(self):
        # Dựa trên yếu tố tải, chúng ta có thể thay đổi kích thước
        # của cấu trúc dữ liệu nền (thay đổi kích thước động).
        self.capacity = 10  # Dung lượng của bảng băm.
        self.keys = [None] * self.capacity  # Mảng lưu trữ khóa.
        self.values = [None] * self.capacity  # Mảng lưu trữ giá trị.

    # Phương thức để chèn một cặp khóa-giá trị vào bảng băm.
    def insert(self, key, data):
        # Tìm vị trí hợp lệ cho giá trị (data) dựa vào khóa.
        index = self.hash_function(key)

        # Có thể xảy ra va chạm, nghĩa là vị trí đã được chiếm.
        while self.keys[index] is not None:
            # Đôi khi cần cập nhật giá trị nếu khóa đã tồn tại.
            if self.keys[index] == key:
                self.values[index] = data
                return

            # Sử dụng phương pháp tuyến tính để thử vị trí tiếp theo.
            index = (index + 1) % self.capacity

        # Đã tìm được vị trí hợp lệ, chèn dữ liệu vào.
        self.keys[index] = key
        self.values[index] = data

    # Phương thức để lấy giá trị dựa vào khóa.
    def get(self, key):
        # Tìm vị trí hợp lệ cho giá trị dựa vào khóa.
        index = self.hash_function(key)

        while self.keys[index] is not None:
            # Khi tìm thấy mục tiêu cần tìm.
            if self.keys[index] == key:
                return self.values[index]

            index = (index + 1) % self.capacity

        # Không tồn tại cặp khóa-giá trị với khóa cho trước trong bảng băm.
        return None

    # Hàm băm: Tính giá trị băm (chỉ số của mảng) dựa trên khóa.
    def hash_function(self, key):
        hash_sum = 0
        # Tính tổng giá trị băm từ từng ký tự của khóa.
        for letter in key:
            hash_sum = hash_sum + ord(letter)

        return hash_sum % self.capacity


# Đoạn mã thử nghiệm.
if __name__ == '__main__':
    # Tạo một đối tượng HashTable.
    table = HashTable()
    # Chèn dữ liệu vào bảng băm.
    table.insert('Adam', 23)
    table.insert('Kevin', 45)
    table.insert('Daniel', 34)
    table.insert('Daniel', 33)  # Cập nhật giá trị cho 'Daniel'

    # Lấy và in giá trị cho khóa 'Daniel'.
    print(table.get('Daniel'))  # Kết quả là 33
