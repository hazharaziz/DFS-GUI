import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe


class Node(object):

    def __init__(self,window,color,pos):
        self.color = color
        self.display = False
        self.window = window
        self.pos = pos

    def draw(self):
        if self.display:
            pygame.draw.circle(self.window,self.color,self.pos,10)
