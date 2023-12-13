# Định nghĩa lớp HeapTransformer để chuyển đổi một mảng thành một đống (heap) tối thiểu.
class HeapTransformer:

    # Hàm khởi tạo của lớp, nhận một mảng 'heap'.
    def __init__(self, heap):
        self.heap = heap  # Lưu trữ mảng được cung cấp trong thuộc tính 'heap'.

    # Phương thức để chuyển đổi mảng thành đống tối thiểu.
    def transform(self):
        # Bắt đầu từ nút cha cuối cùng và di chuyển ngược lên đến gốc.
        for i in range((len(self.heap)-2)//2, -1, -1):
            # Đảm bảo rằng mọi nút con đều thỏa mãn tính chất của đống tối thiểu.
            self.fix_down(i)

    # Phương thức để sắp xếp lại đống từ một nút chỉ định.
    def fix_down(self, index):
        # Tính chỉ số của hai nút con (trái và phải) của nút hiện tại.
        index_left = 2 * index + 1
        index_right = 2 * index + 2

        # Trong đống tối thiểu, nút cha luôn nhỏ hơn các nút con.
        index_smallest = index

        # Tìm nút nhỏ nhất giữa nút cha và nút con trái.
        if index_left < len(self.heap) and self.heap[index_left] < self.heap[index]:
            index_smallest = index_left

        # Nếu nút con phải nhỏ hơn nút con trái: nút nhỏ nhất là nút con phải.
        if index_right < len(self.heap) and self.heap[index_right] < self.heap[index_smallest]:
            index_smallest = index_right

        # Nếu nút cha lớn hơn các nút con: đống đã hợp lệ và kết thúc đệ quy.
        if index != index_smallest:
            # Hoán đổi nút cha với nút nhỏ nhất.
            self.heap[index], self.heap[index_smallest] = self.heap[index_smallest], self.heap[index]
            # Tiếp tục quá trình sắp xếp ở nút con.
            self.fix_down(index_smallest)


# Phần thực thi chính của chương trình.
if __name__ == '__main__':
    # Khởi tạo một mảng.
    n = [210, 100, 23, 2, 5]
    # Tạo một đối tượng của HeapTransformer với mảng n.
    heap_transform = HeapTransformer(n)
    # Chuyển đổi mảng n thành đống tối thiểu.
    heap_transform.transform()
    # In ra mảng sau khi đã được chuyển đổi.
    print(heap_transform.heap)  # Kết quả là đống tối thiểu từ mảng ban đầu.
