# encoding: utf-8
__author__ = 'pax'

import unittest
from objekte_intro.partikel3_aufgabe import Partikel

# Grösse des Spielfensters (virtuell auf 100 x 100 Pixel gesetzt)
screen_geometry = (100, 100)

class PartikelTest(unittest.TestCase):

    def test_abprallen_nein(self):
        p = Partikel(40, 50)
        p.abprallen(screen_geometry)
        self.assertEqual(p.x, 40)
        self.assertEqual(p.y, 50)

    def test_abprallen_links(self):
        p = Partikel(-40, 50)
        p.abprallen(screen_geometry)
        self.assertEqual(p.x, 40)
        self.assertEqual(p.y, 50)

    def test_abprallen_oben(self):
        p = Partikel(20, -50)
        p.abprallen(screen_geometry)
        self.assertEqual(p.x, 20)
        self.assertEqual(p.y, 50)

    def test_abprallen_rechts(self):
        p = Partikel(120, 50)
        p.abprallen(screen_geometry)
        self.assertEqual(p.x, 80)
        self.assertEqual(p.y, 50)

    def test_abprallen_unten(self):
        p = Partikel(40, 120)
        p.abprallen(screen_geometry)
        self.assertEqual(p.x, 40)
        self.assertEqual(p.y, 80)

