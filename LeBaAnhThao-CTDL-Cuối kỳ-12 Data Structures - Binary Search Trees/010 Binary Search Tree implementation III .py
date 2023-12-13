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


    def remove_node(self, data, node):  # Định nghĩa hàm xóa một nút từ cây BST
        if node is None:  # Kiểm tra nếu nút cần xóa tồn tại
            return 
        if data < node.data:  # Nếu dữ liệu cần xóa nhỏ hơn dữ liệu của nút hiện tại
            self.remove_node(data, node.leftChild)  # Tiếp tục tìm kiếm ở nút con bên trái
        elif data > node.data:  # Nếu dữ liệu cần xóa lớn hơn dữ liệu của nút hiện tại
            self.remove_node(data, node.rightChild)  # Tiếp tục tìm kiếm ở nút con bên phải
        else:  # Nếu dữ liệu cần xóa bằng với dữ liệu của nút hiện tại
            if node.leftChild is None and node.rightChild is None:  # Nếu nút hiện tại không có nút con
                print("Removing a leaf node...%d" % node.data)
                parent = node.parent  # Lấy nút cha của nút hiện tại
                if parent is not None and parent.leftChild == node:  # Nếu nút cha tồn tại và nút hiện tại là nút con bên trái của nút cha
                    parent.leftChild = None  # Xóa liên kết từ nút cha đến nút hiện tại
                if parent is not None and parent.rightChild == node:  # Nếu nút cha tồn tại và nút hiện tại là nút con bên phải của nút cha
                    parent.rightChild = None  # Xóa liên kết từ nút cha đến nút hiện tại
                if parent is None:  # Nếu nút cha không tồn tại, có nghĩa là nút hiện tại là nút gốc
                    self.root = None  # Đặt nút gốc của cây thành None
                del node  # Xóa nút hiện tại
            elif node.leftChild is None and node.rightChild is not None:  # Nếu nút hiện tại chỉ có nút con bên phải
                print("Removing a node with single right child..")
                parent = node.parent  # Lấy nút cha của nút hiện tại
                if parent is not None:  # Nếu nút cha tồn tại
                    if parent.leftChild == node:  # Nếu nút hiện tại là nút con bên trái của nút cha
                        parent.leftChild = node.rightChild  # Đặt nút con bên trái của nút cha thành nút con bên phải của nút hiện tại
                    if parent.rightChild == node:  # Nếu nút hiện tại là nút con bên phải của nút cha
                        parent.rightChild = node.rightChild  # Đặt nút con bên phải của nút cha thành nút con bên phải của nút hiện tại
                else:  # Nếu nút cha không tồn tại, có nghĩa là nút hiện tại là nút gốc
                    self.root = node.rightChild  # Đặt nút gốc của cây thành nút con bên phải của nút hiện tại
                node.rightChild.parent = parent  # Đặt nút cha của nút con bên phải của nút hiện tại thành nút cha
                del node  # Xóa nút hiện tại
            elif node.rightChild is None and node.leftChild is not None:  # Nếu nút hiện tại chỉ có nút con bên trái
                print("Removing a node with single left child..")
                parent = node.parent  # Lấy nút cha của nút hiện tại
                if parent is not None:  # Nếu nút cha tồn tại
                    if parent.leftChild == node:  # Nếu nút hiện tại là nút con bên trái của nút cha
                        parent.leftChild = node.leftChild  # Đặt nút con bên trái của nút cha thành nút con bên trái của nút hiện tại
                    if parent.rightChild == node:  # Nếu nút hiện tại là nút con bên phải của nút cha
                        parent.rightChild = node.leftChild  # Đặt nút con bên phải của nút cha thành nút con bên trái của nút hiện tại
                else:  # Nếu nút cha không tồn tại, có nghĩa là nút hiện tại là nút gốc
                    self.root = node.leftChild  # Đặt nút gốc của cây thành nút con bên trái của nút hiện tại
                node.leftChild.parent = parent  # Đặt nút cha của nút con bên trái của nút hiện tại thành nút cha
                del node  # Xóa nút hiện tại
            else:  # Nếu nút hiện tại có cả hai nút con
                print('Removing node with two children...')
                predecessor = self.get_predecessor(node.leftChild)  # Tìm nút tiền nhiệm của nút hiện tại
                temp = predecessor.data  # Lưu giữ dữ liệu của nút tiền nhiệm
                predecessor.data = node.data  # Đặt dữ liệu của nút tiền nhiệm thành dữ liệu của nút hiện tại
                node.data = temp  # Đặt dữ liệu của nút hiện tại thành dữ liệu đã lưu giữ của nút tiền nhiệm
                self.remove_node(data, predecessor)  # Xóa nút tiền nhiệm

    def get_predecessor(self, node):  # Định nghĩa hàm tìm nút tiền nhiệm của một nút nhất định
        if node.rightChild:  # Kiểm tra nếu nút hiện tại có nút con bên phải
            return self.get_predecessor(node.rightChild)  # Nếu có, tiếp tục tìm kiếm ở nút con bên phải
        return node  # Nếu không, trả về nút hiện tại (đây là nút tiền nhiệm)

    def remove(self, data):  # Định nghĩa hàm xóa một nút từ cây BST
        if self.root is not None:  # Kiểm tra nếu cây có nút gốc
            self.remove_node(data, self.root)  # Nếu có, bắt đầu quá trình xóa từ nút gốc


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
bst.insert(1000)
bst.remove(1000)
bst.traverse()