import os
import sys
from datetime import datetime

import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from src.Blockchain import Blockchain
from src.Bloque import Bloquegen

test = Blockchain()
    
class DosbloquesTest(unittest.TestCase):

    def test_dos_bloques_iguales(self):
        bloque1 = Bloquegen(0, 'juandi@prueba.com', 'prueba2BloquesIguales', 'hash_archivo', 'hash_anterior', '2021-04-11 21:00:00', 0)
        bloque2 = Bloquegen(0, 'juandi@prueba.com', 'prueba2BloquesIguales', 'hash_archivo', 'hash_anterior', '2021-04-11 21:00:00', 0)
        self.assertEqual(bloque1.hashBlq, bloque2.hashBlq)

if __name__ == '__main__': unittest.main()