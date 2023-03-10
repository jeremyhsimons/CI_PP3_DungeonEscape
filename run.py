from time import sleep

from sheet_data import get_logins
from sheet_data import update_sheet
from sheet_data import update_user_score

from validation import validate_yes_no
from validation import validate_details
from validation import validate_message

from run_game import start_game
from run_game import clear_screen

from colorama import init
from colorama import Fore

init(autoreset=True)

CURRENT_USER = {
    'name': "Jeremy",
    'score': 0
    }
NEW_SECTION = "-"*30


def welcome():
    """
    Displays a welcome message to the user when they load the game.
    """
    print('\nwelcome to...')
    sleep(0.2)
    print(Fore.RED + " ______                                                     ")
    sleep(0.2)
    print(Fore.RED + "|_   _ `.                                                   ")
    sleep(0.2)
    print(Fore.MAGENTA + "  | | `. \ __   _   _ .--.   .--./) .---.   .--.   _ .--.   ")
    sleep(0.2)
    print(Fore.MAGENTA + "  | |  | |[  | | | [ `.-. | / /'`\;/ /__\\/ .'`\ \ [ `.-. |  ")
    sleep(0.2)
    print(Fore.MAGENTA + " _| |_.' / | \_/ |, | | | | \ \._//| \__.,| \__. | | | | |  ")
    sleep(0.2)
    print(Fore.RED + "|______.'  '.__.'_/[___||__].',__`  '.__.' '.__.' [___||__] ")
    sleep(0.2)
    print(Fore.RED + " ________                  ( ( __))            _            ")
    sleep(0.2)
    print(Fore.RED + "|_   __  |                                    | |           ")
    sleep(0.2)
    print(Fore.RED + "  | |_ \_| .--.   .---.  ,--.  _ .--.   .---. | |           ")
    sleep(0.2)
    print(Fore.MAGENTA + "  |  _| _ ( (`\] / /'`\]`'_\ :[ '/'`\ \/ /__\\ | |           ")
    sleep(0.2)
    print(Fore.MAGENTA + " _| |__/ | `'.'. | \__. // | |,| \__/ || \__.,|_|           ")
    sleep(0.2)
    print(Fore.RED + "|________|[\__) )'.___.'\'-;__/ | ;.__/  '.__.'(_)           ")
    sleep(0.2)
    print(Fore.RED + "                              [__|                          ")
    sleep(0.2)
    print(f"\n{NEW_SECTION}")
    sleep(0.2)


def signup():
    """
     Checks whether the user has signed up already.
     If not, it will add their new user data to the sheet.
     If they have, it will call the login function.
    """
    print("\nDo you already have an account? Y/N")
    sign_up_check = input("\n If yes, press 'y'. if no, press 'n': \n")
    signup_validation = validate_yes_no(sign_up_check)
    if signup_validation:
        if sign_up_check == 'y':
            return True
        elif sign_up_check == 'n':
            return False
    else:
        return signup()


def add_user():
    """
    Takes new username and password input from user and stores it
    in google sheet if it passes validation.
    """
    print("\nPlease choose a valid username and password.\n")
    print('Make sure you remember the username and password you choose.')
    print('You will need them to log back in and see your score!')
    new_uname = input('\n New username: \n')
    new_pword = input(' New password: \n')
    check_details = validate_details(new_uname, new_pword)
    if check_details:
        new_user = [new_uname, new_pword, 0]
        update_sheet(new_user, 'users')
    else:
        add_user()


def login():
    """
    Calls get_logins function and checks if the user's
    inputs match a valid username/password.
    """
    logins = get_logins()
    print('Please enter your username and password')
    uname = input('\n Username: \n')
    pword = input(' Password: \n')
    logins_checked = 0
    for i in logins:
        if uname == i['Username']:
            if pword == i['Password']:
                print('login successful! Welcome!')
                CURRENT_USER['score'] = i["Latest Score"]
                CURRENT_USER['name'] = i['Username']
                sleep(1)
                clear_screen()
                sleep(0.2)
                print(NEW_SECTION)
                sleep(0.2)
            else:
                print('Incorrect password. Please try again.\n')
                login()
        else:
            logins_checked += 1
    if logins_checked == len(logins):
        print('Sorry, this user does not exist. Please try again.\n')
        login()


def end_game_menu(data):
    """
    Informs the user that the game is over,
    saves their score to their account,
    gives them the choice to quit or try again.
    """
    clear_screen()
    sleep(0.5)
    print("Congratulations! You escaped the dungeon!")
    sleep(0.5)
    print(f"You scored {data[0]} points in total!")
    sleep(0.5)
    print("Your score will be saved as your account's most recent score.")
    sleep(1)
    CURRENT_USER['score'] = data[0]
    update_user_score(CURRENT_USER)
    sleep(2)
    print("Score saved successfully!")
    sleep(0.2)
    print("Would you like to quit?")
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
                    else:
                        print("Quitting game for security reasons")
                        sleep(0.5)
                        print("Thanks for playing! See you next time!")
                        print(NEW_SECTION)
                        print("Click 'Run Program' to begin!")
                else:
                    print("Thanks for playing! See you next time!")
                    print(NEW_SECTION)
                    print("Click 'Run Program' to begin!")
            else:
                return end_game_menu(data)
        elif quit_yes_no == "n":
            print("Restarting Game...")
            sleep(1)
            return start_game()
    else:
        return end_game_menu(data)


def main():
    """
    The function which controls the calling of all other functions in the file.
    """
    welcome()
    if signup():
        login()
    else:
        add_user()
        login()
    game_result = start_game()
    if not game_result:
        sleep(0.2)
        print("\n")
    else:
        sleep(2)
        print(game_result)
        end_game_menu(game_result)


# main()

end_game_menu([300, 2])
