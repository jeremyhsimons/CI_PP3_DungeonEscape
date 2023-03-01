# Code to demonstrate how to make a game board/map using a list of lists.
big_list = [
    ['1', '2', '3', '4', '5'], ['1', '.', '3', '4', '5'],
    ['1', '2', '3', '4', '5']
    ]

for i in big_list:
    x = " ".join(i)
    print(x)


class Player:
    """
    A class that defines the common features of users/players
    in-game characters.
    """
    def __init__(self, name, lives, points, keys):
        self.name = name
        self.lives = lives
        self.points = points
        self.keys = keys


class Door:
    """
    A class that defines the common features of different
    doors that the player may come across in the game.
    """
    def __init__(self, status, type, position):
        self.status = status
        self.type = type
        self.position = position


class Room:
    """
    A class that defines the common features of different
    rooms that a player might discover in the game.
    """
    def __init__(self, doors, special_event):
        self.doors = doors
        self.special_event = special_event
