# Định nghĩa hàm fibonacci với tham số n
def fibonacci(n):
    # Trường hợp cơ sở: Nếu n nhỏ hơn hoặc bằng 1
    if n <= 1:
        return n  # Trả về n và kết thúc đệ quy

    # Trường hợp đệ quy: Nếu n lớn hơn 1
    else:
        # Gọi hàm fibonacci chính nó với n-1 và n-2,
        # sau đó cộng kết quả lại với nhau
        return fibonacci(n - 1) + fibonacci(n - 2)

# Sử dụng hàm để tính số Fibonacci thứ 10
result = fibonacci(10)

# In ra kết quả
print("Số Fibonacci thứ 10 là:", result)
