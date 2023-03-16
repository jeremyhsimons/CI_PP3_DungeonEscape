# Imports
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sheet_data import get_logins
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def validate_yes_no(data):
    """
    Checks whether the user has input a valid yes or no response
    to a y/n question in the game.
    """
    try:
        if not isinstance(data, str):
            raise TypeError(
                "You must enter your response in string format"
            )
    except TypeError as d:
        print(f"Invalid response: {d}")
        return False
    try:
        if not (data.lower() == "y" or data.lower() == "n"):
            raise ValueError(
                f"Please answer yes or no (y or n). You answered '{data}'."
                )
    except ValueError as e:
        print(f"\nInvalid response: {e}")
        return False
    else:
        return True


def validate_details(value1, value2):
    """
    Checks whether the data that new users enter for their
    username and password is valid, and checks whether the username
    already exists.
    value1 is the username.
    value2 is the password.
    """
    try:
        if value1 == " " or value2 == " " or value1 == "" or value2 == "":
            raise ValueError(
                "You cannot submit an empty field as your username/password."
            )
    except ValueError as e:
        print(f"\nInvalid data: {e}")
        return False
    try:
        existing_users = get_logins()
        for i in existing_users:
            if i['Username'] == value1:
                raise ValueError(
                    "This username already exists."
                )
    except ValueError as f:
        print(f"\nInvalid username: {f}")
        return False
    try:
        if not (isinstance(value1, str) or isinstance(value2, str)):
            raise TypeError(
                "Please enter your details in a string format."
            )
    except TypeError as r:
        print(f"\nInvalid user data: {r}")
        return False
    else:
        print('New user confirmed...')
        return True


def validate_main_menu(data):
    """
    Checks whether the user's input for the main menu
    when accessing the game is valid."
    """
    try:
        if not (data == "i" or data == "s" or data == "x"):
            raise ValueError(
                f"Please select i, s or x. You selected {data}"
            )
    except ValueError as g:
        print(f"\nInvalid selection: {g}")
        return False
    else:
        return True


def validate_math(data):
    """
    Checks if the user's input for a math question is an integer.
    """
    try:
        if not isinstance(data, str):
            raise TypeError(
                "Please enter your answer in a string format."
            )
    except TypeError as t:
        print(f"\nInvalid Answer: {t}")
        return False
    try:
        if not data.isdigit():
            raise ValueError(
                f"Please enter a valid number. You entered {data}"
            )
    except ValueError as h:
        print(f"\nInvalid Answer: {h}")
        return False
    else:
        return True


def validate_navigation(data):
    """
    Checks if the user's input for moving around the level
    matches what is expected.
    """
    try:
        if not isinstance(data, str):
            raise TypeError(
                "Please enter your move in string format."
            )
    except TypeError as u:
        print(f"\nInvalid move: {u}")
        return False
    try:
        if "," not in data:
            raise ValueError(
                 "Please separate the direction and steps with ','"
            )
    except ValueError as k:
        print(f"\nInvalid entry: {k}")
        return False

    nav_input = data.split(",")
    try:
        if not (
            nav_input[0] == "L"
            or nav_input[0] == "R"
            or nav_input[0] == "U"
            or nav_input[0] == "D"
        ):
            raise ValueError(
                "Please enter L,R,U or D as your direction."
            )
    except ValueError as i:
        print(f"\nInvalid direction: {i}")
        return False
    try:
        if not nav_input[1].isdigit():
            raise ValueError(
                "Please enter a number between 1 and 9 for the steps value."
            )
    except ValueError as x:
        print(f"\nInvalid steps: {x}")
        return False
    try:
        if int(nav_input[1]) > 9:
            raise ValueError(
                "You cannot travel more than 9 steps at a time."
            )
    except ValueError as j:
        print(f"\nInvalid steps: {j}")
        return False
    else:
        return True


def validate_string(data):
    """
    Checks that the player has not entered an empty string
    in an input.
    """
    try:
        if data == "" or data == " ":
            raise ValueError(
                "You cannot have an entry that is empty/only spaces."
            )
    except ValueError as m:
        print(f"\nInvalid entry: {m}")
        return False
    try:
        if isinstance(data, int):
            raise TypeError(
                "You cannot enter a number in this field."
            )
    except TypeError as o:
        print(f"\nInvalid entry: {o}")
        return False
    try:
        if isinstance(data, bool):
            raise TypeError(
                "You cannot enter a Boolean in this field"
            )
    except TypeError as p:
        print(f"\nInvalid entry: {p}")
        return False
    else:
        return True


def validate_message(data):
    """
    Checks that the user is not adding an overly long message.
    Reduces the chance of abuse of the database (google sheet).
    """
    try:
        if not isinstance(data, str):
            raise TypeError(
                "You must enter your message in string format."
            )
    except TypeError as v:
        print(f"\nInvalid entry: {v}")
        return False
    try:
        if data == "" or data == " ":
            raise ValueError(
                "You cannot submit an empty field or only spaces."
            )
    except ValueError as q:
        print(f"\nInvalid entry: {q}")
        return False
    try:
        if len(data) > 80:
            raise ValueError(
                "You cannot have a feedback message longer than 80 characters."
            )
    except ValueError as n:
        print(f"\nInvalid entry: {n}")
        return False
    else:
        return True
