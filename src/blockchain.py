import os
import sys
import json
from bson import json_util
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from src.singleton import Singleton
from datetime import datetime
from src.Bloque import Bloquegen


class Blockchain(metaclass=Singleton): #atributos de la blockchain
    def __init__(self):
        self.__lista = [] #Lista para almacenar los bloques de la blockchain
        self.__zero_count = 0
        self.__crearGenesis()
        

    def __crearGenesis(self): #metodo que crea el bloque genesis en vacio
        bloqueGenesis = Bloquegen(0, "", "","0","0","2021-01-01 00:00:00", self.__zero_count)
        self.__lista.append(bloqueGenesis) 

    def dameBloqueid(self,id):#Devuelve el id de un bloque
        return self.__lista[id]
    
    def __dameidsiguientebloque(self):#Devuelve el id del bloque siguiente
        return len(self.__lista)
    
    def __crearbloq(self, mail, motivo, hasharc,timestamp):#Metodo para crear un bloque
        newBloque = Bloquegen(self.__dameidsiguientebloque(), mail, motivo, hasharc, self.__damehashanterior(),timestamp, self.__zero_count)
        self.__lista.append(newBloque)
        

    def __damehashanterior(self):# Devuelve el hash del anterior bloque
        return self.damehashid(self.__dameidsiguientebloque() - 1)

    def damehashid(self, id):#Devuelve el hash con el id del bloque
        return self.__lista[id].hashBlq


    def setZero_count(self, count):#metodo para la complejidad
        self.__zero_count = count
    
    def damebloquexhash(self, searchhash):#Devuelve un bloque por medio de hash
        for bloque in self.__lista:
            if searchhash == bloque.hashBlq:
                return bloque
        