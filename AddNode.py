import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe

from AddEdge import add_edge
from Node import *
from Button import *
from State import *

def add_node(window, buttons,colors,nodes):


    node = None

    i = 0

    while True:
        window.fill(colors['paper'])

        pygame.draw.lines(window,colors['emerald'],False,((20,70),(780,70)))

        buttons[0].draw(colors['emerald'])
        buttons[1].draw(colors['emerald'])
        buttons[2].draw(colors['emerald'])
        buttons[3].draw(colors['emerald'])

        node = Node(window,colors['brightblue'])

        pos = pygame.mouse.get_pos()

        for event in pe.get():
            if event.type == pl.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pl.MOUSEBUTTONDOWN:
                if pos[1] > 90:
                    i += 1
                    node.pos = pos
                    node.text = "%d"%(i)
                    node.display = True
                    nodes.append(node)
                if buttons[1].isOver(pos):
                    add_edge(window,buttons,colors,nodes)

            if event.type == pl.MOUSEMOTION:
                for button in buttons:
                    if button.isOver(pos):
                        button.color = colors['silver']
                    else:
                        button.color = colors['blacksteel']



        for node in nodes:
            if node.display:
                node.draw()



        pygame.display.update()


















