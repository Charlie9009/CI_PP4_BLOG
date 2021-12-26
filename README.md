# News Blog

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

* The goal of this project is for the site owner to practice Django and to create a News Blog for other users.

## User experience

### Target audience

* This site is targeted towards people who would like to share news.

### User stories

#### Site Visitor

1. As a Site Visitor I can read news so I can keep up to speed with the world.

2. As a Site Visitor I can create an account so that I can interact with the content, add my own content and search for content.

3. As a Site Visitor I can view questions so that I can see what other people have had to say about the site.

#### Site User

4. As a Site User I can create, read, update and delete posts so that I can manage my content.

5. As A Site User I can search for posts so I can find the relevant one for me.

6. As a Site User I can click on a post and see comments and the post so I can get a better view of the posts.

7. As a Site User I can read comments so that I can get a nuanced view of the news.

8. As a Site User I can comment on a post so that I can ask question and be a part of the conversation.


#### Site owner goals

9. As a Site Admin I can create, read, update and delete posts so that I can manage my content.

10. As a Site Admin I can mark posts with warnings so that I can keep track of users abusing the page.

11. As a Site Admin I can search for posts so that I can find posts I am interested in.

12. As a Site Admin I can answer questions so that users feel included in the site.

### Technical design

### Design

* 

#### Colors

* 

#### Fonts

* 

### Wireframes

* Below you can see the images of the wireframes

<details><summary>Wireframe</summary>
<img src="docs/flowchart/pp3_flowchart.jpg">
</details>

### Database diagram

* * Below you can see the images of the database diagram

<details><summary>Flowchart</summary>
<img src="docs/flowchart/pp3_flowchart.jpg">
</details>

## Features

* **News List**

* The opening of the site shows a list of posts
<br>
<img src="docs/features/feature_view_news.JPG">

### User stories covered by this feature:

    1. As a Site Visitor I can read news so I can keep up to speed with the world.
    4. As a Site User I can create, read, update and delete posts so that I can manage my content.
<hr>

* **Account creation**

* A feature was implemented for a user to create an account
<br>
<img src="docs/features/feature_register.png">

### User stories covered by this feature:

    2. As a Site Visitor I can create an account so that I can interact with the content, add my own content and search for content.
<hr>

* **Questions**

* A feature was implemented where the admin answers users questions
<br>
<img src="docs/features/feature_question.png">

### User stories covered by this feature:

    3. As a Site Visitor I can view questions so that I can see what other people have had to say about the site.
<hr>

* **Crud**

**Requires log in**

* A feature was implemented so users can create, read, update and delete their posts
<br>
<img src="docs/features/feature_crud.png">

### User stories covered by this feature:

    4. As a Site User I can create, read, update and delete posts so that I can manage my content.
    9. As a Site Admin I can create, read, update and delete posts so that I can manage my content.
<hr>

* **Search**

**Requires log in**

* A feature was implemented so users can search for content
<br>
<img src="docs/features/feature_search.png">

### User stories covered by this feature:

    5. As A Site User I can search for posts so I can find the relevant one for me.
    11. As a Site Admin I can search for posts so that I can find posts I am interested in.
<hr>

* **Open Post**

**Requires log in**

* A feature was implemented so users can click on a post to read it
<br>
<img src="docs/features/feature_read_post.png">

### User stories covered by this feature:

    6. As a Site User I can click on a post and see comments and the post so I can get a better view of the posts.
    7. As a Site User I can read comments so that I can get a nuanced view of the news.
<hr>

* **Read Comments**

**Requires log in**

* A feature was implemented so users see comments made underneath the post
<br>
<img src="docs/features/feature_read_comment.png">

### User stories covered by this feature:

    6. As a Site User I can click on a post and see comments and the post so I can get a better view of the posts.
    7. As a Site User I can read comments so that I can get a nuanced view of the news.
<hr>

* **Make Comments**

**Requires log in**

* A feature was implemented so users can make comments on posts
<br>
<img src="docs/features/feature_make_comment.png">

### User stories covered by this feature:

    6. As a Site User I can click on a post and see comments and the post so I can get a better view of the posts.
    7. As a Site User I can read comments so that I can get a nuanced view of the news.
    8. As a Site User I can comment on a post so that I can ask question and be a part of the conversation.
