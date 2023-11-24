# Định nghĩa lớp Node để biểu diễn các nút trong danh sách liên kết
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Định nghĩa hàm hiển thị danh sách liên kết
def display(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
# Tạo các nút và liên kết chúng
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
# Gọi hàm hiển thị để in ra danh sách liên kết
display(node1)
