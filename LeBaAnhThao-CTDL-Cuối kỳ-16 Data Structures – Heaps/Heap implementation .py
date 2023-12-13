"""
Heap (hàng đợi ưu tiên)
"""
# Số lượng tối đa các phần tử có thể lưu trữ trong heap
CAPACITY = 10

"""
*** Max Heap ***
----------------
"""

# Định nghĩa lớp heap
class Heap(object):

    def __init__(self):
        # Tạo mảng với số khe như giá trị của CAPACITY
        self.heap = [0] * CAPACITY
        # Theo dõi kích thước của heap (số lượng phần tử trong heap)
        self.heap_size = 0

    # Thêm phần tử vào heap, thời gian chạy O(1) nhưng cần đảm bảo rằng
    # không vi phạm tính chất heap (thời gian chạy O(logN) do phương thức fixUp())
    def insert(self, item):
        # Nếu heap đã đầy, không thể thêm phần tử nữa
        if CAPACITY == self.heap_size:
            return

        # Thêm phần tử vào vị trí index của kích thước heap (vị trí trống cuối cùng)
        # và tăng kích thước lên 1
        self.heap[self.heap_size] = item
        self.heap_size += 1

        # Sau khi thêm, kiểm tra xem tính chất heap có bị vi phạm không
        # Nếu có, sửa chữa
        self.fix_up(self.heap_size - 1)

    # Xem xét phần tử cuối cùng và kiểm tra xem có cần thay đổi vị trí không
    # Thời gian chạy O(logN)
    def fix_up(self, index):
        # Lấy chỉ số cha của nút cụ thể trong heap
        parent_index = (index - 1) // 2

        # Trong khi index > 0 có nghĩa là cho đến khi xem xét tất cả các phần tử "phía trên"
        # phần tử được thêm, ta phải đổi chỗ nút với nút cha nếu tính chất heap bị vi phạm
        # Đây là một MAX HEAP: các phần tử lớn nhất nằm ở các tầng cao (phần tử lớn nhất == nút gốc)
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.swap(index, parent_index)
            # Kiểm tra lại sau khi đổi chỗ trên nút cha
            self.fix_up(parent_index)

    # Lấy phần tử lớn nhất, trả về nút gốc. Vì đây là max heap, nút gốc là phần tử lớn nhất.
    # Vì đây là mảng, nó mất O(1) thời gian
    # Đây là phương thức peek()
    def get_max(self):
        return self.heap[0]

    # Lấy phần tử lớn nhất và ĐỒNG THỜI LOẠI BỎ phần tử đó khỏi heap
    # Lưu ý: cchỉ quan tâm đến phần tử đó nếu như vì mảng có kích thước cố định
    # nên không thể loại bỏ hoàn toàn phần tử đó
    # Thời gian chạy O(logN)
    def poll(self):
        max_val = self.get_max()

        # Đổi chỗ phần tử đầu tiên với phần tử cuối cùng
        self.swap(0, self.heap_size - 1)
        # Giảm kích thước heap (loại bỏ phần tử cuối cùng khỏi heap)
        self.heap_size = self.heap_size - 1

        # Kiểm tra xem tính chất heap có bị vi phạm không và nếu có, sửa chữa
        # (fix down tương tự như fix up nhưng hoạt động từ gốc xuống)
        self.fix_down(0)

        # Trả về phần tử lớn nhất đã được loại bỏ
        return max_val

    # Fix down, có một phần tử cụ thể trong heap và xem xét tất cả các
    # phần tử phía dưới để kiểm tra xem tính chất heap có bị vi phạm không
    def fix_down(self, index):
        # Mỗi nút có 2 con, vì vậy trong mảng, nút i có con trái ở index * i+1 và con phải ở index 2*i+2
        index_left = 2 * index + 1
        index_right = 2 * index + 2
        # Đây là max heap nên nút cha luôn lớn hơn các nút con
        index_largest = index

        # Nếu nút con trái lớn hơn nút cha: nút lớn nhất là nút trái
        if index_left < self.heap_size and self.heap[index_left] > self.heap[index]:
            index_largest = index_left

        # Xác định xem nút con trái hay nút con phải lớn hơn
        # Đầu tiên kiểm tra xem chỉ số cung cấp có hợp lệ không (không lớn hơn kích thước heap)
        # Nếu nút con phải lớn hơn nút con trái: nút lớn nhất là nút phải
        if index_right < self.heap_size and self.heap[index_right] > self.heap[index_largest]:
            index_largest = index_right

        # Không muốn đổi chỗ phần tử với chính nó
        if index != index_largest:
            self.swap(index, index_largest)
            # Kiểm tra đệ quy xuống cây để kiểm tra xem có vi phạm tính chất heap khác không
            # và sửa chữa nếu cần
            self.fix_down(index_largest)

    # Sắp xếp heap
    # Mỗi phép lấy (poll) mất O(logN) thời gian vì phương thức fix down
    # Điều này làm cho thời gian chạy tổng cộng là O(NlogN) cho heap sort
    def heap_sort(self):
        # Giảm kích thước heap trong phương thức poll nên phải lưu lại
        size = self.heap_size

        for i in range(0, size):
            max_val = self.poll()
            print(max_val)

    # Đổi chỗ 2 phần tử với (index1, index2) trong mảng heap
    def swap(self, index1, index2):
        self.heap[index2], self.heap[index1] = self.heap[index1], self.heap[index2]

# Tạo một heap và thêm các phần tử
heap = Heap()
heap.insert(13)
heap.insert(-2)
heap.insert(0)
heap.insert(8)
heap.insert(1)
heap.insert(-5)
heap.insert(99)

# Sắp xếp heap và in ra kết quả
heap.heap_sort()
