# QUTEBA
Quteba is a Tigrinya word for Economy. I have created Quteba as a dynamic website that serves readers with news and analyses pertinent to economic issues.

Quteba is a dynamic website created using Django framework for the back-end and HTML, CSS and frameworks thereof for the front-end.


![Quteba](assets/screenshots/homepage-mockup.png)

[View Quteba live on Heroku](https://quteba.herokuapp.com/)

#

## Table of Contents
* [User Experience Design (UX)](#UX)
    * [The Strategy Plane](#The-Strategy-Plane)
        * [Site Goals](#Site-Goals)
        * [Epics](#Epics)
        * [User Stories](#User-Stories)
    * [The Scope Plane](#The-Scope-Plane)
    * [The Structure Plane](#The-Structure-Plane)
        * [Opportunities](#Opportunities)
    * [The Skeleton Plane](#The-Skeleton-Plane)
        * [Wireframes](#Wireframe-mockups)
        * [Database Schema](#Database-Schema)
    * [The Surface Plane](#The-Surface-Plane)
* [Features](#features)
* [Future Enhancements](#future-enhancements)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## UX Design
## Agile process
The Agile approach was key to the successful completion of this project. I started by creating user story template on Github. I used this template to generate user stories and plan their implementation. 

### The Strategy Plane

#### Site Goals

The goal of the website is to provide a platform for users to discuss and understand relevant economic issues. Quteba has a dual purpose: for the average user, it is a place where they can ask questions and get answers from volunteers. For users who are looking for deeper analyses from experts, quteba has a blog where contributors post articles and users can read, comment on or even open a discussion forum if they will.

Users of Quteba are interested in either getting quick answers to specific questions or a deeper insight on a given problem. As such, they want to engage in discussion forums by asking questions, reading comments, replying and/or reacting to the comments and replies others provide. Users are also interested in grasping the various viewpoints on specific economic topics, and thus they want to read articles that synthesize different theories and pieces of information.


#### Epics
In this project, I created 6 epics which encapsulate the user stories below.

- User registration 
- User login/logout 
- Blog app
- Forum app
- User engagement
- Auxiliary pages
#### User Stories
- As a **contributor** I can **create a profile and have my articles listed under my name** so that **readers can follow, read and engage in my work**
- As a **website user** I can **ask questions and send comments to the site owner** so that **I can get clarifications and express my opinions**
- As a **site admin** I can **verify authors and approve comments** so that **only relevant and engaging content is shared among readers**
- As a **reader** I can **follow and share latest activities on social media** so that **I see updates from a social media app I am using**
- As a **reader** I can **filter and set alert for content in different categories** so that **I do not have to read every article before I find the ones I am interested in**
- As a **reader** I can **like or unlike posts and comments** so that **I express my reaction without writing comments**
- As a **subscriber** I can **receive email notifications of new articles** so that **stay updated on relevant economic issues**
- As a **reader** I can **leave comments and view thread** so that **I become engaged in a conversation on a topic of my interest**
- As a **contributor** I can **create drafts and publish articles** so that **I can share my views and analyses with readers and receive feedback**
- As a **site user** I can **create an account** so that **I have access to both public and members only content**
- As a **reader** I can **view paginated excerpts of articles** so that **I choose which articles to read**
### The Scope Plane

### The Structure Plane

#### Opportunities

### The Skeleton Plane

#### Wireframes

![Home page](assets/wireframes/home-page-guest.png)

#### Database Schema

The ERD tool in postrgresql pgadmin 4 was used to generate the Entity Relationship Diagram for the data models. 

ERD for the user, profile, blog post, forum category and thread models.

![ERD](assets/wireframes/qerd_models.png)

### The Surface Plane

#### Colors

I used green, a calming color, with varying intensity.
To create a good contrast, I used white text on a deep green background.

## Features

* Quteba serves the aforementioned user stories by providing two broad features: Quteba Blog (Qblog) and Quteba Forum (Qforum). Besides these, it has static pages. 

* **Homepage:** Quteba's homepage provides first time users with information and links that helps them navigate the website easily. With first time visitors of the site in mind, the dual purpose of the site is made clear from the outset. Users see links to and information about Qblog and Qforum. There is a nav bar at the top which presents different menu items, so users can choose with a single click to view what quteba is about, a sign up page or if they have an account a sign in page.
The home page also presents the most recently added blog entries and the active discussion forum topics in separate sections. This gives users the chance to have a quick glance at what kinds of topics and questions are being discussed. From users' perspective, this preview is important because it gives them an idea of what to expect before delving into the whole list of either Qblog or Qforum.

* The navigation menu: This is visible in the home page and all other pages. Only some of the items in the menu change depending on whether the user is logged in or not.
(image here)

* **Search form:** Users who are looking for a particular concept may search for it by typing a keyword in the search input form at the top bar of each page. If the keyword exists in Qblog and/or Qforum, the results are displayed in a separate search results page.

* **Search results page:** This page renders the search results when a user searches for a specific keyword and a matching entry is found in either Qblog or Qforum or both. If the keyword the user types in the search form does not exist, the results page shows a feedback message. 

* **About page:** the about page is a static page that gives users important information about the background and services of quteba.

* Users who come across quteba for the first time can read the about page and learn what quteba means and holds. 

* **Qblog:** Qblog lists blog entries showing the author, title, date and excerpts of each blog post. The title is clickable and linked to the blog detail page. By viewing only the list of blog posts, users need not read each blog before they find what they want to read. The excerpts will give users enough information to help them decide whether to continue reading or find another article. There is also a button next to the excerpt which is linked to the details page.

* Blog detail page: The blog detail page shows users the title of the article, author, date, content, likes and comments (if any).
Logged in users also see a form where they can type and submit a comment.
 
* **Qforum:** The purpose of having the Qforum on the menu bar and a list of forum entries (thread list) is similar to that of Qblog. Users can click on the Qforum menu item and land on a page that lists discussion forums. As each forum has a topic and description (question text), users can get an idea of what a particular discussion forum is about. 

* Here we clarify some terminologies. Forum and thread are used interchangeably. When a user creates a new discussion forum, the topic, description and the comments and replies under it are all part of a discussion forum. The comments and replies make a thread.
* **Categories:** we use categories to refer to broad areas of economics that encapsulate the particular discussion topics. For example, a category can be Finance while the discussion topics may relate to specific concepts such as exchange rate.

* The Qforum page has a form for users to submit questions. It is placed at the top but users need to click and expand it. This is efficient because the form does not cover the most central part of the page for users who are interested in reading the forums. It is also intuitively self-evident that a user should click it to create a forum.

* Qforum lists forums based on the date they were created, starting with the most recent ones. users can see how many comments and replies have been given under each discussion forum. 
(How to use vote counts to sort forums.)

* The forum list page has a sidebar that shows the most active topics. These are topics that have the most recent comment or reply.

* **Forum detail page:** When a user clicks on a particular discussion forum topic in the Qforum list page, a separate page with the particular forum at the top and any comments and replies under it. 
A user can edit or delete their own discussion forum and reply to comments and replies except their own. To this effect, the buttons a user sees in this page vary depending on whether the user is logged in or not and if the entries are their own or those of others.

* **Sign up page:**
New users are encouraged to sign up so that they can not only read what others have written but also engage in conversations by creating forums and through comments and replies. Users who decide to sign up at the very beginning will see the sign up menu item, which is also available throughout the quteba pages. Users who want to explore the contents first can do so until they try to add a comment, for example, where they will see a link to the login or sign up pages. 

* **Sign in Page:**
If a user has an account, they can login so that they can interact with Quteba in more ways than they otherwise would. A logged in user can add comments to blog posts, like blog posts, create a discussion forum, comment on a forum, reply to comments, vote up or down on forums, like or unlike replies, edit or delete their own forums and comments, update and delete their profiles. 

* **Profile page:**
When a user logs in, they see their profile picture and their name on the menu bar. By clicking on their profile name, they can view their profile which has two buttons linked to (1) profile update form and (2) profile delete page. 

* **Update profile:**
The profile update page enables users to edit and update their profiles. The user can change their profile picture and update their bio. When they save the changes, they are redirected to the profile page.

* **Delete profile:**
If a user wants to delete the profile they created, they can do so by using the link provided in the profile view page. To make sure that a user does not suddenly delete their profile, the user gets a prompt asking the user if they are sure that they want to delete the profile. Only when they confirm will the profile be deleted. If the user does not want to continue with the deletion of the profile, they can cancel the process in the confirmation page and go back to the profile view page. 

* **Sign out page:**
When a logged in user wants to sign out, they can do so by clicking on the sign out menu in the navigation bar. They can sign out from any page because the navigation bar is available on all pages.
Once they click on sign out, they are asked to confirm that they logout. If the user does not want to complete the process, they can cancel it and go back to the (profile page). 

* **User Interaction:**
One of the key principles of Quteba is user engagement. Users can create discussion forums which can grow in to a big threaded forum with many contributors. Users can also express their views by using likes and unlikes, up and down votes etc. As such, quteba becomes what its users make it to be. 
  - Create a forum: Logged in users can create a forum using the create forum form. They choose a category from a given list of categories, enter a topic and wrote a description of the issue they want other quteba users to address. On submitting the forum, an ajax call handles the backend interaction and the user sees the forum they just created without a page reload. This gives the user a good user experience. 
  - Comment: Comments and replies are technically the same. The only difference is that a comment is the direct child of a forum while a reply follows a comment or another reply. A forum, its comments, replies to comments and replies to replies create a nested tree. Users can add comments to forums by using a comment form modal that pops up when a user clicks on the comment button which displays a down arrow to hint that a click on the button opens a form. Users can edit or delete comments that they created.
  - Reply: As mentioned above, a reply is just a comment on a comment or another reply. Users see the same form when they subit a comment as when they write a reply. In this implementation, users cannot edit or delete replies because they can add another reply and explain themselves further while keeping their original opinion. 
  - Like/unlike a comment/reply: For users who want to express their views with a minimal effort, each comment as well as reply has like and dislike features. A logged in user can like a comment or a reply, or dislike a comment or a reply. 
  - Up/down vote a forum: The voting feature is added only to forums. A user who likes or dislikes a thread (a forum and the comments and replies thereof) can vote up or down respectively. While this captures the user's opinion about the whole issue in a particular forum, it is possible to use the votes as a basis for ranking forums such that forums with highest number of positive votes are, for example, featured in the landing page.
A common characteristic of these modes of user interactions are that they use ajax calls to make the user experience smooth. For the likes and dislikes, one can only like or dislike, but not both, at a time. The same applies to votes: if one has voted up and click on vote down, the up vote is removed and the down vote increases by one.


## Future Enhancements

## Technologies Used

* asgiref==3.5.0
* cloudinary==1.29.0
* dj-database-url==0.5.0
* dj3-cloudinary-storage==0.0.6
* Django==4.0.3
* django-allauth==0.50.0
* django-bootstrap4==22.1
* django-crispy-forms==1.14.0
* django-summernote==0.8.20.0
* fontawesomefree==6.0.0
* gunicorn==20.1.0
* oauthlib==3.2.0
* Pillow==9.1.0
* psycopg2==2.9.3
* PyJWT==2.3.0
* python3-openid==3.2.0
* requests-oauthlib==1.3.1
* sqlparse==0.4.2
* tzdata==2022.1

------

- ### Languages:
    
    + [Python 3.8.5](https://www.python.org/downloads/release/python-385/): the primary language used to develop the server-side of the website.
    + [JS](https://www.javascript.com/): the primary language used to develop interactive components of the website.
    + [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): the markup language used to create the website.
    + [CSS](https://developer.mozilla.org/en-US/docs/Web/css): the styling language used to style the website.
- ### Frameworks and libraries:
    + [Django](https://www.djangoproject.com/): python framework used to create all the logic.
    + [jQuery](https://jquery.com/): was used to control click events and sending AJAX requests.
    + [jQuery User Interface](https://jqueryui.com/) was used to create interactive elements.
- ### Databases:
    + [PostgreSQL](https://www.postgresql.org/): the database used to store all the data.
- ### Other tools:
    + [Git](https://git-scm.com/): the version control system used to manage the code.
    + [Pip3](https://pypi.org/project/pip/): the package manager used to install the dependencies.
    + [Spycopg2](https://www.python.org/dev/peps/pep-0249/): the database driver used to connect to the database.
    + [Django-allauth](https://django-allauth.readthedocs.io/en/latest/): the authentication library used to create the user accounts.
    + [Django-crispy-forms](https://django-cryptography.readthedocs.io/en/latest/): was used to control the rendering behavior of Django forms.
    + [Heroku](https://dashboard.heroku.com/): the hosting service used to host the website.
    + [GitHub](https://github.com/): used to host the website's source code.
    + [VSCode](https://code.visualstudio.com/): the IDE used to develop the website.
    + [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website.
    + [Font Awesome](https://fontawesome.com/): was used to create the icons used in the website.
    + [Coolors](https://coolors.co/202a3c-1c2431-181f2a-0b1523-65e2d9-925cef-6b28e0-ffffff-eeeeee) was used to make a color palette for the website.
    + [BGJar](https://www.bgjar.com/): was used to make a background images for the website.
    + [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website.
    + [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website.
    + [JShint](https://jshint.com/): was used to validate JS code for the website.
    + [PEP8](https://pep8.org/): was used to validate Python code for the website.
    + [Cloudinary](https://cloudinary.com/): the image hosting service used to upload images and other media.
    + [Techsini](https://techsini.com/multi-mockup/index.php): to generate mock up for responsive design for various screen sizes.

HTML, CSS, Javascript, Bootstrap5, Django

I used [Balsamiq Cloud](https://balsamiq.cloud/) to create wireframes.
## Testing
Detailed testing and test results [are documented here](TESTING.md).
### Bugs
- I created user stories in Github and django project in Gitpod. When I tried to push my local changes, I got an error which i fixed using [this solution](https://docs.github.com/en/get-started/using-git/dealing-with-non-fast-forward-errors).

- I was not able to deploy the application to heroku because of an error in backports.zoneinfo which ended up in the requirements file. I removed it manually and it worked. 
- I was not able to login to the admin page and got CSRF error. I added CSRF_TRUSTED_ORIGINS
## Deployment

### Using Heroku
- Development Enviroment
  1.  Create env.py : It needs to contain these 3 variables.
    - [Cloudinary](https://cloudinary.com/)
    - Secret key is the password of your choice.
    - [Heroku](https://id.heroku.com/) postgreSQL.
    ![env file]()
  2. Create requirements.txt file that includes all dependencies needed for the project.
    
    - You can do this by executing the following command in the terminal:
      ```
      pip freeze > requirements.txt
      ```
    
    - Or using the package pipreqs.
      ```
      pipreqs requirements.txt
      ```

  3. Create Procfile containing the commands to run the app.

  4. Commit and push deployment changes to Github.
  5. Create an account and login to Heroku
    - Create a new app, with an appropriate app name and choose a region.
    ![Create App]()
    - In Resources add Heroku Postgres and Heroku Redis.
    ![Resources]()
    
    ![Config Vars]()
    - At the settings tab click on Reveal Config Vars.
    - Add the following config vars or check if they are already added.
      - `DATABASE_URL` : The URL of the database provided by Heroku Postgres.
      - `SECRET_KEY` : The secret key for your Django project.
      - `CLOUDINARY_CLOUD_NAME` : Your Cloudinary Cloud Name.
      - `CLOUDINARY_API_KEY` : Your Cloudinary API Key.
      - `CLOUDINARY_API_SECRET` : Your Cloudinary API Secret.
      - `DISABLE_COLLECTSTATIC` : Set to `1` to disable collectstatic during the development.
    
    - Download and install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
    - And pass following commands in your github terminal:
      - $ heroku login -i
      - Then enter your login credentials
      - $ git add .
      - $ git commit -am "make it better"
      - $ git push heroku main
    

  6. Open the Heroku dashboard and check the status of your app.
      - Copy the URL of your app and add it into `ALLOWED_HOSTS` in your settings.py file.
  7. When the development stage is complete:
    - make sure that you have these settings in your settings.py file:
      - `STATIC_ROOT` : The path to the static files.
      - `DEFUALT_FILE_STORAGE` : The default file storage system, in this case, `cloudinary_storage.storage.MediaCloudinaryStorage`
      - `cloudinary` and `cloudinary_storage` are added to `INSTALLED_APPS`, and `cloudinary.config(...)` receives cloud name, api key, and api secret.
    - Remove the `DISABLE_COLLECTSTATIC` variable from your app's config vars on Heroku.
    - Set the `DEBUG` variable to `False` in your your app's config vars on Heroku.
    - Deploy the latest version of your app to Heroku.
    - Open the Heroku dashboard and check the status of your app.
    - If something is wrong, you can find an error message in the logs and fix it.

#### How to Fork

To fork the repository:

1. Log in (or sign up) to Github.
2. Go to the repository for this project, [Quteba](https://github.com/Amareteklay/quteba).
3. Click the Fork button in the top right corner.

#### How to Clone

To clone the repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, [Quteba](https://quteba.herokuapp.com/).
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

## Credits
- I followed [this tutorial](https://replit.com/talk/learn/DjangoPython-and-HTML-Coding-Campus-Tutorial-1-Create-a-Blog-with-Django/142238?order=new) to create blog posts.

- Image for UX and behavioral economics was taken from [this webpage](https://startupsmagazine.co.uk/article-behavioural-economics-tips-ux-design).

- Template for forum was taken from [this page](https://www.bootdey.com/snippets/view/bs5-forum-list)
- I used the articles and code in [this page](https://www.devhandbook.com/django/user-registration/) to create user registration and profile.

- I began the blog list page by borrowing code from [this](<https://replit.com/talk/learn/DjangoPython-and-HTML-Coding-Campus-Tutorial-1-Create-a-Blog-with-Django/142238?order=new) and [this](https://github.com/Code-Institute-Solutions/Django3blog/blob/master/10_likes/templates/index.html), which i later changed substantially.

- I took the data model for the forum from [this article](https://vertabelo.com/blog/database-model-for-an-online-discussion-forum-part-1/).
- I followed [this tutorial](https://focusustech.com/blog/create-a-comment-and-reply-system-in-django) to modify forum views and templates.
- I followed [this tutorial](https://learndjango.com/tutorials/django-search-tutorial) to implement search functionality.
- I used [this online converter](https://svgtopng.com/) to generate png from svg, which was created using [bgjar](https://bgjar.com/).
- Nav bar and footer background color was inspired by [this](https://www.mp.se/goteborg/just-nu/goteborg-ska-vara-en-karnvapenfri-zon/).
- I copied and edited the deployment procedure from our [hackathon project readme]().
- Code for user registration and signals was adapted from [this](https://www.devhandbook.com/django/user-registration/) and [this](https://www.devhandbook.com/django/user-profile/).
### Acknowledgements



#### [BACK TO TOP](https://github.com/Amareteklay/quteba#readme)