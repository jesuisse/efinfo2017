

pos = []
import pygame
import math
import random
from pygame.locals import *


def normalisiere ( vektor ):

    laenge = math.sqrt ( vektor [0] ** 2 + vektor [1] ** 2)

    norm = [ vektor [0] / laenge ,
         vektor [1] / laenge ]

    return norm
def skaliere ( vektor , faktor ):

    return [ vektor [0] * faktor ,
         vektor [1] * faktor ]


def macheteilchen():
    pos = [random.randint(0, screenGeometry[0]),
           random.randint(0,screenGeometry[1])]
    farbe = (random.randint(0,255),
             random.randint(0,255),
             random.randint(0,255),
             )
    v = [float(random.randint(-60,60)),
         float(random.randint(-60,60))]
    v = normalisiere(v)
    v = skaliere(v, random.randint(3,8))

    return [pos,farbe,v]

def bewege(teilchen, dt):
    s = teilchen[0]
    v = teilchen[2]
    s[0] = s[0] + v[0] * dt
    s[1] = s[1] + v[1] * dt

def zeichneTeilchen(teilchen):
    pos = teilchen[0]
    ipos = (int(pos[0]), int(pos[1]))
    pygame.draw.circle(screen, teilchen[1], ipos, 10)


screenGeometry = (800,600)


legion = []
for i in range(20):
    legion.append(macheteilchen())




pygame.init()
screen = pygame.display.set_mode(screenGeometry)
screen.fill((0,0,0))
for teilchen in legion:
    pygame.draw.circle(screen, teilchen[1], teilchen[0], 10)
pygame.display.flip()


wantsToQuit = False
while not wantsToQuit:
    for event in pygame . event.get():
        if event . type == pygame.QUIT :
            wantsToQuit = True
    screen . fill ((0 ,0 ,0))
    for teilchen in legion :
        bewege(teilchen, 1)
        zeichneTeilchen (teilchen)
    pygame . display . flip ()
    pygame . quit ()


