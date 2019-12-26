import tkinter as tk
from colors import color
from time import sleep
from cell_types import CellTypes
from snake import Snake


class PixelField(tk.Frame):

    def __init__(self, width=1200, height=900, cell_size=30, title="Snakes", tick=250):
        super().__init__()
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.title = title
        self.tick = tick
        self.field = [[0] * self.field_height()
                      for _ in range(self.field_width())]

        self.initUI()

    def initUI(self):
        # create and configurate canvas
        self.master.title(self.title)
        self.pack(fill=tk.BOTH, expand=1)
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)
        self.canvas.pack(fill=tk.BOTH)

        self.snake = Snake('yellow', 39, 27)
        # set up updates
        self.canvas.after(self.tick, self.updates)

        self.canvas.mainloop()

    def updates(self):
        # clear field
        self.canvas.delete('all')
        for x in range(self.field_width()):
            for y in range(self.field_height()):
                self.field[x][y] = 0

        # do something
        self.next_tick()
        # update canvas
        for x in range(self.field_width()):
            for y in range(self.field_height()):
                self.set_pixel(x, y, CellTypes.get(self.field[x][y]))

        self.canvas.after(self.tick, self.updates)

    def next_tick(self):
        self.snake.next_step(self.field)

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
                                     outline=color('black'), fill=col)


if __name__ == '__main__':
    # tests
    field = PixelField()

    print(len(field.field), len(field.field[0]))
