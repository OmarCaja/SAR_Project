import trie_nodo as node

class trie:

    raiz = dict()
    
    def addPalabra(self, palabra):
        
        nodo = node.trie_nodo(1, None, False)
        self.raiz[palabra[0]] = nodo
        
        for letra in palabra[1:-1]:
            nodo.anadirHijo(letra, False)
            nodo = nodo.recuperarNodo(letra)

        if (len(palabra) > 1):
            nodo.anadirHijo(palabra[-1], True)
        else:
            nodo.final = True


    def existePalabra(self, palabra):

        if (len(palabra) != 0):
                nodo = self.raiz.get(palabra[0], False)
            if(not nodo):
                return False
            for letra in palabra[1:]:
                nodo = nodo.recuperarNodo(letra)
                if (not nodo):
                    return False
            return nodo.final
        else:
            return True
                


