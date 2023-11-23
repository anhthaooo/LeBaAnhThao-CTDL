class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.numOfNodes = 0

    def insert_start(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node

    def insert_end(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            actual_node = self.head

            while actual_node.nextNode is not None:
                actual_node = actual_node.nextNode

            actual_node.nextNode = new_node

    def insert_between(self, prev_data, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            prev_node = None

            while current_node and current_node.data != prev_data:
                prev_node = current_node
                current_node = current_node.nextNode

            if current_node and current_node.data == prev_data:
                new_node.nextNode = current_node.nextNode
                current_node.nextNode = new_node
                self.numOfNodes = self.numOfNodes + 1
            else:
                print(f"{prev_data} not found in the list.")

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.nextNode
        print("None")

# Tạo danh sách liên kết
my_linked_list = LinkedList()

# Thêm phần tử vào đầu danh sách
my_linked_list.insert_start(10)

# Thêm phần tử vào đầu danh sách
my_linked_list.insert_start(12)
my_linked_list.insert_start(4)
# Thêm phần tử vào giữa 12 và 10
my_linked_list.insert_between(12, 123)
my_linked_list.insert_between(123, -7)

# Thêm phần tử vào cuối danh sách
my_linked_list.insert_end(25)

# In ra danh sách liên kết
my_linked_list.display()
