# Deletion in Binary Search Tree (xóa nút  trong BST)
class _Node: # Định nghĩa lớp _Node để đại diện cho một nút trong cây nhị phân
    __slots__='_element','_left','_right'#để tối ưu hóa việc lưu trữ dữ liệu bằng cách chỉ định các thuộc tính được phép của đối tượng. Trong trường hợp này, các thuộc tính được phép bao gồm _element, _left, và _right.

    def __init__(self,element,left=None,right=None):#Hàm khởi tạo của lớp _Node với các tham số element, left, và right. Tham số left và right có giá trị mặc định là None.
        self._element=element #Gán giá trị của tham số element cho thuộc tính _element của đối tượng _Node.
        self._left=left    #Gán giá trị của tham số left cho thuộc tính _left của đối tượng _Node.
        self._right=right  #gán giá trị của tham số right cho thuộc tính _right của đối tượng _Node.

class BinarySearchTree:   # Hàm khởi tạo của lớp BinarySearchTree, tạo một cây mới với gốc là None
    def __init__(self):# Phương thức chèn một phần tử e vào cây tìm kiếm nhị phân không đệ quy
        self._root=None

    def insert(self,troot,e):
        temp=None # đặt giá trị tạm thời là rỗng
        while troot:  # kiểm tra nếu troot đang xét tới không rỗng
            temp=troot# gán giá trị troot hiện tại vào biến temp
            if e == troot._element: # kiểm tra nếu giá trị e cần chèn vào bằng giá trị troot hiện tại thì return
                return
            elif e< troot._element:# nếu e nhỏ hơn giá trị troot thì xét tới con bên trái của troot
                troot=troot._left
            elif e> troot._element:# nếu e lớn hơn giá trị troot thì xét tới con bên phải của troot
                troot=troot._right
        n=_Node(e)# tạo một nút n mới để chèn vào cây
        if self._root: # kiểm tra nêu cây không rỗng thì
            if e < temp._element: # nếu giá trị e cần chèn nhỏ hơn giá trị của temp đang xét trước đó thì chèn vào bên trái vị trí temp
                temp._left=n
            else:# nếu giá trị e cần chèn lớn hơn giá trị của temp đang xét trước đó thì chèn vào bên phải vị trí temp
                temp._right=n
        else:
            self._root=n # nếu cây rỗng thì gán n là root của cây luôn

    def inorder(self,troot): # hàm duyệt cây theo inoder( duyệt từ cây con bên trái cùng
        if troot: # kiểm tra nếu troot không phải là None
            self.inorder(troot._left) #duyệt từng nút con bên trái của một nút theo thứ tự trước và thực hiện đệ quy cho đến khi không còn nút con nào,trước khi tiếp tục duyệt nút con bên phải.)
            print(troot._element,end=' ')# in ra giá trị hiện tại
            self.inorder(troot._right)#cho đến khi không còn nút con nào, trước khi tiếp tục duyệt nút con bên phải
            # vì để print(troot._element,end=' ') ở dưới self.inoder(troot.left) nên sẽ duyệt đệ quy tới con bên trái cuối cùng trước
            # rồi duyệt từng bước lên nút gốc rồi duyệt qua mảng bên phải

    def rsearch(self,troot,key):# hàm search có đệ quy
        if troot:# Kiểm tra nếu nút hiện tại tồn tại (khác None)
            if key==troot._element:# Nếu giá trị cần tìm bằng giá trị của nút hiện tại
                return True # Trả về True vì đã tìm thấy giá trị trong cây
            elif key<troot._element:# Nếu giá trị cần tìm nhỏ hơn giá trị của nút hiện tại
                return self.rsearch(troot._left,key)# Gọi đệ quy với nút con bên trái của nút hiện tại
            elif key>troot._element:# Nếu giá trị cần tìm lớn hơn giá trị của nút hiện tại
                return self.rsearch(troot._right,key)# Gọi đệ quy với nút con bên phải của nút hiện tại
        else:
            return False# Nếu nút hiện tại không tồn tại, trả về False

    def delete(self,e): # hàm xóa
        p=self._root# Con trỏ p bắt đầu từ nút gốc (_root) của cây
        pp=None# Con trỏ pp là cha của nút p, khởi tạo là None (vì chưa có nút nào)
        while p and p._element!= e : # Duyệt cây cho đến khi tìm thấy nút có giá trị bằng e hoặc p trở thành None
            pp=p# Lưu trữ nút cha của nút p
            if e<p._element:
                p=p._left # Di chuyển xuống nút con bên trái nếu giá trị cần xóa nhỏ hơn giá trị của nút p
            else:
                p=p._right# Di chuyển xuống nút con bên phải nếu giá trị cần xóa lớn hơn giá trị của nút p
        if not p:
            return False # Nếu không tìm thấy nút có giá trị bằng e, trả về False
        if p._left and p._right: # kiểm tra nếu nút cần xóa có cả hai con
            s=p._left# Con trỏ s bắt đầu từ cây con bên trái của nút p
            ps=p # Con trỏ ps là cha của nút s, ban đầu là nút p
            while s._right: # Tìm nút thay thế s với giá trị lớn nhất trong cây con bên trái của p
                ps=s # Khởi tạo con trỏ ps là cha của s. Ban đầu, ps được gán bằng p.
                s=s._right # di chuyển s sang cây con bên phải
            p._element= s._element         # Thay đổi giá trị của nút p thành giá trị của nút thay thế s
            p=s # Gán nút p thành nút thay thế s để xóa nút p sau này
            pp=ps # Gán pp (cha của p) bằng ps (cha của s).nghĩa là  pp sẽ là cha của nút thay thế s.
        # Xác định con của nút p để xóa (có thể là None)
        c=None
        if p._left:
            c=p._left
        else:
            c=p._right
        if p == self._root: # kiểm tra xem nút p có phải là nút gốc không
            self._root=None  #  nếu là nút gốc thì xóa nút p khỏi cây
        else:  # nếu không phải là nút gốc thì cập nhật con trỏ của nút cha của p để trỏ vào nút con c
            if p==pp._left:
                pp._left=c #Nếu p là nút con bên trái của pp, thì cập nhật con trỏ pp._left để trỏ vào nút con c. nghĩa là loại bỏ nút p khỏi cây và thay nó bằng nút con c
            else:
                pp._right=c#Nếu p là nút con bên phải của pp, thì cập nhật con trỏ pp._right để trỏ vào nút con c. nghĩa là loại bỏ nút p khỏi cây và thay nó bằng nút con c




# Tạo đối tượng BinarySearchTree và chèn các giá trị vào cây.
B=BinarySearchTree()
B.insert(B._root,50)
B.insert(B._root,30)
B.insert(B._root,80)
B.insert(B._root,10)
B.insert(B._root,40)
B.insert(B._root,60)
B.inorder(B._root) # duyệt cây theo inorder
print()
#print(B.rsearch(B._root,70))# kiểm tra có giá trị 60 trong cây không
B.delete(60)
B.inorder(B._root)
