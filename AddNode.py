import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe
import AddEdge
from DFS_Traversal import *
from DFS_Traversal import dfs_traversal
from Node import *
from Graph import *
from Handle_Button import *
# from Reset import *
# from DFS_GUI import *


def collide(pos, node):
    if node.isOver(pos):
        return True
    return False


def create_node(node,pos, i):
    node.pos = pos
    node.text = "%d" % (i)
    node.display = True


def add_node(window, buttons,colors,graph,nodes,edges,i):

    node = None


    # i = 0

    while True:
        window.fill(colors['paper'])

        pygame.draw.line(window,colors['emerald'],(20,70),(780,70))

        drawButtons(buttons,colors['emerald'])


        # buttons[0].draw(colors['emerald'])
        # buttons[1].draw(colors['emerald'])
        # buttons[2].draw(colors['emerald'])
        # buttons[3].draw(colors['emerald'])



        node = Node(window,colors['green'])

        pos = pygame.mouse.get_pos()

        for event in pe.get():
            if event.type == pl.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pl.KEYDOWN:
                if event.key == pl.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pl.MOUSEBUTTONDOWN:
                if pos[1] > 90:
                    if len(nodes) != 0:
                        if not any([collide(pos, x) for x in nodes]):
                            create_node(node,pos,i)
                            nodes.append(node)
                            i += 1
                    else:
                        create_node(node, pos, i)
                        nodes.append(node)
                        i += 1
                button_handler(window, buttons, colors, graph, nodes,edges,i,pos)


                # if buttons[1].isOver(pos):
                #     AddEdge.add_edge(window,buttons,colors,graph,nodes,edges,i)
                # if buttons[2].isOver(pos):
                #     dfs_traversal(window,buttons,colors,graph,nodes,edges)
                # if buttons[3].isOver(pos):
                #     reset(window, buttons, colors,graph,nodes,edges)

            if event.type == pl.MOUSEMOTION:
                for button in buttons:
                    if button.isOver(pos):
                        button.color = colors['silver']
                    else:
                        button.color = colors['blacksteel']

        graph.nodes = nodes
        graph.edges = edges
        graph.graph_show()

        pygame.display.update()


















