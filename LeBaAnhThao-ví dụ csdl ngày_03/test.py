class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_at_position(self, position):
        if position == 0:
            self.head = self.head.next
            return

        current = self.head
        count = 0
        while current:
            if count == position - 1:
                current.next = current.next.next
                break
            current = current.next
            count += 1

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Tạo một danh sách liên kết mới
my_linked_list = LinkedList()

# Thêm các phần tử vào danh sách
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

# Hiển thị danh sách ban đầu
print("Danh sách ban đầu:")
my_linked_list.display()

# Xóa phần tử thứ hai (vị trí 1)
my_linked_list.delete_at_position(1)

# Hiển thị danh sách sau khi xóa
print("Danh sách sau khi xóa phần tử thứ hai:")
my_linked_list.display()
