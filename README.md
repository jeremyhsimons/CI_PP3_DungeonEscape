# **Dungeon Escape**
Developed by Jeremy Simons

<img src="docs/amiresponsivepp3.png" alt="A screenshot of Am I Responsive representation of the website">

[Link to live site](https://dungeonescape.herokuapp.com/)

## Introduction
Dungeon escape is a maze-solving game which also tests the user's multiplication skills. The objective of the game is to complete all 10 levels (mazes) without making more than 2 mistakes, in order to escape the dungeon!. 

After each level, the user must answer a multiplication question to progress to the next round. Any wrong move or incorrect answer will cost the user a life!

If the user loses all three lives, the game will be over and they will have to start from the beginning.

Users can sign up and complete the game, trying to get the highest score possible which is recorded in a google spreadsheet. This allows potential groups of users to play the game on their own devices and compete to see who gets the highest score.

## Contents
* [Project Goals](#project-goals)<br>
    * [For the user](#for-the-user)
    * [For the site owner](#for-the-site-owner)
* [User Experience](#user-experience)<br>
    * [Target audience](#target-audience)
    * [User requirements](#user-requirements)
    * [User Manual](#user-manual)
    * [User Stories](#user-stories)
* [Technical Design](#technical-design)
    * [Data Models](#data-models)
    * [Flowchart](#flowchart)
* [Features](#features)
    * [App Features](#app-features)
    * [Feature Ideas for future development](#feature-ideas-for-future-development)
* [Technologies Used](#technologies-used)
* [Deployment & Local Development](#deployment--local-development)
* [Testing](#testing)
    * [Validation](#validation)
    * [Manual Testing](#manual-testing)
    * [Automated Testing](#automated-testing)
    * [Bugs](#bugs)
* [Credits](#credits)

## Project Goals

### ...For the user
* Play a maze puzzle game and see how many points are earned
* To understand the instructions/how to play
* To sign up with a new account.
* Log back in to an existing account.

### ...For the site owner
* To provide users with all instructions on how to play the game.
* To make sure any user errors are handled and communicated back to the user.
* To receive feedback from the user about the game.

## User Experience

### Target audience
There are no specific users for the site, but the game would suit young users who are learning their times tables in school and need to practise them.

The game would also suit older users who want to refresh their mental arithmetic skills.

### User requirements
* A game that is understandable and works as expected.
* Log-in works as expected and incorrect details do not allow the user access to their account.
* User can quit the game when they want.
* Game score is communicated clearly back to the user.

### User Manual
Click the dropdown to view the user manual:
<details>
<summary>User Manual</summary>

### Log in
When the program starts, the user will be prompted to:
* Enter their existing login
* Sign up for a new account
This choice is navigated by pressing y or n on the keyboard and pressing enter to submit.

The user will then type in their details. The program will reject any incorrect or invalid details and the user will have to try again.

### Main menu
The user will be prompted to enter a player name, and will then be directed to the main menu.
There are 3 options in the menu:
1. Read game instructions
2. Start game
3. Quit game
The user must type i, s, or x and press enter to select one of these options.

### Reading instructions
If i is selected at the main menu, a screen detailing game instructions will appear.
The user can press enter to return to the main menu.

### Quitting the game
If x is selected in the main menu (or at any time during the levels):
* User will be asked if they're sure they want to quit (type y or n, press enter)
* User prompted for feedback (type y or n, press enter)
* User thanked for playing and reminded how to restart the game.

### Playing the game
Once the game is started, the user must complete 10 levels, and successfully answer maths questions between each level. If the user makes 3 mistakes, the game ends and the user must restart or quit.

#### Level navigation
The player must move the character (represented by the letter 'A') to the exit of each level/maze.

In order to navigate through levels of the dungeon, the user must type their moves in the format:
DIRECTION,STEPS where:
* DIRECTION is U, D, L, R (up, down, left, right)
* STEPS is a whole number between 1 and 9
#### Examples
* Entering U,3 in the terminal would move the character up by 3 steps.
* Entering R,1 in the terminal would move the character right by 1 step.

#### Beware
* If the user navigates into a level wall, the character will lose 1 life.
* If the user tries to navigate out of bounds (i.e. enters a number that would move the character outside the level), the character will lose 1 life AND the level will be reset!
* If the user completes a level, but fails to answer the subsequent maths question correctly, the character will lose 1 life and the player will miss out on bonus points. 

### Completing the game
On successful completion of the tenth level, the player will receive their overall score. This score will be saved to the user's account as the most recent score, and it will overwrite any previous score that the user has already attained.
</details><br>

### User Stories
#### As a first time user...
(1) Sign up with a username and for the game.

(2) Have instructions on how to play the game before starting.

(3) To have a visual representation of the dungeon where my in-game character is trapped.

(4) For inputs (whether text or numerical) to work as expected and any erroneous inputs to be flagged by the program.

(5) For the program to give me feedback when I answer game questions correctly or incorrectly.

(6) To receive a score at the end of the game that gets saved by the program in case the user returns to the game to play again.

#### As a returning user... 
(7) Be able to log in with my username and password to beat previous scores.

(8) To skip the instructions because the user is already familiar with them.

(9) Play a game that is not exactly identical to the last time it was played, e.g. questions and dungeon rooms are randomly generated.

(10) To send feedback to the site owner about the game.

#### As the site owner...
(11) Ensure that all data entered by the user is validated so as not to break the program/create bad user experience.

(12) Ensure that all user actions are given feedback in the terminal so that users feel they know what to do next in the game.

(13) To test users’ ability to solve simple arithmetic problems.

(14) To get feedback from the users about how they found the game when they finish the game (either due to failing or completing).

## Technical Design

### Flowchart

A flowchart was created using [Lucidchart](https://lucid.app/) to visualise the logic flow of the game.

<details>
    <summary>Flowchart</summary>
    <p>Dungeon Escape game logic:</p>
    <img src="docs/technical-design/flowchart.png" alt="A screenshot of the flowchart of game logic">
</details><br>

### Data Models

* Two Classes were used to represent each **level** and each new **player**.
    * This allowed attributes to be preset as and when they were needed, such as level design data.
* Dictionaries were used to store user data.
    * This helped to verify user input when signing up to the game as the dictionary of players could be iterated through to prevent usernames getting duplicated.
* Nested Lists were used to represent the levels, as well as groups of data that are returned to functions. 
    * This data model worked best because the level could be sliced/changed/iterated through at multiple levels of abstraction.
* The Google Sheets API was used for user data and user feedback submissions.
    * This allows user data to persist beyond their browser session and allows the site owner to view any user feedback so that changes/improvements can be made to the game.

## Features
The website has a single page with several features within the mock python terminal. These features are listed below.

### App Features:

<details>
    <summary>Game Title</summary>
    <p>This is what the user sees upon loading the site. The title text appears with a simple animation for visual appeal. There is also a login/signup feature here.</p>
    <ul>
        <li>
            <p>Sign up y/n options</p>
        </li>
        <li>
            <img src="docs/features/signup.png" alt="A screenshot of the signup y/n feature">
        </li>
        <li>
            <p>User story covered: 1, 7</p>
        </li>
        <li>
            <p>Authentication - you cannot log in with an account that doesn't exist.</p>
        </li>
        <li>
            <img src="docs/features/authentication.png" alt="A screenshot of the login auth">
        </li>
        <li>
            <p>User story covered: 4, 11, 12</p>
        </li>
        <li>
            <p>Validation - cannot sign up with invalid user data</p>
        </li>
        <li>
            <img src="docs/features/signup-valid.png" alt="A screenshot of the login auth">
        </li>
        <li>
            <p>User story covered: 4, 11, 12</p>
        </li>
    </ul>
</details><br>

<details>
    <summary>Menu</summary>
    <p>This is what the user sees upon loggin in successfully.</p>
    <ul>
        <li>
            <p>Menu options, allowing the player to play straight away, view instructions, or quit.</p>
            <p>The menu also prompts the player to provide a character name that will be used throughout the game.</p>
        </li>
        <li>
            <img src="docs/features/gamemenu.png" alt="A screenshot of the game menu">
        </li>
        <li>
            <p>User story covered: 2, 8</p>
        </li>
        <li>
            <p>Instructions for the player.</p>
        </li>
        <li>
            <img src="docs/features/instructions.png" alt="A screenshot of instructions">
        </li>
        <li>
            <p>User stories covered: 2, 8</p>
        </li>
        <li>
            <p>Quit option for the player - prompts the user to leave a feedback message (subject to validation) for the developer.</p>
        </li>
        <li>
            <img src="docs/features/feedback.png" alt="A screenshot of quit menu">
        </li>
        <li>
            <p>User stories covered: 10, 14</p>
        </li>
    </ul>
</details><br>

<details>
    <summary>Maze Level</summary>
    <p>This is what the user sees upon starting the game or reaching a new level.</p>
    <ul>
        <li>
            <p>A layout of the maze level represented in ASCII characters</p>
            <p>The order of the levels is randomised for each game session. The level is reset to this default layout if the user navigates out of bounds at any point during the level.</p>
        </li>
        <li>
            <img src="docs/features/level-view.png" alt="A screenshot of a level">
        </li>
        <li>
            <p>User story covered: 3, 9, 5, 12</p>
        </li>
        <li>
            <p>If a player makes an invalid entry, they are notified. If they make a valid entry that is a mistake, they lose 1 life.</p>
        </li>
        <li>
            <img src="docs/features/level-invalid.png" alt="A screenshot of invalid entry.">
            <img src="docs/features/level-incorrect.png" alt="A screenshot of incorrect entry.">
        </li>
        <li>
            <p>User stories covered: 5, 11</p>
        </li>
</details><br>

<details>
    <summary>Maths Challenge</summary>
    <p>This is what the user sees upon completing a level and before starting the next level.</p>
    <ul>
        <li>
            <p>A randomly generated multiplication question with 2 integers between 5 and 20.</p>
            <p>A Wrong answer leads to a loss of 1 life. A correct answer gains +20 bonus points.</p>
        <li>
            <img src="docs/features/maths-challenge.png" alt="A screenshot of a maths question">
        </li>
        <li>
            <p>User story covered: 5, 9, 13</p>
        </li>
    </ul>
</details><br>

<details>
    <summary>End of Game</summary>
    <p>This is what the user sees upon completing a level and before starting the next level.</p>
    <ul>
        <li>
            <p>User is told how many points they get, and points are updated to google sheet.</p>
        <li>
            <img src="docs/features/end-game.png" alt="A screenshot of the end game screen">
        </li>
        <li>
            <p>User story covered: 6</p>
        </li>
    </ul>
</details><br>

### Feature ideas for future development
In future the website could be further developed and improved to offer more
game rules and greater complexity in the levels. Some ideas include:
* A counter to measure how many moves it takes the user to complete each level and reward them for passing the level in the fewest steps possible.
* Add other symbols in the levels that trigger different events for extra (optional) bonus points. This would reward players who take greater risks in extending the amount of time navigating and potentially losing lives.
* Alter the score saving system so that the user's score is only saved if it is higher than the one stored in the spreadsheet.
## Technologies Used
### Languages used
Python

### Other tools/websites/libraries used
* [Lucidchart](https://lucid.app/) was used to create wireframes.
* [Git](https://git-scm.com/) was used for version control.
* [GitHub](https://github.com/) was used for saving and storing files.
* [GitPod](https://gitpod.io/) was the IDE used for writing and editing code.
* [Heroku](https://id.heroku.com/) was used as the hosting platform for this site.
* [Ascii art generator](http://patorjk.com/software/taag/#p=display&f=Varsity&t=Dungeon%0AEscape) was used to generate title text. Varsity font was used.
* [amiresponsive](https://ui.dev/amiresponsive?url=https://jeremyhsimons.github.io/CI_PP2_SavvySaver/) was used to test the website across different screens and generate the picture in the [Design](#design) section.

#### 3rd party Python Libraries used
* [Gspread / Google Sheets API](https://github.com/burnash/gspread) was used to handle getting/sending data to the google sheet used in the project. This is also not a standard feature of python, so it was necessary to install it for the purposes of this project.
* [Google OAuth 2.0](https://google-auth.readthedocs.io/en/stable/reference/google.oauth2.credentials.html) was used to set up the connection between the project and the developers personal google account. This was necessary because access to a google account via a program is restricted for security reasons.
* [Colorama](https://pypi.org/project/colorama/) was used to add colour to the game for increased visual appeal. It was necessary to install this dependency since python does not have this feature as standard.


## Deployment & Local Development
The website was deployed to [Heroku](https://id.heroku.com/) using the following process:
1. Login or create an account at [Heroku](https://dashboard.heroku.com/)
<img src="docs/heroku/heroku1.png">
1. Click on New > Create new app in the top right of the screen.
<img src="docs/heroku/heroku2.png">
1. Add an app name and select location, then click 'create app'.
<img src="docs/heroku/heroku3.png">
1. Under the deploy tab of the next page, select connect to GitHub.
1. Log in to your GitHub account when prompted.
<img src="docs/heroku/heroku4.png">
1. Select the repository that you want to be connected to the Heroku app.
<img src="docs/heroku/heroku5.png">
1. Click on the settings tab.
<img src="docs/heroku/heroku6.png">
1. Scroll down to the config vars section, and add 2 config vars:
    * The first key is CREDS and the value here is the creds.json file that was generated for the google sheets API to work properly.
    * The second key is PORT and the Value is 8000
<img src="docs/heroku/heroku7.png">
1. Once you have set up the config vars, scroll down to buildpacks (still under the settings tab)
1. Add the Python and Node.js buildpacks to your app and make sure that when they are displayed, they appear in the order:
    * Python
    * Node.JS
<img src="docs/heroku/heroku8.png">
1. Navigate back to the settings tab.
1. Select automatic deploys to allow Heroku to build the site with new changes each time changes are pushed to GitHub.
<img src="docs/heroku/heroku9.png">
1. In the 'manual deploy' section beneath this, make sure the branch selected is 'main' and click deploy branch.
<img src="docs/heroku/heroku10.png">
1. The site should now be built and Heroku should provide a url for the built site.

This repository can be forked using the following process:
1. On the repository's page, go to the top-right of the page underneath the dark ribbon.
1. Click on the fork button
1. You can now work on a fork of this project. 

This repository can be cloned using the following process:
1. Go to this repository's page on GitHub.
1. Click on the code button (not the one in the navbar, but the one right above the file list).
1. Select an option, HTTPS, SSH, GitHub CLI.
1. Copy the url below to your clipboard.
1. Open Git Bash/your IDE terminal.
1. Ensure the directory you are working in is the correct one you want to paste the project into.
1. Type the command '$ git clone'
1. Paste the URL of the repository after this.
1. Hit enter on your keyboard and the project will be cloned.
 
## Testing
### Debugging
The site was tested using the following browsers: 
* Google Chrome
* Mozilla Firefox
* Microsoft Edge

The site was tested on the following devices:
* Lenovo Ideapad 520S (Windows 10)
* Huawei PSmart 2019 (EMUI version 12.0.0)

### Validation
#### PEP8 Python Validator (from Code Institute)
Code institute's own Python Linter [pep8](https://pep8ci.herokuapp.com/) was used to validate all Python code in this project.

All code passed with no errors apart from the run.py file where the line limit of 80 characters had to be exceeded to display the title. These were the only errors that were found in this file.

<details>
<summary>instructions.py</summary>
<img src="docs/validation/instructions-v.png" alt="A screenshot of pep8 validator confirming instructions code.">
</details>

<details>
<summary>run_game.py</summary>
<img src="docs/validation/run_game-v" alt="A screenshot of pep8 validator confirming game code.">
</details>

<details>
<summary>run.py</summary>
<img src="docs/validation/run-v.png" alt="A screenshot of pep8 validator confirming main program code.">
</details>

<details>
<summary>sheet_data.py</summary>
<img src="docs/validation/sheet_data-v.png" alt="A screenshot of pep8 validator confirming sheet API code.">
</details>

<details>
<summary>test_validation.py</summary>
<img src="docs/validation/test_validation-v.png" alt="A screenshot of pep8 validator confirming testing code.">
</details>

<details>
<summary>validation.py</summary>
<img src="docs/validation/validation-v.png" alt="A screenshot of pep8 validator confirming validation code.">
</details>
<br>

### Manual Testing

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 1. Sign up as a new player | Sign-up prompt | When prompted by the opening view of the game, answer 'n', enter new details and type 'enter' | Program accepts/signs user up. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/manualtest/us1-1.png" alt="A screenshot of the sign up prompt."><br>
    <img src="docs/manualtest/us1-2.png" alt="A screenshot of the sign up prompt."><br>
    <img src="docs/manualtest/us1-3.png" alt="A screenshot of the new users details."><br>
    <img src="docs/manualtest/us1-4.png" alt="A screenshot of the success notification."><br>
    <img src="docs/manualtest/us1-5.png" alt="A screenshot of the new user stored in google sheets."><br>
</details><br>

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 2. Instructions before starting game. | Main menu | When in the main menu, enter 'i' to access instructions. | Program displays instructions and a way to get back to the menu. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/manualtest/us2-1.png" alt="A screenshot of the main menu."><br>
    <img src="docs/manualtest/us2-2.png" alt="A screenshot of the instructions."><br>
</details><br>

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 3. Visual representation of the game | Level view | When user starts the game, a view of the level appears clearly. | Program displays level, which is updated with each successful move the player makes | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="readme-docs/testing-user-stories/us3-1.png" alt="A screenshot of the main menu with s selected."><br>
    <img src="readme-docs/testing-user-stories/us3-2.png" alt="A screenshot of a new game"><br>
</details><br>

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 4. Erroneous data entry to be caught by the program. | Sign up prompt | When at the starting view, enter a response that is not y or n. | Program flags this as an incorrect response. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/manualtest/us4-1.png" alt="A screenshot of the sign up prompt with invalid entry."><br>
    <img src="docs/manualtest/us4-2.png" alt="A screenshot of the error message."><br>
</details><br>

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 5. Player mistakes/wrong answers to receive feedback.| Maths question | When presented with a maths question, deliberately enter the wrong answer. | Program flags this as an incorrect answer and tells the user that they have lost a life. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/manualtest/us5.png" alt="A screenshot of a maths question with wrong answer and program's feedback."><br>
</details><br>

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 6. Receive a score at the end of the game.| End game view | Complete the game | Program notifies user of their score and saves it to the google sheet. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/manualtest/us6.png" alt="A screenshot of the end game page."><br>
</details><br>

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 7. Log into existing account. | Sign up prompt | When prompted, answer yes to existing account and log in with existing details | Program checks user and lets them access the game menu. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/manualtest/us7-1.png" alt="A screenshot of existing user logging in."><br>
    <img src="docs/manualtest/us7-2.png" alt="A screenshot of welcome message"><br>
</details><br>

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 8. Skip instructions. | Main menu | When in main menu, enter 's' to start the game immediately | Program loads the game when this response is submitted. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/manualtest/us8-1.png" alt="A screenshot of the main menu"><br>
    <img src="docs/manualtest/us8-2.png" alt="A screenshot of a new game."><br>
</details><br>

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 9. Play a different game than before. | Level view | Start the game and complete a few levels. | Program has re-organised levels into a different order than before, and maths questions are different. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/manualtest/us9-1.png" alt="A screenshot of a new level 1."><br>
    <img src="docs/manualtest/us9-2.png" alt="A screenshot of a different randomised level 1."><br>
</details><br>

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
|10. Send feedback. | Quit screen | When prompted, answer yes to giving feedback and type a message. Then press enter to submit. | Program sends message to the google sheet. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/manualtest/us10-1.png" alt="A screenshot of a new feedback message from user."><br>
    <img src="docs/manualtest/us10-2.png" alt="A screenshot of program's response."><br>
    <img src="docs/manualtest/us10-3.png" alt="A screenshot of the feedback saved in google sheets."><br>
</details><br>

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 11. (Site owner) Ensure data is validated. | Sign up prompt | Same test as user story 4. See details above. | Same test as user story 4. See details above.  | Same test as user story 4. See details above. |


|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 12. (Site owner) Ensure user actions are given feedback. | Maths question | Same test as user story 5. See details above. | Same test as user story 5. See details above.  | Same test as user story 5. See details above. |


|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 13. (Site owner) Test user's arithmetic ability. | Maths question | Complete a level in the game | To be presented with a multiplication question with 2 random numbers between 5 and 20. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/manualtest/us13-1.png" alt="A screenshot of level 1 being completed"><br>
    <img src="docs/manualtest/us13-2.png" alt="A screenshot of level complete screen."><br>
    <img src="docs/manualtest/us13-3.png" alt="A screenshot of a new maths question after level complete."><br>
</details><br>

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 14. (Site owner) To get feedback from users. | Quit screen | Same test as user story 10. See details above. | Same test as user story 10. See details above.  | Same test as user story 10. See details above. |


### Automated Testing
Seven unit tests were written for this project. The test check that the validation functions (used to check user inputs) return the expected results.

Most tests originally failed because error handling to catch invalid data types had not been included. Once this had been addressed, all tests passed OK.

For each unit test, the assertions test:
* Valid data
* Invalid data and edge cases.

<details>
    <summary>Screenshots</summary>
    <p>All tests passed OK.</p>
    <img src="docs/unittests/tests-passed.png" alt="A screenshot of the Gitpod terminal stating that all tests have passed.">
    <p>1. Test validate_yes_no</p>
    <img src="docs/unittests/test1.png" alt="A screenshot of the first test">
    <p>2. Test validate_details</p>
    <img src="docs/unittests/test2.png" alt="A screenshot of the second test">
    <p>3. Test validate_main_menu</p>
    <img src="docs/unittests/test3.png" alt="A screenshot of the third test">
    <p>4. Test validate_math</p>
    <img src="docs/unittests/test4.png" alt="A screenshot of the fourth test">
    <p>5. Test validate_navigation</p>
    <img src="docs/unittests/test5.png" alt="A screenshot of the fifth test">
    <p>6. Test validate_string</p>
    <img src="docs/unittests/test6.png" alt="A screenshot of the sixth test">
    <p>7. Test validate_message</p>
    <p>This test originally failed because checks for empty strings or spaces had been omitted. Once this had been added to the validation function, the test passed.</p>
    <img src="docs/unittests/test7.png" alt="A screenshot of the seventh test">
</details><br>

### Bugs

| Bug Description  | Action Taken to Fix  |
|---|---|
|The user could sign up with empty username/password fields | I added condition to the validation function that catches empty strings. |
| Submitting user’s feedback would throw an error in the terminal | I had forgotten to format the feedback data as a list, and I was trying to update the sheet with a string. Making a single element list out of the feedback before sending it to the update function fixed the issue. |
| Index error each time the levels were generated. | The list used to randomly order layouts was numbered 1-10 where layouts are indexed 0-9. Changing random order list to integers between 0 and 9 fixed this. |
| When player makes a mistake and navigates into a wall, the notification gets printed twice to the terminal. | Change each check direction function so that it only calls the check route function once. |
| When player makes invalid menu choice, “start” selection doesn’t work on second try and script stops. | I put the menu in a while loop rather than re-calling the function with the same parameters in an if-else statement. |
| When player moved out of bounds, the level would not reset to the original layout, and the updated level with all progress so far was re-printed to the terminal. | A separate reset function was created to loop through the level elements and reset the “A” character to the start. |
| If player selected “no” to whether they wanted to quit, the game still quit. | I added the missing if else statement that I’d forgotten to include to handle that choice. |

## Credits

### 3rd party code used

#### 3rd party Python libraries/modules
* [Gspread / Google Sheets API](https://github.com/burnash/gspread) was used to handle getting/sending data to the google sheet used in the project.
* [Google OAuth 2.0](https://google-auth.readthedocs.io/en/stable/reference/google.oauth2.credentials.html) was used to set up the connection between the project and the developers personal google account.
* [Colorama](https://pypi.org/project/colorama/) was used to add colour to the game for increased visual appeal.
* [Ascii art generator](http://patorjk.com/software/taag/#p=display&f=Varsity&t=Dungeon%0AEscape) was used to generate title text. Varsity font was used.

#### Code found online when solving bugs in own code.
* How to clear screen in python: [www.scaler.com](https://www.scaler.com/topics/how-to-clear-screen-in-python/)

* How to create unit tests in Python [Corey Schafer](https://www.youtube.com/watch?v=6tNS--WetLI)

### Acknowledgements
* Thanks to my Mentor Mo Shami for his <strong>immensely valuable</strong> feedback, advice and encouragement throughout this project. Thanks for pushing me to do the best I can!
* Thanks to the wonderful CI London Community for all the moral support!
* Thanks to my friends: Thommy, Lars, Matt, Nesu, Nathan, Rob, and Oli for testing the game and for their feedback.
