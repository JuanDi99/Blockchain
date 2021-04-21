from datetime import datetime
from hashlib import sha256
from bson import json_util
import json

class Bloquegen: # Atributos del bloque
    def __init__(self, id, mail, motivo, hasharc,hashAnt,timestamp,zero_count):
        self.nonce = 0 #Atributo contador para zero_count
        self.id = id #index de cada bloque
        self.mail = mail
        self.motivo = motivo  
        self.archivo = hasharc #hash del archivo
        self.hashAnt = hashAnt #hast anterior
        self.timestamp = timestamp
        self.hashBlq = self.crearHash(zero_count)
        


    def crearHash(self, zero_count):#metodo para crear hash teniendo en cuenta el zero count para la complejidad 
        if zero_count == 0:
            zero_count = 2 if (datetime.strptime(self.timestamp, '%Y-%m-%d %H:%M:%S').day % 2 == 0 ) else 1
        while True:
            newHash = self.hash()
            if newHash[0:zero_count] == '0' * zero_count:
                break
            else:
                self.nonce += 1
        return newHash

    def hash(self):#hashear los datos 
        hash = json.dumps(self.__dict__, sort_keys=True, default=json_util.default)
        return sha256(hash.encode()).hexdigest()


    
   
   