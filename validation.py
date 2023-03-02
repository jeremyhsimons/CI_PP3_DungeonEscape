from sheet_data import get_logins


def validate_yes_no(data):
    """
    Checks whether the user has input a valid yes or no response
    to a y/n question in the game.
    """
    try:
        if not (data == "y" or data == "n"):
            raise ValueError(
                f"Please answer yes or no (y or n). You answered '{data}'."
                )
    except ValueError as e:
        print(f"Invalid response: {e}")
        return False
    else:
        print('valid data')
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
        if value1 == " " or value2 == " ":
            raise ValueError(
                "You cannot submit an empty field as your username/password."
            )
    except ValueError as e:
        print(f"Invalid data: {e}")
        return False
    try:
        existing_users = get_logins()
        for i in existing_users:
            if i['Username'] == value1:
                raise ValueError(
                    "This username already exists. Please choose another."
                )
    except ValueError as f:
        print(f"Invalid username: {f}")
        return False

    print('Yay! New user!')
    return True
