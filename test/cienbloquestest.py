import unittest
import os
import sys
ruta = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ruta)
from src.Blockchain import Blockchain
from src.Bloque import Bloquegen

class Bloques100Test(unittest.TestCase):
    def test_100_bloques(self):
        test = Blockchain()
        for i in range(100):
            test._Blockchain__crearbloq("juandi@gmail.com", "test", "hashArch", "2021-04-12 13:00:00")
        bloque49 = test.dameBloqueid(49)
        bloque50 = test.dameBloqueid(50)
        self.assertEqual(bloque50.hashAnt, bloque49.hashBlq)#Se compara los hash de los 2 bloques si son iguales
        bloque = Bloquegen(50, "juandi@gmail.com", "test", "hashArch",test.dameBloqueid(49).hashBlq, "2021-04-12 13:00:00", 0)
        self.assertEqual(bloque.hashBlq, bloque50.hashBlq)# Se compara el hash del bloque con el de la blockchain

if __name__ == '__main__':
    unittest.main()