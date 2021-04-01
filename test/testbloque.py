import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from src.blockchain import Bloquegen



class Test(unittest.TestCase): 
   def test_Bloquegen(self):
      test = Bloquegen("aaa",1,"a")
      self.assertEqual(test.mail,"aaa")

if __name__ == '__main__':
   unittest.main()