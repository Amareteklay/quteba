# QUTEBA
Quteba is a Tigrigna word for Economy. I have created Quteba as a dynamic website that serves readers with news and analyses pertinent to economic issues. 


![Quteba](media/qbrand.png)

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

#### Epics

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

#### Database Schema

### The Surface Plane

## Features

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
## Testing
Detailed testing and test results [are documented here](TESTING.md).
### Bugs
- I created user stories in Github and django project in Gitpod. When I tried to push my local changes, I got an error which i fixed using [this solution](https://docs.github.com/en/get-started/using-git/dealing-with-non-fast-forward-errors).

- I was not able to deploy the application to heroku because of an error in backports.zoneinfo which ended up in the requirements file. I removed it manually and it worked. 
- I was not able to login to the admin page and got CSRF error. I added CSRF_TRUSTED_ORIGINS
## Deployment

## Credits
- I followed [this tutorial](https://replit.com/talk/learn/DjangoPython-and-HTML-Coding-Campus-Tutorial-1-Create-a-Blog-with-Django/142238?order=new) to create blog posts.

- Image for UX and behavioral economics was taken from [this webpage](https://startupsmagazine.co.uk/article-behavioural-economics-tips-ux-design).

- Code for carousel was taken from [this page](https://getbootstrap.com/docs/5.0/components/carousel/).

- Template for forum was taken from [this page](https://www.bootdey.com/snippets/view/bs5-forum-list)
- I used the articles and code in [this page](https://www.devhandbook.com/django/user-registration/) to create user registration and profile.

- I took the data model for the forum from [this article](https://vertabelo.com/blog/database-model-for-an-online-discussion-forum-part-1/).
- I followed [this tutorial](https://focusustech.com/blog/create-a-comment-and-reply-system-in-django) to modify forum views and templates.
- I followed [this tutorial](https://learndjango.com/tutorials/django-search-tutorial) to implement search functionality.

### Acknowledgements
