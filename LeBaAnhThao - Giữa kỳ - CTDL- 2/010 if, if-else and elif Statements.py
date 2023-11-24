'''
 # Yêu cầu người dùng nhập một số và chuyển đổi thành số nguyên
n = int ( input ('enter value: '))
# In thông báo "Check the Number"
print ( ' Check the Number ')
# Kiểm tra nếu số nhập vào lớn hơn hoặc bằng 0
if n >= 0 :
    # Nếu số không âm, in ra "Positive Number" và giá trị của số
    print ( ' Positive Number ')
    print ( 'Value is:', n )
else : 
    # Nếu số âm, in ra "Negative Number" và giá trị của số
    print( ' Negative Number ' )
    print( 'Value is : ', n )

# In thông báo "End of Program"
print( 'End of Program')

'''
'''
# Yêu cầu người dùng nhập một số và chuyển đổi thành số nguyên
n = int(input('Nhập giá trị: '))

# Kiểm tra nếu số nhập vào lớn hơn hoặc bằng 0
if n >= 0:
    # Nếu số là 0, in ra "Zero Number"
    if n == 0:
        print('Zero Number')
    # Nếu số dương và khác 0, in ra "Positive Number"
    else:
        print('Positive Number')
else:
    # Nếu số âm, in ra "Negative Number"
    print('Negative Number')
'''
# Yêu cầu người dùng nhập một số và chuyển đổi thành số nguyên
n = int(input('Nhập giá trị: '))

# Kiểm tra nếu số nhập vào lớn hơn 0, in ra "Positive Number"
if n > 0:
    print('Positive Number')
# Kiểm tra nếu số nhập vào nhỏ hơn 0, in ra "Negative Number"
elif n < 0:
    print('Negative Number')
# Nếu không thuộc hai trường hợp trên, in ra "Zero Number"
else:
    print('Zero Number')



