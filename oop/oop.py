#------------------THIS IS OOP WORKPLAY-----------  

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

        pickle_out = open('vdv.pkl', 'wb')
        pickle.dump(list_vdv, pickle_out)
        pickle_out.close()

        print(f'Thông tin vận động viên mới:{list_vdv[len(list_vdv) - 1]} có ID: {vandongvien.GetID()} Họ Tên: {vandongvien.GetHoTen()}, chiều cao = {vandongvien.GetChieuCao()} , cân nặng = {vandongvien.GetCanNang()}')

    # Xem max chieu cao
    if khoidong == 'xem max cao':

        pickle_in = open('vdv.pkl', 'rb')
        pickle_in = pickle.load(pickle_in)

        hoten = ''
        a = 0
    
        
        for i in pickle_in:
            if a < i.GetChieuCao():
                a = i.GetChieuCao()
                hoten = i.GetHoTen()


    
        
        print(f'Vận động viên cao nhất với {a} có họ tên {hoten}')
    
    # Xem max can nang
    if khoidong == 'xem max nang':

        print(f'Vận động viên nặng nhất với {b} có họ tên {hoten} có ID: {obj.GetID()}')

    # ----------AAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHH-------------
    if khoidong == 'tim id':
        
        pickle_in = open('vdv.pkl', 'rb')
        pickle_in = pickle.load(pickle_in)

        hoten = 0
        c = int(input('Nhap id can tim:' ))
                
        for i in pickle_in :
            if c == i.GetID():
               c = i.GetID()
               hoten = i.GetChieuCao()
               print('dang vo IF')
            print(i.GetID(), i.GetHoTen(), c == i.GetID())  
        print(f'Vận động viên với ID = {c} có họ tên {hoten}')

    elif khoidong == 'exit':
        print("..........")
        break