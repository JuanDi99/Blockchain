from src.Bloque import Bloquegen
from datetime import datetime
from src.Bloque import Bloquegen
class Blockchain(metaclass=Singleton)::
    def __init__(self):
        self._lista = []
        self.crearGenesis()
        self.__zero_count = 0

    def crearGenesis(self):
        bloqueGenesis = Bloquegen(0, "", "","0","0","2021-01-01 00:00:00", self.__zero_count)
        self.lista.append(bloqueGenesis) 

    def dameBloqueid(self,id):
        return self.lista[id].hashBlq
    
    def crearbloq(self, mail, motivo, hasharc):
        newBloque = Bloquegen(self.dameidsiguientebloque(), mail, motivo, hasharc, self.damehashanterior(),timestamp, self.__zero_count)
        self.lista.append(newBloque)
        

    def dameidsiguientebloque(self):
        return len(self.lista)

    def damehashanterior(self):
        return self.damehashid(self.dameidsiguientebloque() - 1)

    def damehashid(self, id):
        return self.lista[id].hashBlq

    def damebloqueid(self,id):
        return self.lista[id]

    def setZero_count(self, count):
        self.__zero_count = count
    
    def damebloquexhash(self, searchhash):
        for bloque in self.__lista:
            if searchhash == bloque.hashBlq:
                return bloque
        return 'none'