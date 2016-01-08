from chainreaction5 import*
import unittest

class ProgrammTest(unittest.TestCase):

    def test_macheTeilchen(self):
        self.assertEqual(macheTeilchen(),[])

    def test_normalisiere(self):
        self.assertEqual(normalisiere(vektor),norm)

    def test_bewege(self):
        self.assertEqual(bewege(teilchen,dt),pos[0])

    def test_bewege(self):
        self.assertEqual(bewege(teilchen,dt),pos[1])

    def test_zeichneTeilchen(self):
        self.assertEqual(zeichneTeilchen(teilchen),pygame.draw.circle(screen, teilchen[1], pos, 10))

    def test_range(self):
        self.assertEqual(range(20),legion.append(teilchen()))

if __name__=='__main__':
    unittest.main()
