from time import sleep
import random
import os

from sheet_data import update_sheet

from validation import validate_main_menu
from validation import validate_yes_no
from validation import validate_math

from colorama import init
from colorama import Fore

init(autoreset=True)


LEVELS_LIST = []
LEVELS_PLAYED = 0
CURRENT_PLAYER = {}
NEW_SECTION = "-  "*26


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
         ["|", ".", "%", ".", "|", "@", ".", ".", ".", ".", "|"],
         ["|", ".", "|", ".", "|", "_", "_", ".", "|", ".", "|"],
         ["A", ".", "|", ".", ".", ".", ".", ".", "|", ".", "B"],
         ["|", ".", "|", ".", "|", "_", "_", "_", "|", ".", "|"],
         ["|", ".", "|", ".", "|", "@", ".", ".", ".", ".", "|"],
         ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
        [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
         ["|", ".", ".", ".", ".", "|", ".", ".", ".", ".", "|"],
         ["|", "_", ".", "|", ".", "|", ".", "_", "_", ".", "|"],
         ["A", ".", ".", "|", ".", "|", ".", ".", "|", ".", "B"],
         ["|", "_", ".", "|", ".", "|", "_", ".", "|", ".", "|"],
         ["|", "@", ".", "|", "%", ".", ".", ".", "|", "@", "|"],
         ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
        [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
         ["|", ".", ".", ".", ".", ".", ".", ".", ".", "@", "|"],
         ["|", "_", "_", ".", "|", "_", "_", "_", "_", "_", "|"],
         ["A", ".", "|", ".", ".", ".", ".", ".", ".", ".", "B"],
         ["|", ".", "|", "_", "_", "|", "%", "|", "_", "_", "|"],
         ["|", ".", ".", ".", ".", ".", ".", ".", ".", "@", "|"],
         ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
        [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
         ["|", ".", ".", ".", "%", ".", ".", ".", "|", "@", "|"],
         ["|", ".", "_", "_", "|", ".", "|", ".", "|", ".", "|"],
         ["A", ".", ".", ".", "|", ".", "|", ".", "|", ".", "B"],
         ["|", "_", "_", ".", "|", ".", "|", ".", "|", ".", "|"],
         ["|", ".", ".", ".", "|", "@", "|", ".", ".", ".", "|"],
         ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
        [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
         ["|", ".", "@", ".", ".", ".", "|", ".", ".", ".", "|"],
         ["|", ".", "|", ".", "|", ".", "|", ".", "|", ".", "|"],
         ["A", ".", "|", ".", "|", ".", "%", ".", "|", ".", "B"],
         ["|", ".", "|", ".", "|", ".", "|", "_", "_", ".", "|"],
         ["|", ".", ".", ".", "@", ".", "|", ".", ".", ".", "|"],
         ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
        [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
         ["|", "@", ".", ".", ".", ".", "|", ".", ".", "@", "|"],
         ["|", "_", "|", ".", "|", ".", "|", ".", "_", "_", "|"],
         ["A", ".", "|", ".", "|", ".", ".", ".", "|", ".", "B"],
         ["|", ".", "|", ".", "|", "_", "_", "_", "|", ".", "|"],
         ["|", ".", ".", "%", ".", ".", ".", ".", ".", ".", "|"],
         ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
        [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
         ["|", ".", ".", ".", "|", ".", "|", "@", ".", ".", "|"],
         ["|", ".", "|", ".", "|", ".", "|", "_", "_", ".", "|"],
         ["A", ".", "|", ".", "|", ".", "|", ".", "%", ".", "B"],
         ["|", "_", "_", ".", "|", ".", "|", ".", "|", ".", "|"],
         ["|", "@", ".", ".", ".", ".", ".", ".", "|", ".", "|"],
         ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
        [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
         ["|", "|", ".", ".", "%", ".", ".", ".", ".", "@", "|"],
         ["|", ".", ".", "_", "_", "_", "_", ".", "_", "_", "|"],
         ["A", ".", "|", ".", ".", ".", ".", ".", "|", ".", "B"],
         ["|", "_", "|", ".", "_", "_", "_", "_", "|", ".", "|"],
         ["|", "@", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
         ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
        [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
         ["|", "@", ".", ".", ".", ".", ".", "|", ".", ".", "|"],
         ["|", "_", "|", ".", "_", "_", ".", "|", "_", ".", "|"],
         ["A", ".", "|", ".", ".", "|", ".", ".", ".", ".", "B"],
         ["|", ".", "|", "_", ".", "|", ".", "|", "_", ".", "|"],
         ["|", ".", "%", ".", ".", "|", ".", "|", "@", ".", "|"],
         ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
        [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
         ["|", "@", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
         ["|", "_", ".", "_", "_", "_", "_", ".", "|", ".", "|"],
         ["A", ".", ".", ".", ".", "%", ".", ".", "|", ".", "B"],
         ["|", "_", "_", "_", "_", "_", "_", ".", "|", ".", "|"],
         ["|", "@", ".", ".", ".", ".", ".", ".", "|", ".", "|"],
         ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
    ]

    def __init__(self, level_number, layout_number):
        self.layout_number = layout_number
        self.level_number = level_number


def start_game():
    """
    The function that controls the flow of the game
    """
    level_order = random_layout_selector()
    game_layout = generate_levels(level_order)
    current_player = generate_player()
    run_menu(current_player, game_layout)


def random_layout_selector():
    """
    A function to order the appearance of the different levels
    (stored in the level class.)
    """
    layout_order = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
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
        LEVELS_LIST.append({f"{level_num}": level.layouts[i]})
        this_game_layout.append(level.layouts[i])
    return this_game_layout


def generate_player():
    """
    A function to generate an instance of the player class
    to keep track of the player's score and lives
    """
    print(Fore.GREEN + "What is your name?")
    player_name = input("Type here: \n")
    player = Player(player_name, 3, 0)
    return player


def clear_screen():
    """
    Clears the terminal of content.
    It is called when the user needs a new "screen" or viewport.
    """
    os.system("cls" if os.name == 'nt' else "clear")


def run_menu(player, levels):
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
    menu_selection = input("Type your choice here: \n")
    if validate_main_menu(menu_selection):
        if menu_selection == "i":
            print("These are the instructions")
        elif menu_selection == "s":
            print("Starting...")
            sleep(0.5)
            print(NEW_SECTION)
            sleep(0.5)
            get_level(levels)
        elif menu_selection == "x":
            quit_game()
    else:
        run_menu(player, levels)


def get_level(levels):
    """
    Runs the level and prints it to the terminal.
    """
    for i in range(len(levels)):
        clear_screen()
        print("stats")
        print(NEW_SECTION)
        print_level(levels, i)
        print("stats")
        print("Enter your move in the form DIRECTION,STEPS")
        print("Direction = L, R, U, or D (left, right, up, down)")
        print("Steps = a number between 1 and 9")
        print("e.g. U,3 will move your character up 3 steps")
        input("\nEnter your move here.")


def print_level(levels, level_number):
    """
    Prints the current level to the terminal.
    """
    for j in levels[level_number]:
        y = " ".join(j)
        print(y)


def multiplication_question():
    """
    A function that generates a random multiplication question
    that the player must complete to continue.
    """
    num1 = random.randint(2, 10)
    num2 = random.randint(2, 10)
    print(f"What is {num1} multiplied by {num2}?")
    player_answer = input("\nType your answer here: \n")
    if validate_math(player_answer):
        player_answer_int = int(player_answer)
        answer = num1 * num2
        if player_answer_int == answer:
            print("\nCorrect! +10 points")
            return True
        else:
            print("\nUh oh! That was incorrect...You lose 1 life!")
            print(f"The correct answer was {answer}")
            return False
    else:
        multiplication_question()


def bonus_question():
    """
    A more difficult and optional question that is called each
    time the player navigates to @ symbol in the level.
    """
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    print("BONUS QUESTION:")
    sleep(0.2)
    print(NEW_SECTION)
    sleep(0.2)
    print(f"What is {num1} multiplied by {num2}?")
    player_answer = input("\nType your answer here: \n")
    if validate_math(player_answer):
        player_answer_int = int(player_answer)
        answer = num1 * num2
        if player_answer_int == answer:
            print("\nCorrect! +20 points")
            # return player to the level, change @ marker to X, add points
            return True
        else:
            print("\nUh oh! That was incorrect...You lose 1 life!")
            print(f"The correct answer was {answer}")
            # return player to the level, change @ marker to X, minus lives
            return False
    else:
        bonus_question()


def quit_game():
    """
    Checks if the user would like to write some feedback on
    the game before thanking them and exiting the program.
    """
    clear_screen()
    sleep(0.2)
    print(NEW_SECTION)
    sleep(0.2)
    print("Are you sure you want to quit?")
    quit_yes_no = input("\nType y for yes, n for no: \n")
    if validate_yes_no(quit_yes_no):
        print("Would you like to give us feedback on this game?")
        feedback_yes_no = input("\nType y for yes, n for no: \n")
        if validate_yes_no(feedback_yes_no):
            if feedback_yes_no == "y":
                feedback_message = input("\nLeave your message here: \n")
                feedback_data = [feedback_message]
                # call validation function to stop long message.
                update_sheet(feedback_data, "feedback")
                sleep(2)
                clear_screen()
                print("Thanks for the feedback and Thanks for playing!")
                print("See you next time!")
                print(NEW_SECTION)
                print("Click 'Run Program' to begin!")
            else:
                print("Thanks for playing! See you next time!")
                print(NEW_SECTION)
                print("Click 'Run Program' to begin!")
        else:
            quit_game()
    else:
        quit_game()


start_game()

# bonus_question()
