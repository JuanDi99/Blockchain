import os
import sys
from datetime import datetime

import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from src.Blockchain import Blockchain
from src.Bloque import Bloquegen

class SingletonTest(unittest.TestCase):

    def test_Singleton(self):
            testSingleton1 = Blockchain()
            testSingleton2 = Blockchain()
            message = "Test Singleton no funciona"
            self.assertTrue(id(testSingleton1) == id(testSingleton2), message)

if __name__ == '__main__': unittest.main()