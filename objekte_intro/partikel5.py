# encoding: utf-8
__author__ = 'pax'


import random
import math
import pygame

from objekte_intro.vektor3 import Vektor2D


class Partikel(object):
    """
    Ein Partikel hat Position, Geschwindigkeit und Farbe
    und weiss, wie es sich bewegen und wie es sich darstellen
    kann.
    """

    def __init__(self, x, y):
        """
        Konstruiert ein Partikel mit zufälliger
        Geschwindigkeit und zufälliger Farbe.
        :param x: Die x-Koordinate der Position
        :param y: Die y-Koordinate der Position
        """
        self.pos = Vektor2D(x=x, y=y)
        self.v = Vektor2D(w=random.randint(0, 360), l=1)
        self.color = (random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255))

    def bewege(self, dt):
        """
        Bewegt das Partikel um die Distanz, die
        es in der Zeit dt aufgrund seiner Geschwindigkeit
        zurücklegt
        :param dt: Zur Verfügung stehende Zeit
        """

        x, y = self.pos.get_xy()
        vx, vy = self.v.get_xy()

        self.pos.setze_kartesisch(x + vx * dt, y + vy * dt)

    def zeichne(self, canvas):
        """
        Zeichnet das Partikel auf das angegebene pygame canvas
        :param canvas: Pygame-Zeichnungsfläche
        """
        x = int(self.pos.get_x())
        y = int(self.pos.get_y())
        pygame.draw.circle(canvas, self.color, (x,y), 10)
