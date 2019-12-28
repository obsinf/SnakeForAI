from copy import copy
from random import choice

_cells = {
    # game's colors
    'apple': '#ff0000',
    'empty_cell': '#ffffff',

    # snake's colors
    'green_snake': '#2ffa70',
    'yellow_snake': '#ffff0a',
    'cyan_snake': '#05f5ed',
    'blue_snake': '#0040ff',
    'burgundy_snake': '#fa07fa',
    'orange_snake': '#ff9924',
    'purple_snake': '#4e1296',
    'grey_snake': '#bfbebb',
}


def cell(cell_name):
    if cell_name in _cells:
        return _cells[cell_name]
    else:
        raise Exception(f'No cell called {cell_name}')


class SnakeDistributor:
    # distributes colors in random order

    def __init__(self):
        self.cells = copy(_cells)
        del self.cells['apple']
        del self.cells['empty_cell']

    def next_snake(self):
        if len(self.cells) == 0:
            raise Exception('No more free colors')

        name = choice(self.cells.keys())
        del self.cells[name]
        return name
