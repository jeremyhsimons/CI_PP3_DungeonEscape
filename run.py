from sheet_data import get_logins
from sheet_data import update_sheet


def signup():
    """
     Checks whether the user has signed up already.
     If not, it will add their new user data to the sheet.
     If they have, it will call the login function.
    """
    print("Do you already have an account? Y/N")
    sign_up_check = input("\n If yes, press 'y'. if no, press 'n'")
    if sign_up_check == 'y':
        login()
    elif sign_up_check == 'n':
        print("Please enter a valid username and password\n")
        print("Choose a username that you would like your in-game")
        print("character to have.\n")
        print('Make sure you remember the password you choose!')
        print('You will need it to log back in and see your score!')
        new_uname = input('\n New username')
        new_pword = input('\n New password')
        new_user = [new_uname, new_pword, 0]
        update_sheet(new_user, 'users')


def login():
    """
    Calls get_logins function and checks if the user's
    inputs match a valid username/password.
    """
    logins = get_logins()
    print('Please enter your username and password')
    uname = input('\n Username: ')
    pword = input('\n Password: ')
    logins_checked = 0
    for i in logins:
        if uname == i['Username']:
            print('\nValid user.')
            if pword == i['Password']:
                print('login successful! Welcome!')
            else:
                print('Incorrect password. Please try again.\n')
                login()
        else:
            logins_checked += 1
    if logins_checked == len(logins):
        print('Sorry, this user does not exist. Please try again.\n')
        login()


signup()
