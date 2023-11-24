l1 = [10, 54, 2, 61, 15]  # Tạo danh sách l1 với các giá trị
l2 = [2, 61, 15, 10, 54]  # Tạo danh sách l2 với các giá trị

# Kiểm tra xem l1 và l2 có cùng tham chiếu không (cùng một địa chỉ bộ nhớ)
print(l1 is l2)  # Kết quả: False
# Giải thích: l1 và l2 là hai danh sách khác nhau về mặt tham chiếu, nghĩa là chúng trỏ đến các vị trí bộ nhớ khác nhau.

# So sánh l1 và l2 theo giá trị
print(l1 == l2)  # Kết quả: False
# Giải thích: Toán tử == so sánh giá trị của các phần tử trong danh sách l1 và l2. 
# Mặc dù chúng có cùng số lượng phần tử và giá trị, nhưng thứ tự khác nhau, nên kết quả là False.

l2 = l1  # Gán l1 cho l2

# Kiểm tra xem l1 và l2 có cùng tham chiếu không sau khi gán
print(l1 is l2)  # Kết quả: True
# Giải thích: Sau khi gán l1 cho l2, l1 và l2 thực sự trỏ đến cùng một danh sách trong bộ nhớ.
