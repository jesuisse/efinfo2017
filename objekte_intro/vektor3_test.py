# encoding: utf-8
__author__ = 'pax'

import unittest
from objekte_intro.vektor3 import Vektor2D


class VektorTest(unittest.TestCase):

    def test_kartesisch_def(self):
        v = Vektor2D(x=10,y=8)
        x, y = v.get_xy()
        self.assertEqual(x, 10)
        self.assertEqual(y, 8)

    def test_setze_kartesisch_1(self):
        v = Vektor2D(x=1, y=1)
        v.setze_kartesisch(3,4)
        x, y = v.get_xy()
        self.assertEqual(x, 3)
        self.assertEqual(y, 4)
        self.assertEqual(5, v.get_l())

    def test_setze_kartesisch_2(self):
        v = Vektor2D(x=1, y=1)
        v.setze_kartesisch(4,3)
        x, y = v.get_xy()
        self.assertEqual(x, 4)
        self.assertEqual(y, 3)

        self.assertEqual(5, v.get_l())

    def test_setze_polar_laenge(self):
        v = Vektor2D(x=1, y=1)
        v.setze_polar(90, 5)
        w, l  = v.get_wl()
        self.assertEqual(l, 5)

    def test_setze_polar_winkel(self):
        v = Vektor2D(x=1, y=1)
        v.setze_polar(90, 5)
        w, l  = v.get_wl()
        self.assertEqual(w, 90)

    def test_setze_polar_beides(self):
        v = Vektor2D(x=1, y=1)
        v.setze_polar(45, 6)
        w, l  = v.get_wl()
        self.assertAlmostEqual(w, 45)
        self.assertAlmostEqual(l, 6)



