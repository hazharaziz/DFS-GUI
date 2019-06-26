import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe
from Node import *
from Button import *
from AddNode import *

pygame.init()

window_size = (800, 500)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("DFS GUI")


colors = {'black':(0, 0, 0),'white':(255, 255, 255),'blacksteel':(8,7,6),'paper':(239,239,239),
          'goldleaf' : (209, 178, 128),'brightblue':(51,123,174),'yellow':(235,223,0),'emerald':(38,92,0),
          'silver':(89,77,70)}

buttons = [
    Button(window, colors['blacksteel'], 20, 20, 160, 40, 'AddNode'),
    Button(window, colors['blacksteel'], 220, 20, 160, 40, 'AddEdge'),
    Button(window, colors['blacksteel'], 420, 20, 160, 40, 'DFS Traversal'),
    Button(window, colors['blacksteel'], 620, 20, 160, 40, 'Reset')
]


def main(window,colors,buttons):

    # nodes = []

    while True:
        window.fill(colors['paper'])

        pygame.draw.lines(window,colors['emerald'],False,((20,70),(780,70)))


        buttons[0].draw(colors['emerald'])
        buttons[1].draw(colors['emerald'])
        buttons[2].draw(colors['emerald'])
        buttons[3].draw(colors['emerald'])

        node = Node(window,colors['white'])

        pos = pygame.mouse.get_pos()

        for event in pe.get():
            if event.type == pl.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pl.MOUSEBUTTONDOWN:
                if buttons[0].isOver(pos):
                    add_node(window, buttons,colors)
            if event.type == pl.MOUSEMOTION:
                for button in buttons:
                    if button.isOver(pos):
                        button.color = colors['silver']
                    else:
                        button.color = colors['blacksteel']





        # for i in range(len(nodes)):
        #     if nodes[i].display:
        #         nodes[i].draw()


        pygame.display.update()


if __name__ == '__main__':
    main(window,colors,buttons)






