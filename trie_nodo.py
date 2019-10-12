
class trie_nodo:

    

    def __init__(self, indice, nodo_padre, final):
        self.indice = indice
        self.nodo_padre = nodo_padre
        self.final = final
        self.hijos = dict()


    def anadirHijo(self, letra, esPalabra):
        nodo = self.hijos.get(letra,False)
        if(not nodo):
            self.hijos[letra] = trie_nodo(self.indice + 1, self, esPalabra)
            return 1
        
        nodo.final = esPalabra
        return 0

        

    def recuperarNodo(self, letra):
        return self.hijos[letra]

