# Với mảng
array = [1, 2, 3, 4, 5]

# Thêm phần tử cuối cùng vào mảng
array.append(6)  # Thêm phần tử 6 vào cuối mảng
print(array)  # Output: [1, 2, 3, 4, 5, 6]

# Xóa phần tử cuối cùng khỏi mảng
array.pop()  # Xóa phần tử cuối cùng
print(array)  # Output: [1, 2, 3, 4, 5]

# Thêm phần tử vào vị trí tùy ý trong mảng
array.insert(2, 6)  # Thêm phần tử 6 vào vị trí thứ 2
print(array)  # Output: [1, 2, 6, 3, 4, 5]

# Xóa phần tử từ vị trí tùy ý trong mảng
del array[3]  # Xóa phần tử tại vị trí thứ 3 (giá trị 3)
print(array)  # Output: [1, 2, 6, 4, 5]

# Với danh sách liên kết
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Thêm phần tử cuối cùng vào danh sách liên kết
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Xóa phần tử cuối cùng khỏi danh sách liên kết
    def pop(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None

    # Xóa phần tử từ vị trí tùy ý trong danh sách liên kết
    def delete_node(self, value):
        if not self.head:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

# Sử dụng danh sách liên kết
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

# Xóa phần tử cuối cùng từ danh sách liên kết
linked_list.pop()

# Xóa phần tử từ vị trí tùy ý trong danh sách liên kết
linked_list.delete_node(3)
