__author__ = '17hcan'
import pygame
import random
import math
from pygame.locals import *

screenGeometry = (800,600)

def normalisiere(vektor):
    # """Normalisiert den vektor (x,y), d.h. sorgt dafuer, dass seine Laenge genau 1 betraegt"""

    # Berechne Laenge des Vektors mit Pythagoras
    laenge = math.sqrt(vektor[0] ** 2 + vektor[1] ** 2)

    # berechne normalisiere x- und y-Komponenten
    norm = [vektor[0] / laenge,
            vektor[1] / laenge ]

    # Gib normalisierten Vektor zurueck
    return norm

def skaliere(vektor, faktor):
    """Skaliert den Vektor (x,y)"""
    return [ vektor[0] * faktor,
             vektor[1] * faktor ]


def macheTeilchen():
    pos = [random.randint(0, screenGeometry[0]),
           random.randint(0, screenGeometry[1]) ]
    v = [float(random.randint(-60,60)),
         float(random.randint(-60,60))]
    v = normalisiere(v)
    v = skaliere(v, random.randint(3,8) )
    farbe = ( random.randint(0,255),
              random.randint(0,255),
              random.randint(0,255) )
    return [pos, farbe, v]


pygame.init()
screen = pygame.display.set_mode(screenGeometry)
screen.fill((0,0,0))

legion = []

for i in range(20):
    legion.append(macheTeilchen())

for teilchen in legion:
    pygame.draw.circle(screen, teilchen[1], teilchen[0], 10)
    pygame.display.flip()

wantsToQuit = False
while not wantsToQuit:
    # Nachschauen, ob wir Fenster geschlossen haben
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            wantsToQuit = True
    screen.fill((0,0,0))
    for teilchen in legion:
        macheTeilchen(teilchen)
        pygame.display.flip()

    pygame.quit()