
import unittest
from objekte_intro.vektor1 import Vektor2D


class VektorTest(unittest.TestCase):

    def test_null_polar_vektor(self):
        v = Vektor2D(w=0, l=0)
        self.assertEquals(v.x, 0)
        self.assertEquals(v.y, 0)

    def test_null_kartesisch_vektor(self):
        v = Vektor2D(x=0, y=0)
        self.assertEquals(v.w, 0)
        self.assertEquals(v.l, 0)

    def test_90_polar(self):
        v = Vektor2D(w=90, l=2)
        self.assertAlmostEquals(v.x, 0)
        self.assertAlmostEquals(v.y, 2)

    def test_normalisieren(self):
        v = Vektor2D(w=45, l=5)
        v.normalisiere()
        self.assertEquals(v.w, 45)
        self.assertEquals(v.l, 1)

