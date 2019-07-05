import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe
from Node import *
from Button import *
from collections import defaultdict
import time

# Graph class containing the nodes and edges of the graph
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
            if node.color != self.colors['brightblue']:
                node.color = self.colors['green']
            node.draw()

        self.adjacency_list = {i:[] for i in range(len(self.nodes))}

        for edge in self.edges:
            if edge.start_node.data != edge.end_node.data:
                self.adjacency_list[edge.start_node.data].append(edge.end_node.data)
                self.adjacency_list[edge.end_node.data].append(edge.start_node.data)
        
        for i in range (len(self.adjacency_list)):
            self.adjacency_list[i].sort()
        
   
    def dfs(self, v): # v is the start node

        visited = [False] * (len(self.adjacency_list))
        self._dfs_(v, visited)

        for flag in visited:
            if flag == False:
                self._dfs_(visited.index(flag), visited)
        


    def _dfs_(self, v, visited):
        
        visited[v] = True
        self.dfs_list.append(v)

        for i in self.adjacency_list[v]:
            if visited[i] == False:
                self._dfs_(i, visited)
                
    def dfs_show(self):
        
        self.graph_show()

        for i in self.dfs_list:
            self.nodes[i].color = self.colors['brightblue']
            self.nodes[i].draw()
            pygame.display.update()
            time.sleep(0.5)

        self.dfs_list = []

        

            