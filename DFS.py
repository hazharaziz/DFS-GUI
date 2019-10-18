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

    graph.nodes = nodes
    graph.edges = edges
 
    # showing the depth first search
    graph.dfs_show()

    pygame.display.update()

