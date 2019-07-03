import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe
from Node import *
from Button import *
from collections import defaultdict


class Graph:

    def __init__(self, window, colors, nodes = [], edges = []):
        self.window = window
        self.colors = colors
        self.nodes = nodes
        self.edges = edges
        self.adjacency_list = {} 
        self.dfs_list = []

    def graph_show(self):

        for edge in self.edges:
            edge.draw()

        for node in self.nodes:
            node.color = self.colors['green']
            node.draw()

        self.adjacency_list = {i:[] for i in range(len(self.nodes))} 

        for edge in self.edges:
            #  if edge.start_node.data != edge.end_node.data:
            self.adjacency_list[edge.start_node.data].append(edge.end_node.data)
            self.adjacency_list[edge.end_node.data].append(edge.start_node.data)
        
        for i in range (len(self.adjacency_list)):
            self.adjacency_list[i].sort()
        
   
    def dfs(self, v):
    
        print(self.adjacency_list)
        visited = [False] * (len(self.adjacency_list))
        self.dfs_util(v, visited)
        

    def dfs_util(self, v, visited):
        
        visited[v] = True
        self.dfs_list.append(v)
        for i in self.adjacency_list[v]:
            if visited[i] == False:
                self.dfs_util(i, visited)
