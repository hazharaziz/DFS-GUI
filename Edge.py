import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe
from Button import *

class Edge:

    def __init__(self,window,color,start_node = None,end_node = None):
        self.window = window
        self.color = color
        self.start_node = start_node
        self.end_node = end_node

    def draw(self):
        pygame.draw.line(self.window,self.color,self.start_node.pos,self.end_node.pos,4)
