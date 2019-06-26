import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe
from Node import *
from Button import *
from Graph import *



def add_edge(window,buttons,colors,graph,nodes):

    start_node = None

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
                        # print('.')
                        # node.color = colors['yellow']
                        if start_node != None:
                            # print('..')
                            node.color = colors['yellow']
                            new_nodes.append([start_node,node])
                            graph.add_edge(start_node,node)
                            print(graph.adj_dict[start_node].text)
                            # node.color = colors['brighblue']
                            start_node = None
                            # print('...')
                        else:
                            # print('....')
                            start_node = node
                            start_node.color = colors['yellow']


            if event.type == pl.MOUSEMOTION:
                for button in buttons:
                    if button.isOver(pos):
                        button.color = colors['silver']
                    else:
                        button.color = colors['blacksteel']


        for node in nodes:
            node.color = colors['brightblue']
            node.draw()


        for edge in new_nodes:
            if len(edge) == 2:
                pygame.draw.line(window,colors['blacksteel'],edge[0].pos,edge[1].pos)

        pygame.display.update()


