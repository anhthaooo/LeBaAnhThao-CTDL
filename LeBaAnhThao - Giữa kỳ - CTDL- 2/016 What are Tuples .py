# Tạo một tuple chứa thông tin về một sản phẩm
product_info = ("Laptop", 999.99, 1000)

# Truy cập và in ra các thông tin trong tuple
print("Loại sản phẩm:", product_info[0])
print("Giá sản phẩm:", product_info[1])
print("Số lượng còn lại:", product_info[2])

# Tuple lồng nhau
seller_info = ("Anh Thảo ", "anhthao@gmail.com")
product_with_seller = (product_info, seller_info)

# Truy cập thông tin người bán trong tuple lồng nhau
print("Tên người bán:", product_with_seller[1][0])
print("Email người bán:", product_with_seller[1][1])
