def is_min_heap(heap):
    # Tính số lượng phần tử không phải là lá. Trong heap dạng mảng, node cuối cùng không phải lá 
    # được tính bằng công thức (len(heap) - 2) // 2
    num_items = (len(heap) - 2) // 2

    # Duyệt qua từng node không phải lá
    for i in range(num_items):
        # Kiểm tra xem node hiện tại có lớn hơn bất kỳ con nào của nó không.
        # Nếu có, trả về False vì đây không phải là min heap
        if heap[i] > heap[2*i+1] or heap[i] > heap[2*i+2]:
            return False

    # Nếu không tìm thấy trường hợp vi phạm, trả về True.
    return True

# Kiểm tra chức năng của hàm với các ví dụ cụ thể
if __name__ == '__main__':
    # Danh sách n tuân theo tính chất min heap
    n = [1, 2, 3, 2, 5]
    # Danh sách m không tuân theo tính chất min heap
    m = [4, 6, 3, 2, -2]
    # In kết quả kiểm tra
    print(is_min_heap(n)) # In True nếu n là min heap
    print(is_min_heap(m)) # In False nếu m không phải là min heap
