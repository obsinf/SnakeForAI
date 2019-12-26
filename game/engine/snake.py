from colors import color
from collections import deque
from cell_types import CellTypes


class Snake:

    def __init__(self, color_name, start_x, start_y):
        self.color_name = color_name
        self.color = color(color_name)
        self.segments = deque()
        self.score = 0

        self.segments.append([start_x, start_y])
        self.segments.append([start_x, start_y + 1])
        self.segments.append([start_x, start_y + 2])
        self.segments.append([start_x, start_y + 3])

        self.direction = 'up'
        self.n = 0

    direct = {
        'up': (0, -1),
        'down': (0, 1),
        'left': (-1, 0),
        'right': (1, 0),
    }

    def next_step(self, game_field):

        step = self.direct[self.direction]

        head = self.segments.popleft()
        self.segments.appendleft(head)
        new_head = [head[0] + step[0], head[1] + step[1]]
        self.segments.appendleft(new_head)
        self.segments.pop()

        self.n += 1
        if self.n == 10:
            self.direction = 'left'
        elif self.n == 15:
            self.direction = 'down'

        for segment in self.segments:
            game_field[segment[0]][segment[1]
                                   ] = CellTypes.color_to_id[self.color_name]