<hr>

* **Admin Crud**

**Requires superuser**

* A feature was implemented so the admin can manage the content on the page
<br>
<img src="docs/features/feature_admin_crud.png">

### User stories covered by this feature:

    9. As a Site Admin I can create, read, update and delete posts so that I can manage my content.
<hr>

* **Admin Warning**

**Requires superuser**

* A feature was implemented so the admin can mark posts with warnings to keep track of abusing users
<br>
<img src="docs/features/feature_admin_warning.png">

### User stories covered by this feature:

    10. As a Site Admin I can mark posts with warnings so that I can keep track of users abusing the page.
<hr>

* **Admin Search**

**Requires superuser**

* A feature was implemented so the admin can search for posts
<br>
<img src="docs/features/feature_admin_search.png">

### User stories covered by this feature:

    11. As a Site Admin I can search for posts so that I can find posts I am interested in.
<hr>

* **Admin Questions**

**Requires superuser**

* A feature was implemented so the admin can answer and post questions
<br>
<img src="docs/features/feature_admin_question.JPG">

### User stories covered by this feature:

    5. As A Site User I can search for posts so I can find the relevant one for me.
    11. As a Site Admin I can search for posts so that I can find posts I am interested in.
<hr>

### Features left to implement

* Adding images to posts.

* Adding the possibility for the users to have profiles to edit.

* Adding news categories.

## Technologies used

### Languages

* Python

* HTML

* CSS

* Django 3.2

## Libraries and programs

