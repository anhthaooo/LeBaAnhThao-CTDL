#011 Lets Implement Graphs ADT
import numpy as np
# Import thư viện numpy với tên gọi ngắn gọn là np. Thư viện này hỗ trợ nhiều hàm và phương thức hữu ích cho việc tính toán khoa học và đại số tuyến tính.

class Graph:
# Khai báo một lớp mới tên là Graph.

    def __init__(self, vertices):
    # Định nghĩa phương thức khởi tạo cho lớp. Phương thức này sẽ được gọi khi một đối tượng mới của lớp được tạo ra.
    # 'vertices' là một tham số đầu vào, đại diện cho số lượng đỉnh trong đồ thị.

        self._vertices = vertices 
        # Gán giá trị của tham số 'vertices' cho thuộc tính '_vertices' của đối tượng.

        self._adjMat = np.zeros((vertices, vertices))
        # Tạo một ma trận kề với tất cả các giá trị ban đầu là 0. Kích thước của ma trận này là 'vertices' x 'vertices'.

    def insert_edge(self, u, v, x=1):
    # Định nghĩa phương thức 'insert_edge' để thêm một cạnh vào đồ thị. 
    # 'u' và 'v' là các đỉnh mà cạnh nối, 'x' là trọng số của cạnh (mặc định là 1).

        self._adjMat[u][v] = x
        # Thêm cạnh vào ma trận kề bằng cách gán giá trị 'x' cho phần tử tại hàng 'u', cột 'v'.

    def remove_edge(self, u, v): 
    # Định nghĩa phương thức 'remove_edge' để xóa một cạnh khỏi đồ thị. 'u' và 'v' là các đỉnh mà cạnh nối.

        self._adjMat[u][v] = 0
        # Xóa cạnh khỏi ma trận kề bằng cách gán giá trị 0 cho phần tử tại hàng 'u', cột 'v'.

    def exist_edge(self, u, v): 
    # Định nghĩa phương thức 'exist_edge' để kiểm tra xem có tồn tại cạnh giữa hai đỉnh 'u' và 'v' hay không.

        return self._adjMat[u][v] != 0
        # Trả về True nếu cạnh tồn tại (giá trị tại hàng 'u', cột 'v' khác 0), ngược lại trả về False.

    def vertex_count(self):
    # Định nghĩa phương thức 'vertex_count' để trả về số lượng đỉnh trong đồ thị.

        return self._vertices
        # Trả về giá trị của thuộc tính '_vertices'.

    def edge_count(self):
    # Định nghĩa phương thức 'edge_count' để đếm và trả về số lượng cạnh trong đồ thị.

        count = 0
        # Khởi tạo biến đếm 'count' với giá trị ban đầu là 0.

        for i in range(self._vertices): 
        # Vòng lặp 'for' để duyệt qua tất cả các đỉnh.

            for j in range(self._vertices):
            # Vòng lặp 'for' lồng trong vòng lặp trên để duyệt qua tất cả các đỉnh.

                if self._adjMat[i][j] != 0:
                # Kiểm tra xem có tồn tại cạnh giữa hai đỉnh 'i' và 'j' hay không.

                    count = count + 1
                    # Nếu có cạnh, tăng biến đếm 'count' lên 1.

        return count
        # Trả về giá trị của biến đếm 'count', tức là số lượng cạnh trong đồ thị.

    def vertices(self):
    # Định nghĩa phương thức 'vertices' để in ra tất cả các đỉnh của đồ thị.

        for i in range(self._vertices):
        # Vòng lặp 'for' để duyệt qua tất cả các đỉnh.

            print(i, end=' ')
            # In ra đỉnh hiện tại.

            print()
            # Xuống dòng sau mỗi đỉnh.

    def edges(self):
    # Định nghĩa phương thức 'edges' để in ra tất cả các cạnh của đồ thị.

        for i in range(self._vertices): 
        # Vòng lặp 'for' để duyệt qua tất cả các đỉnh.

            for j in range(self._vertices):
            # Vòng lặp 'for' lồng trong vòng lặp trên để duyệt qua tất cả các đỉnh.

                if self._adjMat[i][j] != 0:
                # Kiểm tra xem có tồn tại cạnh giữa hai đỉnh 'i' và 'j' hay không.

                    print(i,'--',j)
                    # Nếu có cạnh, in ra cạnh đó.

    def outdegree(self, v):
    # Định nghĩa phương thức 'outdegree' để trả về bậc ra của một đỉnh 'v' (số lượng cạnh đi ra từ 'v').

        count = 0
        # Khởi tạo biến đếm 'count' với giá trị ban đầu là 0.

        for j in range(self._vertices):
        # Vòng lặp 'for' để duyệt qua tất cả các đỉnh.

             if self._adjMat[v][j] != 0:
             # Kiểm tra xem có tồn tại cạnh từ đỉnh 'v' đến đỉnh 'j' hay không.

                 count = count + 1
                 # Nếu có cạnh, tăng biến đếm 'count' lên 1.

        return count
        # Trả về giá trị của biến đếm 'count', tức là bậc ra của đỉnh 'v'.

    def indegree(self, v): 
    # Định nghĩa phương thức 'indegree' để trả về bậc vào của một đỉnh 'v' (số lượng cạnh đi vào 'v').

        count = 0
        # Khởi tạo biến đếm 'count' với giá trị ban đầu là 0.

        for i in range(self._vertices):
        # Vòng lặp 'for' để duyệt qua tất cả các đỉnh.

            if self._adjMat[i][v] != 0:
            # Kiểm tra xem có tồn tại cạnh từ đỉnh 'i' đến đỉnh 'v' hay không.

                count = count + 1
                # Nếu có cạnh, tăng biến đếm 'count' lên 1.

        return count
        # Trả về giá trị của biến đếm 'count', tức là bậc vào của đỉnh 'v'.

    def display_adjMat(self):
    # Định nghĩa phương thức 'display_adjMat' để hiển thị ma trận kề của đồ thị.

        print(self._adjMat)
        # In ra ma trận kề. Ma trận này biểu diễn các cạnh giữa các đỉnh: mỗi hàng và cột tương ứng với một đỉnh, và giá trị tại hàng i, cột j là trọng số của cạnh từ i đến j (hoặc 0 nếu không có cạnh).


