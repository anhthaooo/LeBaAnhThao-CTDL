# Định nghĩa lớp Student để biểu diễn thông tin của một học sinh
class Student:

    # Hàm khởi tạo của lớp Student, được gọi khi tạo một đối tượng Student mới
    # Nhận ba tham số: name (tên), roll (số thứ tự), và marks (điểm số)
    def __init__(self, name='abc', roll=101, marks=78.25):
        self.name = name      # Gán tên học sinh từ tham số truyền vào hoặc giá trị mặc định
        self.roll = roll      # Gán số thứ tự từ tham số truyền vào hoặc giá trị mặc định
        self.marks = marks    # Gán điểm số từ tham số truyền vào hoặc giá trị mặc định

    # Phương thức display() để in ra thông tin của học sinh
    def display(self):
        print(self.name, self.roll, self.marks)

# Tạo một đối tượng Student với các giá trị mặc định
S = Student()

# Gọi phương thức display() để in ra thông tin của học sinh
S.display()
