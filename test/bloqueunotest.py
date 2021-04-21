import os
import sys
from datetime import datetime
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from src.Blockchain import Blockchain
from src.Bloque import Bloquegen
class BloqueTest(unittest.TestCase):
 def test_bloqueuno(self):
        test = Bloquegen(0,"juandi@gmail.com", "prueba", "hashArc","hashanterior","2021-04-11 21:00:00",0)
        self.assertEqual(0, test.id)
        self.assertEqual("juandi@gmail.com", test.mail)
        self.assertEqual("prueba", test.motivo)
        self.assertEqual("hashArc", test.archivo)
        self.assertEqual("hashanterior", test.hashAnt)
        self.assertEqual("2021-04-11 21:00:00", test.timestamp)       
        self.assertEqual('0df8c68664f684fa937b3371d1b9b83f2d71b69080a5d7d5e9c28c08718bb4e5', test.hashBlq)
        
if __name__ == '__main__': unittest.main()