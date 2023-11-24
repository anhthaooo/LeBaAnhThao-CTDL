def radixsort(A):
    n = len(A)  # Số lượng phần tử trong danh sách A
    maxelement = max(A)  # Tìm giá trị lớn nhất trong danh sách A
    digits = len(str(maxelement))  # Số chữ số của giá trị lớn nhất

    l = []  # Danh sách tạm thời để lưu trữ các phần tử
    bins = [l] * 10  # Mảng chứa 10 thùng tạm thời, mỗi thùng đại diện cho một chữ số từ 0 đến 9

    # Bắt đầu vòng lặp qua từng chữ số (từ chữ số cuối cùng đến đầu)
    for i in range(digits):
        # Vòng lặp trong danh sách A để đặt các phần tử vào các thùng tương ứng
        for j in range(n):
            e = int((A[j]) / pow(10, i)) % 10  # Xác định chữ số của A[j]
            
            # Kiểm tra xem thùng tạm thời bins[e] có chứa phần tử nào không
            if len(bins[e]) > 0:
                bins[e].append(A[j])  # Thêm phần tử vào thùng tạm thời
            else:
                bins[e] = [A[j]]  # Tạo danh sách mới nếu thùng tạm thời trống

        k = 0  # Biến k để đánh dấu vị trí trong danh sách A

        # Lặp qua từng thùng tạm thời
        for x in range(10):
            # Kiểm tra xem thùng tạm thời bins[x] có chứa phần tử nào không
            if len(bins[x]) > 0:
                for y in range(len(bins[x])):
                    A[k] = bins[x].pop(0)  # Lấy phần tử từ thùng và đặt vào danh sách A
                    k = k + 1  # Tăng biến k để đánh dấu vị trí tiếp theo trong danh sách A

A = [28, 115, 435, 650, 760, 54]
print('Original Array:', A)
radixsort(A)
print('Sorted Array:', A)
