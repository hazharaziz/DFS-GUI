import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe
from Graph import *


class Node:

    def __init__(self, window, color, pos = (0,0), text = '', display = False):
        self.window = window
        self.color = color
        self.pos = pos
        self.text = text
        self.display = display

    def draw(self, outline_color = (0,0,0)):
        if self.display:
            pygame.draw.circle(self.window,outline_color,self.pos,22,3)
            pygame.draw.circle(self.window,self.color,self.pos,20)

        if self.text != '':
            font = pygame.font.SysFont('Times New Roman',15)
            text = font.render(self.text,1,(0,0,0))
            self.window.blit(text,(self.pos[0] - text.get_width()/2, self.pos[1] - text.get_height()/2))


    def isOver(self,pos):
        if pos[0] > (self.pos[0] - 45) and pos[0] < (self.pos[0] + 45):
            if pos[1] > (self.pos[1] - 45) and pos[1] < (self.pos[1] + 45):
                if (((pos[0] - self.pos[0]) ** 2 + (pos[1] - self.pos[1]) ** 2) ** 0.5) <= 45:
                    return True
        return False

