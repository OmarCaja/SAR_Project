import collections

from .trie_nodo import trie_nodo as node


class trie:

    def __init__(self):
        self.raiz = node(0, None, False, "", 0)
        self.numNodo = 0

    def addPalabra(self, palabra):
        nodo = self.raiz.hijos.get(palabra[0], False)
        if (not nodo):
            self.numNodo += 1
            nodo = node(1, self.raiz, False, palabra[0], self.numNodo)
            self.raiz.hijos[palabra[0]] = nodo

        for letra in palabra[1:-1]:
            self.numNodo += nodo.anadirHijo(letra, False, self.numNodo)
            nodo = nodo.recuperarNodo(letra)

        if (len(palabra) > 1):
            self.numNodo += nodo.anadirHijo(palabra[-1], True, self.numNodo)
        else:
            nodo.final = True

    def existePalabra(self, palabra):

        if (len(palabra) != 0):
            nodo = self.raiz.hijos.get(palabra[0], False)
            if (not nodo):
                return False
            for letra in palabra[1:]:
                nodo = nodo.recuperarNodo(letra)
                if (not nodo):
                    return False
            return nodo.final
        else:
            return True

    def getNumNodo(self):
        return self.numNodo

    def getAllNode(self):
        res = []
        c = collections.deque()
        for e in self.raiz.hijos.values():
            c.append(e)
        while (len(c) > 0):
            nuevo_nodo = c.pop()
            res.append(nuevo_nodo)
            for hijo in nuevo_nodo.hijos.values():
                c.append(hijo)

        res.sort(key=lambda nodo: nodo.indice)
        return res
    def index_words_list_in_trie(self, words_list):
        for word in words_list:
            self.addPalabra(word)
