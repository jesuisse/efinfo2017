# encoding: utf-8
__author__ = 'pax'

import unittest
from objekte_intro.raum3_aufgabe import Raum


class PartikelTest(unittest.TestCase):

    def setUp(self):
        self.kiesweg = Raum("Kiesweg", "Du stehst auf einem Kiesweg.")
        self.haus = Raum("Haus", "Im Haus ist es unheimlich schummerig. Morsche Balken knarren.")
        self.garten = Raum("Kirschgarten", "Dutzende Kirschbäume blühen in diesem Garten, und das Gras steht kniehoch.")

        self.kiesweg.verbinde('n', self.haus)
        self.haus.verbinde('s', self.kiesweg)
        self.kiesweg.verbinde('o', self.garten)
        self.garten.verbinde('w', self.kiesweg)

    def test_finde_keine_verbindung(self):
        raum = self.kiesweg.finde_raum_in_richtung('w')
        self.assertEqual(raum, None)

    def test_finde_erste_verbindung(self):
        raum = self.kiesweg.finde_raum_in_richtung('n')
        self.assertEqual(raum, self.haus)

    def test_finde_letzte_verbindung(self):
        raum = self.kiesweg.finde_raum_in_richtung('o')
        self.assertEqual(raum, self.garten)

