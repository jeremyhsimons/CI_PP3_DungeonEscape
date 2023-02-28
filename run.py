from sheet_data import get_logins


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


login()
