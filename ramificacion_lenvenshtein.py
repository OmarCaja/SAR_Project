import trie
import collections

def ramificacion(palabra, trie, tolerancia):
    cola = collections.deque()
    cola.append((0,1,0))
    res = list()
    nodos = trie.getNodeDict()
    while (len(cola) != 0):
        (letra, nodo, distancia) = cola.pop()
        if (nodo.final and distancia <= tolerancia):
            palabra = nodos[nodo].myKey
            padre = nodos[nodo].nodo_padre
            while padre :            
                palabra = padre.myKey + palabra
                padre = padre.nodo_padre
            res.append(palabra)
        else:
            if(distancia > tolerancia):
                continue

            cola.append((letra+1,nodo,distancia+1))
            nodoSig = nodos[nodo+1]
            if(nodoSig.nodo.padre != 0)
            cola.append((letra, nodo, distacia + 1)

            
