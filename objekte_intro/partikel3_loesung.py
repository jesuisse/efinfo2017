# encoding: utf-8
__author__ = 'pax'

"""
Aufgabe: Sorge dafür, dass die unit tests in partikel3_test.py
         fehlerlos durchlaufen. Du musst dazu nur dieses
         Python-Programm um eine einzige Methode erweitern.
"""

import random
import math
import pygame


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
        self.x = x
        self.y = y
        self.vx, self.vy = self._normalisiere(random.randint(-60, 60),
                                              random.randint(-60, 60))
        self.color = (random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255))

    def _normalisiere(self, vec_x, vec_y):
        """
        Normalisiert einen Vektor mit 2 Komponenten
        :param vec_x: x-Komponente des Vektors
        :param vec_y: y-Komponente des Vektors
        :return: Neuer Vektor (als Tupel) mit Länge 1
        """
        d = math.sqrt(vec_x ** 2 + vec_y ** 2)
        return vec_x / d, vec_y / d

    def bewege(self, dt):
        """
        Bewegt das Partikel um die Distanz, die
        es in der Zeit dt aufgrund seiner Geschwindigkeit
        zurücklegt
        :param dt: Zur Verfügung stehende Zeit
        """
        self.x = self.x + self.vx * dt
        self.y = self.y + self.vy * dt

    def zeichne(self, canvas):
        """
        Zeichnet das Partikel auf das angegebene pygame canvas
        :param canvas: Pygame-Zeichnungsfläche
        """
        ipos = (int(self.x), int(self.y))
        pygame.draw.circle(canvas, self.color, ipos, 10)

    def abprallen(self, geometry):
        """
        Lässt Ball von Rand abprallen.
        :param geometry: Ausdehnung des Spielfelds als (x,y) Tupel
        :return:
        """
        max_x, max_y = geometry[0], geometry[1]
        if self.x < 0:
            self.x = -self.x
            self.vx = -self.vx
        if self.x > max_x:
            self.x = max_x - (self.x - max_x)
            self.vx = -self.vx
        if self.y < 0:
            self.y = -self.y
            self.vy = -self.vy
        if self.y > max_y:
            self.y = max_y - (self.y - max_y)
            self.vy = -self.vy

