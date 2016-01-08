# -*- coding: utf-8 -*-

import unittest
from chainreaction5 import *


class Chainreaction_1(unittest.TestCase):


    def test_normalisiere(self):
        vektor = [4, 5]
        n = normalisiere(vektor)
        self.assertEqual(n[0]**2 + n[1]** 2, 1)


    def testmacheTeilchen(self):
        t = macheTeilchen()
        self.assertEqual(type(t), list)
        self.assertEqual(len(t), 3)
        #len fragt nach wie viele Elemente in liste sind

    def testmacheTeilchen2(self):
        t = macheTeilchen()
        self.assertIsNotNone(t)

    def testmacheTeilchen3(self):
        t = macheTeilchen()
        self.assertEqual(type(t[2]), list)
        self.assertEqual(type(t[2][0]), float)
        self.assertEqual(type(t[2][1]), float)










