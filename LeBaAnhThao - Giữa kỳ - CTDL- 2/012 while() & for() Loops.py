'''# Yêu cầu người dùng nhập một giá trị nguyên và lưu vào biến n
n = int(input('enter value:: '))

# In ra thông điệp để thông báo về việc in các số từ 1 đến n
print('Number from 1 to', n)

# Khởi tạo biến i với giá trị 1 để sử dụng cho vòng lặp
i = 1

# Bắt đầu vòng lặp while, sẽ tiếp tục cho đến khi i > n
while i <= n:
    # In ra giá trị hiện tại của i
    print(i)
    
    # Tăng giá trị của i lên 1 để chuẩn bị cho vòng lặp tiếp theo
    i = i + 1

# In ra thông điệp để thông báo về kết thúc chương trình
print('End of Program')
'''
# Tạo một đối tượng range bắt đầu từ 10, kết thúc ở 1 (không bao gồm 0), và bước nhảy là -1.
x = range(10, 0, -1)

# In ra đối tượng range. Lưu ý rằng đối tượng range này chưa được biểu diễn dưới dạng danh sách.
print(x)

# Bắt đầu vòng lặp for để lặp qua các phần tử của đối tượng range x.
for i in x:
    # In ra giá trị của i trong đối tượng range x.
    print(i)

    