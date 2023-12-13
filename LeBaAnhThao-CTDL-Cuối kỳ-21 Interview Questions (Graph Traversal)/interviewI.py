#How to implementation dept-first-search with the recursion
#(triển khai thuật toán dept-first bằng đệ quy)

class Node:
    def __init__(self, name):
        self.name = name #khai báo tên của Node                                                                                                                                       (thôi)
        self.adjacency_list = [] #viết theo cấu trúc của linked-list tránh space complexity                                                                                      (để không tốn bộ nhớ)
        self.visited = False #ban đầu không có liên kết nên xem như giữa các Node không tồn tại Edge nên vissited mặc định là 0.

def dept_first_search(node): #hàm tìm đường đi để duyệt hết tất cả các node trong Graph
    node.visited = True #Node được sử dụng nên mặc định là đã được visited
    print(node.name, end=" ") #in ra name của Node đó
    for n in node.adjacency_list: #duyệt các phần tử trong graph                                                                                                                       (cụ thể là trong adjacency_list)
        if not n.visited: #nếu node đó chưa được visited                                                                                                                           (tức là vẫn đang False)
            dept_first_search(n) #đệ quy lại hàm cho Node tiếp theo được duyệt, đệ quy liên tục cho đến khi hết các node.

node1 = Node("A") #tạo Node A
node2 = Node("B") #tạo Node B
node3 = Node("C") #tạo Node C
node4 = Node("D") #tạo Node D
node5 = Node("E") #tạo Node E

node1.adjacency_list.append(node2) #tạo liên kết giữa node 1 và node 2                                                                                                                            (này giống như node1.next = node2 đó nha)
node1.adjacency_list.append(node3) #tạo liên kết giữa node 1 và node 3
node2.adjacency_list.append(node4) #tạo liên kết giữa node 2 và node 4
node4.adjacency_list.append(node5) #tạo liên kết giữa node 4 và node 5

dept_first_search(node1) #sử dụng hàm dept-first-search cho node1






