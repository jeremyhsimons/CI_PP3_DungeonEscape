def print_instructions():
    """
    A function that prints the game instructions to the terminal
    """
    print(
        """
        Dungeon escape is a maze game with an a couple of added twists...\n
        Your job is to navigate your character (represented by letter 'A')\n
        To the exit of each level (represented by letter 'B'.)\n\n
        But beware! The walls of each level are electrified!\n
        If you touch a wall you will lose a life.\n
        If you lose all three lives, your character will die\n
        and you will have to restart the game.\n\n
        Be careful how you navigate your character!\n
        If you enter an instruction that moves you outside the bounds\n
        of the level you will lose a life and have to restart the level\n
        from the beginning.\n\n
        After each level there is a multiplication question that you must\n
        complete in order to progress to the next level.\n
        Correct answers will result in BONUS POINTS.\n
        Incorrect answers will result in lost lives!\n\n
        Remember to enter your characters movements in the form:\n
        DIRECTION,STEPS\n
        E.G an entry of U,2 will move your character UP by 2 steps.
        """
    )


print_instructions()
