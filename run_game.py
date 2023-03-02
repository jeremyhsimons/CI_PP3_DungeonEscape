import random
from run import CURRENT_USER


class Player:
    """
    A class that defines the common features of users/players
    in-game characters.
    """
    def __init__(self, name, lives, points):
        self.name = name
        self.lives = lives
        self.points = points


class Level:
    """
    A class that defines the levels that the player will encounter.
    a level will be passed a layout number to select which layout 
    will be presented to the player, and a level_number to keep
    track of how far the player has progressed.
    """

    layouts = [
        [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
        ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
        ["|", "-", "-", "-", "-", "-", "-", "-", "-", "-", "|"],
        [" ", ".", ".", ".", ".", ".", ".", ".", ".", ".", " "],
        ["|", "-", "-", "-", "-", "-", "-", "-", "-", "-", "|"],
        ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
        ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
        [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
        ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
        ["|", "-", "-", "-", "-", "-", "-", "-", "-", "-", "|"],
        [" ", ".", ".", ".", ".", ".", ".", ".", ".", ".", " "],
        ["|", "-", "-", "-", "-", "-", "-", "-", "-", "-", "|"],
        ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
        ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
    ]

    def __init__(self, layout_number, level_number):
        self.layout_number = layout_number
        self.level_number = level_number


# O - - - - - - - - - O
# | . % . | @ . . . . |
# | . | . | _ _ . | . |
#   . | . . . . . | .
# | . | . | _ _ _ | . |
# | . | . | @ . . . . |
# O - - - - - - - - - O

# for j in room_layout:
#    y = " ".join(j)
#    print(y)


def start_game():
    """
    The function that controls the flow of the game
    """
    random_layout_selector()
    level = Level(0, 1)
    print(level.layouts[0])


def random_layout_selector():
    layout_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random_order = random.shuffle(layout_order)
    print(random_order)

start_game()