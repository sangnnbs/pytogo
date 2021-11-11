import pickle


class ThanhVien:
    
    # Bien Private

    
    # Khoi tao bien thanh vien
    
    def __init__(self, id, hoten, cannang, chieucao):
        
        self.__id = id
        self.__hoten = hoten
        self.__cannang = cannang
        self.__chieucao = chieucao
 
    # Lấy ID
    def GetID(self):
        return self.__id

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

list_vdv = []

# File lưu thông tin VDV
file_vdv = "./vdv.txt"

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
    # Them thanh vien
    if khoidong == 'them':
        vandongvien = ThanhVien(    id = int(input('Nhập ID: ')), 
                                    hoten = input('Nhập Họ Tên: '), 
                                    cannang = int(input('Nhập cân nặng: ')), 
                                    chieucao= int(input('Nhập chiều cao: '))
                        )
        list_vdv.append(vandongvien)

        # Nạp vandongvien

        with open('vdv.pkl', 'wb') as w:
            pickle.dump(list_vdv, w)

        print(f'Thông tin vận động viên mới:{list_vdv[len(list_vdv) - 1]} có Họ Tên: {vandongvien.GetHoTen()}, chiều cao = {vandongvien.GetChieuCao()} , cân nặng = {vandongvien.GetCanNang()}')

        # Xuất vandongvien
        with open('vdv.pkl', 'rb') as r:
            new_list = pickle.load(r)
        
        print(new_list) # ---------> Hiện list_vdv đã thêm vandongvien

    # Xem max chieu cao
    if khoidong == 'xem max cao':

        with open('vdv.pkl', 'rb') as r:
            new_list = pickle.load(r)
        hoten = ''
        a = 0
        for obj in new_list:
            if a < obj.GetChieuCao():
                a = obj.GetChieuCao()
                hoten = obj.GetHoTen()

        print(f'Vận động viên cao nhất với {a} có họ tên {hoten}')
    
    # Xem max can nang
    if khoidong == 'xem max nang':

        with open('vdv.pkl', 'rb') as r:
            new_list = pickle.load(r)
        hoten = ''
        b = 0
        for obj in new_list:
            if b < obj.GetCanNang():
                b = obj.GetCanNang()  
                hoten = obj.GetHoTen()

        print(f'Vận động viên nặng nhất với {b} có họ tên {hoten}')

    # ----------AAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHH-------------
    if khoidong == 'tim id':
        
        with open('vdv.pkl', 'rb') as r:
            new_list = pickle.load(r)
        
        hoten = ''
        aidi = input('Nhập ID của vdv cần tìm: ')
        for obj in new_list:
            if aidi == obj.GetID():
                aidi = obj.GetID()  
                hoten = obj.GetHoTen()

        print(f'Vận động viên với ID = {aidi} có họ tên {hoten}')

    elif khoidong == 'exit':
        print("..........")
        break