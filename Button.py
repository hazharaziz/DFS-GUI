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

        if self.text != '':
            font = pygame.font.SysFont('Times New Roman',25)
            text = font.render(self.text,1,(0,0,0))
            self.window.blit(text,(self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))


    def isOver(self,pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


