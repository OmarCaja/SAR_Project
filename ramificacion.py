def ramificacion(palabra, trie, tolerancia):
    cola = collections.deque()
    cola.append((0,0,0))
    res = list()
    nodos = trie.getNodeDict()
    numNodo = len(nodos)
    while (len(cola) != 0):
        print(cola)
        print(res)
        (letra, nodo, distancia) = cola.pop()
        print((letra,nodo,distancia))
        if(distancia > tolerancia):
            continue
            
        if (letra == len(palabra) and nodos[nodo].final and distancia <= tolerancia):
            palabra = nodos[nodo].myKey
            padre = nodos[nodo].nodo_padre
            while padre :            
                palabra = padre.myKey + palabra
                padre = padre.nodo_padre
            res.append(palabra)
        
        
        if(letra < len(palabra)-1):
            cola.append((letra+1,nodo,distancia+1))
           
        if(nodo+1 <= numNodo):
            nodoSig = nodos[nodo+1]
            if(nodoSig.nodo_padre == 0):
                cola.append((0,nodo+1,1))
            else:
                cola.append((letra, nodo+1,distancia+1))
                if(letra < len(palabra)):
                    if(palabra[letra] == nodoSig.myKey):
                        cola.append((letra+1, nodo+1, distancia))
                    else:
                        cola.append((letra+1, nodo+1, distancia+1))
    return res