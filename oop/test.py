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


vandongvien = ThanhVien(None, None, None, None )
#print(vandongvien.GetHoTen())
#vandongvien.NhapThongTin()
#vandongvien.ThemThongTin()
#print(vandongvien.GetThongTin())
#print(vandongvien.GetHoTen())




#vandongvien = ThanhVien(    id = int(input('Nhập ID: ')), 
#                            hoten = input('Nhập Họ Tên: '), 
#                            cannang = int(input('Nhập cân nặng: ')), 
#                            chieucao= int(input('Nhập chiều cao: '))
#                        )



while True:
    khoidong = input('Hello, muốn làm gì: ')
    if khoidong == 'them':
        vandongvien.NhapThongTin()
        vandongvien.ThemThongTin()
        print(f'Thông tin vận động viên mới:{vandongvien.GetThongTin()} và {vandongvien.GetChieuCao()} ')
    if khoidong == 'xem':
        a = 0
        for i in vandongvien.GetThongTin():
            if a < i[3]:
                a = i[3]
            
        print(a)


    elif khoidong == 'exit':
        print("..........")
        break