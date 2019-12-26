from colors import color


class CellTypes:
    # game objects
    EMPTY_CELL = 0
    APPLE = 1

    # colors
    GREEN = 2
    YELLOW = 3
    CYAN = 4
    BLUE = 5
    BURGUNDLY = 6
    ORANGE = 7
    PURPLE = 8
    GREY = 9

    id_to_color = {
        EMPTY_CELL: 'white',
        APPLE: 'red',

        GREEN: 'green',
        YELLOW: 'yellow',
        CYAN: 'cyan',
        BLUE: 'blue',
        BURGUNDLY: 'burgundly',
        ORANGE: 'orange',
        PURPLE: 'purple',
        GREY: 'grey',
    }
    color_to_id = {c[1]: c[0] for c in id_to_color.items()}
    
    @staticmethod
    def get(cell_id):

        return CellTypes.id_to_color[cell_id]


"""
    'green': '#2ffa70',
    'yellow': '#ffff0a',
    'cyan': '#05f5ed',
    'blue': '#0040ff',
    'burgundy': '#fa07fa',
    'orange': '#ff9924',
    'purple': '#4e1296',
    'grey': '#bfbebb',
"""
