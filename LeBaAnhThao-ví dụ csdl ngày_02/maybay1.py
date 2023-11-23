class MayBay:
    def __init__(self, so_hieu, loai, so_cho):
        self.so_hieu = so_hieu
        self.loai = loai
        self.so_cho = so_cho

class ChuyenBay:
    def __init__(self, ma_cb, ngay_gio_khoi_hanh, san_bay_den, trang_thai, so_hieu_mb):
        self.ma_cb = ma_cb
        self.ngay_gio_khoi_hanh = ngay_gio_khoi_hanh
        self.san_bay_den = san_bay_den
        self.trang_thai = trang_thai
        self.so_hieu_mb = so_hieu_mb
        self.danh_sach_ve = []

    def dat_ve(self, cmnd):
        if self.trang_thai == 0:
            print("Chuyến bay đã bị hủy.")
            return
        elif self.trang_thai == 2:
            print("Chuyến bay đã hết vé.")
            return

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
    so_hieu = input("Nhập số hiệu máy bay: ")
    if so_hieu in MayBayDict:
        print("Máy bay đã tồn tại. Bạn có muốn cập nhật thông tin không?")
        choice = input("Nhập 'yes' để cập nhật hoặc 'no' để bỏ qua: ")
        if choice.lower() == 'yes':
            loai = input("Nhập loại máy bay: ")
            so_cho = int(input("Nhập số chỗ trống: "))
            MayBayDict[so_hieu] = MayBay(so_hieu, loai, so_cho)
            print("Cập nhật thông tin máy bay thành công.")
    else:
        loai = input("Nhập loại máy bay: ")
        so_cho = int(input("Nhập số chỗ trống: "))
        if so_cho < 20:
            print("Số chỗ trống phải ít nhất là 20.")
        else:
            MayBayDict[so_hieu] = MayBay(so_hieu, loai, so_cho)
            print("Thêm máy bay mới thành công.")

# Chức năng b: Cập nhật chuyến bay
def cap_nhat_chuyen_bay():
    ma_cb = input("Nhập mã chuyến bay: ")
    ngay_gio_khoi_hanh = input("Nhập ngày giờ khởi hành (dd/mm/yyyy hh:mm): ")
    san_bay_den = input("Nhập sân bay đến: ")
    trang_thai = int(input("Nhập trạng thái chuyến bay (0: hủy chuyến, 1: còn vé, 2: hết vé, 3: hoàn tất): "))
    so_hieu_mb = input("Nhập số hiệu máy bay: ")

    if so_hieu_mb not in MayBayDict:
        print("Máy bay không tồn tại.")
        return

    chuyen_bay = ChuyenBay(ma_cb, ngay_gio_khoi_hanh, san_bay_den, trang_thai, so_hieu_mb)
    ChuyenBayList.append(chuyen_bay)
    print("Thêm chuyến bay mới thành công.")

# Chức năng c: Đặt vé
def dat_ve():
    ma_cb = input("Nhập mã chuyến bay: ")
    cmnd = input("Nhập số CMND: ")

    for chuyen_bay in ChuyenBayList:
        if chuyen_bay.ma_cb == ma_cb:
            chuyen_bay.dat_ve(cmnd)
            return

    print("Không tìm thấy chuyến bay với mã đã nhập.")

# Chức năng d: In danh sách hành khách thuộc chuyến bay
def in_danh_sach_hanh_khach(ma_cb):
    for chuyen_bay in ChuyenBayList:
        if chuyen_bay.ma_cb == ma_cb:
            print(f"DANH SÁCH HÀNH KHÁCH THUỘC CHUYẾN BAY {ma_cb}")
            print(f"Ngày giờ khởi hành: {chuyen_bay.ngay_gio_khoi_hanh}")
            print(f"Nơi đến: {chuyen_bay.san_bay_den}")
            print("STT  SỐ VÉ  SỐ CMND  HỌ TÊN  PHÁI")
            for ve in chuyen_bay.danh_sach_ve:
                cmnd = ve["CMND"]
                for hanh_khach in HanhKhachList:
                    if hanh_khach.cmnd == cmnd:
                        stt = ve["STT"]
                        ho = hanh_khach.ho
                        ten = hanh_khach.ten
                        phai = hanh_khach.phai
                        print(f"{stt}    {cmnd}    {ho} {ten}    {phai}")
            return
    print(f"Không tìm thấy chuyến bay với mã {ma_cb}.")

