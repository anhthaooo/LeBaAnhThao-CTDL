x = True
y = False

# Sử dụng toán tử AND logic để kiểm tra x và y
ket_qua1 = x and y
# Khi sử dụng AND, cả hai biểu thức phải là True để kết quả là True.
# Trong trường hợp này, x là True và y là False, vì vậy kết quả của x and y là False.

# Sử dụng toán tử OR logic để kiểm tra x hoặc y
ket_qua2 = x or y
# Khi sử dụng OR, chỉ cần một trong hai biểu thức là True để kết quả là True.
# Trong trường hợp này, x là True, vì vậy kết quả của x or y là True.

# Sử dụng toán tử NOT logic để đảo ngược giá trị của biến x
ket_qua3 = not x
# Toán tử NOT đảo ngược giá trị của biểu thức. Nếu x là True, thì not x là False, và ngược lại.

# In kết quả ra màn hình
print("Kết quả của x and y:", ket_qua1)  # Kết quả: False
print("Kết quả của x or y:", ket_qua2)   # Kết quả: True
print("Kết quả của not x:", ket_qua3)    # Kết quả: False
