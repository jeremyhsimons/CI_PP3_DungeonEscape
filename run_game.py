# Imports
# Python
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from time import sleep
import random
import os
# 3rd party
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from colorama import init
from colorama import Fore
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sheet_data import update_sheet
from validation import validate_main_menu
from validation import validate_yes_no
from validation import validate_math
from validation import validate_navigation
from validation import validate_string
from validation import validate_message
from instructions import print_instructions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


init(autoreset=True)

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
         ["|", ".", ".", ".", "|", ".", ".", ".", ".", ".", "|"],
         ["|", ".", "|", ".", "|", "_", "_", ".", "|", ".", "|"],
         ["A", ".", "|", ".", ".", ".", ".", ".", "|", ".", "B"],
         ["|", ".", "|", ".", "|", "_", "_", "_", "|", ".", "|"],
         ["|", ".", "|", ".", "|", ".", ".", ".", ".", ".", "|"],
         ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
        [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
         ["|", ".", ".", ".", ".", "|", ".", ".", ".", ".", "|"],
         ["|", "_", ".", "|", ".", "|", ".", "_", "_", ".", "|"],
         ["A", ".", ".", "|", ".", "|", ".", ".", "|", ".", "B"],
         ["|", "_", ".", "|", ".", "|", "_", ".", "|", ".", "|"],
         ["|", ".", ".", "|", ".", ".", ".", ".", "|", ".", "|"],
         ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
        [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
         ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
         ["|", "_", "_", ".", "|", "_", "_", "_", "_", "_", "|"],
         ["A", ".", "|", ".", ".", ".", ".", ".", ".", ".", "B"],
         ["|", ".", "|", "_", "_", "|", ".", "|", "_", "_", "|"],
         ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
         ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
        [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
         ["|", ".", ".", ".", ".", ".", ".", ".", "|", ".", "|"],
         ["|", ".", "_", "_", "|", ".", "|", ".", "|", ".", "|"],
         ["A", ".", ".", ".", "|", ".", "|", ".", "|", ".", "B"],
         ["|", "_", "_", ".", "|", ".", "|", ".", "|", ".", "|"],
         ["|", ".", ".", ".", "|", ".", "|", ".", ".", ".", "|"],
         ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
        [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
         ["|", ".", ".", ".", ".", ".", "|", ".", ".", ".", "|"],
         ["|", ".", "|", ".", "|", ".", "|", ".", "|", ".", "|"],
         ["A", ".", "|", ".", "|", ".", ".", ".", "|", ".", "B"],
         ["|", ".", "|", ".", "|", ".", "|", "_", "_", ".", "|"],
         ["|", ".", ".", ".", ".", ".", "|", ".", ".", ".", "|"],
         ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
        [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
         ["|", ".", ".", ".", ".", ".", "|", ".", ".", ".", "|"],
         ["|", "_", "|", ".", "|", ".", "|", ".", "_", "_", "|"],
         ["A", ".", "|", ".", "|", ".", ".", ".", "|", ".", "B"],
         ["|", ".", "|", ".", "|", "_", "_", "_", "|", ".", "|"],
         ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
         ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
        [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
         ["|", ".", ".", ".", "|", ".", "|", ".", ".", ".", "|"],
         ["|", ".", "|", ".", "|", ".", "|", "_", "_", ".", "|"],
         ["A", ".", "|", ".", "|", ".", "|", ".", ".", ".", "B"],
         ["|", "_", "_", ".", "|", ".", "|", ".", "|", ".", "|"],
         ["|", ".", ".", ".", ".", ".", ".", ".", "|", ".", "|"],
         ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
        [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
         ["|", "|", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
         ["|", ".", ".", "_", "_", "_", "_", ".", "_", "_", "|"],
         ["A", ".", "|", ".", ".", ".", ".", ".", "|", ".", "B"],
         ["|", "_", "|", ".", "_", "_", "_", "_", "|", ".", "|"],
         ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
         ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
        [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
         ["|", ".", ".", ".", ".", ".", ".", "|", ".", ".", "|"],
         ["|", "_", "|", ".", "_", "_", ".", "|", "_", ".", "|"],
         ["A", ".", "|", ".", ".", "|", ".", ".", ".", ".", "B"],
         ["|", ".", "|", "_", ".", "|", ".", "|", "_", ".", "|"],
         ["|", ".", ".", ".", ".", "|", ".", "|", ".", ".", "|"],
         ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
        [["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"],
         ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
         ["|", "_", ".", "_", "_", "_", "_", ".", "|", ".", "|"],
         ["A", ".", ".", ".", ".", ".", ".", ".", "|", ".", "B"],
         ["|", "_", "_", "_", "_", "_", "_", ".", "|", ".", "|"],
         ["|", ".", ".", ".", ".", ".", ".", ".", "|", ".", "|"],
         ["O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O"]],
    ]

    def __init__(self, level_number, layout_number):
        self.layout_number = layout_number
        self.level_number = level_number


def start_game():
    """
    The function that controls the flow of the game
    """
    clear_screen()
    level_order = random_layout_selector()
    game_layout = generate_levels(level_order)
    current_player = generate_player()
    menu = run_menu(current_player)
    if menu == 1:
        clear_screen()
        print_instructions()
        input("press 'Enter' to return to menu")
        clear_screen()
        return start_game()
    elif menu == 2:
        pass
    elif menu == 3:
        levels_played = 0
        lives = current_player.lives
        points = current_player.points
        # Main game loop
        for i in range(len(game_layout)):
            if lives == 0:
                level_result = player_die()
                if level_result[1] == 1:
                    break
            else:
                get_new_level = get_level(game_layout, i)
                print_level(get_new_level)
                sleep(0.5)
                level_result = run_level(get_new_level, lives)
                if level_result[1] == 0:
                    sleep(0.5)
                    lives = level_result[0]
                    levels_played += 1
                    points += 15
                    print(
                        Fore.GREEN + f"+ 15 points! You have {points} points"
                        )
                    sleep(1)
                    clear_screen()
                    if levels_played >= 10:
                        sleep(1)
                        print("Game ended")
                        points += lives * 20
                        return [points, lives]
                    maths_answer = maths_question()
                    if maths_answer is True:
                        points += 20
                        sleep(1)
                        print(f"{current_player.name} has {points} points!")
                    else:
                        lives -= 1
                        sleep(1)
                        print(f"You have {lives} lives remaining.")
                elif level_result[1] == 1:
                    break
    if quit_game():
        print("\n")
        return False
    else:
        sleep(1)
        start_game()


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
        this_game_layout.append(level.layouts[i])
    return this_game_layout


def generate_player():
    """
    A function to generate an instance of the player class
    to keep track of the player's score and lives
    """
    print(Fore.GREEN + "What will your character's name be?")
    player_name = input("Type here: \n")
    if validate_string(player_name):
        player = Player(player_name, 3, 0)
        return player
    return generate_player()


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
    while True:
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
            sleep(2)
            clear_screen()
            sleep(0.2)


def get_level(levels, level_number):
    """
    Gets the current level from the .
    """
    current_level = [levels[level_number], level_number]
    return current_level


def print_level(data):
    """
    Prints the current level to the terminal.
    """
    clear_screen()
    print(NEW_SECTION)
    for j in data[0]:
        y = " ".join(j)
        print(y)


def run_level(current_level, lives):
    """
    Runs the game logic for each level.
    """
    player_position = [0, 3]
    level_complete = False
    # Level loop
    while level_complete is False:
        if lives == 0:
            death = player_die()
            return death
        else:
            current_layout = current_level[0]
            player_move = []
            print(f"Level: {current_level[1] + 1}, Lives: {lives}")
            print(NEW_SECTION)
            print("Enter your move in the form DIRECTION,STEPS")
            print("Direction = L, R, U, or D (left, right, up, down)")
            print("Steps = a number between 1 and 9")
            print("e.g. U,3 will move your character up 3 steps")
            nav_str = input("\nEnter your move here (press x to quit): \n")
            if nav_str == "x":
                return [lives, 1]
            if validate_navigation(nav_str):
                nav_data = nav_str.split(",")
                int_nav_data = [nav_data[0], int(nav_data[1])]
                player_move = calc_navigation(
                    int_nav_data,
                    player_position,
                    current_layout
                    )
            else:
                sleep(3)
                print_level(current_level)
            if not player_move:
                sleep(0.2)
            elif player_move[0] is False:
                sleep(1)
                print("Restarting level!")
                player_position = [0, 3]
                sleep(1)
                lives -= 1
                clear_screen()
                reset_level = reset(current_level)
                print_level([reset_level, current_level[1]])
            elif player_move[1] == 1:
                sleep(0.2)
                current_layout = player_move[0]
                player_position = player_move[2]
                current_level[0] = current_layout
                print_level(current_level)
            elif player_move[1] == 2:
                lives -= 1
                sleep(2)
                clear_screen()
                sleep(0.5)
                print_level(current_level)
            elif player_move[1] == 0:
                sleep(0.2)
                break
            else:
                pass
    clear_screen()
    level_complete = True
    sleep(2)
    print(NEW_SECTION)
    sleep(0.2)
    print(Fore.GREEN + f"Level {current_level[1] + 1} complete!")
    sleep(0.2)
    print(Fore.MAGENTA + f"{lives} lives remaining")
    sleep(1.5)
    return [lives, 0]


def reset(data):
    """
    Resets the player's position in the level
    if the player goes out of bounds.
    """
    for i in data[0]:
        for j in range(len(i)):
            if i[j] == "A":
                i[j] = "."
    data[0][3][0] = "A"
    return data[0]


def check_out_of_bounds(data):
    """
    Checks if the player is trying to move beyond the
    boundaries of the level.
    """
    if data[0] > 10 or data[0] < 0:
        print("You've moved out of bounds! You lose 1 life")
        return False
    elif data[1] > 6 or data[1] < 0:
        print("You've moved out of bounds!")
        print("You lose 1 life and must restart the level.")
        return False
    else:
        return True


def calc_navigation(nav, position, level):
    """
    Calculates where the player is in the level, and where
    they will move to based on their input.
    """
    col = []
    for i in range(len(level)):
        col.append(level[i][position[0]])
    if nav[0] == "L":
        new_position = [(position[0] - nav[1]), position[1]]
        route_slice = level[position[1]][new_position[0]: position[0] + 1]
        outcome = check_move(level, position, new_position, route_slice)
    if nav[0] == "R":
        new_position = [(position[0] + nav[1]), position[1]]
        route_slice = level[position[1]][position[0]: new_position[0] + 1]
        outcome = check_move(level, position, new_position, route_slice)
    if nav[0] == "U":
        new_position = [position[0], (position[1] - nav[1])]
        route_slice = col[new_position[1]:position[1] + 1]
        outcome = check_move(level, position, new_position, route_slice)
    if nav[0] == "D":
        new_position = [position[0], (position[1] + nav[1])]
        route_slice = col[position[1]:new_position[1] + 1]
        outcome = check_move(level, position, new_position, route_slice)
    return outcome


def check_move(level, pos1, pos2, route):
    """
    Checks the players move by looping back through the level
    list to see if their route is valid.
    """
    out_of_bounds = check_out_of_bounds(pos2)
    if out_of_bounds is False:
        return [False, "FALSE"]
    level_layout = level
    route_checked = check_route(route)
    return return_to_run_level(
        level_layout, route_checked, pos1, pos2, out_of_bounds
        )


def return_to_run_level(layout, route, pos1, pos2, bounds):
    """
    Passes back all data from player's move to the run_level
    function
    """
    if route == 1:
        layout[pos1[1]][pos1[0]] = "."
        layout[pos2[1]][pos2[0]] = "A"
        return [layout, 1, pos2, bounds]
    elif route == 0:
        return [layout, 0, pos2, bounds]
    else:
        return [layout, 2, pos2, bounds]


def check_route(route):
    """
    Checks if the player runs into any obstacles in their move.
    """
    for i in route:
        if i in ("|", "-", "_", "O"):
            print("You tried to navigate into a wall.")
            sleep(1)
            print("You lose one life!")
            sleep(1)
            return 2
    if "B" in route:
        return 0
    else:
        return 1


def maths_question():
    """
    A maths question that is called between each level. Player
    must answer correctly to avoid losing a life. If they answer
    correctly they also get bonus points.
    """
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    print("MULTIPLICATION QUESTION:")
    print("Answer this to progress to the next level!")
    sleep(0.2)
    print(NEW_SECTION)
    sleep(0.2)
    print(f"What is {num1} multiplied by {num2}?")
    player_answer = input("\nType your answer here: \n")
    if validate_math(player_answer):
        player_answer_int = int(player_answer)
        answer = num1 * num2
        if player_answer_int == answer:
            print("\nCorrect! +20 BONUS points")
            return True
        else:
            print("\nUh oh! That was incorrect...You lose 1 life!")
            print(f"The correct answer was {answer}")
            return False
    else:
        sleep(2)
        clear_screen()
        return maths_question()


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
        if quit_yes_no == "y":
            print("\nWould you like to give us feedback on this game?")
            feedback_yes_no = input("\nType y for yes, n for no: \n")
            if validate_yes_no(feedback_yes_no):
                if feedback_yes_no == "y":
                    feedback_message = input(
                        "\nLeave your message here (max 80 char): \n"
                        )
                    feedback_data = [feedback_message]
                    if validate_message(feedback_message):
                        update_sheet(feedback_data, "feedback")
                        sleep(2)
                        clear_screen()
                        print("Thanks for the feedback and for playing!")
                        print("See you next time!")
                        print(NEW_SECTION)
                        print("Click 'Run Program' to begin!")
                        return True
                    else:
                        print("Quitting game for security reasons")
                        sleep(0.5)
                        print("Thanks for playing! See you next time!")
                        print(NEW_SECTION)
                        print("Click 'Run Program' to begin!")
                        return True
                else:
                    print("Thanks for playing! See you next time!")
                    print(NEW_SECTION)
                    print("Click 'Run Program' to begin!")
                    return True
            else:
                return quit_game()
        elif quit_yes_no == "n":
            print("Restarting Game...")
            sleep(1)
            return False
    else:
        return quit_game()


def player_die():
    """
    Runs this code to check if the player wants
    to play again after dying.
    """
    clear_screen()
    sleep(0.2)
    print(Fore.RED + "###  UH OH   ###")
    sleep(0.2)
    print(Fore.RED + "### YOU DIED ###")
    sleep(0.2)
    print("Press y to start again, press n to quit")
    replay_yes_no = input("\nType choice here: \n")
    if validate_yes_no(replay_yes_no):
        if replay_yes_no == "y":
            print("Restarting Game")
            start_game()
        elif replay_yes_no == "n":
            return [0, 1]
    else:
        sleep(1)
        player_die()
