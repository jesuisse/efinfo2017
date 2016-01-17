# -*- coding: utf-8 -*-
import sys
import random
import pygame
import math
from pygame.locals import *

screenGeometry = (800,600)  # Die Grösse des Grafikfensters

def macheTeilchen():
    """Erzeuge ein Teilchen mit zufälliger Position und Farbe"""
    pos = [ random.randint(0, screenGeometry[0]), 
            random.randint(0, screenGeometry[1]) ]

    v = [ random.randint(-60,60),
          random.randint(-60,60)]

    v = normalisiere(v)
    
    farbe = ( random.randint(0,255), 
              random.randint(0,255),
              random.randint(0,255) )
    return [pos, farbe, v]

def normalisiere(vektor):
    """Normalisiert den Vektor (x,y), d.h. setzt seine Länge auf 1"""
    d = math.sqrt(vektor[0] ** 2 + vektor[1] ** 2)
    norm = [ vektor[0] / d, vektor[1] / d ]
    return norm

def bewege(teilchen, dt):
    """Bewegt ein Teilchen um die Distanz, die es in
       dt Zeiteinheiten zurücklegen kann"""
    pos = teilchen[0]
    v = teilchen[2]

    pos[0] = pos[0] + v[0] * dt
    pos[1] = pos[1] + v[1] * dt

def abprallen(teilchen):
    """Sort dafür, dass ein Teilchen vom Fensterrand abprallt"""
    pos = teilchen[0]
    v = teilchen[2]

    for i in range(2):
        maximum = screenGeometry[i]
        if pos[i] < 0:
            pos[i] = -pos[i]
            v[i] = -v[i]
        elif pos[i] > maximum:
            pos[i] = maximum - (pos[i]-maximum)
            v[i] = -v[i]

def kollision(teilchen, heisseZone):
    """Liefert True, wenn teilchen mit heisseZone kollidiert ist,
       sonst False"""

    posT = teilchen[0]
    posZ = heisseZone[0]
    radiusT = 10
    radiusZ = heisseZone[1]
    
    d = abs(posT[0] - posZ[0])**2 + abs(posT[1] - posZ[1])**2
    return d < (radiusT+radiusZ)**2
   

def zeichneTeilchen(teilchen):
    pos = teilchen[0]
    ipos = (int(pos[0]), int(pos[1]))
    pygame.draw.circle(screen, teilchen[1], ipos, 10)


def zeichneHeisseZone(zone):
    pos = zone[0]
    radius = zone[1]
    farbe = zone[2]
    pygame.draw.circle(screen, farbe, pos, radius)


def macheHeisseZone(pos, farbe):
    """Erzeugt an Position pos (x,y) eine heisse Zone"""
    return [ [int(pos[0]), int(pos[1]) ], 30, farbe ]


heisseZonen = []
legion = []
for i in range(20):
    legion.append(macheTeilchen())

screen = pygame.display.set_mode(screenGeometry)
clock=pygame.time.Clock()
rot = (255,0,0)

wantsToQuit = False
while not wantsToQuit:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            wantsToQuit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            heisseZonen.append(macheHeisseZone(event.pos, rot))            
    screen.fill((0,0,0))
    for teilchen in legion:
        bewege(teilchen, 5)
        abprallen(teilchen)
        zeichneTeilchen(teilchen)
    for zone in heisseZonen:
        for teilchen in legion:
            if kollision(teilchen, zone):
                heisseZonen.append(macheHeisseZone(teilchen[0], teilchen[1]))
                legion.remove(teilchen)
        zeichneHeisseZone(zone)
    pygame.display.flip()
   
            
# Sorgt dafür, dass Pygame-Ressourcen und Fenster sauber
# freigegeben werden
pygame.quit()
