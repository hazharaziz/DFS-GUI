import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe
import AddNode
from DFS import *
from Edge import Edge
from Graph import *
import Handle_Button 

# add_edge func for drawing the edges on the screen
def add_edge(window, buttons, colors, graph, nodes, edges, i):

    start_node = None
    edge = None

    while True:
        window.fill(colors['paper'])
        pygame.draw.line(window, colors['emerald'], (20, 70), (780, 70))
        pos = pygame.mouse.get_pos()
        edge = Edge(window, colors['blacksteel'])
        Handle_Button.draw_btns(buttons, colors['emerald'])

        # event handling
        for event in pe.get():

            if event.type == pl.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pl.KEYDOWN:
                if event.key == pl.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pl.MOUSEBUTTONDOWN:
                for node in nodes:
                    if node.isOver(pos):
                        if start_node != None:
                            edge.start_node = start_node
                            edge.end_node = node
                            edges.append(edge)
                            start_node = None
                        else:
                            start_node = node
                Handle_Button.button_handler(window, buttons, colors, graph, nodes, edges, i, pos)

            if event.type == pl.MOUSEMOTION:
                for button in buttons:
                    if button.isOver(pos):
                        button.color = colors['silver']
                    else:
                        button.color = colors['blacksteel']

        graph.edges = edges

        # showing the graph
        graph.graph_show()

        pygame.display.update()
