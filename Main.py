import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe
from Button import *
from Graph import *
import AddEdge
import AddNode
import DFS
import Handle_Button


# main window initialization
pygame.init()

window_size = (800, 700)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("DFS GUI")

colors = {'black': (0, 0, 0), 'white': (255, 255, 255), 'blacksteel': (8, 7, 6), 'paper': (239, 239, 239),
          'goldleaf': (209, 178, 128), 'brightblue': (51, 123, 174), 'yellow': (235, 223, 0), 'emerald': (38, 92, 0),
          'silver': (89, 77, 70), 'green': (24, 255, 0), 'red': (255, 0, 0)}

buttons = [
    Button(window, colors['blacksteel'], 20, 20, 160, 40, 'Add Node'),
    Button(window, colors['blacksteel'], 220, 20, 160, 40, 'Add Edge'),
    Button(window, colors['blacksteel'], 420, 20, 160, 40, 'DFS'),
    Button(window, colors['blacksteel'], 620, 20, 160, 40, 'Reset')
]

# global int for node indexing
global i

# main func for starting the program
def main(window, colors, buttons):

    i = 0
    edges = []
    nodes = []
    graph = Graph(window, colors)

    while True:
        window.fill(colors['paper'])
        pygame.draw.line(window, colors['emerald'], (20, 70), (780, 70))
        Handle_Button.draw_btns(buttons, colors['emerald'])
        pos = pygame.mouse.get_pos()

        # event handling
        for event in pe.get():

            if event.type == pl.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pl.KEYDOWN:
                if event.key == pl.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pl.MOUSEBUTTONDOWN:
                Handle_Button.button_handler(window, buttons, colors, graph, nodes, edges, i, pos)

            if event.type == pl.MOUSEMOTION:
                for button in buttons:
                    if button.isOver(pos):
                        button.color = colors['silver']
                    else:
                        button.color = colors['blacksteel']

        graph.nodes = nodes
        graph.edges = edges

        # showing the graph
        graph.graph_show()

        pygame.display.update()


if __name__ == '__main__':
    main(window, colors, buttons)
