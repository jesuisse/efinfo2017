# -*- coding: utf-8 -*-

import unittest
from chainreaction5 import *


class Chainreaction_1(unittest.TestCase):
    #def test_macheTeilchen(self):
    #self.assertIsNotNone(macheTeilchen(), [pos, farbe, v])

    def test_normalisiere(self):
        vektor = [4, 5]
        n = normalisiere(vektor)
        self.assertEqual(n[0]**2 + n[1]** 2, 1)


    def testmacheTeilchen(self):
        t = macheTeilchen()
        self.assertEqual(type(t), list)
        self.assertEqual(len(t), 3)

    def testmacheTeilchen2(self):
        self.assertIsNotNone(macheTeilchen(), Teilchen)

    def testmacheTeilchen3(self):
        t = macheTeilchen()
        self.assertEqual(type(t[2]), list)
        self.assertEqual(type(t[2][0]), float)
        self.assertEqual(type(t[2][1]), float)










