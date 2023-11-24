# Hàm A gọi hàm B
def A(x):
    if x > 0:  # Kiểm tra xem x có lớn hơn 0 không
        print(f"Hàm A: {x}")  # In ra thông báo về việc hàm A được gọi với giá trị x
        B(x - 1)  # Gọi hàm B với giá trị nhỏ hơn x

# Hàm B gọi hàm A
def B(y):
    if y > 0:  # Kiểm tra xem y có lớn hơn 0 không
        print(f"Hàm B: {y}")  # In ra thông báo về việc hàm B được gọi với giá trị y
        A(y - 1)  # Gọi hàm A với giá trị nhỏ hơn y

# Gọi hàm A với đối số 3 để bắt đầu đệ quy
A(3)
