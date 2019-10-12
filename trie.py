import trie_nodo as node
import collections
class trie:

    def __init__(self):
        self.raiz = dict()
        self.numNodo = 0

    def addPalabra(self, palabra):
        nodo = self.raiz.get(palabra[0],False)
        if(not nodo):
            self.numNodo += 1
            nodo = node.trie_nodo(1, None, False,palabra[0],self.numNodo)
            self.raiz[palabra[0]] = nodo
        
        
        
        
        for letra in palabra[1:-1]:
            self.numNodo += nodo.anadirHijo(letra, False,self.numNodo)
            nodo = nodo.recuperarNodo(letra)

        if (len(palabra) > 1):
            self.numNodo += nodo.anadirHijo(palabra[-1], True,self.numNodo)
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
    
    def getNumNodo(self):
        return self.numNodo

    def getAllNode(self):
        res = list()
        c = collections.deque()
        for e in self.raiz.values():
            c.append(e)
        while len(c)>0:
            nodo = c.pop()
            res.append(nodo)
            for e in nodo.hijos.values():
                c.append(e)
        return res 
                


