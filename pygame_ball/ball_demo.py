# encoding: utf-8

import sys, pygame

pygame.init()

size = width, height = 800, 600
speed = [1, 1]
black = 0, 0, 0

def rebound(ballrect, speed):
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]


screen = pygame.display.set_mode(size)

ball = pygame.image.load("resource/ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ballrect = ballrect.move(speed)
    rebound(ballrect, speed)

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
