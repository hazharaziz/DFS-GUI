import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe
from Node import *
from Button import *


class Graph:

    def __init__(self,window,adj_dict = {}):
        self.window = window
        self.adj_dict = adj_dict

    def add_edge(self,v,w):
        self.adj_dict[v] = w
        self.adj_dict[w] = v





