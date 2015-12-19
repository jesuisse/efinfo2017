# -*- coding: utf-8 -*-

import unittest
from chainreaction1 import *


class Chainreaction_1(unittest.TestCase):
    #def test_macheTeilchen(self):
        #self.assertIsNotNone(macheTeilchen(), [pos, farbe, v])

   def test_normalisiere(self):
       self.assertEqual(normalisiere(vektor), 1)
   def testnormalisiere2(self):
        self.assertIs(laenge, 1)

    def testmacheTeilchen(self):
        self.assertIn(macheTeilchen(), Teilchen)

    def testmacheTeilchen2(self):
        self.assertIsNotNone(macheTeilchen(), Teilchen)

    def testmacheTeilchen3(self):
        self.assertEqual(macheTeilchen(), v == float)











if __name__ == "__main__":