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


class Test(unittest.TestCase):
    def test_bloqueGenesis(self):
        test = Blockchain()
        self.assertEqual(0,test.lista[0].id)
        self.assertEqual("",test.lista[0].mail)
        self.assertEqual("",test.lista[0].motivo)
        self.assertEqual("0",test.lista[0].archivo)
        self.assertEqual("0",test.lista[0].hashAnt)
        self.assertEqual("69e0c792b76a5be3a8d03d060cad1f7f69856e8db550ccd87f0ea1ca0344bc40", test.dameBloqueid(0))
    
if __name__ == '__main__':
    unittest.main()