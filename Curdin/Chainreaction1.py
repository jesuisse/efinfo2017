

import random
import pygame
from pygame. locals import *

screenGeometry = (800 ,600)

pos = [50, 100]
farbe = (50, 100, 200)
teilchen = [pos, farbe]

def macheTeilchen():
    pos = [random.randint(0, sreenGeometry[0]),
           random.randint(0, screenGeometry[1])]

    v = [float(random.randint(-60,60)),
         float(random.randint(-60,60))]

    v= normalisiere(v)
    v = skaliere(v, random.randint(3,8))

    farbe = [random.randint(0,255),
             random.randint(0, 255),
             random.randint(0, 255)]

    return [pos, farbe]

legion = []
for i in range(20):
    legion.append(macheTeilchen())

pygame.init()
screen = pygame.display.set_mode( screenGeometry )
screen.fill ((0,0,0))
for teilchen in legion:
    pygame.draw.circle(screen, teilchen[1], teilchen [0], 10)
pygame.display.flip()

wantsToQuit = False
while not wantsToQuit:
    for event in pygame.event.get():
        if event.type == pygame.Quit:
            wantsToQuit = True
        screen.fill((0,0,0))
        for teilchen in leigon:
            zeichneTeilchen(teilchen)
        pygame.display.flip()

pygame.quit()




















