class trie_nodo:

    def __init__(self, profundidad, nodo_padre, final, myKey, indice):
        self.profundidad = profundidad
        self.nodo_padre = nodo_padre
        self.final = final
        self.hijos = dict()
        self.myKey = myKey
        self.indice = indice

    def anadirHijo(self, letra, esPalabra, indice):
        nodo = self.hijos.get(letra, False)
        if (not nodo):
            self.hijos[letra] = trie_nodo(self.profundidad + 1, self, esPalabra, letra, indice + 1)
            return 1

        nodo.final = esPalabra
        return 0

    def recuperarNodo(self, letra):
        return self.hijos[letra]
