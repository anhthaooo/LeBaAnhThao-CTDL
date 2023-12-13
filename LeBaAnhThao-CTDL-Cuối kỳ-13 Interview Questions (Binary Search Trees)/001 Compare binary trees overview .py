# Định nghĩa lớp Node, đại diện cho một nút trong cây nhị phân
class Node:
    # Hàm khởi tạo của lớp, được gọi khi tạo một đối tượng Node mới
    def __init__(self, data):
        self.data = data  # Lưu giữ dữ liệu cho nút
        self.left = None  # Khởi tạo con trái của nút, mặc định là None
        self.right = None # Khởi tạo con phải của nút, mặc định là None

# Định nghĩa hàm để kiểm tra xem hai cây nhị phân có giống nhau không
def identicalTrees(a, b):
    # Kiểm tra xem cả hai nút đều là None, tức là cả hai cây đều trống
    if a is None and b is None:
        return True

    # Kiểm tra xem cả hai nút đều không phải là None và dữ liệu của chúng có giống nhau không
    # Nếu có, tiếp tục kiểm tra đệ quy cho cặp con trái và con phải
    if a is not None and b is not None:
        return ((a.data == b.data) and
                identicalTrees(a.left, b.left) and
                identicalTrees(a.right, b.right))

    # Nếu một trong hai nút là None hoặc dữ liệu không giống nhau, trả về False
    return False

# Tạo nút gốc cho cây nhị phân thứ nhất
root1 = Node(1)
# Tạo con trái và con phải cho root1
root1.left = Node(2)
root1.right = Node(3)
# Tạo con trái và con phải cho nút con trái của root1
root1.left.left = Node(4)
root1.left.right = Node(5)

# Tạo nút gốc cho cây nhị phân thứ hai tương tự như cây thứ nhất
root2 = Node(1)
# Tạo con trái và con phải cho root2
root2.left = Node(2)
root2.right = Node(3)
# Tạo con trái và con phải cho nút con trái của root2
root2.left.left = Node(4)
root2.left.right = Node(5)

# Điều kiện này đảm bảo rằng đoạn mã dưới đây chỉ được thực thi khi file này là script chính
if __name__ == "__main__":
    # Gọi hàm identicalTrees với hai cây root1 và root2
    # In ra kết quả: True nếu hai cây giống nhau, False nếu không giống
    if identicalTrees(root1, root2):
        print("True")
    else:
        print("False")
