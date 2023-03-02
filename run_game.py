import random
GAME_LAYOUT = []
LEVELS_DICT = {}
LEVELS_PLAYED = 0

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
    layouts = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]

    #layouts = [
    #   [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
    #    ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
    #    ["|", "-", "-", "-", "-", "-", "-", "-", "-", "-", "|"],
    #    [" ", ".", ".", ".", ".", ".", ".", ".", ".", ".", " "],
    #    ["|", "-", "-", "-", "-", "-", "-", "-", "-", "-", "|"],
    #    ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
    #    ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
    #    [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
    #    ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
    #    ["|", "-", "-", "-", "-", "-", "-", "-", "-", "-", "|"],
    #    [" ", ".", ".", ".", ".", ".", ".", ".", ".", ".", " "],
    #    ["|", "-", "-", "-", "-", "-", "-", "-", "-", "-", "|"],
    #    ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
    #    ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
    #]

    def __init__(self, level_number, layout_number):
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
    level_order = random_layout_selector()
    # GAME_LAYOUT = level_order
    generate_levels(level_order)
    print(GAME_LAYOUT)
    print(LEVELS_DICT)


def random_layout_selector():
    """
    A function to order the appearance of the different levels
    (stored in the level class.)
    """
    layout_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(layout_order)
    return layout_order

def generate_levels(data):
    """
    A function to create new instances of the Level class and return
    a randomised list of the levels for the game.
    """
    this_game_layout = []
    level_num = 0
    for i in data:
        level_num += 1
        level = Level(level_num, i)
        LEVELS_DICT.update({f"{level_num}" : i})
        GAME_LAYOUT.append(level.layouts[i])
        this_game_layout.append(level.layouts[i])
    return this_game_layout


start_game()