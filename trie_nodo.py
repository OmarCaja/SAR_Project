
class trie_nodo:

    

    def __init__(self, profundidad, nodo_padre,myKey,indice, final=False):
        self.profundidad = profundidad
        self.nodo_padre = nodo_padre
        self.final = final
        self.hijos = dict()
        self.myKey = myKey
        self.indice = indice


    def anadirHijo(self, letra,indice):
        nodo = self.hijos.get(letra,False)
        if(not nodo):
            self.hijos[letra] = trie_nodo(self.profundidad + 1, self,letra,indice+1)
            return 1
        
        return 0

        

    def recuperarNodo(self, letra):
        return self.hijos[letra]

