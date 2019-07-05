import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe
import AddEdge
import AddNode
import DFS
import Main

# reset func for reseting the window and initializing a new one
def reset(window, buttons, colors, graph, nodes, edges):
    Main.main(window, colors, buttons)
