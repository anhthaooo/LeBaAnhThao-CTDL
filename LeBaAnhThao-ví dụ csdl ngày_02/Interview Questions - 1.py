def sum_of_digits(n):
    if n == 0:
        return 0
    elif n < 0:
        n = abs(n)
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

# Nhập một số từ người dùng
user_input = input("Nhập một số nguyên: ")

try:
    n = int(user_input)
    result = sum_of_digits(n)
    print(f"Tổng các chữ số của {n} là {result}")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")

