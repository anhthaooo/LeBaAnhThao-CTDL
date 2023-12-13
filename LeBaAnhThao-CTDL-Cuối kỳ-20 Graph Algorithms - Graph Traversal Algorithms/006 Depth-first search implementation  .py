# Định nghĩa lớp Node để biểu diễn một nút trong đồ thị.
class Node:
    # Hàm khởi tạo cho Node.
    def __init__(self, name):
        self.name = name  # Tên của nút.
        self.adjacency_list = []  # Danh sách các nút liền kề.
        self.visited = False  # Biến cờ để đánh dấu nút đã được thăm.

# Hàm thực hiện thuật toán Tìm kiếm Sâu (Depth-First Search).
def depth_first_search(start_node):
    # Khởi tạo một ngăn xếp và thêm nút bắt đầu vào ngăn xếp.
    stack = [start_node]

    # Vòng lặp chạy khi ngăn xếp không rỗng.
    while stack:
        # Lấy nút cuối cùng từ ngăn xếp và đánh dấu là đã thăm.
        actual_node = stack.pop()
        actual_node.visited = True
        # In tên của nút.
        print(actual_node.name)

        # Duyệt qua tất cả các nút liền kề của nút hiện tại.
        for n in actual_node.adjacency_list:
            # Nếu nút liền kề chưa được thăm, thêm vào ngăn xếp.
            if not n.visited:
                stack.append(n)

# Mã để thử nghiệm thuật toán.
if __name__ == '__main__':
    # Tạo các nút.
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    # Xác định mối quan hệ giữa các nút (đồ thị).
    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)

    # Thực hiện thuật toán DFS bắt đầu từ nút A.
    depth_first_search(node1)
