import sys
import unittest
import os
ruta = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ruta)
from src.Blockchain import Bloquegen, Blockchain

class Test(unittest.TestCase):
    def test_bloquegenesis_atributocorreo_esveradero_cuandomail_es_vacio(self):
        test = Blockchain()
        self.assertEqual(test.lista[0].mail, "")
    def test_bloquegenesis_atributoid_esverdadero_cuandoid_es_0(self):
        test = Blockchain()
        self.assertEqual(test.lista[0].id, 0)
    def test_bloquegenesis_atributomotivo_esverdadero_cuandomotivo_es_vacio(self):
        test = Blockchain()
        self.assertEqual(test.lista[0].motivo, "")
    def test_bloquegenesis_atributo_hash_anterior_esverdadero_cuando_hashanterior_es_string_cero(self):
        test = Blockchain()
        self.assertEqual(test.lista[0].hashAnt, "0")


if __name__ == '__main__':
    unittest.main() 