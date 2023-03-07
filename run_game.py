from time import sleep
import random
import os

from sheet_data import update_sheet

from validation import validate_main_menu
from validation import validate_yes_no
from validation import validate_math
from validation import validate_navigation

from colorama import init
from colorama import Fore

init(autoreset=True)


LEVELS_LIST = []
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
    menu = run_menu(current_player)
    if menu == 1:
        print("instructions")
    elif menu == 2:
        quit_game()
    elif menu == 3:
        # All wrapped in For loop that loops through game layout.
        # Successfull passing of each level, triggers next iteration.
        # Each successful iteration adds 1 to LEVELS_PLAYED
        # At the end of each iteration, LEVELS_PLAYED is checked to see
        # if winning conditions are met.
        LEVELS_PLAYED = 0
        lives = current_player.lives
        points = current_player.points
        game_stats = [
            f"Level: {LEVELS_PLAYED + 1}", 
            f"Lives: {lives}", 
            f"points: {points}"
            ]
        for i in range(len(game_layout)):  # MAIN LOOP
            get_new_level = get_level(game_layout, i, game_stats)
            # returns a list: [layout, number]
            run_level(get_new_level, lives)

            LEVELS_PLAYED += 1
            points += 15
            if LEVELS_PLAYED >= 10:
                quit_game()


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
    menu_selection = input("Type your choice here: \n")
    if validate_main_menu(menu_selection):
        if menu_selection == "i":
            return 1
        elif menu_selection == "s":
            print("Starting...")
            sleep(0.5)
            print(NEW_SECTION)
            sleep(0.5)
            return 3
        elif menu_selection == "x":
            return 2
    else:
        run_menu(player)


def get_level(levels, level_number, stats):
    """
    Runs the level and prints it to the terminal.
    """
    clear_screen()
    print(stats)
    print(NEW_SECTION)
    current_level = [levels[level_number], level_number]
    return current_level


def print_level(data):
    """
    Prints the current level to the terminal.
    """
    for j in data[0]:
        y = " ".join(j)
        print(y)


def run_level(current_level, lives):
    """
    Runs the game logic for each level.
    """
    while current_level[0][3][10] == "b":
        current_layout = current_level[0]
        print_level(current_layout)
        print("Enter your move in the form DIRECTION,STEPS")
        print("Direction = L, R, U, or D (left, right, up, down)")
        print("Steps = a number between 1 and 9")
        print("e.g. U,3 will move your character up 3 steps")
        nav_str = input("\nEnter your move here.")
        if validate_navigation(nav_str):
            nav_data = nav_str.split(",")
            int_nav_data = [nav_data[0], int(nav_data[1])]
            player_position = [0, 3]
            new_position = calc_navigation(int_nav_data, player_position)
            if new_position[0] > 10 or new_position[0] < 0:
                print("You've moved out of bounds! You lose 1 life")
                lives -= 1
                run_level(current_level, lives)
            elif new_position[1] > 6 or new_position[1] < 0:
                print("You've moved out of bounds!")
                print("You lose 1 life and must restart the level.")
                lives -= 1
                run_level(current_level, lives)
            else:
                print("position OK")
                if nav_data[0] == "R":
                    check_move_right(
                        current_level, player_position, new_position, lives
                        )
                sleep(1)
        else:
            run_level(current_level, lives)


def calc_navigation(nav, position):
    """
    Calculates where the player is in the level, and where
    they will move to based on their input.
    """
    if nav[0] == "L":
        position = [(position[0] - nav[1]), position[1]]
        print(position)
        return position
    if nav[0] == "R":
        position = [(position[0] + nav[1]), position[1]]
        print(position)
        return position
    if nav[0] == "U":
        position = [position[0], (position[1] - nav[1])]
        print(position)
        return position
    if nav[0] == "D":
        position = [position[0], (position[1] + nav[1])]
        print(position)
        return position


def check_move_left(level, pos1, pos2):
    """
    Checks the players move by looping back through the level
    list to see if their route is valid.
    """


def check_move_right(level, pos1, pos2, lives):
    """
    Checks the players move by looping forward through the level
    list to see if their route is valid.
    """
    level_layout = level[0]
    route = level_layout[pos1[1]][pos1[0]:pos2[0]+1]
    if check_route(route, lives):
        level_layout[pos1[1]][pos1[0]] = "."
        level_layout[pos2[1]][pos2[0]] = "A"
        return level_layout


def check_move_up(level):
    """
    Checks the player's move by looping back through the elements of
    each level list with the same index as the player horizontal position.
    """


def check_move_down(level):
    """
    Checks the player's move by looping forward through the elements of
    each level list with the same index as the player horizontal position.
    """


def check_route(route, lives):
    """
    Checks if the player runs into any obstacles in their move.
    """
    for i in route:
        if i == ".":
            print("OK")
        elif i == "|" or i == "-" or i == "_" or i == "O":
            print(NEW_SECTION)
            print("You tried to move through a wall!")
            print("You lose one life and move back to the start.")
            lives -= 1
            return False
        elif i == "%":
            print("math1")
        elif i == "@":
            print("math2")
        else:
            print("An unknown error occurred. Restarting level.")
            sleep(1)
            print(NEW_SECTION)
            sleep(1)
            return False
        return True


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
        print("\nWould you like to give us feedback on this game?")
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
