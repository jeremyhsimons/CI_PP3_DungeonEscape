# Imports
# 3rd party
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from colorama import init
from colorama import Fore
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


init(autoreset=True)


def print_instructions():
    """
    A function that prints the game instructions to the terminal
    """
    print(
        Fore.YELLOW +
        """
        Dungeon escape is a maze game with a couple of added twists...
        Your job is to navigate your character (represented by letter 'A')
        To the exit of each level (represented by letter 'B').
        Beware! The walls of each level are electrified!
        If you touch a wall you will lose a life.
        If you lose all three lives, your character will die
        and you will have to restart the game.\n
        Be careful how you navigate your character.
        If you enter an instruction that moves you outside the bounds
        of the level you will lose a life and have to restart the level
        from the beginning.\n
        After each level there is a multiplication question that you must
        complete in order to progress to the next level.
        Correct answers will result in BONUS POINTS.
        Incorrect answers will result in lost lives!\n
        Remember to enter your characters movements in the form:
        DIRECTION,STEPS (U=up, D=down, L=left, R=right). Steps must be 1-9.
        E.G an entry of U,2 will move your character UP by 2 steps.
        """
        )
