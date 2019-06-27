import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe

from Graph import *


class Node(object):

    def __init__(self, window, color, pos = (0,0), text = '', display = False,
                 edge_state = False, target = None, is_start_node = False, adj = []):
        self.window = window
        self.color = color
        self.pos = pos
        self.text = text
        self.display = display
        self.edge_state = edge_state
        self.target = target
        self.is_start_node = is_start_node
        self.adj = adj

    def draw(self):
        if self.display:
            pygame.draw.circle(self.window,self.color,self.pos,20)

        if self.text != '':
            font = pygame.font.SysFont('Times New Roman',15)
            text = font.render(self.text,1,(0,0,0))
            self.window.blit(text,(self.pos[0] - text.get_width()/2, self.pos[1] - text.get_height()/2))

    def isOver(self,pos):
        if pos[0] > (self.pos[0] - 20) and pos[0] < (self.pos[0] + 20):
            if pos[1] > (self.pos[1] - 20) and pos[1] < (self.pos[1] + 20):
                if (((pos[0] - self.pos[0]) ** 2 + (pos[1] - self.pos[1]) ** 2) ** 0.5) <= 20:
                    return True
        return False

    def drawEdge(self,color):
        if self.target:
            pygame.draw.line(self.window,color,self.pos,self.target.pos)
