__author__ = 'David'

import unittest
from textabenteuer import *

class ProgrammTest(unittest.TestCase):

    def testGoto(self):
        self.assertEqual(goto(strasse,"n"),stadt)

    def testGoto_falscheRichtung(self):
        self.assertEqual(goto(strasse,"o"),strasse)

    def testEreignis(self):
        spieler.gewicht = 100
        self.assertEqual(checkEreignis(bruecke),0)

    def testKeinEreignis(self):
        spieler.gewicht = 80
        self.assertNotEqual(checkEreignis(bruecke),0)


    def testGehe_undEreignis(self):
        spieler.gewicht = 100
        self.assertEqual(gehe(strasse,"s"),0)

    def testGehe(self):
        spieler.gewicht = 80
        self.assertEqual(gehe(strasse,"s"),bruecke)


    def testBefehl(self):
        self.assertEqual(checkBefehl("nehmen"),"nimm")

    def testKeinBefehl(self):
        self.assertEqual(checkBefehl("Hallo"),"nicht erkannt")

    def testRichtung(self):
        self.assertEqual(checkRichtung("Gehe nach Norden"),"n")

    def testRichtungFalsch(self):
        self.assertNotEqual(checkRichtung("Gehe nach Nord"),"n")

