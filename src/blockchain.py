from datetime import datetime
from hashlib import sha256
import json

class Bloquegen:
    def __init__(self, email, motivo, archivo, hashAnt, hashBlq, hashVer):
        self.email = email
        self.motivo = motivo  
        self.archivo = archivo
        self.hashAnt = hashAnt
        self.hashBlq = hashBlq
        self.hashVer = hashVer

    def crearHash(self):
        hash = json.dumps(self.__dict__, sort_keys=True)
        return sha256(hash.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.cadena = []
        self.crearGenesis()

    def crearGenesis(self):
        bloqueGenesis = Bloquegen("", "", "", "0", "0", "0")
        bloqueGenesis.hashBlq = bloqueGenesis.crearHash()
        self.cadena.append(bloqueGenesis) 