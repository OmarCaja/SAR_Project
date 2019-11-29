import collections


def ramificacion(palabra, trie, tolerancia):
    cola = collections.deque()
    cola.append((0, trie.raiz, 0, "nada"))
    res = set()
    while (len(cola) != 0):
        (letra, nodo, distancia, forma) = cola.pop()
        if (distancia > tolerancia):
            continue

        if (letra == len(palabra) and nodo.final and distancia <= tolerancia):
            palabraRes = nodo.myKey
            padre = nodo.nodo_padre
            while padre:
                palabraRes = padre.myKey + palabraRes
                padre = padre.nodo_padre
            res.add(palabraRes)

        if (letra < len(palabra)):
            cola.append((letra + 1, nodo, distancia + 1, "l+1"))

        for n in nodo.hijos.values():
            cola.append((letra, n, distancia + 1, "n+1"))
            if (letra < len(palabra)):
                if (palabra[letra] == n.myKey):
                    cola.append((letra + 1, n, distancia, "s"))
                else:
                    cola.append((letra + 1, n, distancia + 1, "s"))

    return res


    def ramificacion_damerau(palabra, trie, tolerancia):
    cola = collections.deque()
    cola.append((0,trie.raiz,0,"nada"))
    res = set()
    while (len(cola) != 0):
        (letra, nodo, distancia,forma) = cola.pop()
        if(distancia > tolerancia):
            continue
            
        if (letra == len(palabra) and nodo.final and distancia <= tolerancia):
            palabraRes = nodo.myKey
            padre = nodo.nodo_padre
            while padre :            
                palabraRes = padre.myKey + palabraRes
                padre = padre.nodo_padre
            res.add(palabraRes)
        
        
        if(letra < len(palabra)):
            cola.append((letra+1,nodo,distancia+1,"l+1"))
           
        for n in nodo.hijos.values():
            cola.append((letra,n,distancia+1,"n+1"))
            if(letra < len(palabra)):
                if(palabra[letra] == n.myKey):
                    cola.append((letra+1,n,distancia,"s"))
                else:
                    cola.append((letra+1,n,distancia+1,"s"))

            if(letra >=2 and letra < len(palabra) and nodo.indice != 0):
                if(palabra[letra-1] == n.myKey and palabra[letra] == nodo.myKey):
                    cola.append((letra+1,n,distancia,"sus"))

            
    return list(res)
