import pygame
import random
from pygame.locals import *
#Die Groesse des Grafikfensters
screenGeometry = (800, 600)

def macheTeilchen():#erzeuge Teilchen mit zufaelliger position und Farbe und Bewegungsrichtung
    pos = [ random.randint(0, screenGeometry[0]),
        random.randint(0, screenGeometry[1]) ]

    v = [ float(random.randint(-60, 60)),
      float(random.randint(-60, 60))]

    v = normalisiere (v)
    v = skaliere (v, random.randint (3, 8) )

    farbe = ( random.randint(0, 255),
          random.randint(0, 255),
          random.randint(0, 255) )
    teilchen = [pos, farbe, v]
    return [pos, farbe, v]

teilchen = macheTeilchen()
#surface->screen, colour-->teilchen[1], position-->teilchen[0], radius-->10
    pygame.draw.circle(screen, teilchen[1], teilchen[0], 10)

def normalisiere(vektor):
    laenge = math.sqrt(vektor[0] ** 2 + vektor[1] ** 2)
    norm = [ vektor[0] / laenge,
             vektor[1] / laenge ]

    return norm

def skaliere(vektor, faktor):

    return [ vektor[0] * faktor,
             vektor[1] * faktor ]



#Teilchen erzeugen
legion = []
for i in range(100):
    legion.append(macheTeilchen())

pygame.init()
#Bildschirmfenster erzeugen
screen = pygame.display.set_mode(screenGeometry)

#fuellt gesamtes Fenster schwarz-->definiert durch (0,0,0)
screen.fill((0, 0, 0))

#Gameloop - Wiederholen, bis Fenster geschlossen wird
wantsToQuit = False
while not wantsToQuit:
    #Nachschauen, ob wir Fenster geschlossen haben
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            wantsToQuit = True
    screen.fill((0, 0, 0))
    for teilchen in legion:
        zeichneTeilchen(teilchen)
    pygame.display.flip()

pygame.quit()