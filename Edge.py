import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe
from Button import *

class Edge:

    def __init__(self,window,color,start_pos,end_pos):
        self.window = window
        self.color = color
        self.start_pos = start_pos
        self.end_pos = end_pos

    def draw(self):
        pygame.draw.line(self.window,self.color,self.start_pos,self.end_pos)
