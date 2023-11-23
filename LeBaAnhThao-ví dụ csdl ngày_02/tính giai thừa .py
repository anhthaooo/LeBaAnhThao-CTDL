def tinh_giai_thua(n):
    if n == 0:
        return 1
    else:
        return n * tinh_giai_thua(n - 1)

def main():
    user_input = input("Nhập một số nguyên dương : ")

    try:
        n = float(user_input)
        if n < 0:
            print("Không thể tính giai thừa cho số âm.")
        elif n != int(n):
            print("Không thể tính giai thừa cho số thập phân.")
        else:
            n = int(n)
            ket_qua = tinh_giai_thua(n)
            print(f"{n}! = {ket_qua}")
    except ValueError:
        print("Không phải là một số hợp lệ.")

if __name__ == "__main__":
    main()
