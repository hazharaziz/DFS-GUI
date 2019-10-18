import AddEdge
import DFS
import Reset

# draw_btns func for drawing the header buttons
def draw_btns(buttons, color):
    for i in range(len(buttons)):
        buttons[i].draw(color)

# button_handler func for handling the buttons
def button_handler(window, buttons, colors, graph, nodes, edges, i, pos):
    if buttons[0].isOver(pos):
        return 1
    if buttons[1].isOver(pos):
        return 2
    if buttons[2].isOver(pos):
        return 3
    if buttons[3].isOver(pos):
        return 0
