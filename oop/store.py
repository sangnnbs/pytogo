class ThanhVien:
    
    # Bien Private

    
    # Khoi tao bien thanh vien
    
    def __init__(self, id, hoten, cannang, chieucao):
        
        self.__id = id
        self.__hoten = hoten
        self.__cannang = cannang
        self.__chieucao = chieucao

    def GetHoTen(self):
        return self.__hoten

    def GetChieuCao(self):
        return self.__chieucao

    def ThayDoiChieuCao(self, a):
        self.__chieucao = a
    
    def GetCanNang(self):
        return self.__cannang
        

vandongvien1 = ThanhVien(1, 'Sang', 37, 190)
vandongvien2 = ThanhVien(2, 'Song', 55, 134)
vandongvien3 = ThanhVien(3, 'Seng', 77, 193)
vandongvien4 = ThanhVien(4, 'Syng', 77, 198)
vandongvien5 = ThanhVien(5, 'Geng', 100, 166)




list_vdv = [vandongvien1, vandongvien2, vandongvien3, vandongvien4, vandongvien5]
tim = list_vdv[0]

for i in list_vdv:
    if tim.GetChieuCao() > i.GetChieuCao():
        tim = i
    if tim.GetCanNang() < i.GetCanNang():
        tim = i
    
    

        

print(f"Vận động viên {tim.GetHoTen()} có {tim.GetChieuCao()} thấp nhất Team")
print(f"Vận động viên {tim.GetHoTen()} có {tim.GetCanNang()} nặng nhất Team")