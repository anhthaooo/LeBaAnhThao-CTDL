# Định nghĩa lớp Node để tạo nút trong danh sách liên kết
class Node:
    def __init__(self, data):
        # Lưu trữ dữ liệu trong nút
        self.data = data
        # Khởi tạo tham chiếu đến nút tiếp theo là None
        self.next_node = None

# Định nghĩa lớp LinkedList để quản lý danh sách liên kết
class LinkedList:
    def __init__(self):
        # Khởi tạo đầu danh sách (head) là None khi danh sách rỗng
        self.head = None

    def append(self, data):
        # Tạo một đối tượng Node mới với dữ liệu mới
        new_node = Node(data)
        if not self.head:
            # Nếu danh sách liên kết trống, đặt nút mới làm đầu danh sách
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                # Di chuyển đến nút cuối cùng của danh sách
                current = current.next_node
            # Gán tham chiếu của nút cuối cùng đến nút mới, thêm nút mới vào cuối danh sách
            current.next_node = new_node


