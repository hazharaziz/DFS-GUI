import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe


class Node(object):

    def __init__(self,window,color,pos = (0,0), display = False):
        self.color = color
        self.display = display
        self.window = window
        self.pos = pos

    def draw(self):
        if self.display:
            pygame.draw.circle(self.window,self.color,self.pos,10,5)
