import math

class Vektor2D(object):
    """
    Repräsentiert einen 2dimensionalen Vektor und ermöglicht den Zugriff sowohl
    auf die kartesische Darstellung (x,y) wie auch auf eine Darstellung in Polar-
    koordinaten (winkel, länge).
    """
    def __init__(self, x=None, y=None, w=None, l=None):
        """
        Erzeugt einen Vektor entweder aus den Komponenten x,y ODER aus Winkel w und
        Länge l.
        :param x: x-Komponente
        :param y: y-Komponente
        :param w: Winkel (im Gradmass ab 3-Uhr Position gegen den Uhrzeigersinn gemessen)
        :param l: Länge
        """
        if x is not None and y is not None and w is None and l is None:
            self.x = x
            self.y = y
            self._update_polar()
        elif w is not None and l is not None and x is None and y is None:
            self.w = w
            self.l = l
            self._update_kartesisch()
        else:
            raise ValueError("Entweder x,y oder w,l müssen angegeben werden.")

    def _update_kartesisch(self):
        """
        Berechnet aufgrund der Polarkoordinaten des Vektors die
        kartesischen Koordinaten neu
        """
        # Trigonometrische Funktionen erwarten Winkel im Bogenmass, deshalb
        # Umrechung des Winkels vom Grad- uns Bogenmass
        self.x = self.l * math.cos(self.w * (math.pi/180))
        self.y = self.l * math.sin(self.w * (math.pi/180))

    def _update_polar(self):
        """
        Berechnet aufgrund der kartesischen Koordinaten des Vektors
        die Polarkoordianten neu
        """
        if self.y == 0:
            self.w = 0 if self.x >= 0 else 180
        else:
            self.w = math.atan(self.x/self.y) * (180/math.pi)
        self.l = math.sqrt(self.x**2 + self.y**2)

    def normalisiere(self):
        """
        Normalisiert den Vektor (d.h. setzt seine Länge auf 1)
        """
        self.l = 1
        self._update_kartesisch()

    def setze_kartesisch(self, x, y):
        """
        Setzt die kartesischen Komponenten des Vektors
        :param x: x-Komponente
        :param y: y-Komponente
        """
        self.x = x
        self.y = y
        self._update_polar()

    def setze_polar(self, w, l):
        """
        Setzt den Vektor mit Polarkoordinaten
        :param w: Der Winkel im Gradmass (von der 3-Uhr-Position im Gegenurzeigrsinn)
        :param l: Die Länge des Vektors
        """
        self.w = w
        self.l = l
        self._update_kartesisch()


if __name__ == '__main__':
    v = Vektor2D(w=90, l=5)
    print(v.x, v.y, v.w, v.l)
    v.setze_kartesisch(3, 4)
    print(v.x, v.y, v.w, v.l)