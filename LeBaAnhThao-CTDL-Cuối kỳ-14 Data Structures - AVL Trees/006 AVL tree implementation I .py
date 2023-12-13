class Node:
    # Constructor của class Node để tạo một nút mới.
    def __init__(self, data, parent):
        self.data = data  # Giá trị của nút
        self.left_node = None  # Con trái của nút, ban đầu là None
        self.right_node = None  # Con phải của nút, ban đầu là None
        self.parent = parent  # Nút cha của nút hiện tại
        self.height = 0  # Chiều cao của nút, quan trọng cho việc cân bằng cây AVL

class AVLTree:
    # Constructor của class AVLTree để tạo một cây AVL mới.
    def __init__(self):
        self.root = None  # Nút gốc của cây AVL, ban đầu là None

    def remove(self, data):
        if self.root:  # Nếu cây không rỗng
            self.remove_node(data, self.root)  # Gọi hàm xóa nút

    def insert(self, data):
        if self.root is None:  # Nếu cây rỗng
            self.root = Node(data, None)  # Tạo nút gốc mới
        else:
            self.insert_node(data, self.root)  # Nếu không, gọi hàm chèn nút

    def insert_node(self, data, node):
        if data < node.data:  # Nếu dữ liệu cần chèn nhỏ hơn dữ liệu của nút hiện tại
            if node.left_node:  # Nếu con trái tồn tại
                self.insert_node(data, node.left_node)  # Chèn vào con trái
            else:
                node.left_node = Node(data, node)  # Nếu không, tạo nút con trái mới
                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1  # Cập nhật chiều cao của nút
        else:  # Nếu dữ liệu cần chèn lớn hơn hoặc bằng dữ liệu của nút hiện tại
            if node.right_node:  # Nếu con phải tồn tại
                self.insert_node(data, node.right_node)  # Chèn vào con phải
            else:
                node.right_node = Node(data, node)  # Nếu không, tạo nút con phải mới
                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1  # Cập nhật chiều cao của nút
        self.handle_violation(node)  # Kiểm tra và xử lý vi phạm cân bằng

    def remove_node(self, data, node):
        if node is None:  # Nếu nút không tồn tại
            return

        if data < node.data:  # Nếu dữ liệu cần xóa nhỏ hơn dữ liệu của nút hiện tại
            self.remove_node(data, node.left_node)  # Xóa ở con trái
        elif data > node.data:  # Nếu dữ liệu cần xóa lớn hơn dữ liệu của nút hiện tại
            self.remove_node(data, node.right_node)  # Xóa ở con phải
        else:  # Nếu dữ liệu cần xóa bằng dữ liệu của nút hiện tại
            if node.left_node is None and node.right_node is None:  # Nếu nút là nút lá
                print("Xóa một nút lá...%d" % node.data)  # In thông báo xóa nút lá
                parent = node.parent  # Lưu nút cha của nút hiện tại
                if parent:  # Nếu nút cha tồn tại
                    if parent.left_node == node:  # Nếu nút hiện tại là con trái của nút cha
                        parent.left_node = None  # Xóa liên kết đến nút hiện tại
                    elif parent.right_node == node:  # Nếu nút hiện tại là con phải của nút cha
                        parent.right_node = None  # Xóa liên kết đến nút hiện tại
                else:  # Nếu không có nút cha, tức nút hiện tại là nút gốc
                    self.root = None  # Đặt nút gốc của cây là None
                del node  # Xóa nút khỏi bộ nhớ
                self.handle_violation(parent)  # Kiểm tra và xử lý vi phạm cân bằng từ nút cha

            elif node.left_node is None and node.right_node is not None:  # Nếu nút chỉ có con phải
                print("Xóa một nút có một con phải...")  # In thông báo xóa nút có một con phải
                parent = node.parent  # Lưu nút cha của nút hiện tại
                if parent:  # Nếu nút cha tồn tại
                    if parent.left_node == node:  # Nếu nút hiện tại là con trái của nút cha
                        parent.left_node = node.right_node  # Đặt con phải của nút hiện tại làm con trái của nút cha
                    else:  # Nếu nút hiện tại là con phải của nút cha
                        parent.right_node = node.right_node  # Đặt con phải của nút hiện tại làm con phải của nút cha
                else:  # Nếu không có nút cha, tức nút hiện tại là nút gốc
                    self.root = node.right_node  # Đặt con phải của nút hiện tại làm nút gốc mới
                node.right_node.parent = parent  # Cập nhật nút cha cho con phải của nút hiện tại
                del node  # Xóa nút khỏi bộ nhớ
                self.handle_violation(parent)  # Kiểm tra và xử lý vi phạm cân bằng từ nút cha

            elif node.right_node is None and node.left_node is not None:  # Nếu nút chỉ có con trái
                print("Xóa một nút có một con trái...")  # In thông báo xóa nút có một con trái
                parent = node.parent  # Lưu nút cha của nút hiện tại
                if parent:  # Nếu nút cha tồn tại
                    if parent.left_node == node:  # Nếu nút hiện tại là con trái của nút cha
                        parent.left_node = node.left_node  # Đặt con trái của nút hiện tại làm con trái của nút cha
                    else:  # Nếu nút hiện tại là con phải của nút cha
                        parent.right_node = node.left_node  # Đặt con trái của nút hiện tại làm con phải của nút cha
                else:  # Nếu không có nút cha, tức nút hiện tại là nút gốc
                    self.root = node.left_node  # Đặt con trái của nút hiện tại làm nút gốc mới
                node.left_node.parent = parent  # Cập nhật nút cha cho con trái của nút hiện tại
                del node  # Xóa nút khỏi bộ nhớ
                self.handle_violation(parent)  # Kiểm tra và xử lý vi phạm cân bằng từ nút cha

            else:  # Nếu nút có cả hai con
                print('Xóa nút có hai con...')  # In thông báo xóa nút có hai con
                predecessor = self.get_predecessor(node.left_node)  # Tìm nút tiền nhiệm của nút hiện tại
                temp = predecessor.data  # Lưu dữ liệu của nút tiền nhiệm
                predecessor.data = node.data  # Đổi dữ liệu của nút tiền nhiệm thành dữ liệu của nút hiện tại
                node.data = temp  # Đổi dữ liệu của nút hiện tại thành dữ liệu của nút tiền nhiệm
                self.remove_node(data, predecessor)  # Xóa nút tiền nhiệm

    def get_predecessor(self, node):
        if node.right_node:  # Nếu con phải của nút tồn tại
            return self.get_predecessor(node.right_node)  # Lấy nút tiền nhiệm
        return node  # Trả về nút tiền nhiệm

    def handle_violation(self, node):
        while node is not None:  # Lặp cho đến khi không còn nút nào
            node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1  # Cập nhật chiều cao của nút
            self.violation_helper(node)  # Kiểm tra và xử lý vi phạm cân bằng
            node = node.parent  # Di chuyển lên nút cha

    def violation_helper(self, node):
        balance = self.calculate_balance(node)  # Tính toán sự cân bằng của nút

        # Các trường hợp cân bằng:
        # Nếu cân bằng lớn hơn 1, nghĩa là cây nghiêng về bên trái
        if balance > 1:
            # Nếu con trái của con trái nghiêng về bên phải, thực hiện xoay trái
            if self.calculate_balance(node.left_node) < 0:
                self.rotate_left(node.left_node)
            # Xoay phải nút hiện tại để cân bằng
            self.rotate_right(node)

        # Nếu cân bằng nhỏ hơn -1, nghĩa là cây nghiêng về bên phải
        if balance < -1:
            # Nếu con phải của con phải nghiêng về bên trái, thực hiện xoay phải
            if self.calculate_balance(node.right_node) > 0:
                self.rotate_right(node.right_node)
            # Xoay trái nút hiện tại để cân bằng
            self.rotate_left(node)

    def calc_height(self, node):
        # Kiểm tra xem nút có tồn tại hay không
        if node is None:
            # Nếu nút không tồn tại, trả về -1
            return -1
        # Nếu nút tồn tại, trả về chiều cao của nút
        return node.height

    def calculate_balance(self, node):
        # Kiểm tra xem nút có tồn tại hay không
        if node is None:
            # Nếu nút không tồn tại, trả về 0
            return 0
        # Tính toán và trả về chỉ số cân bằng của nút dựa trên chiều cao của nút con trái và phải
        return self.calc_height(node.left_node) - self.calc_height(node.right_node)

    def traverse(self):
        # Kiểm tra xem cây có nút gốc hay không
        if self.root is not None:
            # Nếu có nút gốc, bắt đầu duyệt cây từ nút gốc
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        # Kiểm tra xem nút hiện tại có nút con trái hay không
        if node.left_node:
            # Nếu có, duyệt qua nút con trái
            self.traverse_in_order(node.left_node)

        # Khởi tạo các biến để lưu giá trị của nút con trái, phải và nút cha
        l = ''
        r = ''
        p = ''

        # Gán giá trị cho nút con trái, nếu không có thì gán 'NULL'
        l = node.left_node.data if node.left_node is not None else 'NULL'
        # Gán giá trị cho nút con phải, nếu không có thì gán 'NULL'
        r = node.right_node.data if node.right_node is not None else 'NULL'
        # Gán giá trị cho nút cha, nếu không có thì gán 'NULL'
        p = node.parent.data if node.parent is not None else 'NULL'

        # In thông tin của nút hiện tại bao gồm dữ liệu nút, nút con trái, phải, nút cha và chiều cao
        print("%s trái: %s phải: %s cha: %s chiều cao: %s" % (node.data, l, r, p, node.height))

        # Kiểm tra xem nút hiện tại có nút con phải hay không
        if node.right_node:
            # Nếu có, duyệt qua nút con phải
            self.traverse_in_order(node.right_node)

    def rotate_right(self, node):
        # Thực hiện xoay phải tại nút hiện tại và in thông báo
        print("Xoay về bên phải tại nút", node.data)

        # Lưu nút con trái của nút hiện tại và nút con phải của nút con trái
        temp_left_node = node.left_node
        t = temp_left_node.right_node

        # Cập nhật liên kết giữa nút hiện tại và nút con trái của nó
        temp_left_node.right_node = node
        node.left_node = t

        # Nếu nút con phải của nút con trái tồn tại, cập nhật nút cha của nó
        if t is not None:
            t.parent = node

        # Lưu nút cha của nút hiện tại và cập nhật liên kết với nút con trái và nút cha
        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        # Nếu nút con trái có nút cha và nút cha đó có liên kết với nút hiện tại, cập nhật liên kết đó
        if temp_left_node.parent is not None and temp_left_node.parent.left_node == node:
            temp_left_node.parent.left_node = temp_left_node
        if temp_left_node.parent is not None and temp_left_node.parent.right_node == node:
            temp_left_node.parent.right_node = temp_left_node

        # Nếu nút hiện tại là nút gốc, cập nhật nút gốc thành nút con trái
        if node == self.root:
            self.root = temp_left_node

        # Cập nhật chiều cao cho nút hiện tại và nút con trái sau khi xoay
        node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node))
        temp_left_node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1

    def rotate_left(self, node):
        # Thực hiện xoay trái tại nút hiện tại và in thông báo
        print("Xoay về bên trái tại nút", node.data)

        # Lưu nút con phải của nút hiện tại và nút con trái của nút con phải
        temp_right_node = node.right_node
        t = temp_right_node.left_node

        # Cập nhật liên kết giữa nút hiện tại và nút con phải của nó
        temp_right_node.left_node = node
        node.right_node = t

        # Nếu nút con trái của nút con phải tồn tại, cập nhật nút cha của nó
        if t is not None:
            t.parent = node

        # Lưu nút cha của nút hiện tại và cập nhật liên kết với nút con phải và nút cha
        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        # Nếu nút con phải có nút cha và nút cha đó có liên kết với nút hiện tại, cập nhật liên kết đó
        if temp_right_node.parent is not None and temp_right_node.parent.left_node == node:
            temp_right_node.parent.left_node = temp_right_node
        if temp_right_node.parent is not None and temp_right_node.parent.right_node == node:
            temp_right_node.parent.right_node = temp_right_node

        # Nếu nút hiện tại là nút gốc, cập nhật nút gốc thành nút con phải
        if node == self.root:
            self.root = temp_right_node

        # Cập nhật chiều cao cho nút hiện tại và nút con phải sau khi xoay
        node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node))
        temp_right_node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1



if __name__ == '__main__':
    avl = AVLTree()  # Tạo một cây AVL mới
    # Chèn các giá trị vào cây AVL
    avl.insert(32)
    avl.insert(16)
    avl.insert(48)
    avl.insert(8)
    avl.insert(24)
    avl.insert(40)
    avl.insert(56)
    avl.insert(36)
    avl.insert(44)
    avl.insert(52)
    avl.insert(60)
    avl.insert(4)
    avl.insert(58)
    avl.insert(62)
    avl.remove(4)  # Xóa một giá trị khỏi cây AVL

    avl.traverse()  # Duyệt và in thông tin của cây AVL

