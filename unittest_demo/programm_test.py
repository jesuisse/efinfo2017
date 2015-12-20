# encoding: utf-8
__author__ = 'pax'

import unittest
from programm import *

class ProgrammTest(unittest.TestCase):

    def testHalloWelt1(self):
        self.assertEqual(hallo_welt("Homer"), "Hallo Homer")

    def testHalloWeltOhneNamen(self):
        self.assertNotEqual(hallo_welt(""), "Hallo ")
        # oder besser
        self.assertEqual(hallo_welt(""), "Hallo")


    def testQuadrat(self):
        self.assertEqual(quadrat(5), 25)

    def testQuadratNeg(self):
        self.assertEqual(quadrat(-5), 25)

if __name__ == "__main__":
    unittest.main()
