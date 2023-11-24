# Định nghĩa hàm display() để hiển thị chuỗi văn bản "Hello" và "Python"
def display():
    print('Hello')  # In ra màn hình chuỗi "Hello"
    print('Python')  # In ra màn hình chuỗi "Python"

# Định nghĩa hàm mysum(a, b) để thực hiện phép cộng hai số và trả về kết quả
def mysum(a, b):
    c = a + b  # Thực hiện phép cộng và lưu kết quả vào biến c
    return c  # Trả về giá trị của biến c

# Định nghĩa hàm mymul(a, b) để thực hiện phép nhân hai số và trả về kết quả
def mymul(a, b):
    c = a * b  # Thực hiện phép nhân và lưu kết quả vào biến c
    return c  # Trả về giá trị của biến c

# Gọi hàm display() để hiển thị thông điệp "Hello" và "Python" trên màn hình
display()  # Kết quả: Hello Python

# Gọi hàm mysum(2, 5) và lưu kết quả vào biến x
x = mysum(2, 5)

# In ra giá trị của biến x
print(x)  # Kết quả: 7 (2 + 5 = 7)

# Gọi hàm mymul(2, 5) và lưu kết quả vào biến y
y = mymul(2, 5)

# In ra giá trị của biến y
print(y)  # Kết quả: 10 (2 * 5 = 10)
