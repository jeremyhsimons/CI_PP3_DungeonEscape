import random

from time import sleep

GAME_LAYOUT = []
LEVELS_DICT = {}
LEVELS_PLAYED = 0
CURRENT_PLAYER = {}
NEW_SECTION = "-"*30

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
    #    ["|", ".", "%", ".", "|", "@", ".", ".", ".", ".", "|"],
    #    ["|", ".", "|", ".", "|", "_", "_", ".", "|", ".", "|"],
    #    ["X", ".", "|", ".", ".", ".", ".", ".", "|", ".", " "],
    #    ["|", ".", "|", ".", "|", "_", "_", "_", "|", ".", "|"],
    #    ["|", ".", "|", ".", "|", "@", ".", ".", ".", ".", "|"],
    #    ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
    #   [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
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
# X . | . . . . . | .
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
    generate_levels(level_order)
    current_player = generate_player()
    run_menu(current_player)


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


def generate_player():
    """
    A function to generate an instance of the player class
    to keep track of the player's score and lives
    """
    print("What is your name?")
    player_name = input("Type here: ")
    player = Player(player_name, 3, 0)
    return player


def clear_screen():
    """
    Clears the terminal of content.
    It is called when the user needs a new "screen" or viewport.
    """
    os.system("cls" if os.name == 'nt' else "clear")


def run_menu(player):
    """
    Creates a menu for the player to decide whether or not to
    read the instructions, quit, or play the game.
    """
    print(NEW_SECTION)
    sleep(0.2)
    print(f"Welcome {player.name}! What would you like to do?\n")
    sleep(0.2)
    print("Press i for game instructions")
    print("Press s to start the game")
    print("Press x to quit")
    menu_selection = input("Type your choice here: ")
    # call a validation function here
    if menu_selection == "i":
        print("These are the instructions")
    elif menu_selection == "s":
        print("let the games begin!")
    elif menu_selection == "x":
        quit_game()


def multiplication_question():
    """
    A function that generates a random multiplication question
    that the player must complete to continue.
    """
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    print(f"What is {num1} multiplied by {num2}?")
    player_answer = int(input("\nType your answer here: "))
    # call a validation function here
    answer = num1 * num2
    if player_answer == answer:
        print("\nCorrect! +10 points")
        return True
    else:
        print("\nUh oh! That was incorrect...You lose 1 life!")
        print(f"The correct answer was {answer}")
        return False


start_game()