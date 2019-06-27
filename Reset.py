import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe


from AddEdge import *
from AddNode import *
from DFS_Traversal import *
from DFS_GUI import *

def reset(window,buttons,colors,graph,nodes):

    main(window,colors,buttons)
    # while True:
    #     window.fill(colors['paper'])
    #
    #     pygame.draw.line(window,colors['emerald'],(20,70),(780,70))
    #
    #     buttons[0].draw(colors['emerald'])
    #     buttons[1].draw(colors['emerald'])
    #     buttons[2].draw(colors['emerald'])
    #     buttons[3].draw(colors['emerald'])
    #
    #     pos = pygame.mouse.get_pos()
    #
    #     for event in pe.get():
    #         if event.type == pl.QUIT:
    #             pygame.quit()
    #             sys.exit()
    #
    #         if event.type == pl.MOUSEBUTTONDOWN:
    #             if buttons[0].isOver(pos):
    #                 add_node(window, buttons, colors, graph, nodes)
    #             if buttons[1].isOver(pos):
    #                 add_edge(window, buttons, colors, graph, nodes)
    #             if buttons[2].isOver(pos):
    #                 dfs_traversal(window, buttons, colors, graph, nodes)
    #
    #
    #         if event.type == pl.MOUSEMOTION:
    #             for button in buttons:
    #                 if button.isOver(pos):
    #                     button.color = colors['silver']
    #                 else:
    #                     button.color = colors['blacksteel']
    #
    #     for node in nodes:
    #         node.draw()
    #
    #
    #
    #     pygame.display.update()




