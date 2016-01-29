# encoding: utf-8

import math

"""
Aufgabe: Ergänze die Klasse um die Methoden setze_kartesisch und setze_polar.
Die benötigten Argumente kannst du dem Klassendiagramm entnehmen.

Überprüfe, ob du alles richtig gemacht hast, indem du die Tests in vektor3_test.py
laufen lässt.
"""


class Vektor2D(object):
    """
    Repräsentiert einen 2dimensionalen Vektor und ermöglicht den Zugriff sowohl
    auf die kartesische darstellung (x,y) wie auch auf eine Darstellung in Polar-
    koordinaten (winkel, länge) mittels Getter-Methoden.
    """
    def __init__(self, x=None, y=None, w=None, l=None):
        """
        Erzeugt einen Vektor entweder aus den Komponenten x,y ODER aus Winkel w und
        Länge l.
        :param x: x-Komponente
        :param y: y-Komponente
        :param w: Winkel
        :param l: Länge
        """
        if x is not None and y is not None and w is None and l is None:
            self.x = x
            self.y = y
        elif w is not None and l is not None and x is None and y is None:
            self.x, self.y = self._polar_zu_kartesisch(w*(math.pi/180), l)
        else:
            raise ValueError("Entweder x,y oder w,l müssen angegeben werden.")

    def _polar_zu_kartesisch(self, w, l):
        return l * math.cos(w), l*math.sin(w)

    def _kartesisch_zu_polar(self, x, y):
        return math.atan(y/x), math.sqrt(x**2 + y**2)

    def normalisiere(self):
        """
        Normalisiert den Vektor (d.h. setzt seine Länge auf 1)
        """
        w, l = self._kartesisch_zu_polar(self.x, self.y)
        self.x, self.y = self._polar_zu_kartesisch(w, 1)

    def get_xy(self):
        """
        Liefert die kartesischen Koordinaten dieses Vektors

        :return: Ein Tupel (x,y)
        """
        return self.x, self.y

    def get_x(self):
        """
        Liefert die kartesische Koordinate x

        :return: x
        """
        return self.x

    def get_y(self):
        """
        Liefert die kartesische Koordinate y

        :return: y
        """
        return self.y

    def get_wl(self):
        """
        Liefert die Polarkoordinaten dieses Vektors

        :return: Ein Tupel (w,l)
        """
        w, l = self._kartesisch_zu_polar(self.x, self.y)
        return w/math.pi*180, l

    def get_w(self):
        """
        Liefert den Winkel w des Vektors

        :return: w
        """
        w, l = self.get_wl()
        return w

    def get_l(self):
        """
        Liefert die Lönge l des Vektors

        :return: l
        """
        w, l = self.get_wl()
        return l

    def setze_kartesisch(self,x,y):
            self.x = x
            self.y = y

    def setze_polar(self,w,l):
        winkel = w/180.0*math.pi
        self.x, self.y = self._polar_zu_kartesisch(winkel,l)



if __name__ == '__main__':
    v = Vektor2D(x=5, y=5)
    print(v.get_xy(), v.get_wl())
