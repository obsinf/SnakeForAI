import tkinter as tk
from time import sleep
from cells import cell, SnakeDistributor
from snake import Snake
from random import randrange
from AI import AI
from copy import deepcopy


class Game(tk.Frame):

    def __init__(self, ai_array, width=1200, height=900, cell_size=20, title="Snakes", tick=2000):
        super().__init__()
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.title = title
        self.tick = tick
        self.field = [['empty_cell'] * self.field_height()
                      for _ in range(self.field_width())]
        self.alive = len(ai_array)
        self.scores = [0] * len(ai_array)

        # create apples
        for _ in range(self.field_height() * self.field_width()//20):
            self.field[randrange(0, self.field_width())][randrange(
                0, self.field_height())] = 'apple'

        # create snakes
        self.snakes = []
        for i, brain in enumerate(ai_array):
            random_x = randrange(0, self.field_width())
            random_y = randrange(0, self.field_height() - 4)
            self.snakes += [Snake(i, brain,
                                  'green_snake', random_x, random_y)]
            # and add snake to the field
            for segment in self.snakes[-1].segments:
                self.field[segment[0]][segment[1]] = self.snakes[-1].color

        self.initUI()

    def initUI(self):
        # create and configurate canvas
        self.master.title(self.title)
        self.pack(fill=tk.BOTH, expand=1)
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)
        self.canvas.pack(fill=tk.BOTH)

        # set up updates
        self.canvas.after(self.tick, self.updates)

        self.canvas.mainloop()

    def updates(self):
        print(self.alive)
        # get snakes's position
        enemies = [
            [False] * self.field_height()
            for _ in range(self.field_width())
        ]
        for snake in self.snakes:
            if snake is not None:
                for segment in snake.segments:
                    enemies[segment[0]][segment[1]] = True

        # remove snakes from field
        for x in range(self.field_width()):
            for y in range(self.field_height()):
                if self.field[x][y] != 'empty_cell' and self.field[x][y] != 'apple':
                    self.field[x][y] = 'empty_cell'

        # do something
        self.next_tick(enemies)

        # delete killed snakes
        self.delete_killed()

        # add snakes to field
        for snake in self.snakes:
            if snake is not None:
                for segment in snake.segments:
                    self.field[segment[0]][segment[1]] = snake.color

        # with probability 25% create new apple
        if randrange(0, 100) <= 25:
            rand_x = randrange(0, self.field_width())
            rand_y = randrange(0, self.field_height())
            while self.field[rand_x][rand_y] != 'empty_cell':
                rand_x = randrange(0, self.field_width())
                rand_y = randrange(0, self.field_height())
            self.field[rand_x][rand_y] = 'apple'

        # update canvas
        self.canvas.delete('all')
        for x in range(self.field_width()):
            for y in range(self.field_height()):
                self.set_pixel(x, y, cell(self.field[x][y]))

        self.canvas.after(self.tick, self.updates)

    def next_tick(self, enemies):
        for snake in self.snakes:
            if snake is not None:
                snake.next_step(self.field, enemies)

    def field_width(self):
        return self.width // self.cell_size \
            + min(1, self.width % self.cell_size)

    def field_height(self):
        return self.height // self.cell_size \
            + min(1, self.height % self.cell_size)

    def set_pixel(self, x, y, col):
        x *= self.cell_size
        y *= self.cell_size

        self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size,
                                     outline='#000000', fill=col)

    def delete_killed(self):
        sgm = []
        heads = []
        ids = []
        directions = []
        results = []

        to_delete = []

        for index, snake in enumerate(self.snakes):
            if snake is None:
                sgm += [None]
                heads += [None]
                ids += [None]
                directions += [None]
                results += [None]
            else:
                body = list(snake.segments)
                sgm += [set(map(tuple, body[1:]))]
                heads += [tuple(body[0])]
                ids += [snake.id]
                directions += [snake.direction]
                results += [snake.score]

        # collision face-to-face
        opposites = {
            'up': 'down',
            'down': 'up',
            'left': 'right',
            'right': 'left',
        }

        for head1_index in range(len(heads)):
            for head2_index in range(head1_index + 1, len(heads)):

                if self.snakes[head1_index] is None or \
                        self.snakes[head2_index] is None:
                    continue

                if heads[head1_index] == heads[head2_index] \
                   and directions[head1_index] == opposites[directions[head2_index]]:

                    print(f"DESRUPTION({head1_index}, {head2_index})")

                    # save scores
                    self.scores[ids[head1_index]] = results[head1_index]
                    self.scores[ids[head2_index]] = results[head2_index]

                    to_delete += [head1_index, head2_index]

        # collisions
        for head_index in range(len(heads)):
            for segments_index in range(len(sgm)):
                if heads[head_index] is None \
                        or sgm[segments_index] is None:
                    continue
                if heads[head_index] in sgm[segments_index]:
                    print(f"DISRUPTION2({head_index})")
                    to_delete += [head_index]

        to_delete = list(set(to_delete))

        for index in to_delete:
            self.snakes[index] = None
            self.alive -= 1