# Chức năng e: In danh sách các chuyến bay khởi hành trong ngày
def in_danh_sach_chuyen_bay_trong_ngay(ngay):
    print(f"DANH SÁCH CÁC CHUYẾN BAY KHỞI HÀNH TRONG NGÀY {ngay}")
    print("MÃ CB  NGÀY GIỜ KHỞI HÀNH  SÂN BAY ĐẾN  TRẠNG THÁI")
    for chuyen_bay in ChuyenBayList:
        if ngay in chuyen_bay.ngay_gio_khoi_hanh:
            print(f"{chuyen_bay.ma_cb}  {chuyen_bay.ngay_gio_khoi_hanh}  {chuyen_bay.san_bay_den}  {chuyen_bay.trang_thai}")

# Chức năng f: In danh sách vé còn trống của chuyến bay
def in_danh_sach_ve_con_trong(ma_cb):
    for chuyen_bay in ChuyenBayList:
        if chuyen_bay.ma_cb == ma_cb:
            if chuyen_bay.trang_thai == 0:
                print("Chuyến bay đã bị hủy.")
                return
            elif chuyen_bay.trang_thai == 2:
                print("Chuyến bay đã hết vé.")
                return
            print(f"DANH SÁCH VÉ CÒN TRỐNG CỦA CHUYẾN BAY {ma_cb}")
            print("STT  SỐ VÉ")
            for ve in chuyen_bay.danh_sach_ve:
                print(f"{ve['STT']}    {ve['CMND']}")
            return
    print(f"Không tìm thấy chuyến bay với mã {ma_cb}.")

# Chức năng g: Thống kê số lượt thực hiện chuyến bay của từng máy bay
def thong_ke_so_luot_thuc_hien_chuyen_bay():
    print("THỐNG KÊ SỐ LƯỢT THỰC HIỆN CHUYẾN BAY CỦA TỪNG MÁY BAY")
    print("SỐ HIỆU MÁY BAY  SỐ LƯỢT THỰC HIỆN CHUYẾN BAY")
    may_bay_luot_thuc_hien = {}
    for chuyen_bay in ChuyenBayList:
        if chuyen_bay.trang_thai == 3:  # Chuyến bay đã hoàn tất
            if chuyen_bay.so_hieu_mb in may_bay_luot_thuc_hien:
                may_bay_luot_thuc_hien[chuyen_bay.so_hieu_mb] += 1
            else:
                may_bay_luot_thuc_hien[chuyen_bay.so_hieu_mb] = 1
    for so_hieu_mb, luot in may_bay_luot_thuc_hien.items():
        print(f"{so_hieu_mb}  {luot}")

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
    
    choice = input("Chọn chức năng (1/2/3/4/5/6/7/0): ")
    
    if choice == '1':
        cap_nhat_may_bay()
    elif choice == '2':
        cap_nhat_chuyen_bay()
    elif choice == '3':
        dat_ve()
    elif choice == '4':
        ma_cb = input("Nhập mã chuyến bay: ")
        in_danh_sach_hanh_khach(ma_cb)
    elif choice == '5':
        ngay = input("Nhập ngày (dd/mm/yyyy): ")
        in_danh_sach_chuyen_bay_trong_ngay(ngay)
    elif choice == '6':
        ma_cb = input("Nhập mã chuyến bay: ")
        in_danh_sach_ve_con_trong(ma_cb)
    elif choice == '7':
        thong_ke_so_luot_thuc_hien_chuyen_bay()
    elif choice == '0':
        break
    else:
        print("Chức năng không hợp lệ. Hãy chọn lại.")

