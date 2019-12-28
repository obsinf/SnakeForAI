from cells import cell
from collections import deque
from copy import deepcopy


class Snake:

    def __init__(self, ai, color, start_x, start_y):
        self.color = color
        self.segments = deque()
        self.score = 0
        self.dead = False

        # create snake's body (with length 4)
        self.segments.append([start_x, start_y])
        self.segments.append([start_x, start_y + 1])
        self.segments.append([start_x, start_y + 2])
        self.segments.append([start_x, start_y + 3])

        # create brain for our snake
        self.brain = ai

        # set default direction in start of game
        self.direction = 'up'

    direct = {
        'up': (0, -1),
        'down': (0, 1),
        'left': (-1, 0),
        'right': (1, 0),
    }

    def next_step(self, game_field, enemy_map):
        # normalize field

        normalized_field = [['empty_cell'] *
                            len(game_field[0]) for _ in range(len(game_field))]

        for x in range(len(game_field)):
            for y in range(len(game_field[x])):
                if game_field[x][y] == 'apple':
                    normalized_field[x][y] = 'apple'
                elif enemy_map[x][y]:
                    normalized_field[x][y] = 'enemy'

        # make our snake recognize itself
        head = self.segments.popleft()

        normalized_field[head[0]][head[1]] = 'head'
        for pos in self.segments:
            normalized_field[pos[0]][pos[1]] = 'me'
        self.segments.appendleft(head)

        self.direction = self.brain.next_step(normalized_field, self.direction)

        step = self.direct[self.direction]

        new_head = [head[0] + step[0], head[1] + step[1]]
        self.segments.appendleft(new_head)

        if game_field[new_head[0]][new_head[1]] == 'apple':
            # print("THIS IS APPLE")
            print(f'{self.color} got apple!')
        elif game_field[new_head[0]][new_head[1]] == 'empty_cell':
            self.segments.pop()

        self.score += len(self.segments)
