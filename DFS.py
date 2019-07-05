from Graph import *
import time
import pygame,sys
import pygame.event as pe
import pygame.locals as pl
import Handle_Button 
import Reset

# depth_first_search func for showing the depth first search
def depth_first_search(window, buttons ,colors , graph, nodes, edges):    

    graph.dfs(0)

    while True:
        window.fill(colors['paper'])
        pygame.draw.line(window, colors['emerald'], (20, 70), (780, 70))
        Handle_Button.draw_btns(buttons, colors['emerald'])
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
                    if buttons[3].isOver(pos):
                        Reset.reset(window, buttons, colors, graph, nodes, edges)

            if event.type == pl.MOUSEMOTION:
                for button in buttons:
                    if button.isOver(pos):
                        button.color = colors['silver']
                    else:
                        button.color = colors['blacksteel']

        graph.nodes = nodes
        graph.edges = edges

        # showing the depth first search
        graph.dfs_show()

        pygame.display.update()
        

