from collections import deque

class MazeSolver:
    def __init__(self, matrix):
        self.matrix = matrix #khởi tạo maxtrix bằng kích thước với matrix truyền vào
         #tạo ma trận visited, ban đầu tất cả các node trong Graph đều chưa có edge nên xem như là False
         #ma trận cần có kích thước [len(matrix)-1]*[(len(matrix)-1)]
        self.visited = [[False for _ in range(len(matrix))] for _ in range(len(matrix))]

        #biểu thị cho di chuyển x(sang phải,0,0, sang trái), 
        # cách code này phải tương ứng với y một cách đồng thời để có được ý nghĩa
        self.move_x = [1, 0, 0, -1] 
        #tương tự đối với y
        self.move_y = [0, -1, 1, 0]
        #đặt độ dài đường đi tối thiểu ban đầu là inf
        self.minDistance = float('inf')
    
    def is_valid(self, row, col):

        #kiểm tra điều kiện khi chạy sang bên ngoài hàng của matrix
        if row < 0 or row >= len(self.matrix):
            return False
        
        #kiểm tra điều kiện khi chạy sang bên ngoài cột của matrix
        if col < 0 or col >= len(self.matrix):
            return False
        
        #Điều kiện khai báo 0 là các bức tường(chướng ngại vật), nghĩa là đường đi không đi qua đây
        if self.matrix[row][col] == 0:
            return False #False đồng nghĩa với việc không thể có edge giữa của 2 node của row và column tương ứng
        
        #Điều kiện cho hàng, cột được khi đã visited Node
        if self.visited[row][col]:
            return False #False đồng nghĩa với việc hàng và cột này đã có và không tiếp tục truy từ vertex này nữa
        
        return True
    
    def search(self, i, j, destination_x, destination_y): #hàm tìm kiếm đường đi từ tọa độ của source tới tọa độ của destination
        self.visited[i][j] = True
        #Sử dụng deuque để giảm độ khó thuật toán thành O(1)
        queue = deque()
        #đặt i là trục x
        #đặt j là trục y
        queue.append((i, j, 0))

        while queue:
            #Dòng code này để có thể đảm bảo rằng bên trong queue đã có các phần tử đầu tiên vừa được chèn vào
            (i, j, dist) = queue.popleft()

            #Điều kiện khi mà queue đã trỏ được tới vị trí đích 
            if i == destination_x and j == destination_y:
                self.minDistance = dist #minDistance(đường đi ngắn nhất) cần tìm chính là giá trị của dist
                break #cho dừng chương trình
            
            #Vòng lặp này cho biết được là node đang dừng ở trị trí (j, j), và ta có 4 lựa chọn: Phải -> Xuống -> Lên -> Trái 
            # len(self.move_x) chỉ để đảm bảo move sẽ chạy hết cả 4 lựa chọn nên không có ý nghĩa gì đặc biệt
            for move in range(len(self.move_x)):
                next_x = i + self.move_x[move] #dịch chuyển vị trí đang dừng theo trục X
                next_y = j + self.move_y[move] #dịch chuyển vị trí đang dừng theo trục Y

                #Điều kiện này có thể xem là có thực sự tồn tại edge từ 2 node tương ứng với next_x và next_y đã cho
                if self.is_valid(next_x, next_y): #Kiểm tra điều kiện có thõa mãn là có tồn tại edge hay không
                    self.visited[next_x][next_y] = True #Nếu đúng thì trả về True -> đã visited
                    queue.append((next_x, next_y, dist+1)) #thêm giá trị vừa mới đúng vào queue -> giá trị đường đi +1

    def show_result(self):
         #điều kiện để đảm bảo minDistance là 1 số.(trong trường hợp xấu là từ source đến destination không tồn tại đường đi nào)
        if self.minDistance != float('inf'):       
            print("Độ dài con đường ngắn nhất đi từ gốc đã chọn đến đích là:", self.minDistance)
        else:
            print("Không có con đường nào đi được từ gốc đến đích")

m = [
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1]
]

make_solver = MazeSolver(m) #Khởi tạo object là make_solver
make_solver.search(0, 0, 4, 4) #điểm bắt đầu là tọa độ (0, 0) và đích là tọa độ (4, 4)
make_solver.show_result() #In ra độ dài của đường đi ngắn nhất đi từ (0, 0)->(4,4) 

