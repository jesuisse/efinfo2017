# -*- coding: utf-8 -*-

import unittest
from chainreaction_6 import *


class Chainreaction(unittest.TestCase):


    def test_normalisiere1(self):
        vektor = [6, 8]
        n = normalisiere(vektor)
        self.assertEqual(n[0]**2 + n[1]** 2, 1)

    def test_normalisiere2(self):
        vektor = [10, 12]
        n = normalisiere(vektor)
        self.assertEqual(n[0]**2 + n[1]** 2, 1)

    def test_normalisiere3(self):
        vektor = [2, 4]
        n = normalisiere(vektor)
        self.assertEqual(n[0]**2 + n[1]** 2, 1)

    def testmacheTeilchen(self):
        t = macheTeilchen()
        self.assertEqual(type(t), list)
        self.assertEqual(len(t), 3)

    def testmacheTeilchen2(self):
        t = macheTeilchen()
        self.assertIsNotNone(t)

    def testmacheTeilchen3(self):
        t = macheTeilchen()
        self.assertEqual(type(t[2]), list)
        self.assertEqual(type(t[2][0]), float)
        self.assertEqual(type(t[2][1]), float)

    def bewegeTeilchen1(self):
        dt = 6
        pos = teilchen[2,4]
        v = teilchen[2,8]
        self.assertEqual(pos[0] + v [0] * dt, pos[0])
        self.assertEqual(pos[1] + v [1] * dt, pos[1])

    def bewegeTeilchen2(self):
        dt = 4
        pos = teilchen[1,2]
        v = teilchen[2,1]
        self.assertEqual(pos[0] + v [0] * dt, pos[0])
        self.assertEqual(pos[1] + v [1] * dt, pos[1])

    def bewegeTeilchen3(self):
        dt = 2
        pos = teilchen[3,6]
        v = teilchen[2,1]
        self.assertEqual(pos[0] - v [0] * dt, pos[0])
        self.assertEqual(pos[1] - v [1] * dt, pos[1])

    def bewegeTeilchen4(self):
        dt = 2
        pos = teilchen[9,12]
        v = teilchen[3,2]
        self.assertEqual(pos[0] - v [0] * dt, pos[0])
        self.assertEqual(pos[1] - v [1] * dt, pos[1])