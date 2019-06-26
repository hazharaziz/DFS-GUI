import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe
from Node import *
from Button import *




def add_edge(window,buttons,colors,nodes):

    node1 , node2 = None , None

    new_nodes = []

    while True:
        window.fill(colors['paper'])

        pygame.draw.line(window,colors['emerald'],(20,70),(780,70))

        pos = pygame.mouse.get_pos()

        buttons[0].draw(colors['emerald'])
        buttons[1].draw(colors['emerald'])
        buttons[2].draw(colors['emerald'])
        buttons[3].draw(colors['emerald'])

        for event in pe.get():
            if event.type == pl.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pl.MOUSEBUTTONDOWN:
                for node in nodes:
                    if node.isOver(pos):
                        print('.')
                        # node.color = colors['yellow']
                        if node1 != None:
                            print('..')
                            node1.target = node
                            node1.drawEdge(colors['black'])
                            new_nodes.append([node1,node])

                            node1 = None
                            print('...')
                        else:
                            print('....')
                            node1 = node


            if event.type == pl.MOUSEMOTION:
                for button in buttons:
                    if button.isOver(pos):
                        button.color = colors['silver']
                    else:
                        button.color = colors['blacksteel']


        for node in nodes:
            node.draw()


        for edge in new_nodes:
            if len(edge) == 2:
                pygame.draw.line(window,colors['blacksteel'],edge[0].pos,edge[1].pos)



        pygame.display.update()


