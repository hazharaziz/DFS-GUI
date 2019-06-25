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

# node = Node(window, white)

node = None

nodes = []

while True:
    window.fill(black)

    node = Node(window,white)


    for event in pe.get():
        if event.type == pl.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pl.MOUSEBUTTONDOWN:
            node.pos = pygame.mouse.get_pos()
            node.display = True
            nodes.append(node)

    for i in range(len(nodes)):
        if nodes[i].display:
            nodes[i].draw()

    # if node.display:
    #     node.draw()

    pygame.display.update()











