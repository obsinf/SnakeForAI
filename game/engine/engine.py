import tkinter as tk
from time import sleep
from cells import cell, SnakeDistributor
from snake import Snake
from random import randrange
from AI import AI
from copy import deepcopy


class PixelField(tk.Frame):

    def __init__(self, ai_array, width=1200, height=900, cell_size=20, title="Snakes", tick=2000):
        super().__init__()
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.title = title
        self.tick = tick
        self.field = [['empty_cell'] * self.field_height()
                      for _ in range(self.field_width())]

        # create apples
        for _ in range(self.field_height() * self.field_width()//20):
            self.field[randrange(0, self.field_width())][randrange(
                0, self.field_height())] = 'apple'

        # create snakes
        self.snakes = []
        for brain in ai_array:
            random_x = randrange(0, self.field_width())
            random_y = randrange(0, self.field_height() - 4)
            self.snakes += [Snake(brain,
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

        # get snakes's position
        enemies = [
            [False] * self.field_height()
            for _ in range(self.field_width())
        ]
        for snake in self.snakes:
            for segment in snake.segments:
                enemies[segment[0]][segment[1]] = True

        # remove snakes from field
        for x in range(self.field_width()):
            for y in range(self.field_height()):
                if self.field[x][y] != 'empty_cell' and self.field[x][y] != 'apple':
                    self.field[x][y] = 'empty_cell'

        # do something
        self.next_tick(enemies)

        # add snakes to field
        for snake in self.snakes:
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


if __name__ == '__main__':
    # tests
    ai1 = AI()
    # ai2 = AI(b=True)

    field = PixelField([ai1])

    print(len(field.field), len(field.field[0]))
