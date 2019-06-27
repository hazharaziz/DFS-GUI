from enum import Enum


class State(Enum):
    add_node = 1
    add_edge = 2
    dfs = 3
    reset = 4