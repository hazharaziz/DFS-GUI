import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe
from AddEdge import *
from DFS_Traversal import *
from DFS_Traversal import dfs_traversal
from Node import *
from Graph import *
# import Reset
# from DFS_GUI import *
# import DFS_GUI
from Reset import *

def add_node(window, buttons,colors,graph,nodes):

    node = None

    i = 0

    while True:
        window.fill(colors['paper'])

        pygame.draw.line(window,colors['emerald'],(20,70),(780,70))

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
                    add_edge(window,buttons,colors,graph,nodes)
                if buttons[2].isOver(pos):
                    dfs_traversal(window,buttons,colors,graph,nodes)
                if buttons[3].isOver(pos):
                    reset(window, buttons, colors,graph,nodes)

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


















