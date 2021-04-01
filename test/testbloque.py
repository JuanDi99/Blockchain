import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from src.blockchain import Bloquegen



class Test(unittest.TestCase): 
   def test_Bloquegen(self):
      test = Bloquegen("Juandiproxd@gmail.com",1,"a")
      self.assertEqual(test.mail,"Juandiproxd@gmail.com")

if __name__ == '__main__':
   unittest.main()