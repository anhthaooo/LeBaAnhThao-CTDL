class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Tạo các nút
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Liên kết các nút với nhau
node1.next = node2
node2.next = node3

# Duyệt danh sách và in ra các phần tử
current = node1
while current is not None:
    print(current.data)
    current = current.next
