import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe
import AddEdge
from DFS import *
from Node import *
from Graph import *
import Handle_Button


# collide fund for checking if two nodes collide
def collide(pos, node):
    return node.isOver(pos)

# create_node func for creatind a new node
def create_node(node, pos, i):
    node.pos = pos
    node.text = "%d" % (i)
    node.data = i
    node.display = True

# add_node func for drawing the nodes on the window
def add_node(window, buttons, colors, graph, nodes, edges, i, event):
    node = Node(window, colors['green'])
    pos = pygame.mouse.get_pos()
    add_node = False

    # event handling
    if event.type == pl.MOUSEBUTTONDOWN:
        if pos[1] > 90:
            if len(nodes) != 0:
                if not any([collide(pos, x) for x in nodes]):
                    create_node(node, pos, i)
                    nodes.append(node)
                    add_node = True
            else:
                create_node(node, pos, i)
                nodes.append(node)
                add_node = True

        graph.nodes = nodes
        graph.edges = edges

        # showing the graph
        graph.graph_show()

        pygame.display.update()
        return add_node
