import cgi, cgitb 

def listInc(list):                          # Space Complexity (0)= 1  ; Time Complexity (0) = n^2 

    for i in range(0, len(list)):   
        for j in range(i + 1, len(list)):  #------> range(i + 1, len(listA))
            if list[j] > list[i]:
                list[j], list[i] = list[i], list[j]
                
    return print(list)



def listDec(list):

    for i in range(0, len(list)):
        for j in range(i + 1, len(list)): #------> range(i + 1, len(listA))
            if list[j] < list[i]:
                list[j], list[i] = list[i], list[j]
    return print(list)

listA = [55,124,32,44,55,1,9]

listInc(listA) #-- Hàm list tăng
print('and')
listDec(listA) #-- Hàm list giảm



# Tách chuỗi string

text = 'dump v.duration n.dynamic adj.eager adj.economics n.economist n.editorial adj.efficiently adv'

def TachChuoi(a):
    x = a.split('.')
    c = ''
    b = []
    for i in x:
        c = i.split(' ')
        b.append(c[0])
            
    for i in range(0,len(b)):
        print(b[i])

TachChuoi(text)
