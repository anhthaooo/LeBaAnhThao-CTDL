# Lớp Color định nghĩa hai màu sử dụng trong cây Red-Black: Đỏ và Đen.
class Color:
    RED = 1    # Khai báo màu Đỏ với giá trị là 1
    BLACK = 2  # Khai báo màu Đen với giá trị là 2

# Lớp Node đại diện cho một nút trong cây Red-Black.
class Node:

    # Phương thức khởi tạo nút. Mặc định nút có màu Đỏ và không có cha (parent).
    def __init__(self, data, parent=None, color=Color.RED):
        self.data = data  # Gán dữ liệu cho nút
        self.color = color  # Gán màu sắc cho nút, mặc định là Đỏ
        self.parent = parent  # Gán nút cha, mặc định là None
        self.left = None  # Khởi tạo nút con trái, mặc định là None
        self.right = None  # Khởi tạo nút con phải, mặc định là None

# Lớp RedBlackTree đại diện cho cấu trúc tổng thể của cây Red-Black.
class RedBlackTree:

    # Phương thức khởi tạo cây với nút gốc ban đầu là None.
    def __init__(self):
        self.root = None  # Khởi tạo nút gốc là None

    # Phương thức để chèn dữ liệu mới vào cây.
    def insert(self, data):
        if not self.root:
            self.root = Node(data)  # Nếu cây rỗng, tạo nút mới làm nút gốc
            self.violate(self.root)  # Kiểm tra và giải quyết vi phạm sau khi chèn
        else:
            self.insert_node(data, self.root)  # Gọi phương thức insert_node để chèn nút mới

    # Phương thức đệ quy để chèn nút mới vào cây.
    def insert_node(self, data, node):

        # So sánh dữ liệu và quyết định chèn vào bên trái hoặc phải của nút hiện tại.
        if data < node.data:
            if node.left:
                self.insert_node(data, node.left)  # Chèn vào bên trái nếu nút con trái đã tồn tại
            else:
                node.left = Node(data, node)  # Tạo nút con trái mới nếu trống
                self.violate(node.left)  # Kiểm tra và giải quyết vi phạm sau khi chèn
        else:
            if node.right:
                self.insert_node(data, node.right)  # Chèn vào bên phải nếu nút con phải đã tồn tại
            else:
                node.right = Node(data, node)  # Tạo nút con phải mới nếu trống
                self.violate(node.right)  # Kiểm tra và giải quyết vi phạm sau khi chèn


    def violate(self, node):
        # Khởi tạo biến cho nút cha và nút ông (cha của cha)
        parent_node = None
        grand_parent_node = None

        # Vòng lặp kiểm tra điều kiện vi phạm trong cây Red-Black
        while node != self.root and node.parent.color == Color.RED:
            # Gán nút cha và nút ông cho nút hiện tại
            parent_node = node.parent
            grand_parent_node = parent_node.parent

            # Nếu không có nút ông, thoát khỏi hàm
            if grand_parent_node is None:
                return

            # Kiểm tra nếu nút cha là nút con trái của nút ông
            if parent_node == grand_parent_node.left:
                # Gán nút chú (nút con phải của nút ông)
                uncle = grand_parent_node.right

                # Trường hợp 1 và 4: Nếu nút chú tồn tại và màu của nút chú là đỏ
                if uncle and uncle.color == Color.RED:
                    # Đổi màu nút ông thành đỏ và in ra thông báo
                    print("Re-coloring node %s to RED" % grand_parent_node.data)
                    grand_parent_node.color = Color.RED
                    # Đổi màu nút cha và nút chú thành đen và in ra thông báo
                    print("Re-coloring node %s to BLACK" % parent_node.data)
                    parent_node.color = Color.BLACK
                    uncle.color = Color.BLACK
                    # Gán nút hiện tại là nút ông để tiếp tục kiểm tra
                    node = grand_parent_node
                else:
                    # Trường hợp 2: Nếu nút chú là đen và nút hiện tại là nút con phải
                    if node == parent_node.right:
                        # Xoay trái nút cha
                        self.rotate_left(parent_node)
                        # Cập nhật lại nút hiện tại và nút cha
                        node = parent_node
                        parent_node = node.parent

                    # Trường hợp 3: Đổi màu nút cha thành đen và nút ông thành đỏ, sau đó xoay phải nút ông
                    parent_node.color = Color.BLACK
                    grand_parent_node.color = Color.RED
                    print("Re-color %s to BLACK" % parent_node.data)
                    print("Re-color %s to RED" % grand_parent_node.data)
                    self.rotate_right(grand_parent_node)
            else:
                # Tương tự như trên nhưng xử lý cho trường hợp nút cha là nút con phải của nút ông
                uncle = grand_parent_node.left

                # Trường hợp 1 và 4: Nếu nút chú tồn tại và màu của nút chú là đỏ
                if uncle and uncle.color == Color.RED:
                    # Đổi màu nút ông thành đỏ và in ra thông báo
                    print("Re-coloring node %s to RED" % grand_parent_node.data)
                    grand_parent_node.color = Color.RED
                    # Đổi màu nút cha và nút chú thành đen và in ra thông báo
                    print("Re-coloring node %s to BLACK" % parent_node.data)
                    parent_node.color = Color.BLACK
                    uncle.color = Color.BLACK
                    # Gán nút hiện tại là nút ông để tiếp tục kiểm tra
                    node = grand_parent_node
                else:
                    # Trường hợp 2: Nếu nút chú là đen và nút hiện tại là nút con trái
                    if node == parent_node.left:
                        # Xoay phải nút cha
                        self.rotate_right(parent_node)
                        # Cập nhật lại nút hiện tại và nút cha
                        node = parent_node
                        parent_node = node.parent

                    # Trường hợp 3: Đổi màu nút cha thành đen và nút ông thành đỏ, sau đó xoay trái nút ông
                    parent_node.color = Color.BLACK
                    grand_parent_node.color = Color.RED
                    print("Re-color %s to BLACK" % parent_node.data)
                    print("Re-color %s to RED" % grand_parent_node.data)
                    self.rotate_left(grand_parent_node)

        # Nếu nút gốc có màu đỏ, đổi màu nút gốc thành đen
        if self.root.color == Color.RED:
            print("Recoloring the root to black...")
            self.root.color = Color.BLACK


    def traverse(self):
        # Kiểm tra nếu cây không phải là rỗng
        if self.root is not None:
            # Gọi hàm duyệt cây theo thứ tự inorder bắt đầu từ nút gốc
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        # Nếu nút hiện tại có nút con trái
        if node.left:
            # Duyệt tiếp tục với nút con trái của nút hiện tại
            self.traverse_in_order(node.left)
    


        
    def rotate_right(self, node):
        # In ra thông báo đang xoay phải tại nút có dữ liệu là node.data
        print("Rotating to the right on node ", node.data)

        # Lưu nút con trái của nút hiện tại vào biến temp_left_node
        temp_left_node = node.left
        # Lưu nút con phải của nút con trái vào biến t
        t = temp_left_node.right

        # Đặt nút hiện tại làm nút con phải của nút con trái tạm thời
        temp_left_node.right = node
        # Đặt nút t làm nút con trái mới của nút hiện tại
        node.left = t

        # Nếu nút t không phải là None, cập nhật cha của nó là nút hiện tại
        if t is not None:
            t.parent = node

        # Lưu cha của nút hiện tại vào biến temp_parent
        temp_parent = node.parent
        # Đặt cha mới của nút hiện tại là nút con trái tạm thời
        node.parent = temp_left_node
        # Đặt cha mới của nút con trái tạm thời là cha cũ của nút hiện tại
        temp_left_node.parent = temp_parent

        # Nếu cha của nút con trái tạm thời không phải là None và nút hiện tại là nút con trái của cha đó, cập nhật nút con trái của cha là nút con trái tạm thời
        if temp_left_node.parent is not None and temp_left_node.parent.left == node:
            temp_left_node.parent.left = temp_left_node

        # Nếu cha của nút con trái tạm thời không phải là None và nút hiện tại là nút con phải của cha đó, cập nhật nút con phải của cha là nút con trái tạm thời
        if temp_left_node.parent is not None and temp_left_node.parent.right == node:
            temp_left_node.parent.right = temp_left_node

        # Nếu nút hiện tại là nút gốc của cây, cập nhật nút gốc mới là nút con trái tạm thời
        if node == self.root:
            self.root = temp_left_node

    def rotate_left(self, node):
        # In ra thông báo đang xoay trái tại nút có dữ liệu là node.data
        print("Rotating to the left on node ", node.data)

        # Lưu nút con phải của nút hiện tại vào biến temp_right_node
        temp_right_node = node.right
        # Lưu nút con trái của nút con phải vào biến t
        t = temp_right_node.left

        # Đặt nút hiện tại làm nút con trái của nút con phải tạm thời
        temp_right_node.left = node
        # Đặt nút t làm nút con phải mới của nút hiện tại
        node.right = t

        # Nếu nút t không phải là None, cập nhật cha của nó là nút hiện tại
        if t is not None:
            t.parent = node

        # Lưu cha của nút hiện tại vào biến temp_parent
        temp_parent = node.parent
        # Đặt cha mới của nút hiện tại là nút con phải tạm thời
        node.parent = temp_right_node
        # Đặt cha mới của nút con phải tạm thời là cha cũ của nút hiện tại
        temp_right_node.parent = temp_parent

        # Nếu cha của nút con phải tạm thời không phải là None và nút hiện tại là nút con trái của cha đó, cập nhật nút con trái của cha là nút con phải tạm thời
        if temp_right_node.parent is not None and temp_right_node.parent.left == node:
            temp_right_node.parent.left = temp_right_node

        # Nếu cha của nút con phải tạm thời không phải là None và nút hiện tại là nút con phải của cha đó, cập nhật nút con phải của cha là nút con phải tạm thời
        if temp_right_node.parent is not None and temp_right_node.parent.right == node:
            temp_right_node.parent.right = temp_right_node

        # Nếu nút hiện tại là nút gốc của cây, cập nhật nút gốc mới là nút con phải tạm thời
        if node == self.root:
            self.root = temp_right_node



rbt = RedBlackTree()
rbt.insert(32)
rbt.insert(10)
rbt.insert(55)
rbt.insert(1)
rbt.insert(19)
rbt.insert(79)
rbt.insert(16)
rbt.insert(23)
rbt.insert(12)

rbt.traverse()

