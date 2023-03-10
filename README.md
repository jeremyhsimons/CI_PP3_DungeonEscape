# **Savvy Saver**
Developed by Jeremy Simons

<img src="readme-docs/design/ss-amiresponsive2.png" alt="A screenshot of Am I Responsive representation of the website">

[Link to live site](https://jeremyhsimons.github.io/CI_PP2_SavvySaver/)

## Introduction
Many young people today enter adult life having no concept of how to manage their finances wisely. They have no experience saving money for large purchases and, in Western countries, are engulfed by one of the most consumerist cultures that has ever existed. This combination of factors means that many are adopting lifestyles that are not conducive to long-term financial stability. 

Savvy Saver is a website that aims to help people like this. It offers three main features that can help young people and those wishing to learn more about saving:

1. The savings calculator: a simple-to-use webform that calculates what you will save and offers a print-out of recommendations for your finances.
2. The Quiz: a small game to test the user's knowledge of some basic principles of managing money.
3. An FAQ page which seeks to answer some questions that users might have about finances, and a contact form with working email notification to submit questions that are not addressed.

These features aims to achieve the project goals [below](#project-goals) through offering an interactive and responsive website that gives regular visual feedback and notification of what their interactions with the site achieve.

## Contents
* [Project Goals](#project-goals)<br>
    * [For the user](#for-the-user)
    * [For the site owner](#for-the-site-owner)
* [User Experience](#user-experience)<br>
    * [Target audience](#target-audience)
    * [User requirements](#user-requirements)
    * [User Stories](#user-stories)
* [Design](#design)
    * [Design Summary](#design-summary)
    * [Colour Scheme](#colour-scheme)
    * [Wireframes](#wireframes)
* [Features](#features)
    * [Feature Ideas for future development](#feature-ideas-for-future-development)
* [Technologies Used](#technologies-used)
* [Deployment & Local Development](#deployment--local-development)
* [Testing](#testing)
    * [Validation](#validation)
        * [HTML](#html)
        * [CSS](#css)
        * [JavaScript](#js)
        * [Accessibility](#accessibility)
        * [Performance](#performance)
    * [Testing user stories](#testing-user-stories)
    * [Bugs](#bugs)
* [Credits](#credits)

## Project Goals

### ...For the user
* This project will be a helpful tool in checking whether they meet their savings goal.
* This project will offer information/education about how to manage their finances/budget better.
* Where either of these things is not achieved, This project will have a way for feedback to be given to the site owner about problems/questions.

### ...For the site owner
* This project will help others who are looking to manage their money better.
* This project will answer a good proportion of the questions that the user may have about the site itself and how to use it.
* This project will showcase the site owner's development skills and direct users to their GitHub page.

## User Experience

### Target audience
Potential users of the site may include, but are not limited to:
* Young people, university students, or recent graduates who are entering the workplace.
* People who may have been in the workplace for a while, but who are looking to improve how they manage their money.
* People who are looking to save for a significant expense and want an easy way to find out how best to do it.

### User requirements
* The features of the site work as expected and any interaction provides visual or information feedback/notification.
* Users can calculate their savings.
* Users can print off their results.
* Users can send a message to site owner.
* Users can complete a quiz and keep track of their highscore while on the tab.
* Site content is accessible to users with visual impairments.
* User can access the site on multiple kinds of devices/screen widths.

### User Stories
#### As a first time user...


#### As a returning user... 


#### As the site owner...


## Technical Design

### Flowchart

A flowchart was created using [Lucidchart](https://lucid.app/) to visualise the logic flow of the game.

### Data Models

* 2 Classes were used to represent each level and each new player.
    * This allowed attributes to be preset as and when they were needed, such as level design data.
* Dictionaries were used to store user data.
    * This helped to verify user input when signing up to the game as the dictionary of players could be iterated through to prevent usernames getting duplicated.
* Nested Lists were used to represent the levels, as well as groups of data that are returned to functions. 
    * This data model worked best because the level could be sliced/changed/iterated through at multiple levels of abstraction.
* The Google Sheets API was used for user data and user feedback submissions.
    * This allows user data to persist beyond their browser session and allows the site owner to view any user feedback so that changes/improvements can be made to the game. 

<details>
    <summary>Flowchart</summary>
    <p>Dungeon Escape game logic:</p>
    <img src="" alt="">

</details>


## Features
The website has a single page with several features within the mock python terminal. These features are listed below:

<details>
    <summary>Calculator page</summary>
    <p>The calculator page is the main feature of the site and contains a form which the user fills in to check if they will meet their savings goal.</p>
    <ul>
        <li>
            <p>Calculator form.</p>
        </li>
        <li>
            <p>User story covered: 2, 7</p>
            <img src="readme-docs/features/calc-form.png" alt="A screenshot of the calculator form">
        </li>
        <li>
            <p>Results of their calculation and recommendations that are generated based on the user's inputs</p>
        </li>
        <li>
            <p>User story covered: 8</p>
            <img src="readme-docs/features/results-calc.png" alt="A screenshot of the results sections generated by the form submission">
        </li>
        <li>
            <p>Button to print the user's personalised results section, with a pop up notification to warn the user that this action will also reset the form.</p>
        </li>
        <li>
            <p>User story covered: 6, 9</p>
            <img src="readme-docs/features/print-calc.png" alt="A screenshot of the print button">
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
* [figma](https://www.figma.com/) was used to create wireframes.
* [Git](https://git-scm.com/) was used for version control.
* [GitHub](https://github.com/) was used for saving and storing files.
* [GitPod](https://gitpod.io/) was the IDE used for writing and editing code.
*[Heroku](https://id.heroku.com/) was used as the hosting platform for this site.
icons in the site.
* [Favicon.io](https://favicon.io/) was used to generate the site's favicon.
* [amiresponsive](https://ui.dev/amiresponsive?url=https://jeremyhsimons.github.io/CI_PP2_SavvySaver/) was used to test the website across different screens and generate the picture in the [Design](#design) section.


## Deployment & Local Development
The website was deployed to [Heroku](https://id.heroku.com/) using the following process:

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
Code institute's own Python Linter was used to validate all Python code in this project.



### Testing user stories

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 1. Navigate main features | Navigation bar | Starting at home page navigate to about page and reviews page. | Navigation elements lead to the expected pages. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="readme-docs/testing-user-stories/us1-1.png" alt="A screenshot of the home page"><br>
    <img src="readme-docs/testing-user-stories/us1-2.png" alt="A screenshot of the calculator nav element highlighted"><br>
    <img src="readme-docs/testing-user-stories/us1-3.png" alt="A screenshot of the calculator page"><br>
    <img src="readme-docs/testing-user-stories/us1-4.png" alt="A screenshot of the faq nav element highlighted"><br>
    <img src="readme-docs/testing-user-stories/us1-5.png" alt="A screenshot of faq page"><br>
    <img src="readme-docs/testing-user-stories/us1-6.png" alt="A screenshot of quiz nav element highlighted"><br>
    <img src="readme-docs/testing-user-stories/us1-7.png" alt="A screenshot of quiz page">
</details><br>

### Bugs

| Bug Description  | Action Taken to Fix  |
|---|---|


## Credits

### 3rd party code used

#### 3rd party Python libraries/modules
* [Gspread / Google Sheets API]()
* [Colorama]()

#### External APIs/libraries
* [favicon.io](https://favicon.io/) code was used in the head elements to generate favicon, and images are stored in assets/images.


#### Code found online when solving bugs in own code.


### Acknowledgements
* Thanks to my Mentor Mo Shami for his <strong>immensely valuable</strong> feedback, advice and encouragement throughout this project!
* Thanks to the wonderful CI London Community for all the moral support!
