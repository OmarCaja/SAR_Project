import trie
import numpy as np


def levenshteinTrie(p,t,tolerancia):
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
                

                indicePadre = n.nodo_padre.indice


                if(n.myKey == p[i-1]):
                    disMin = dis[i-1][indicePadre]
                else:
                    disMin = dis[i-1][indicePadre]+1
                
                if(dis[i][indicePadre]+1 < disMin):
                    if(dis[i][indicePadre]+1 < disMin):
                        disMin = dis[i][indicePadre]+1

                if(dis[i-1][n.indice]+1 < disMin):
                    if(dis[i-1][n.indice]+1 < disMin):
                        disMin = dis[i-1][n.indice]+1


                dis[i][n.indice] = disMin

                if(i == lenpalabra and n.final and disMin <= tolerancia):
                    palabra = n.myKey
                    padre = n.nodo_padre
                    while padre :
                        
                        palabra = padre.myKey + palabra
                        padre = padre.nodo_padre
                    res.append((palabra,disMin))
    
    return res




def damareu_levenshteinTrie(p,t,tolerancia):
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
                

                indicePadre = n.nodo_padre.indice


                if(n.myKey == p[i-1]):
                    disMin = dis[i-1][indicePadre]
                else:
                    disMin = dis[i-1][indicePadre]+1
                
                if(dis[i][indicePadre]+1 < disMin):
                    if(dis[i][indicePadre]+1 < disMin):
                        disMin = dis[i][indicePadre]+1

                if(dis[i-1][n.indice]+1 < disMin):
                    if(dis[i-1][n.indice]+1 < disMin):
                        disMin = dis[i-1][n.indice]+1
                if i >= 2 and n.profundidad >= 2:

                    if(n.myKey == p[i-2] and n.nodo_padre.myKey == p[i-1]):
                        abuelo = n.nodo_padre.nodo_padre.indice
                        if(dis[i-2][abuelo]+1 < disMin):
                            disMin = dis[i-2][abuelo]+1


                dis[i][n.indice] = disMin

                if(i == lenpalabra and n.final and disMin <= tolerancia):
                    palabra = n.myKey
                    padre = n.nodo_padre
                    while padre :
                        
                        palabra = padre.myKey + palabra
                        padre = padre.nodo_padre
                    res.append((palabra,disMin))
    
    return res