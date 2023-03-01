# Code to demonstrate how to make a game board/map using a list of lists.
rooms = []


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
    def __init__(self, status, door_type, position):
        self.status = status
        self.door_type = door_type
        self.position = position


class Room:
    """
    A class that defines the common features of different
    rooms that a player might discover in the game.
    """
    def __init__(self, doors, special_event):
        self.doors = doors
        self.special_event = special_event

    def generate_new_room(self):
        """
        A method that creates a new room.
        """
        room_layout = [
            ["O", "-", "-", "-", "-", " ", "-", "-", "-", "-", "O"],
            ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
            ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
            [" ", ".", ".", ".", ".", ".", ".", ".", ".", ".", " "],
            ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
            ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
            ["O", "-", "-", "-", "-", " ", "-", "-", "-", "-", "O"]
        ]
        for j in room_layout:
            y = " ".join(j)
            print(y)


room1 = Room(1, 2)
room1.generate_new_room()

# O - - - -   - - - - O
# | . . . . . . . . . |
# | . . . . . . . . . |
#   . . . . . . . . .
# | . . . . . . . . . |
# | . . . . . . . . . |
# O - - - -   - - - - O
