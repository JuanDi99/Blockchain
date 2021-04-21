import os
import sys
import json
from bson import json_util
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from src.singleton import Singleton
from datetime import datetime
from src.Bloque import Bloquegen


class Blockchain(metaclass=Singleton):
    def __init__(self):
        self.__lista = []
        self.__zero_count = 0
        self.__crearGenesis()
        

    def __crearGenesis(self):
        bloqueGenesis = Bloquegen(0, "", "","0","0","2021-01-01 00:00:00", self.__zero_count)
        self.__lista.append(bloqueGenesis) 

    def dameBloqueid(self,id):
        return self.__lista[id]
    
    def __dameidsiguientebloque(self):
        return len(self.__lista)
    
    def __crearbloq(self, mail, motivo, hasharc,timestamp):
        newBloque = Bloquegen(self.__dameidsiguientebloque(), mail, motivo, hasharc, self.__damehashanterior(),timestamp, self.__zero_count)
        self.__lista.append(newBloque)
        

    def __damehashanterior(self):
        return self.damehashid(self.__dameidsiguientebloque() - 1)

    def damehashid(self, id):
        return self.__lista[id].hashBlq


    def setZero_count(self, count):
        self.__zero_count = count
    
    def damebloquexhash(self, searchhash):
        for bloque in self.__lista:
            if searchhash == bloque.hashBlq:
                return bloque
        return 'none'