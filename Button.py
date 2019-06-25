import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe

class Button:

    def __init__(self,window,color, x, y, width, height, text = ''):
        self.window = window
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,outline = False):
        if outline:
            pygame.draw.rect(self.window,outline,(self.x - 2,self.y - 2,self.width + 4,self.height + 4))
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))
