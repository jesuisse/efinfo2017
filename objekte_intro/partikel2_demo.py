# encoding: utf-8
__author__ = 'pax'

import random
import pygame

from pygame.locals import *
from objekte_intro.partikel2 import Partikel

screenGeometry = (800,600)  # Die Grösse des Grafikfensters

legion = []
for i in range(20):
    x = random.randint(0, screenGeometry[0])
    y = random.randint(0, screenGeometry[1])
    p = Partikel(x, y)
    legion.append(p)

screen = pygame.display.set_mode(screenGeometry)
wantsToQuit = False
while not wantsToQuit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            wantsToQuit = True
    screen.fill((0,0,0))
    for teilchen in legion:
        teilchen.bewege(1)
        teilchen.zeichne(screen)
    pygame.display.flip()


# Sorgt dafür, dass Pygame-Ressourcen und Fenster sauber
# freigegeben werden
pygame.quit()