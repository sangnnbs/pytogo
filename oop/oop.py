
def listInc(list):

    for i in range(0, len(list)):
        for j in range(i + 1, len(list)): #------> range(i + 1, len(listA))
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

