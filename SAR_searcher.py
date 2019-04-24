'''
Proyecto de Prácticas SAR: indexer
Autores:
Omar Caja García
Zhihao Zhang
Pablo López Orrios
Jose Antonio Culla de Moya
'''
import sys

def opAND(list1,list2):
    i = 0
    j = 0
    res = list()
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            res.append(list1[i])
            i+=1
            j+=1
        elif list1[i]< list2[j]:
            i+=1
        else:
            j+=1
    return res

#por eficiencia,cuando (l1 and notl2) o (notl1 and l2) se calcula con esta función
#caso = 1 (notl1 and l2)
#caso = 2 (l1 and notl2)
def opAND(list1,list2,caso):
    if caso == 1:
        si = list2
        no = list1
    else:
        si = list1
        no = list2

    res = list()
    i = 0
    j = 0
    while i < len(si) and j < len(no):
        if si[i] == no[j]:
            i+=1
            j+=1
        elif si[i] <no[j]:
            res.append(si[i])
            i+=1
        else:
            j+=1
    while i < len(si):
        res.append[si[i]]
        i+=1
    return res


def opOR(list1,list2):
    i = 0
    j = 0
    res = list()
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            res.append(list1[i])
            i+=1
            j+=1
        elif list1[i]< list2[j]:
            res.append(list1[i])
            i+=1
        else:
            res.append(list2[j])
            j+=1
    if i == len(list1):
        aux = j
        aux2 = list2
    else:
        aux = i
        aux2 = list1
    while aux < len(aux2):
        res.append(aux2[aux])
        aux+=1
    return res


#param: num = numero de docid
def opNOT(num,list):
    i = 0
    j = 0
    res = list()
    while i < len(list):
        if j == list[i]:
            j+=1
            i+=1
        elif j < i:
            res.append(j)
            j+=1
        else:
            i+=1
    while j < num:
        res.append(j)
        j+=1
    return res
         

if __name__ == "__main__":
    pass