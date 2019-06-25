import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe
from Node import *
from Button import *

def main():
    pygame.init()

    window_size = (800, 500)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("DFS GUI")

    black = (0, 0, 0)
    white = (255, 255, 255)

    node = None


    button1 = Button(window,(0,255,0),20,20,160,40,'AddNode')
    button2 = Button(window,(0,255,0),220,20,160,40,'AddEdge')
    button3 = Button(window,(0,255,0),420,20,160,40,'DFS Traversal')
    button4 = Button(window,(0,255,0),620,20,160,40,'Reset')



    nodes = []

    while True:
        window.fill(black)


        button1.draw(white)
        button2.draw(white)
        button3.draw(white)
        button4.draw(white)

        node = Node(window,white)


        for event in pe.get():
            if event.type == pl.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pl.MOUSEBUTTONDOWN:
                node.pos = pygame.mouse.get_pos()
                node.display = True
                nodes.append(node)

        for i in range(len(nodes)):
            if nodes[i].display:
                nodes[i].draw()

        # if node.display:
        #     node.draw()

        pygame.display.update()


if __name__ == '__main__':
    main()






