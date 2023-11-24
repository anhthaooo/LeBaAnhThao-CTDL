# Định nghĩa lớp Student để biểu diễn thông tin của một học sinh
class Student:

    # Hàm khởi tạo của lớp Student, được gọi khi tạo một đối tượng Student mới
    # Nhận ba tham số: name (tên), roll (số thứ tự), và marks (điểm số)
    def __init__(self, name, roll, marks):
        self.name = name      # Gán tên học sinh
        self.roll = roll      # Gán số thứ tự
        self.marks = marks    # Gán điểm số

    # Phương thức này trả về một chuỗi mô tả của đối tượng lớp, không được sử dụng trong code này
    def __str__(self):
        return 'This is student class'

    # Phương thức display() được sử dụng để in ra thông tin của học sinh
    def display(self):
        print('Student Name:', self.name)
        print('Roll Number:', self.roll)
        print('Marks:', self.marks)

# Tạo danh sách (S) chứa ba đối tượng Student với thông tin tùy chỉnh
S = [Student('aaa', 101, 78.25),
     Student('bbb', 102, 62.55),
     Student('ccc', 103, 87.45)]

# Duyệt qua từng đối tượng Student trong danh sách và gọi phương thức display() để in ra thông tin của học sinh
for i in S:
    i.display()
