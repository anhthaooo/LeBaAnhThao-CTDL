# Recursive search ( search sử dụng  đệ quy)
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
print(B.rsearch(B._root,70))# kiểm tra có giá trị 70 trong cây không

