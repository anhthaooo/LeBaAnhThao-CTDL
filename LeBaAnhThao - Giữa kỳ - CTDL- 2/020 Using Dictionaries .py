# Tạo một từ điển (dictionary) d với các cặp khóa-đối tượng
d = {'USA': 100, 'UK': 200, 'India': 300}

# In ra toàn bộ từ điển d
print(d)
# Kết quả: {'USA': 100, 'UK': 200, 'India': 300}
# Giải thích: In ra toàn bộ từ điển d, nơi mỗi khóa (quốc gia) đi kèm với một giá trị (số dân số).

# In ra số lượng cặp khóa-đối tượng trong từ điển d
print(len(d))
# Kết quả: 3
# Giải thích: Hàm len(d) trả về số lượng cặp khóa-đối tượng trong từ điển d, trong trường hợp này là 3.

# Truy cập và in ra giá trị của các khóa cụ thể trong từ điển d
print(d['USA'])   # Truy cập giá trị của khóa 'USA'
print(d['UK'])    # Truy cập giá trị của khóa 'UK'
print(d['India']) # Truy cập giá trị của khóa 'India'

# Kết quả:
# 100
# 200
# 300
# Giải thích: Chúng ta truy cập và in ra giá trị của các khóa 'USA', 'UK', và 'India' trong từ điển d.

# Thêm một cặp khóa-đối tượng mới vào từ điển d
d['Aus'] = 400

# In ra toàn bộ từ điển d sau khi thêm khóa 'Aus'
print(d)
# Kết quả: {'USA': 100, 'UK': 200, 'India': 300, 'Aus': 400}
# Giải thích: Sau khi thêm cặp khóa-đối tượng mới 'Aus': 400 vào từ điển d, nó xuất hiện trong danh sách.

# In ra danh sách các khóa (keys) trong từ điển d
print(d.keys())
# Kết quả: dict_keys(['USA', 'UK', 'India', 'Aus'])
# Giải thích: Hàm keys() trả về danh sách các khóa trong từ điển d.

# In ra danh sách các giá trị (values) trong từ điển d
print(d.values())
# Kết quả: dict_values([100, 200, 300, 400])
# Giải thích: Hàm values() trả về danh sách các giá trị trong từ điển d.
