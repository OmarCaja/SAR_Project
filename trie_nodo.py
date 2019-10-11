
class trie_nodo:

    hijos = dict()

    def __init__(self, indice, nodo_padre, final):
        self.indice = indice
        self.nodo_padre = nodo_padre
        self.final = final


    def anadirHijo(self, letra, esPalabra):
        self.hijos[letra] = trie_nodo(self.indice + 1, self, esPalabra)

    def recuperarNodo(self, letra):
        return self.hijos[letra]

