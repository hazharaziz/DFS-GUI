import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe
from Node import *


pygame.init()

window_size = (500,500)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pygame")

black = (0,0,0)
white = (255,255,255)

node = Node(window,white,(100,100))


while True:
    window.fill(black)

    for event in pe.get():
        if event.type == pl.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pl.KEYDOWN:
            if event.key == pygame.K_SPACE:
                node.display = True

    if node.display:
        node.draw()

    pygame.display.update()