#012 Lets Implement Undirected Graph
G = Graph(4)
# Tạo một đối tượng Graph mới với 4 đỉnh.

G.display_adjMat()
# Hiển thị ma trận kề ban đầu của đồ thị. Vì chưa có cạnh nào được thêm vào, tất cả các giá trị trong ma trận đều là 0.

print('Vertices:',G.vertex_count())
# In ra số lượng đỉnh của đồ thị, trong trường hợp này là 4.

print('Edges:',G.edge_count())
# In ra số lượng cạnh của đồ thị. Vì chưa có cạnh nào được thêm vào, kết quả sẽ là 0.

G.insert_edge(0,1)
G.insert_edge(0,2)
G.insert_edge(1,0)
G.insert_edge(1,2)
G.insert_edge(2,0)
G.insert_edge(2,1)
G.insert_edge(2,3)
G.insert_edge(3,2)
# Thêm các cạnh vào đồ thị.

G.display_adjMat()
# Hiển thị ma trận kề sau khi thêm các cạnh.

print('Edges:',G.edge_count())
# In ra số lượng cạnh của đồ thị sau khi thêm các cạnh.

G.edges()
# In ra tất cả các cạnh của đồ thị.

print('Edge between 1-3',G.exist_edge(1,3))
# Kiểm tra xem có tồn tại cạnh giữa đỉnh 1 và 3 hay không.

print('Edge between 1-2',G.exist_edge(1,2))
# Kiểm tra xem có tồn tại cạnh giữa đỉnh 1 và 2 hay không.

print('Degree', G.indegree(2))
# In ra bậc vào của đỉnh 2.

G.remove_edge(1,2)
# Xóa cạnh giữa đỉnh 1 và 2.

print('Edge between 1-2',G.exist_edge(1,2))
# Kiểm tra lại xem cạnh giữa đỉnh 1 và 2 còn tồn tại hay không sau khi đã xóa.


#013 Lets Implement Weighted Undirected Graph 
G = Graph(4)
# Tạo một đối tượng Graph mới với 4 đỉnh.

G.display_adjMat()
# Hiển thị ma trận kề ban đầu của đồ thị. Vì chưa có cạnh nào được thêm vào, tất cả các giá trị trong ma trận đều là 0.

print('Vertices:',G.vertex_count())
# In ra số lượng đỉnh của đồ thị, trong trường hợp này là 4.

print('Edges:',G.edge_count())
# In ra số lượng cạnh của đồ thị. Vì chưa có cạnh nào được thêm vào, kết quả sẽ là 0.

G.insert_edge(0,1,26)
G.insert_edge(0,2,16)
G.insert_edge(1,0,26)
G.insert_edge(1,2,12)   
G.insert_edge(2,0,16)
G.insert_edge(2,1,12)
G.insert_edge(2,3,8)
G.insert_edge(3,2,8)
# Thêm các cạnh vào đồ thị. Trọng số của mỗi cạnh được chỉ định bởi tham số thứ ba của phương thức 'insert_edge'.

