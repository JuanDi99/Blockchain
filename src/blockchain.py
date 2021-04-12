from src.Bloque import Bloquegen
from datetime import datetime
from src.Bloque import Bloquegen
class Blockchain:
    def __init__(self):
        self.lista = []
        self.crearGenesis()

    def crearGenesis(self):
        bloqueGenesis = Bloquegen(0, "", "","0","0")
        self.lista.append(bloqueGenesis) 

    def dameBloqueid(self,id):
        return self.lista[id].hashBlq
    
    def crearbloq(self, mail, motivo, hasharc):
        newBloque = Bloquegen(self.dameidsiguientebloque(), mail, motivo, hasharc, self.damehashanterior())
        self.lista.append(newBloque)
        

    def dameidsiguientebloque(self):
        return len(self.lista)

    def damehashanterior(self):
        return self.damehashid(self.dameidsiguientebloque() - 1)

    def damehashid(self, id):
        return self.lista[id].hashBlq

    def getTime(self):
        datatime= datetime.now()
        return datatime.isoformat
