import collections

def levenshtein(palabra, trie, tolerancia):
    cola = collections.deque()
    cola.append((0, trie.raiz, 0))
    res = set()
    final_node_list = []
    while (len(cola) != 0):
        (letra, nodo, distancia) = cola.pop()
        if(distancia <= int(tolerancia)):
            if letra < len(palabra): 
                cola.append((letra + 1, nodo, distancia + 1))
            
            for n in nodo.hijos.values():
                cola.append((letra, n, distancia + 1))

                if letra < len(palabra): 
                    if(palabra[letra] == n.myKey):
                        cola.append((letra + 1, n, distancia))
                    else:
                        cola.append((letra + 1, n, distancia + 1))

            if (letra == len(palabra) and nodo.final):
                final_node_list.append(nodo)                
    
    for node in final_node_list:
        palabra = node.myKey
        padre = node.nodo_padre
        while padre :
            palabra = padre.myKey + palabra
            padre = padre.nodo_padre
        res.add(palabra)
            
    return list(res)

def damerau_levenshtein(palabra, trie, tolerancia):
    cola = collections.deque()
    cola.append((0, trie.raiz, 0))
    res = set()
    final_node_list = []
    while (len(cola) != 0):
        (letra, nodo, distancia) = cola.pop()
        if(distancia <= int(tolerancia)):
            if letra < len(palabra): 
                cola.append((letra + 1, nodo, distancia + 1))
            
            for n in nodo.hijos.values():
                cola.append((letra, n, distancia + 1))

                if letra < len(palabra): 
                    if(palabra[letra] == n.myKey):
                        cola.append((letra + 1, n, distancia))
                    else:
                        cola.append((letra + 1, n, distancia + 1))

                    if(letra >=2 and nodo.indice != 0):
                        if(palabra[letra-1] == n.myKey and palabra[letra] == nodo.myKey):
                            cola.append((letra + 1, n, distancia))

            if (letra == len(palabra) and nodo.final):
                final_node_list.append(nodo)                
    
    for node in final_node_list:
        palabra = node.myKey
        padre = node.nodo_padre
        while padre :
            palabra = padre.myKey + palabra
            padre = padre.nodo_padre
        res.add(palabra)
            
    return list(res)