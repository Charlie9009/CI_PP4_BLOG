# Story Game

<img src="">

<hr>

## Welcome to my program []()!

<br>

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-
refresh-toc -->

# Table of Content

1. [Project goals](#project-goals)

2. [User experience](#user-experience)

    1. [Target audience](#target-audience)

    2. [User stories](#user-stories)

    3. [Technical design](#technical-design)

3. [Features](#features)

4. [Technologies used](#technologies-used)

    1. [Languages](#languages)

    2. [Libraries and programs](#libraries-and-programs)

5. [Testing](#testing)

    1. [Python](#python)

    2. [Further testing](#further-testing)

    3. [Testing user stories](#testing-user-stories)

6. [Bugs](#bugs)

7. [Deployment](#deployment)

8. [Credit](#credit)

    1. [Acknowledgement](#acknowledgement)

## Project goals

* . 

## User experience

### Target audience

* .

### User stories

1. As a user I want an original story.

2. As a user I want to be challenged when playing the game.

3. As a user I want to be able to write my name in to the story.

4. As a user I want to be able to choose multiple paths.

5. As a user I want to be able to chose multiple classes.

6. As a user I want to be able to see my stats.

#### Site owner goals

7. As a site owner I want the user to be challenged.

8. As a site owner I want the user to experience an original story. 

9. As a site owner I want the user to have multiple path options.

10. As a site owner I want to be able to see how many has finished the story in either path.

11. As a site owner I want to have a loot system for the user.

### Technical design

* Below you can see the images of the flowchart.

<details><summary>Flowchart</summary>
<img src="docs/flowchart/pp3_flowchart.jpg">
</details>


## Features

* **Naming your character**

* .
<br>
<img src="">

### User stories covered by this feature:

* 3. .
<hr>


### Features left to implement


## Technologies used

### Languages

* Python

## Libraries and programs

* Django 3.2.

* Github

* Gitpod

* VS code

## Testing

### Validator testing

#### Python

<details><summary>No errors were found on run.py when passing through PEP8 Validator.</summary>
<img src="">
</details>


## Further testing

## Testing user stories

1. .

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  The story has been written by the site owner |    None    |       Original story                         |  Original story     |
|   Different paths changes the story   |    Choose path     |   Story will change with different paths     |   Works as expected |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


2. .

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Different paths ends the game  |    Choose path     |      If the user picks a wrong path the game ends  | Works as expected   |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


3. .

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Write your name and it stays in the story  |  Write you name | After user writes name it will show up in the story | Works as expected   |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


4. .

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Different paths in the story   |  Choose path       |      Different story depending on choice           |   Works as expected |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


5. .

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|   Choosing a class            |  Choose class        |   A user will be able to choose different classes  | Works as expected   |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


6. .

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|   Display stats               |   Pick a class       |  When picking a class the stats will be displayed  |  Works as expected  |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


7. .

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Different paths ends the game  |    Choose path     |      If the user picks a wrong path the game ends  | Works as expected   |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


8. . 

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  The story has been written by the site owner |    None    |       Original story                         |  Original story     |
|   Different paths changes the story   |    Choose path     |   Story will change with different paths     |   Works as expected |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


9. .

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Different paths in the story   |  Choose path       |      Different story depending on choice           |   Works as expected |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


10. .

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
| When a user finishes a story, data is sent to a sheet  |   Finish the game |  Sheet will be updated       | Works as expected   |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


11. .

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Defeating the ogre generates loot  |   Defeating the ogre |    when defeating the ogre loot should be presented |  Works as expected |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>

### API


## Bugs



### Known bugs


## Deployment

### Deploying to Heroku

1. Use **pip3 freeze > requirements.txt** in terminal to save libraries that needs to be installed on Heroku as well.

2. Log in to Heroku.

3. Click on the **new** button in the top right corner and in the drop down menu choose **Create new app**.

4. Choose a name for the app and a region and click **Create app**.

5. Go to the **settings** tab and go to **Config Vars**, click **Reveal Config Vars** and add **CREDS** to the key field. Add creds.json content to the value field.

6. In the **settings** tab add the python build pack first and then the node.js build pack.

7. Go to the **deploy** tab and pick **GitHub** as deployment method.

8. Search for a repository and connect to it.

9. Click the button **enable automatic deploys** and then the button **deploy branch**.

10. Wait for the app to build and then click the **view** button.

### Forking a repository

1. Log in to Github.
2. Find the repository.
3. In the top right corner click the fork button.
4. Now you will have a copy of the repository in your account.

### Cloning a repository
1. Log in to Github.
2. Find the repository.
3. Above the file window locate the green code button and click it.
4. To clone the repository using https copy the link.
5. Open Git bash.
6. Change the current directory to where you want the repository cloned.
7. In your terminal type now type “Git clone” followed by the repository you copied.
8. Press Enter.
9. Done.

## Credit


### I mainly watched these videos to get inspiration for my own project


## Acknowledgement

* My Mentor Mo has been invaluable, he pushed me to challenge myself and he was able to provide consistent and helpful feedback throughout my project.