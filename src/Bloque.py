
from hashlib import sha256
import json

class Bloquegen:
    def __init__(self, id, mail, motivo, hasharc,hashAnt):
        self.id = id
        self.mail = mail
        self.motivo = motivo  
        self.archivo = hasharc
        self.hashAnt = hashAnt
        self.hashBlq = self.crearHash()
        
        

    def crearHash(self):
        hash = json.dumps(self.__dict__, sort_keys=True)
        return sha256(hash.encode()).hexdigest()


    
   
   