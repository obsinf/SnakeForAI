

class AI:

    def __init__(self, b=False):
        self.b = b

    def next_step(self, normalized_field, current_derection):
        """if current_derection == 'left':
            return 'down'
        elif current_derection == 'down':
            return 'right'
        elif current_derection == 'right':
            return 'up'
        else:
            return 'right'"""

        # head_x, head_y = -1, -1

        """
        for x in range(len(normalized_field)):
            for y in range(len(normalized_field[x])):
                if normalized_field[x][y] == 'head':
                    head_x, head_y = x, y
        """

        if self.b:
            with open('output.txt', 'w') as ouf:

                to_print = [[0] * len(normalized_field)
                            for _ in range(len(normalized_field[0]))]

                for x in range(len(normalized_field)):
                    for y in range(len(normalized_field[x])):
                        to_print[y][x] = normalized_field[x][y]

                for x in range(len(to_print)):
                    for y in range(len(to_print[x])):
                        ouf.write(to_print[x][y].rjust(13, ' '))
                    ouf.write('\n')

        self.b = False
        return input()
