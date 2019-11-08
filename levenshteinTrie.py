import trie
import numpy as np


def levenshteinTrie(p,t):
    lenpalabra = len(p)
    numNodo = t.getNumNodo()
    nodos = t.getAllNode()
    dis= np.empty(dtype = np.int8,shape=(lenpalabra+1,numNodo+1))
    res = list()
        
    for i in range(lenpalabra+1):
        dis[i][0] = i
        for n in nodos:
            if(i == 0):
                dis[i][n.indice] = n.profundidad
            else:
                disMin = dis[i][n.indice] + 1

                if(n.nodo_padre):
                    indicePadre = n.nodo_padre.indice
                else:
                    indicePadre = 0
                if(dis[i][indicePadre]+1 < disMin):
                    disMin = dis[i][indicePadre]+1
                if(dis[i-1][indicePadre] < disMin):
                    disMin = dis[i-1][indicePadre]
                    if(p[i-1] != n.myKey):
                        disMin +=1
                dis[i][n.indice] = disMin
                if(i == lenpalabra and n.final):
                    palabra = n.myKey
                    padre = n.nodo_padre
                    while padre :
                        
                        palabra = padre.myKey + palabra
                        padre = padre.nodo_padre
                    res.append((palabra,disMin))
    
    return res

    