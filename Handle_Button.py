import AddEdge
import AddNode
import DFS
import Reset

# draw_btns func for drawing the header buttons
def draw_btns(buttons, color):
    for i in range(len(buttons)):
        buttons[i].draw(color)

# button_handler func for handling the buttons
def button_handler(window, buttons, colors, graph, nodes, edges, i, pos):
    if buttons[0].isOver(pos):
        AddNode.add_node(window, buttons, colors, graph, nodes, edges, i)
    if buttons[1].isOver(pos):
        AddEdge.add_edge(window, buttons, colors, graph, nodes, edges, i)
    if buttons[2].isOver(pos):
        DFS.depth_first_search(window, buttons, colors, graph, nodes, edges)
    if buttons[3].isOver(pos):
        Reset.reset(window, buttons, colors, graph, nodes, edges)
