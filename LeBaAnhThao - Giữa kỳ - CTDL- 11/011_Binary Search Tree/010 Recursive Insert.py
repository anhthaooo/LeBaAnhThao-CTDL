# Recursive insertion( chèn có sử dụng đệ quy)
class _Node: # Định nghĩa lớp _Node để đại diện cho một nút trong cây nhị phân
    __slots__='_element','_left','_right'#để tối ưu hóa việc lưu trữ dữ liệu bằng cách chỉ định các thuộc tính được phép của đối tượng. Trong trường hợp này, các thuộc tính được phép bao gồm _element, _left, và _right.

    def __init__(self,element,left=None,right=None):#Hàm khởi tạo của lớp _Node với các tham số element, left, và right. Tham số left và right có giá trị mặc định là None.
        self._element=element #Gán giá trị của tham số element cho thuộc tính _element của đối tượng _Node.
        self._left=left    #Gán giá trị của tham số left cho thuộc tính _left của đối tượng _Node.
        self._right=right  #gán giá trị của tham số right cho thuộc tính _right của đối tượng _Node.

class BinarySearchTree:   # Hàm khởi tạo của lớp BinarySearchTree, tạo một cây mới với gốc là None
    def __init__(self):# Phương thức chèn một phần tử e vào cây tìm kiếm nhị phân không đệ quy
        self._root=None

    def rinsert(self,troot,e): # phương thức chèn có đệ quy
        if troot: # nêu troot không rỗng
            if e < troot._element: # kiểm tra nếu e nhỏ hơn giá trị tại troot thì đệ quy tới cây con bên trái
                troot._left=self.rinsert(troot._left,e)
            elif e>troot._element: # nều e lớn hơn giá trị tại troot thì đệ quy tới giá trị cây con bên phải
                troot._right=self.rinsert(troot._right,e)
        else: # nếu troot là rỗng, tức cây rỗng
            n=_Node(e) # tạo một nút n mới có giá trị e để chèn vào cây
            troot =n # gán nút n cho troot
        return troot # trả về cây đã được chèn

    def inorder(self,troot): # hàm duyệt cây theo inoder( duyệt từ cây con bên trái cùng
        if troot: # kiểm tra nếu troot không phải là None
            self.inorder(troot._left) #duyệt từng nút con bên trái của một nút theo thứ tự trước và thực hiện đệ quy cho đến khi không còn nút con nào,trước khi tiếp tục duyệt nút con bên phải.)
            print(troot._element,end=' ')# in ra giá trị hiện tại
            self.inorder(troot._right)#cho đến khi không còn nút con nào, trước khi tiếp tục duyệt nút con bên phải
            # vì để print(troot._element,end=' ') ở dưới self.inoder(troot.left) nên sẽ duyệt đệ quy tới con bên trái cuối cùng trước
            # rồi duyệt từng bước lên nút gốc rồi duyệt qua mảng bên phải


# Tạo đối tượng BinarySearchTree và chèn các giá trị vào cây.
B=BinarySearchTree()
B._root = B.rinsert(B._root,50)
B.rinsert(B._root,30)
B.rinsert(B._root,80)
B.rinsert(B._root,10)
B.rinsert(B._root,40)
B.rinsert(B._root,60)
B.inorder(B._root) # duyệt cây theo inorder