* [Github](https://github.com/)

* [Gitpod](https://gitpod.io/projects)

* [VS code](https://code.visualstudio.com/)

* [Bootstrap 5](https://getbootstrap.com/)

* [Heroku for deployment and storing Postgresql database](https://id.heroku.com/login)

* [Crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/)

* [Balsamiq](https://balsamiq.com/)

* [Pep8 Online](http://pep8online.com/)

* [Ami responsivedesign](http://ami.responsivedesign.is/)

* [Lighthouse](https://developers.google.com/web/tools/lighthouse)

* [HTML Validator](https://validator.w3.org/)

* [CSS Validator](https://jigsaw.w3.org/css-validator/)

## Testing

### Validator testing

#### HTML

<details><summary>No errors were found on index.html when passing through WC3 Validator.</summary>
<img src="docs/validation/index_validation.JPG">
</details>

<details><summary>No errors were found on login.html when passing through WC3 Validator.</summary>
<img src="docs/validation/login_validation.JPG">
</details>

<details><summary>No errors were found on logout.html when passing through WC3 Validator.</summary>
<img src="docs/validation/logout_validation.JPG">
</details>

<details><summary>No errors were found on post_create.html when passing through WC3 Validator.</summary>
<img src="docs/validation/post_create_validation.JPG">
</details>

<details><summary>No errors were found on post_delete_confirm.html when passing through WC3 Validator.</summary>
<img src="docs/validation/post_delete_confirm_validation.JPG">
</details>

<details><summary>No errors were found on post_detail.html when passing through WC3 Validator.</summary>
<img src="docs/validation/post_detail_validation.JPG">
</details>

<details><summary>No errors were found on post_update.html when passing through WC3 Validator.</summary>
<img src="docs/validation/post_update_validation.JPG">
</details>

<details><summary>No errors were found on question.html when passing through WC3 Validator.</summary>
<img src="docs/validation/question_validation.JPG">
</details>

<details><summary>No errors were found on register.html when passing through WC3 Validator.</summary>
<img src="docs/validation/register_validation.JPG">
</details>

<details><summary>No errors were found on search_results.html when passing through WC3 Validator.</summary>
<img src="docs/validation/search_results_validation.JPG">
</details>
<hr>

#### CSS

<details><summary>No errors were found on the CSS file when passing through Jigsaw W3 Validator.</summary>
<img src="docs/validation/css_validation.JPG">
</details>
<hr>


#### Python

<details><summary>No errors were found on admin.py when passing through PEP8 Validator.</summary>
<img src="docs/validation/admin_validation.JPG">
</details>

<details><summary>No errors were found on blog_urls.py when passing through PEP8 Validator.</summary>
<img src="docs/validation/blog_urls_validation.JPG">
</details>

<details><summary>No errors were found on forms.py when passing through PEP8 Validator.</summary>
<img src="docs/validation/forms_validation.JPG">
</details>

<details><summary>No errors were found on models.py when passing through PEP8 Validator.</summary>
<img src="docs/validation/models_validation.JPG">
</details>

<details><summary>No errors were found on newsblog_urls.py when passing through PEP8 Validator.</summary>
<img src="docs/validation/newsblog_urls_validation.JPG">
</details>

<details><summary>No errors were found on views.py when passing through PEP8 Validator.</summary>
<img src="docs/validation/views_validation.JPG">
</details>
<hr>

#### Accessibility

<details><summary>No errors were found on the base/index.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/wave_base_index_validation.JPG">
</details>

<details><summary>No errors were found on the login.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/wave_login_validation.JPG">
</details>

<details><summary>No errors were found on the logout.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/wave_logout_validation.JPG">
</details>

<details><summary>No errors were found on the signup.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/wave_register_validation.JPG">
</details>

<details><summary>No errors were found on the question.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/wave_question_validation.JPG">
</details>

<details><summary>No errors were found on the delete_confirm.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/wave_delete_confirm_validation.JPG">
</details>

<details><summary>No errors were found on the post_create.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/wave_post_create_validation.JPG">
</details>

<details><summary>No errors were found on the post_detail.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/wave_post_detail_validation.JPG">
</details>

<details><summary>No errors were found on the post_update.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/wave_post_update_validation.JPG">
</details>

<details><summary>No errors were found on the search_results.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/wave_search_results_validation.JPG">
</details>
<hr>

#### Performance

* Lighthouse was used to test the performance and the speed of the site. <br>

<details><summary>index.html</summary>
<img src="docs/validation/index_light.JPG">
</details>

<details><summary>login.html</summary>
<img src="docs/validation/login_light.JPG">
</details>

<details><summary>logout.html</summary>
<img src="docs/validation/logout_light.JPG">
</details>

<details><summary>post_create.html</summary>
<img src="docs/validation/post_create_light.JPG">
</details>

<details><summary>post_delete_confirm.html</summary>
<img src="docs/validation/post_delete_confirm_light.JPG">
</details>

<details><summary>post_detail.html</summary>
<img src="docs/validation/post_detail_light.JPG">
</details>

<details><summary>post_update.html</summary>
<img src="docs/validation/post_update_light.JPG">
</details>

<details><summary>question.html</summary>
<img src="docs/validation/question_light.JPG">
</details>

<details><summary>register.html</summary>
<img src="docs/validation/register_light.JPG">
</details>

<details><summary>search_results.html</summary>
<img src="docs/validation/search_results_light.JPG">
</details>
<hr>


## Further testing

## Testing user stories

1. As a Site Visitor I can read news so I can keep up to speed with the world.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  The newspost are on the home page |    arrive on home page    |       posts will appear on home page     |  Works as expected  |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


2. As a Site Visitor I can create an account so that I can interact with the content, add my own content and search for content.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Different paths ends the game  |    Choose path     |      If the user picks a wrong path the game ends  | Works as expected   |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


3. As a Site Visitor I can view questions so that I can see what other people have had to say about the site.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Write your name and it stays in the story  |  Write you name | After user writes name it will show up in the story | Works as expected   |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


4. As a Site User I can create, read, update and delete posts so that I can manage my content.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Different paths in the story   |  Choose path       |      Different story depending on choice           |   Works as expected |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


5. As A Site User I can search for posts so I can find the relevant one for me.



|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|   Choosing a class            |  Choose class        |   A user will be able to choose different classes  | Works as expected   |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


6. As a Site User I can click on a post and see comments and the post so I can get a better view of the posts.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|   Display stats               |   Pick a class       |  When picking a class the stats will be displayed  |  Works as expected  |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


7. As a Site User I can read comments so that I can get a nuanced view of the news.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Different paths ends the game  |    Choose path     |      If the user picks a wrong path the game ends  | Works as expected   |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


8. As a Site User I can comment on a post so that I can ask question and be a part of the conversation.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  The story has been written by the site owner |    None    |       Original story                         |  Original story     |
|   Different paths changes the story   |    Choose path     |   Story will change with different paths     |   Works as expected |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


9. As a Site Admin I can create, read, update and delete posts so that I can manage my content.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Different paths in the story   |  Choose path       |      Different story depending on choice           |   Works as expected |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


10. As a Site Admin I can mark posts with warnings so that I can keep track of users abusing the page.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
| When a user finishes a story, data is sent to a sheet  |   Finish the game |  Sheet will be updated       | Works as expected   |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


11. As a Site Admin I can search for posts so that I can find posts I am interested in.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Defeating the ogre generates loot  |   Defeating the ogre |    when defeating the ogre loot should be presented |  Works as expected |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


12. As a Site Admin I can answer questions so that users feel included in the site.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Defeating the ogre generates loot  |   Defeating the ogre |    when defeating the ogre loot should be presented |  Works as expected |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>

### API


## Bugs

* **Bug:** Search_results.html would just give a site error and not appear.

    * **Fix:** I changed places in urls.py file so *search_results* was over *post_detail*.

### Known bugs


## Deployment

### Deploying to Heroku

1. Use **pip3 freeze > requirements.txt** in terminal to save libraries that needs to be installed on Heroku as well.

2. Create **Procfile** and add **web: gunicorn newsblog.wsgi**

3. Log in to Heroku.

4. Click on the **new** button in the top right corner and in the drop down menu choose **Create new app**.

5. Choose a name for the app and a region and click **Create app**.

6. Go to the **resources** tab and go to **add-ons**, search for **postgres** and add **heroku postgres**.

7. Go to the **settings** tab and go to **Config Vars**, click **Reveal Config Vars** and copy the DATABASE_URL**VALUE**. Add **DATABASE_URL** and **VALUE** to env in the code.

8. Add **SECRET_KEY** and **VALUE** to **Config Vars** and add to env in code.

9. Add **DATABASES** in settings.py to fork with heroku database

10. Write python3 manage.py migrate in terminal

11. Add url in settings.py on **ALLOWED_HOSTS**

12. Go to the **deploy** tab and pick **GitHub** as deployment method.

13. Search for a repository and connect to it.

14. Click the button **enable automatic deploys** and then the button **deploy branch**.

15. Wait for the app to build and then click the **view** button.

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

###

* [Developer mozillas](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication) site was used to get authentication up and running , in combination with Code Institutes way of importing files for html and using [Django allauth](https://django-allauth.readthedocs.io/en/latest/templates.html#overridable-templates) to connect the files.

* In order to build the project [Django Central](https://djangocentral.com/building-a-blog-application-with-django/) was used to help in development.

* In order to get the comment function working [Code Institutes](https://codeinstitute.net/se/) learning project *I think therefore I blog* comment class was used.

* For the search function I used the [learn django](https://learndjango.com/tutorials/django-search-tutorial) site to set it up and used [django project](https://docs.djangoproject.com/en/3.1/topics/db/queries/#complex-lookups-with-q-objects) to use Q objects.

#### Articles used for site

* Author: By Stephen Collinson and Maeve Reston [CNN](https://edition.cnn.com/2020/11/07/politics/joe-biden-wins-us-presidential-election/index.html).

* [The Guardian](https://www.theguardian.com/world/2021/dec/21/eu-in-row-over-inclusion-of-gas-and-nuclear-in-sustainability-guidance)

* Author: Neil Lupin/Getty [The Rolling Stone](https://www.rollingstone.com/music/music-news/eric-clapton-management-statement-widow-bootleg-cd-1275158/)

* Author: Amar Mehta [Sky News](https://news.sky.com/story/james-webb-space-telescope-begins-voyage-back-to-the-birth-of-the-universe-after-perfect-launch-12503731)


### I mainly watched these videos to get inspiration for my own project


## Acknowledgement

* My Mentor Mo has been invaluable, he pushed me to challenge myself and he was able to provide consistent and helpful feedback throughout my project.