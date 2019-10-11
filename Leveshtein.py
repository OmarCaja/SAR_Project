
import numpy as np


def damerau_levenshtein(p1,p2):
    l1 = len(p1)
    l2 = len(p2)
    dismax = l1 + l2 + 1
    m = np.empty(dtype = np.int8,shape=(l1 + 1, l2 + 1))
    for i in range(l1 + 1):
        for j in range(l2 + 1):
            dis = dismax
            if i == 0 and j == 0:
                dis = 0
            elif i == 0 and j > 0:
                dis = j
            elif i > 0 and j == 0:
                dis = i
            else:
                if p1[i - 1] == p2[j - 1]:
                    dis = m[i - 1, j - 1]
                else:
                    dis = m[i - 1, j - 1] + 1
                if m[i, j - 1] + 1 < dis:
                    dis = m[i, j - 1] +1
                if m[i - 1, j] + 1 < dis:
                    dis = m[i - 1, j] + 1
                """quitar siguiente if,es levenshtein normal"""
                if i > 1 and j > 1:
                    if p1[i - 1] == p2[j - 2] and p1[i - 2] == p2[j - 1]:
                        if m[i - 2, j - 2] + 1 < dis:
                            dis = m[i - 2, j - 2] + 1
            m[i, j] = dis
    return m
    
pal1 = "abc"
pal2 = "dbav"
print(damerau_levenshtein(pal1,pal2))