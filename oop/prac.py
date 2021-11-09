#Đề bài: Viết chương trình cho phép quản lý vận động viên
#Các tính năng bao gồm
#- Cho phép Nhập số lượng vận động viên
#- Vận động viên bao gồm các thông tin sau: họ tên, cân nặng, chiều cao
#- Chương trình Cho phép xuất ra vận động viên cao nhất
#- Chương trình Cho phép xuất ra vận động viên nặng nhất

class ThanhVien:
    
    # Bien Private

    
    # Khoi tao bien thanh vien
    
    def __init__(self, id, hoten, cannang, chieucao):
        
        self.__id = id
        self.__hoten = hoten
        self.__cannang = cannang
        self.__chieucao = chieucao
        self.list_vdv = []

    # Nhập Thông tin VĐV mới
    def NhapThongTin(self):    
        self.__id = int(input('Nhập ID: '))
        self.__hoten = str(input('Nhập Họ Ten: '))
        self.__cannang = int(input('Nhập cân nặng: '))
        self.__chieucao = int(input('Nhập chiều cao: '))
    
    # Thêm thông tin và list => tuple
    def ThemThongTin(self):
        
        self.list_vdv.append((self.__id, self.__hoten, self.__cannang, self.__chieucao))

    
    def GetThongTin(self):
        return self.list_vdv
    
    # Lấy Họ Tên
    def GetHoTen(self):
        return self.__hoten
    
    # Lấy Chiều cao
    def GetChieuCao(self):
        return self.__chieucao
    
    # Lấy Cân nặng
    def GetCanNang(self):
        return self.__cannang


# Khởi tạo
vandongvien = ThanhVien(None, None, None, None )

# Chạy vòng lặp với input => nhập 'them' hoặc 'xem'
while True:
    khoidong = input('Hello, muốn làm gì: ')

    #Nhập 'them' để thêm thông tin vandongvien
    if khoidong == 'them': 
        vandongvien.NhapThongTin()
        vandongvien.ThemThongTin()
        print(f'Thông tin vận động viên mới:{vandongvien.GetThongTin()} và {vandongvien.GetChieuCao()} ') # Cần chỉnh lại hiển thị giá trị
    
    #Nhập 'xem' để xem chiều cao cao nhất ...........  i[3] = vị trí 0 1 2 3 trong tuple => chiều cao
    if khoidong == 'xem':
        a = 0
        for i in vandongvien.GetThongTin():
            if a < i[3]:
                a = i[3]
            
        print(a)

    #Nhập 'exit' để thoát vòng lặp
    elif khoidong == 'exit':
        print("..........")
        break