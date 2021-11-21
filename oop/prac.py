#------------CRAFTING STATION => FAIL, FAIL AND FAIL----------

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


def SaveFile(list):
    pickle_out = open('vdv.pkl', 'wb')
    pickle.dump(list, pickle_out)
    pickle_out.close()

def LoadFile():
    pickle_in = open('vdv.pkl', 'rb')
    pickle_in = pickle.load(pickle_in)
    return pickle_in


list_vdv = []

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

        SaveFile(list_vdv)

        print(f'Thông tin vận động viên mới:{list_vdv[len(list_vdv) - 1]} có ID: {vandongvien.GetID()} Họ Tên: {vandongvien.GetHoTen()}, chiều cao = {vandongvien.GetChieuCao()} , cân nặng = {vandongvien.GetCanNang()}')

    # Xem max chieu cao
    if khoidong == 'xem max cao':

        hoten = ''
        maxcao = 0
    
        
        for i in LoadFile():
            if maxcao < i.GetChieuCao():
                maxcao = i.GetChieuCao()
                hoten = i.GetHoTen()
        
        print(f'Vận động viên cao nhất với {maxcao} có họ tên {hoten}')
    
    # Xem max can nang
    if khoidong == 'xem max nang':
 

        hoten = ''
        cannang = 0
    
        
        for i in LoadFile():
            if cannang < i.GetCanNang():
                cannang = i.GetCanNang()
                hoten = i.GetHoTen()
        print(f'Vận động viên nặng nhất với {cannang} có họ tên {hoten}')

    # ----------AAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHH-------------
    if khoidong == 'tim id':
        
        list2 = LoadFile()
        
        hoten = 0
        id = int(input('Nhap id can tim:' ))
                
        for i in list2 :
            if id == i.GetID():
               id = i.GetID()
               hoten = i.GetChieuCao()
               
        print(f'Vận động viên với ID = {id} có họ tên {hoten}')

    elif khoidong == 'exit':
        print("..........")
        break
