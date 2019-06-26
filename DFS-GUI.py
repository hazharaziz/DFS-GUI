import pygame.locals as pl
import pygame.event as pe
import pygame, sys, random
from Node import *
from Button import *

def main():
    pygame.init()

    window_size = (800, 500)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("DFS GUI")

    black = (0, 0, 0)
    white = (255, 255, 255)
    orange = (255,69,0)
    blue = (0,0,205)
    aquamarine = (74,152,120)
    cerulean = (10,25,30)
    amber = (216,182,92)
    mist = (144,175,197)
    stone = (51,107,135)
    shadow = (42,49,50)
    foliage = (118,54,38)
    sky = (55,94,151)
    sunset = (251,101,66)
    sunflower = (255,187,0)
    grass = (63,104,28)
    blacksteel = (8,7,6)
    paper = (239,239,239)
    goldleaf = (209,178,128)
    silver = (89,77,70)
    brightblue = (51,123,174)
    yellow = (235,223,0)
    emerald = (38,92,0)

    node = None

    buttons = [
    Button(window,blacksteel,20,20,160,40,'AddNode'),
    Button(window,blacksteel,220,20,160,40,'AddEdge'),
    Button(window,blacksteel,420,20,160,40,'DFS Traversal'),
    Button(window,blacksteel,620,20,160,40,'Reset')
    ]


    nodes = []

    while True:
        window.fill(paper)

        buttons[0].draw(emerald)
        buttons[1].draw(emerald)
        buttons[2].draw(emerald)
        buttons[3].draw(emerald)

        node = Node(window,white)

        pos = pygame.mouse.get_pos()

        for event in pe.get():
            if event.type == pl.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pl.MOUSEBUTTONDOWN:
                # node.pos = pygame.mouse.get_pos()
                # node.display = True
                # nodes.append(node)
                if buttons[0].isOver(pos):
                    add_node()

            if event.type == pl.MOUSEMOTION:
                for button in buttons:
                    if button.isOver(pos):
                        button.color = silver
                    else:
                        button.color = blacksteel





        for i in range(len(nodes)):
            if nodes[i].display:
                nodes[i].draw()

        # if node.display:
        #     node.draw()

        pygame.display.update()


if __name__ == '__main__':
    main()






