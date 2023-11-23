def fibonacci(n):
    if n < 0:
        return "Không có số Fibonacci nào cho n < 0"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    user_input = input("Nhập một số nguyên dương: ")

    try:
        n = int(user_input)
        if n < 0:
            print("Vui lòng nhập số nguyên dương hoặc 0.")
        else:
            ket_qua = fibonacci(n)
            print(f"Số Fibonacci thứ {n} là {ket_qua}")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")

if __name__ == "__main__":
    main()
