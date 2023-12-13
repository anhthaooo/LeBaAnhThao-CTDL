# Định nghĩa lớp Node
class Node: 
    # Hàm khởi tạo cho lớp Node
    def __init__(self, data, parent):
        self.data = data  # Dữ liệu chứa trong nút
        self.leftChild = None  # Con trỏ đến nút con bên trái
        self.rightChild = None  # Con trỏ đến nút con bên phải
        self.parent = parent  # Con trỏ đến nút cha

# Định nghĩa lớp BinarySearchTree
class BinarySearchTree:
    # Hàm khởi tạo cho lớp BinarySearchTree
    def __init__(self):
        self.root = None  # Con trỏ đến nút gốc của cây

    # Phương thức để chèn một nút mới vào cây
    def insert(self, data):
        if self.root is None:  # Nếu cây đang trống
            self.root = Node(data, None)  # Tạo nút mới làm nút gốc
        else:  # Nếu cây không trống
            self.insert_node(data, self.root)  # Gọi phương thức insert_node

    # Phương thức đệ quy để tìm vị trí phù hợp để chèn nút mới
    def insert_node(self, data, node):
        if data < node.data:  # Nếu dữ liệu của nút mới nhỏ hơn dữ liệu của nút hiện tại
            if node.leftChild:  # Nếu nút con bên trái tồn tại
                self.insert_node(data,node.leftChild)  # Di chuyển sang nút con bên trái
            else:  # Nếu nút con bên trái không tồn tại
                node.leftChild = Node(data, node)  # Chèn nút mới tại đó
        else:  # Nếu dữ liệu của nút mới lớn hơn hoặc bằng dữ liệu của nút hiện tại
            if node.rightChild:  # Nếu nút con bên phải tồn tại
                self.insert_node(data, node.rightChild)  # Di chuyển sang nút con bên phải
            else:  # Nếu nút con bên phải không tồn tại
                node.rightChild = Node(data, node)  # Chèn nút mới tại đó

    
    def traverse(self):  # Định nghĩa hàm duyệt qua cây BST
        if self.root is not None:  # Kiểm tra nếu cây có nút gốc
            self.traverse_in_order(self.root)  # Nếu có, bắt đầu duyệt từ nút gốc

    def get_max_value(self):  # Định nghĩa hàm lấy giá trị lớn nhất trong cây
        if self.root is not None:  # Kiểm tra nếu cây có nút gốc
            return self.get_max(self.root)  # Nếu có, bắt đầu tìm giá trị lớn nhất từ nút gốc

    def get_max(self, node):  # Định nghĩa hàm tìm giá trị lớn nhất từ một nút chỉ định
        if node.rightChild:  # Kiểm tra nếu nút hiện tại có nút con bên phải
            return self.get_max(node.rightChild)  # Nếu có, tiếp tục tìm kiếm ở nút con bên phải
        return node.data  # Nếu không, trả về giá trị của nút hiện tại (đây là giá trị lớn nhất)

    def get_min_value(self):  # Định nghĩa hàm lấy giá trị nhỏ nhất trong cây
        if self.root is not None:  # Kiểm tra nếu cây có nút gốc
            return self.get_min(self.root)  # Nếu có, bắt đầu tìm giá trị nhỏ nhất từ nút gốc

    def get_min(self, node):  # Định nghĩa hàm tìm giá trị nhỏ nhất từ một nút chỉ định
        if node.leftChild:  # Kiểm tra nếu nút hiện tại có nút con bên trái
            return self.get_min(node.leftChild)  # Nếu có, tiếp tục tìm kiếm ở nút con bên trái
        return node.data  # Nếu không, trả về giá trị của nút hiện tại (đây là giá trị nhỏ nhất)

    def traverse_in_order(self, node):  # Định nghĩa hàm duyệt qua cây BST theo thứ tự từ trái qua phải
        if node.leftChild:  # Kiểm tra nếu nút hiện tại có nút con bên trái
            self.traverse_in_order(node.leftChild)  # Nếu có, tiếp tục duyệt ở nút con bên trái
        print('%s' % node.data)  # In giá trị của nút hiện tại
        if node.rightChild:  # Kiểm tra nếu nút hiện tại có nút con bên phải
            self.traverse_in_order(node.rightChild)  # Nếu có, tiếp tục duyệt ở nút con bên phải


# Tạo một đối tượng mới của lớp BinarySearchTree
bst = BinarySearchTree()
# Chèn các nút mới vào cây với dữ liệu tương ứng là 10, 5, 66, -5, 1, 99, 34
bst.insert(10)
bst.insert(5)
bst.insert(66)
bst.insert(-5)
bst.insert(1)
bst.insert(99)
bst.insert(34)
bst.insert(-1000)
# In ra giá trị lớn nhất trong cây
print('Max item: %d'%bst.get_max_value())
# In ra giá trị nhỏ nhất trong cây
print('Min item: %d'%bst.get_min_value())
# Duyệt qua tất cả các nút trong cây và in ra dữ liệu của chúng
bst.traverse()
