def validate_yes_no(data):
    """
    Checks whether the user has input a valid yes or no response
    to a y/n question in the game.
    """
    try:
        if data != "y":
            raise ValueError(
                f"Please answer yes or no (y or n). You answered {data}"
                )
    except ValueError as e:
        print(f"Invalid response: {e}")
        return False
    else:
        print('valid data')
        return True


validate_yes_no("y")
