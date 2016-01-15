# encoding: utf-8
__author__ = 'pax'

import random
import math

def normalisiere(v):
    """
    Normalisiert einen Vektor mit 2 Komponenten
    :param v: Vektor (als Liste)
    :return: Neuer Vektor (als Liste) mit Länge 1
    """
    assert len(v) == 2
    d = math.sqrt(v[0] ** 2 + v[1] ** 2)
    norm = [ v[0] / d, v[1] / d ]
    return norm


class Partikel(object):
    """Repräsentiert ein Partikel."""
    def __init__(self, x, y):
        """
        Konstruiert ein Partikel mit zufälliger
        Geschwindigkeit und zufälliger Farbe.
        :param x: Die x-Koordinate
        :param y: Die y-Koordinate
        """
        self.x = x
        self.y = y
        v = normalisiere([random.randint(-60, 60),
                          random.randint(-60, 60)])
        self.vx = v[0]
        self.vy = v[1]
        self.color = (random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255))


