class MayBay:
    def __init__(self, so_hieu, loai, so_cho):
        self.so_hieu = so_hieu
        self.loai = loai
        self.so_cho = so_cho

class ChuyenBay:
    def __init__(self, ma_cb, ngay_gio_khoi_hanh, san_bay_den, trangThai, so_hieu_mb):
        self.ma_cb = ma_cb
        self.ngay_gio_khoi_hanh = ngay_gio_khoi_hanh
        self.san_bay_den = san_bay_den
        self.trangThai = trangThai
        self.so_hieu_mb = so_hieu_mb
        self.danh_sach_ve = []

    def dat_ve(self, cmnd):
        # Kiểm tra trạng thái chuyến bay
        if self.trangThai == 0:
            print("Chuyến bay đã bị hủy.")
            return
        elif self.trangThai == 2:
            print("Chuyến bay đã hết vé.")
            return
        
        # Kiểm tra số chỗ còn trống
        if len(self.danh_sach_ve) < MayBayDict[self.so_hieu_mb].so_cho:
            ve = {"STT": len(self.danh_sach_ve) + 1, "CMND": cmnd}
            self.danh_sach_ve.append(ve)
            print(f"Đặt vé thành công cho CMND {cmnd}")
        else:
            print("Chuyến bay đã hết chỗ.")

class HanhKhach:
    def __init__(self, cmnd, ho, ten, phai):
        self.cmnd = cmnd
        self.ho = ho
        self.ten = ten
        self.phai = phai

# Tạo các danh sách lưu thông tin
MayBayDict = {}
ChuyenBayList = []
HanhKhachList = []

# Chức năng a: Cập nhật danh sách máy bay
def cap_nhat_may_bay():
    # Hãy thêm code cho chức năng này
    pass

# Chức năng b: Cập nhật chuyến bay
def cap_nhat_chuyen_bay():
    # Hãy thêm code cho chức năng này
    pass

# Chức năng c: Đặt vé
def dat_ve():
    # Hãy thêm code cho chức năng này
    pass

# Chức năng d: In danh sách hành khách thuộc chuyến bay
def in_danh_sach_hanh_khach(ma_cb):
    # Hãy thêm code cho chức năng này
    pass

# Chức năng e: In danh sách các chuyến bay khởi hành trong ngày
def in_danh_sach_chuyen_bay_trong_ngay(ngay):
    # Hãy thêm code cho chức năng này
    pass

# Chức năng f: In danh sách vé còn trống của chuyến bay
def in_danh_sach_ve_con_trong(ma_cb):
    # Hãy thêm code cho chức năng này
    pass

# Chức năng g: Thống kê số lượt thực hiện chuyến bay của từng máy bay
def thong_ke_so_luot_thuc_hien_chuyen_bay():
    # Hãy thêm code cho chức năng này
    pass

# Chạy chương trình
while True:
    print("1. Cập nhật danh sách máy bay")
    print("2. Cập nhật chuyến bay")
    print("3. Đặt vé")
    print("4. In danh sách hành khách thuộc chuyến bay")
    print("5. In danh sách các chuyến bay khởi hành trong ngày")
    print("6. In danh sách vé còn trống của chuyến bay")
    print("7. Thống kê số lượt thực hiện chuyến bay của từng máy bay")
    print("0. Thoát")
    
    choice = int(input("Chọn chức năng: "))
    
    if choice == 1:
        cap_nhat_may_bay()
    elif choice == 2:
        cap_nhat_chuyen_bay()
    elif choice == 3:
        dat_ve()
    elif choice == 4:
        ma_cb = input("Nhập mã chuyến bay: ")
        in_danh_sach_hanh_khach(ma_cb)
    elif choice == 5:
        ngay = input("Nhập ngày (dd/mm/yyyy): ")
        in_danh_sach_chuyen_bay_trong_ngay(ngay)
    elif choice == 6:
        ma_cb = input("Nhập mã chuyến bay: ")
        in_danh_sach_ve_con_trong(ma_cb)
    elif choice == 7:
        thong_ke_so_luot_thuc_hien_chuyen_bay()
    elif choice == 0:
        break
    else:
        print("Chức năng không hợp lệ. Hãy chọn lại.")
