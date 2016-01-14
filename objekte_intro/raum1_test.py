# encoding: utf-8
__author__ = 'pax'

import unittest
from objekte_intro.raum1 import Raum

class PartikelTest(unittest.TestCase):

    def test_eigenschaften(self):
        r = Raum("Kiesweg", "Du stehst auf einem verlassenen Kiesweg.")
        self.assertEqual(r.name, "Kiesweg")
        self.assertEqual(r.beschreibung, "Du stehst auf einem verlassenen Kiesweg.")
        self.assertListEqual(r.verbindungen, [])
