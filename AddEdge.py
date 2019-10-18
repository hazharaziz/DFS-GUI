import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe
import AddNode
from DFS import *
from Edge import Edge
from Graph import *
import Handle_Button 

# add_edge func for drawing the edges on the screen
def add_edge(window, buttons, colors, graph, nodes, edges, i, event):

    start_node = None
    edge = None

    pos = pygame.mouse.get_pos()
    edge = Edge(window, colors['blacksteel'])

    if event.type == pl.MOUSEBUTTONDOWN:
        for node in nodes:
            if node.isOver(pos):
                if not graph.current_edge.start_node:
                    graph.current_edge.start_node = node
                    print("start")
                elif not graph.current_edge.end_node:
                    print("end")
                    graph.current_edge.end_node = node
                    graph.edges.append(graph.current_edge)
                    graph.current_edge.start_node = Node(window, colors)
                    graph.current_edge.end_node = Node(window, colors)

        #graph.edges = edges

        # showing the graph
        graph.graph_show()

        pygame.display.update()
