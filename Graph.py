import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe
from Node import *
from Button import *


class Graph:

    def __init__(self,window,colors,nodes = [], edges = []):
        self.window = window
        self.colors = colors
        self.nodes = nodes
        self.edges = edges


    def graph_show(self):

        for edge in self.edges:
            edge.draw()

        for node in self.nodes:
            node.color = self.colors['green']
            node.draw()





