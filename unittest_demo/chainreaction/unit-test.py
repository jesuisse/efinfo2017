import unittest

from unittest_demo.chainreaction.chainreaction5 import*


class ProgrammTest(unittest.TestCase):

    def test_macheTeilchen(self):
        self.assertEqual(type(macheTeilchen()),list)

    def test_normalisiere(self):
        vektor = [4, 5]
        d = math.sqrt(vektor[0] ** 2 + vektor[1] ** 2)
        norm = [ vektor[0] / d, vektor[1] / d ]
        self.assertEqual(normalisiere(vektor),norm)

    def test_bewege(self):
        pos = [random.randint(0, screenGeometry[0]), random.randint(0, screenGeometry[1])]
        farbe = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        v = [ random.randint(-60,60), random.randint(-60,60)]
        teilchen = [pos, farbe, v]
        self.assertEqual(bewege(teilchen, 5),pos[0])

    def test_zeichneTeilchen(self):
        self.assertEqual(zeichneTeilchen(teilchen),pygame.draw.circle(screen, teilchen[1], pos, 10))

    def test_range(self):
        self.assertEqual(range(20),legion.append(teilchen()))

if __name__=='__main__':
    unittest.main()
