import unittest
import os
import sys
import json
from bson import json_util
ruta = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ruta)
from src.singleton import Singleton
from src.Blockchain import Blockchain
from src.Bloque import Bloquegen

test = Blockchain()
test._Blockchain__crearbloq("correo@bloqueOne.com", "prueba", "hashArc", "2021-01-01 22:00:00")
test._Blockchain__crearbloq("correo@bloqueOne.com", "pruebaBloque2", "hashArc", "2021-01-01 22:00:10")

class Test(unittest.TestCase):
    def test_bloqueGenesis(self):
        bloquegen = test.dameBloqueid(0)
        self.assertEqual(0,bloquegen.id)
        self.assertEqual("",bloquegen.mail)
        self.assertEqual("",bloquegen.motivo)
        self.assertEqual("0",bloquegen.archivo)
        self.assertEqual("0",bloquegen.hashAnt)
        self.assertEqual("2021-01-01 00:00:00", bloquegen.timestamp)
        self.assertEqual("0bd586086ce0a8cfcf8bbbf665ca1e144277e65c0720810408307fbd7576a6c5", test.damehashid(0))

    def test_2_Bloque_uno_creado(self):
        bloque1 = test.dameBloqueid(1) #creamos un objeto bloque y le pasamos la id que le corresponde y despues se cargan los datos
        self.assertEqual(1, bloque1.id)
        self.assertEqual("correo@bloqueOne.com", bloque1.mail)
        self.assertEqual("prueba", bloque1.motivo)
        self.assertEqual("hashArc", bloque1.archivo)
        self.assertEqual("0bd586086ce0a8cfcf8bbbf665ca1e144277e65c0720810408307fbd7576a6c5", bloque1.hashAnt)
        self.assertEqual("2021-01-01 22:00:00", bloque1.timestamp)
        self.assertEqual('0242e056cfffdf36db91f7e9199dce47138e79f29afb86e605dc277e65a42fcb', test.damehashid(1))
    
    def test_3_Bloque_dos_creado(self):
        bloque2 = test.dameBloqueid(2)
        self.assertEqual(2, bloque2.id)
        self.assertEqual("correo@bloqueOne.com", bloque2.mail)
        self.assertEqual("pruebaBloque2", bloque2.motivo)
        self.assertEqual("hashArc", bloque2.archivo)
        self.assertEqual("0242e056cfffdf36db91f7e9199dce47138e79f29afb86e605dc277e65a42fcb", bloque2.hashAnt)
        self.assertEqual("2021-01-01 22:00:10", bloque2.timestamp)
        self.assertEqual('0e0b127d6007edeaf25648c832b8db9cdccb11ce910d5ff01359aa2a9e4a8a13', test.damehashid(2))
    
    def test_4_Identificar_bloque_por_hash(self):
        bloqueHash = test.damebloquexhash("0bd586086ce0a8cfcf8bbbf665ca1e144277e65c0720810408307fbd7576a6c5")
        bloque = test.dameBloqueid(0)
        self.assertEqual(bloque, bloqueHash)
    
if __name__ == '__main__':
    unittest.main()