import os
import sys
from datetime import datetime
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from src.blockchain import Blockchain
from src.bloque import Bloque

 def test_bloqueuno(self):
        test = Blockchain()
        test.crearbloq("juandi@gmail.com", "prueba", "hashArc")
        self.assertEqual(1, test.lista[1].id)
        self.assertEqual("juandi@gmail.com", test.lista[1].mail)
        self.assertEqual("prueba", test.lista[1].motivo)
        self.assertEqual("hashArc", test.lista[1].archivo)
        self.assertEqual("69e0c792b76a5be3a8d03d060cad1f7f69856e8db550ccd87f0ea1ca0344bc40", test.lista[1].hashAnt)
        self.assertEqual('eb2d4475624082bbc4d5b22f8cf2bc60de341be9395308b9e3a1a58caded1e19', test.damehashid(1))
        
if __name__ == '__main__': unittest.main()