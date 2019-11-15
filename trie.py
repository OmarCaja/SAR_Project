import trie_nodo as node
import collections
class trie:

    def __init__(self):
        self.raiz = node.trie_nodo(0,None,"",0)
        self.numNodo = 0

    def addPalabra(self, palabra):
        nodo = self.raiz

        for letra in palabra:
            self.numNodo += nodo.anadirHijo(letra,self.numNodo)
            nodo = nodo.recuperarNodo(letra)
        nodo.final = True

    def existePalabra(self, palabra):

        if (len(palabra) != 0):
            nodo = self.raiz.recuperarNodo(palabra[0])
            if(not nodo):
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
        res = list()
        c = collections.deque()
        for e in self.raiz.hijos.values():
            c.append(e)
        while len(c)>0:
            nodo = c.pop()
            res.append(nodo)
            for e in nodo.hijos.values():
                c.append(e)
        return res 
                


