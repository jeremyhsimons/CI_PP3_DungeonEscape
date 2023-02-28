import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('dungeon-escape-sheet')
USERS = SHEET.worksheet('users')
FEEDBACK = SHEET.worksheet('feedback')


def get_logins():
    """
    Gets the data from the users spreadsheet and adds them to a list of lists.
    """
    user_data = USERS.get_all_records()
    return user_data


def update_sheet(data, worksheet):
    """
    Updates the sheet with new user data or feedback data depending on
    parameters given. Code originally from CI love sandwiches project.
    See Readme for link.
    """
    print(f"Adding {worksheet} data...")
    sheet_to_update = SHEET.worksheet(worksheet)
    sheet_to_update.append_row(data)
    print(f"{worksheet} data updated successfully!")


get_logins()