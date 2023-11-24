class Student:

    def __init__(self, name, roll, marks):
        self.name = name      # Gán tên học sinh từ tham số truyền vào
        self.roll = roll      # Gán số thứ tự từ tham số truyền vào
        self.marks = marks    # Gán điểm số từ tham số truyền vào
    
    def display(self):
        print('Student Name:', self.name)
        print('Student Roll no :', self.roll)
        print('Student Marks:', self.marks)
        college = ' UCLA'
        print('College name:', Student.college)  # Truy cập biến lớp college
        print()
Student.college = 'UTD'
# Tạo đối tượng S1 của lớp Student với thông tin tùy chỉnh
S1 = Student('aaa', 101, 78.25)

# Tạo đối tượng S2 của lớp Student với thông tin tùy chỉnh
S2 = Student('bbb', 102, 55.65)

# Gọi phương thức display() của đối tượng S1 để hiển thị thông tin của học sinh và tên trường
S1.display()

# Gọi phương thức display() của đối tượng S2 để hiển thị thông tin của học sinh và tên trường
S2.display()
