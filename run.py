from time import sleep

from sheet_data import get_logins
from sheet_data import update_sheet

from validation import validate_yes_no
from validation import validate_details

from run_game import start_game
from run_game import clear_screen

from colorama import init
from colorama import Fore

init(autoreset=True)

CURRENT_USER = {
    'name': "",
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
            login()
        elif sign_up_check == 'n':
            add_user()
    else:
        signup()


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
                start_game()
            else:
                print('Incorrect password. Please try again.\n')
                login()
        else:
            logins_checked += 1
    if logins_checked == len(logins):
        print('Sorry, this user does not exist. Please try again.\n')
        login()


def main():
    """
    The function which controls the calling of all other functions in the file.
    """
    welcome()
    signup()


main()