G.display_adjMat()
# Hiển thị ma trận kề sau khi thêm các cạnh.

print('Edges:',G.edge_count())
# In ra số lượng cạnh của đồ thị sau khi thêm các cạnh.

G.edges()
# In ra tất cả các cạnh của đồ thị.

print('Edge between 1-3',G.exist_edge(1,3))
# Kiểm tra xem có tồn tại cạnh giữa đỉnh 1 và 3 hay không.

print('Edge between 1-2',G.exist_edge(1,2))
# Kiểm tra xem có tồn tại cạnh giữa đỉnh 1 và 2 hay không.

print('Degree', G.indegree(2))
# In ra bậc vào của đỉnh 2.

G.remove_edge(1,2)
# Xóa cạnh giữa đỉnh 1 và 2.

print('Edge between 1-2',G.exist_edge(1,2))
# Kiểm tra lại xem cạnh giữa đỉnh 1 và 2 còn tồn tại hay không sau khi đã xóa.


#014 Lets Implement Directed Graph 
G = Graph(4)
# Tạo một đối tượng Graph mới với 4 đỉnh.

G.display_adjMat()
# Hiển thị ma trận kề ban đầu của đồ thị. Vì chưa có cạnh nào được thêm vào, tất cả các giá trị trong ma trận đều là 0.

print('Vertices:',G.vertex_count())
# In ra số lượng đỉnh của đồ thị, trong trường hợp này là 4.

G.insert_edge(0,1)
G.insert_edge(0,2)
G.insert_edge(1,2)
G.insert_edge(2,3)
# Thêm các cạnh vào đồ thị.

print('Edges',G.edge_count())
# In ra số lượng cạnh của đồ thị sau khi thêm các cạnh.

G.edges()
# In ra tất cả các cạnh của đồ thị.

print('Edge 1-3',G.exist_edge(1,3))
# Kiểm tra xem có tồn tại cạnh giữa đỉnh 1 và 3 hay không.

print('Edge 1-2',G.exist_edge(1,2))
# Kiểm tra xem có tồn tại cạnh giữa đỉnh 1 và 2 hay không.

print('Indegree 2', G.indegree(2))
# In ra bậc vào của đỉnh 2.

print('Outdegree 2',G.outdegree(2))
# In ra bậc ra của đỉnh 2.

G.remove_edge(1,2)
# Xóa cạnh giữa đỉnh 1 và 2.

print('Edge 1-2',G.exist_edge(1,2))
# Kiểm tra lại xem cạnh giữa đỉnh 1 và 2 còn tồn tại hay không sau khi đã xóa.



#015 Lets Implement Weighted Directed Graph 
G = Graph(4)
# Tạo một đối tượng Graph mới với 4 đỉnh.

G.display_adjMat()
# Hiển thị ma trận kề ban đầu của đồ thị. Vì chưa có cạnh nào được thêm vào, tất cả các giá trị trong ma trận đều là 0.

print('Vertices:',G.vertex_count())
# In ra số lượng đỉnh của đồ thị, trong trường hợp này là 4.

G.insert_edge(0,1,26)
G.insert_edge(0,2,16)
G.insert_edge(1,2,12)
G.insert_edge(2,3,8)
# Thêm các cạnh vào đồ thị. Trọng số của mỗi cạnh được chỉ định bởi tham số thứ ba của phương thức 'insert_edge'.

print('Edges',G.edge_count())
# In ra số lượng cạnh của đồ thị sau khi thêm các cạnh.

G.edges()
# In ra tất cả các cạnh của đồ thị.

print('Edge 1-3',G.exist_edge(1,3))
# Kiểm tra xem có tồn tại cạnh giữa đỉnh 1 và 3 hay không.

print('Edge 1-2',G.exist_edge(1,2))
# Kiểm tra xem có tồn tại cạnh giữa đỉnh 1 và 2 hay không.

print('Indegree 2', G.indegree(2))
# In ra bậc vào của đỉnh 2.

print('Outdegree 2',G.outdegree(2))
# In ra bậc ra của đỉnh 2.

G.remove_edge(1,2)
# Xóa cạnh giữa đỉnh 1 và 2.

print('Edge 1-2',G.exist_edge(1,2))
# Kiểm tra lại xem cạnh giữa đỉnh 1 và 2 còn tồn tại hay không sau khi đã xóa.



