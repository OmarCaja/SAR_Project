import numpy as np

def levenshtein(p, t, tolerancia):
    lenpalabra = len(p)
    numNodo = t.getNumNodo()
    nodos = t.getAllNode()
    dis= np.empty(dtype = np.int8,shape=(lenpalabra + 1, numNodo + 1))
    final_node_list = []
    res = []
    tol = int(tolerancia)
    dis[0][0] = 0
    for n in nodos:
        dis[0][n.indice] = n.profundidad
        
    for i in range(1, lenpalabra + 1):
        dis[i][0] = i
        char = p[i-1]
        end_check = i == lenpalabra

        for n in nodos:
            indicePadre = n.nodo_padre.indice
            indice = n.indice

            if(n.myKey == char):
                disMin = dis[i-1][indicePadre]
            else:
                disMin = dis[i-1][indicePadre] + 1
                
            if (dis[i][indicePadre] + 1 < disMin):
                disMin = dis[i][indicePadre] + 1

            if(dis[i-1][indice] + 1 < disMin):
                disMin = dis[i-1][indice] + 1

            dis[i][indice] = disMin

            if(end_check and disMin <= tol and n.final):
                final_node_list.append(n)
                    
    for node in final_node_list:
        palabra = node.myKey
        padre = node.nodo_padre
        while padre :
            palabra = padre.myKey + palabra
            padre = padre.nodo_padre
        res.append(palabra)
    
    return res




def damerau_levenshtein(p,t,tolerancia):
    lenpalabra = len(p)
    numNodo = t.getNumNodo()
    nodos = t.getAllNode()
    dis= np.empty(dtype = np.int8,shape=(lenpalabra + 1, numNodo + 1))
    final_node_list = []
    res = []
    tol = int(tolerancia)
    dis[0][0] = 0
    for n in nodos:
        dis[0][n.indice] = n.profundidad
        
    for i in range(1, lenpalabra + 1):
        dis[i][0] = i
        char = p[i-1]
        end_check = i == lenpalabra

        for n in nodos:
            indicePadre = n.nodo_padre.indice
            indice = n.indice

            if(n.myKey == char):
                disMin = dis[i-1][indicePadre]
            else:
                disMin = dis[i-1][indicePadre] + 1
                
            if (dis[i][indicePadre] + 1 < disMin):
                disMin = dis[i][indicePadre] + 1

            if(dis[i-1][indice] + 1 < disMin):
                disMin = dis[i-1][indice] + 1

            if i > 1 and n.profundidad > 1:
                if(n.myKey == p[i-2] and n.nodo_padre.myKey == char):
                    abuelo = n.nodo_padre.nodo_padre.indice
                    if(dis[i-2][abuelo] + 1 < disMin):
                        disMin = dis[i-2][abuelo] + 1

            dis[i][indice] = disMin

            if(end_check and disMin <= tol and n.final):
                final_node_list.append(n)
                    
    for node in final_node_list:
        palabra = node.myKey
        padre = node.nodo_padre
        while padre :
            palabra = padre.myKey + palabra
            padre = padre.nodo_padre
        res.append(palabra)
    
    return res
