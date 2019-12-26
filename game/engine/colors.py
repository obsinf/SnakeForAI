from copy import copy
from random import choice

_colors = {
    # game's colors
    'red': '#ff0000',
    'white': '#ffffff',
    'black': '#000000',

    # snake's colors
    'green': '#2ffa70',
    'yellow': '#ffff0a',
    'cyan': '#05f5ed',
    'blue': '#0040ff',
    'burgundy': '#fa07fa',
    'orange': '#ff9924',
    'purple': '#4e1296',
    'grey': '#bfbebb',
}


def color(color_name):
    if color_name in _colors:
        return _colors[color_name]
    else:
        return _colors['white']


class ColorDistributor:
    # distributes colors in random order

    def __init__(self):
        self.colors = copy(_colors)
        del self.colors['red']
        del self.colors['white']
        del self.colors['black']

    def next_color(self):
        if len(self.colors) == 0:
            raise Exception('No more free colors')

        name, col = choice(list(self.colors.items()))
        del self.colors[name]
        return name, col
