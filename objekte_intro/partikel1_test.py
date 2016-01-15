# encoding: utf-8
__author__ = 'pax'

import unittest
from objekte_intro.partikel1 import Partikel

class PartikelTest(unittest.TestCase):

    def test_position(self):
        p = Partikel(40, 50)
        self.assertEqual(p.x, 40)
        self.assertEqual(p.y, 50)

    def test_normalized_velocity(self):
        p = Partikel(40, 50)
        self.assertEqual(p.vx**2 + p.vy**2, 1.0)

    def test_randomized_color(self):
        for i in range(100):
            p1 = Partikel(20, 30)
            p2 = Partikel(60, 50)
            self.assertNotEqual(p1.color, p2.color)
