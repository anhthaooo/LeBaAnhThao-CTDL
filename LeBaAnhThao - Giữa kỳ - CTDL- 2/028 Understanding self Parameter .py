# Định nghĩa lớp Student để biểu diễn thông tin của một học sinh
class Student:

    # Hàm khởi tạo của lớp Student, được gọi khi tạo một đối tượng Student mới
    # Nhận ba tham số: name (tên), roll (số thứ tự), và marks (điểm số)
    def __init__(self, name, roll, marks):
        self.name = name      # Gán tên học sinh từ tham số truyền vào
        self.roll = roll      # Gán số thứ tự từ tham số truyền vào
        self.marks = marks    # Gán điểm số từ tham số truyền vào
    
    # Phương thức display() để in ra thông tin của học sinh
    def display(abc):
        print('Student Name:', abc.name)
        print('Student Roll no :', abc.roll)
        print('Student Marks:', abc.marks)
        print()

# Tạo một đối tượng Student với các giá trị tùy chỉnh (tên 'aaa', số thứ tự 101, và điểm số 78.25)
S = Student('aaa', 101, 78.25)

# Gọi phương thức display() của đối tượng S để hiển thị thông tin của học sinh
S.display()
