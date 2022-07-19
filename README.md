# QUTEBA
Quteba is a dynamic website that aims to serve users by providing views and analyses pertinent to economic issues as well as by enabling them to participate in discussion forums. Quteba got its name from a Tigrinya word that can roughly be translated as Economy. Quteba is as much a platform for user-created content as it is a source of information for those who want to read blog posts. Users can start discussion forums as well as engage in discussions by way of comments and replies.

Quteba was built using Django framework for the back-end and JavaScript (and Jquery), HTML and CSS (and bootstrap) for the front-end.  

![Quteba](assets/screenshots/quteba-mockup.png)

[View Quteba live on Heroku](https://quteba.herokuapp.com/).

#

# Table of Contents
* [UX Design ](#ux-design)
    * [The Strategy Plane](#the-strategy-plane)
        * [Site Goals](#site-goals)
        * [Epics](#epics)
        * [User Stories](#user-stories)
    * [The Scope Plane](#the-scope-plane)
    * [The Structure Plane](#the-structure-plane)
    * [The Skeleton Plane](#the-skeleton-plane)
        * [Wireframes](#wireframes)
        * [Information Architecture](#information-architecture)
        * [Database](#database)
        * [ERD](#erd)
    * [The Surface Plane](#the-surface-plane)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Future Enhancements](#future-enhancements)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
    * [Acknowledgements](#acknowledgements)


# UX Design

## The Strategy Plane
 
### **Site Goals**

* Owner goals: 
   * The goal of the website is to provide a platform for users to discuss and understand relevant economic issues. Quteba has a dual purpose: 
     * For the average user, it is a place where they can ask questions and get answers from other users. 
     * For users who are looking for deeper analyses from experts, quteba has a blog where contributors post articles and users can read, comment on or even open a discussion forum if they will.

* User goals: 
   * Users of Quteba are interested in either getting quick answers to specific questions or a deeper insight on a given problem. 
   * Users want to engage in discussion forums by asking questions, reading comments, replying and/or reacting to the comments and replies others provide. 
   * Users are also interested in grasping the various viewpoints on specific economic topics, and thus they want to read articles that synthesize different theories and pieces of information.

### **Epics**
In this project, the following 8 epics were created which encapsulate the user stories below.

- Useability
- User authentication
- User profile  
- Quteba blog 
- Quteba forum
- Nested threads
- Search for content
- User interaction 

### **User Stories**

The above user goals and epics were decomposed into user stories that are crucial to identify and implement the required features. The agile process was followed and many of the user stories and different tasks under them were listed in the [project kanban board](https://github.com/Amareteklay/quteba/projects/1) to keep track of the status of each feature. 

- **Useability**
   - As a first time visitor, I want to get information about the site so that I can understand what the site focuses on and how I can make the best out of it.
   - As a first time visitor, I want to be able to navigate the site so that I can find the most important information with the least amount of effort.
   - As an engaged user, I want to see relevant feedback so that I can understand if my interactions with the site are successful or not. 
   - As a user, I want to know which menu item is active so that I can know which part of the site I am currently navigating. 
   - As a user, I want to be able to access quteba's contents and functionalities from my mobile or tablet so that I do not have to wait until I find a computer.
   - As a frequent user, I want to follow the site owner on social media so that I can see recent activities and updates from my favourite social media apps.

- **User authentication**
   - As a first time visitor, I want to sign up so that I can have login credentials which I can use to login to the site every time I want to use it. 
   - As a registered user, I want to be able to login with my registered credentials so that I can access my profile as well as all the contents and functionalities that require user authentication.
   - As a logged in user, I want to be able to logout easily so that I feel safe that others do not interact with the site via my account.

- **User profile** 
   - As a registered user, I want to have a profile so that I can choose a profile picture and share my bio with other quteba users.
   - As a registered user, I want to be able to update and delete my profile so that I have control of what I want to do with my personal information.

- **Quteba blog**
   - As a reader, I want to read excerpts of blog posts so that I choose which articles to read without going through the whole content of each post.
   - As a contributor, I want to be able to create drafts and publish posts without entering the admin page so that I can quickly share my views and analyses with readers.
   - As a regular reader, I want to read the contents of each post on its own page so that I can focus on the contents of the specific post at a time while being able to see other users' feedbacks to the particular post.
   - As a registered user, I want to be able to like posts and add comments so that I can express my impression and engage in a discussion.

- **Quteba forum**
   - As a first time visitor, I want to see sample forum entries so that I can decide if I want to join the discussions. 
   - As a registered user, I want to be able to create a discussion forum so that I can get answers to my questions and start conversations.
   - As a registered user, I want update or delete my own discussion forum entries so that I can opt out from a conversation whenever I want.
   - As a frequent user, I want to vote up or vote down a forum so that I can quickly reward or punish contents based on their importance and relevance without having to write comments. 
 
- **Nested threads**
   - As a dedicated user, I want to reply to comments on a forum I created so that I can open and lead an engaging conversation on relevant topics. 
   - As a registered user, I want to leave comments on discussion forums so that I can express my views and lead to further discussions.
   - As a frequent user, I want to be able to like or unlike comments and replies to express my opinions of them without having to write comments or replies.
   - As a registered user, I want to reply to other users' comments and replies so that I can follow the threads and identify the forkroads that emerge from the discussions.
   - As a forum reader, I want to see nested threads of forum topics, comments and replies so that I can visually see which replies are given to which comment.

- **Search for content**
   - As a user, I want to search for specific content so that I can find quick answers to the questions I have in mind.
   - As a user, I want to see excerpts of my search results so that I can quickly identify the most relevant content I want to read further.

- **User interaction**
   - As a user, I want to interact with the site smoothly so that I can see the effect of my actions without refreshing the pages.  
   - As a user, I want to contact the site admin so that I can ask questions and send comments to get clarifications and to express my opinions and expectations.

## The Scope Plane
### **Functional specifications**
When Quteba was built, the following set of features was planned. 
- User registration, login and logout features
- Read, update and delete features in user profiles
- Read and update blog posts, and create comments and add likes
- Create, read, update and delete forum entries
- Add comments and replies in forums
- Vote forums up or down, like or unlike comments and replies in threaded forums
- Search blogs and forums
- Create and send contact messages 
### **Content requirements**

Quteba presents two types of contents: 

1. Blog posts created by users with permission to do so or with the help of admin. 
2. Forums created by users who only need to be logged in. 

Comments on blog posts will be moderated by site admin to make sure that only relevant comments are visible. Logged in users will be able to add comments and replies, as in social media platforms such as Facebook. The scope of moderation in this feature is limited to the admin's ability to remove comments if need be there. 


*I would like to add a reporting mechanism, as a future enhancement, so that users can report offensive or irrelevant comments so that the admin can delete them.*

## The Structure Plane

The dual purpose of Quteba, blog and forum, needs to be made obvious to the user from the outset. First time visitors should land on the home page where they can see the main menu, a call to action invisiting new users to create account and registered users to sign in. 

Links to and brief descriptions of Qblog and Qforum should be presented in the same view port on medium to large sized screens. Moreover,

- First time users should be able to see static information about Quteba. The about page should be accessible from the menu bar. 

- To enable users to contact quteba without having to create an account, the contact page should be available to all users and be accessible from and with a single click on the menu bar.

- User registration should be easy and intuitive. The menu bar and the home page should have links to the sign up page. The same applies to user login. Users should be able to see the signup or signin page with a single click on the relevant and intuitively labeled link.

- The home page features Qblog and Qforum, links which should take the user to the respective sections in the home page. A pen icon should be used for Qblog to indicate that the content is text. The icon on Qforum should reflect that one expects a community of users in the forum.

- Qblog should be linked to the Recent Posts section where any user can read the titles and excerpts of three recent posts. Then users should be invited to sign up or signin to access all blog posts.

- Qforum should be linked to the Recent Forums section where any user can read three of the most recently created forums, not the entire thread. Then users should be invited to sign up or signin to access all threaded forums.

- A footer with social links that open in new tab should be presented at the bottom of each page. A copyright section in the footer should be used to link the home page so that users can click on it and go back to the home page.

- *Progressve disclosure:* When a user is logged in, the home page should still show the featured Qblog and Qforum links and sections. The menu bar will now show links to the entire lists of blog posts and forums as well as the user's profile image and a dropdown menu that toggles the username linked to the profile page and a logout link.

- *User profile:* Once a user is logged in, they should be able to read, update and delete their profile. These features should be accessible from the profile page which should be accessible from the menu bar.

- *Blog list:* While the home page displays three of the most recent posts, the entire list of blog posts should be shown in a dedicated page. This page should open with a single click on the Qblog menu item in the menu bar.

- *Blog detail:* While the blog list gives users the ability to have a quick glance at the title and excerpts to decide whether to continue reading a particuar post or not, the whole content of the post should be displayed on a separate page. This page should open with a single click on the post title in the blog list page.

- *Forum list:* The forum list page should present the list of forums so that users can pick the topics they like. Once they decide which forum to read, they should click only once to see the entire thread.

- *Thread:* A thread is a single discussion forum topic and all comments and replies under it. Each forum should have its own page so that users can stay focused on the topic while reading other people's comments and adding their own comments and replies.

- *Nested comments:* Quteba's users are likely to be familiar with most social media platforms. Presenting Qforum in a nexted forum-comments-reply structure with familiar icons for likes and unlikes will help the user leverage their experience in social media such as Facebook.

- *Dual search:* To provide users with what they want, a search feature should be added to the menu bar so that a user with specific concepts in mind can enter a search word and see results quickly. The search should be performed on both the blog and forum databases simultaneously so that the user will have more options. 

## The Skeleton Plane
### **Wireframes**

- **Home page:** First time users want to learn about quteba and its contents. The home page presents links to the about page while featuring Qblog and Qforum. After showing three blog posts and three forum entries, the user is invited to sign up or sign in to unlock the whole content. The home page has several places where the user is nudged to create account and login: menu items in the menu bar, first section in the home page and each of the Qblog and Qforum sections.

![Home page](assets/wireframes/home-page-guest-desktop.png)


- Wireframe for the [Home page on mobile](assets/wireframes/home-page-mobile.png)

- **Qblog:** Logged in users can easily navigate to Quteba Blog (Qblog) by using the menu bar or the button on the Recent Posts section of the home page. Qblog lists all blog entries displaying only title, author, date and excerpts of each post. The most recent entries are shown first. 

![Blog page](assets/wireframes/blog-list-page-desktop.png)


- Wireframe for the [Blog page on mobile](assets/wireframes/blog-list-page-mobile.png) 


- **Qforum:** The Forum list page allows users to read and create forums. The purpose of listing all forum entries without the comments and replies under them is to help the user choose a topic that is of interest to them before spending time reading the whole thread of each forum. If a user visits this page with the intension of asking a question or starting a conversation, they can create a forum directly. Each forum also shows the number of comments and replies in the thread as well as the number of up and down votes. 

![Forum list page](assets/wireframes/thread-list-page-desktop.png)

- Wireframe for the [Forum list page on mobile](assets/wireframes/thread-list-page-mobile.png) 


- **Threads:** A thread is a single forum and its comments and replies. A logged in user can comment on a forum, reply to comments and other replies (except one's own), vote up or down on a forum and like or unlike a comment or a reply.

![Forum detail page](assets/wireframes/single-thread-page-desktop.png)

- Wireframe for the [Forum detail page on mobile](assets/wireframes/single-thread-page-mobile.png) 


- **Profile:** Registered users can login and read their profile information in a dedicated profile page. The profile page has buttons which enable the user to update their profile information including their profile picture or delete their profile. 

![Profile page](assets/wireframes/profile-page-desktop.png)


- Wireframe for the [Profile page on mobile](assets/wireframes/profile-page-mobile.png) 

- **About page:** The about page provides static information about Quteba. It is accessible from the main menu for all users.

![About page on desktop](assets/wireframes/about-page-desktop.png)

- Wireframe for the [About page on mobile](assets/wireframes/about-page-mobile.png).  


## Information Architecture
The M (for Model) part of the MVC pattern plays a crucial role in providing users with dynamic information and allowing them to interact with the application. 

While the wireframes presented in the previous section show the view (template) side of the framework, the data architecture (represented in the Entity Relationship Diagram) below shows the models used to represent the data required to meet the site goals.
### **Database**

- Postgresql database was used to store information about Quteba's contents and its users. 

### **ERD**

- The ERD tool in postrgresql pgadmin 4 was used to generate the Entity Relationship Diagram for the data models. 

- Here is the ERD for the user, profile, blog post, forum category and thread models. 

![ERD](assets/wireframes/qerd_models.png)

A more detailed version of the ERD can be found [Here](assets/wireframes/qerd.png).


### **Data Models**
Quteba has the following data models, their respective field attributes and validators.
- **Allauth User Model**
    - I used Django's allauth for the user model. 

- **Profile Model**


| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| User          | user          | OneToOneField | User, on_delete=models.CASCADE, related_name='user_profile'    |
| Image        | image        | CloudinaryField    | default='default.jpg'     |
| Bio           | bio           | TextField    | max_length=255, null=True, blank=True      |



- **Post model**


| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
|Title          |title         |CharField  | max_length=200, unique=True    |
|Slug         |slug       |SlugField     |  max_length=200, unique=True      |
|Author       |author   |ForeignKey    |User, on_delete=models.CASCADE, related_name="blog_posts"       |
|Last Updated |last_updated   |DateTimeField    | auto_now=True       |
|Content      |content     |TextField    |       |
|Featured Image     |   featured_image  | CloudinaryField      |'image', default='placeholder'  |
|Excerpt        |excerpt       |TextField     |blank=True      |
|Created on           |created_on           |DateTimeField     |  auto_now_add=True     |
|Status            |status         |IntegerField    |choices=STATUS, default=0      |
|Likes            |likes       | ManyToManyField    |User, related_name='post_likes', blank=True      |


- **Post Comment Model**

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| Post          | post          | ForeignKey | Post, on_delete=models.CASCADE, related_name='comments'    |
| Name        | name        | CharField    |  max_length=50     |
| Email      | email    | EmailField    | null=True, blank=True      |
| Body    | body    | TextField    | max_length=200   |
| Created On    | created_on     | DateTimeField    | auto_now_add=True     |
| Approved      | approved      | BooleanField | default=False     |


- **Category Model**

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| Subject          | subject          | CharField| default='Uncategorized', max_length=50   |
| Description        | description        | TextField    | max_length=255     |
| Name      | name    | ForeignKey    | User, on_delete=models.CASCADE, related_name="categories"      |
| Created On    | created_on    | DateTimeField    | auto_now_add=True     |
| Status     | status    | IntegerField   | choices=STATUS, default=0     |
| Thread Count       | thread_count       | IntegerField | default=0      |


- **Thread Model**

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| Name          | name          | ForeignKey | User, on_delete=models.CASCADE, related_name='forum_topics'    |
| Topic        | topic        | CharField    | max_length=300, unique=True     |
| Slug      | slug    | SlugField    |max_length=300, unique=True      |
| Description    | description    | TextField    | max_length=500      |
| Category     | category     | ForeignKey    | Category, on_delete=models.CASCADE, related_name="threads"      |
| Status       | status       | IntegerField | choices=STATUS, default=0    |
| Created On       | created_on       | DateTimeField    | auto_now_add=True      |
| Up votes         | up_votes          | ManyToManyField    | User, blank=True, related_name='up_votes'     |
| Down votes           | down_votes           | ManyToManyField    | User, blank=True, related_name='up_votes'      |

- **Thread Comment Model**

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| Thread         | thread          | ForeignKey | Thread, on_delete=models.CASCADE, related_name='comments'    |
| Name       | name        | ForeignKey    |      |
| Content      | content    | TextField    | null=True, max_length=900     |
| Parent    | parent    | ForeignKey    | "self", null=True, blank=True, on_delete=models.CASCADE, related_name='replies'     |
| Created     | created     | DateTimeField    | auto_now_add=True      |
| Updated       | updated       | DateTimeField | auto_now_add=True      |
| Active       | active       | BooleanField    | default=True     |
| Likes          | likes          | ManyToManyField    | User, blank=True, related_name='comment_likes'      |
| Dislikes           | dislikes           | ManyToManyField    | User, blank=True, related_name='comment_dislikes'       |


- **Contact Model**

name = models.CharField(blank=False, max_length=200)
   

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| Name         | name          | CharField | blank=False, max_length=100    |
| Email        | email        | EmailField    |      |
| Subject      | subject    | CharField    | blank=False, max_length=200     |
| Message    | message    | TextField    | max_length=500, blank=False      |



## The Surface Plane

### **Color Scheme**


- The main color used in this website is a deep green (British Racing Green) color, which is a calming color, with varying intensity.

- To create a good contrast, I used white text on the deep green background.
- I used lightsalmon color for the site logo, which is an alphabet representing 'Qu' in my native language, Tigrinya.The lightsalmon color makes the logo stand out in the deep green background color of the navbar. 
- Red, Green and Blue colors in buttons and links are mainly from bootstrap classes ending with 'danger', 'success' and 'primary' respectively. As they give good contrast, contextual meaning (as in using danger for delete button, for example), these colors have fitted well. 

![Main color](assets/screenshots/color-palette.png)


### **Typography**

- I used the Roboto font family for the body.
- I used Robik font family for the headings.
- The font in the blog articles comes from summernote because of the WYSIWYG property of working with the latter. I did not change the summernote configuration because the the Verdana font in summernote looks good for blog posts. 


### **Imagery**

- The background image throughout the site was generated from the [BGJar website](https://bgjar.com/). The icons in the background image reflect various consumer items that are central to the user's economic decision problems.

- [Quteba's Background image](/static/images/qu-bg.png).


# Features

## Existing Features

Quteba Blog (Qblog) and Quteba Forum (Qforum) being the two broad categories of services that this website aims to provide, the following specific features have been implemented to meet the aforementioned user stories.  

* **Homepage:** Quteba's homepage provides first time users with information and links that helps them navigate the website easily. The dual purpose of the site is made clear from the outset.

![Home page](assets/screenshots/home-section-one-guest.png)

* Users see links to and information about Qblog and Qforum. There is a nav bar at the top which presents different menu items, so users can choose with a single click to view what quteba is about, a sign up page or if they have an account a sign in page.

* The home page also presents three recently added blog entries and three recent discussion forum topics in separate sections. 

![Home page, recent posts section](assets/screenshots/recent-posts.png)

* This gives users the chance to have a quick glance at what kinds of topics and questions are being discussed. From users' perspective, this preview is important because it gives them an idea of what to expect before delving into the whole list of either Qblog or Qforum.

![Home page, recent forums section](assets/screenshots/recent-forums.png)


* **The navigation menu:** This is visible in the home page and all other pages. Only some of the items in the menu change depending on whether the user is authenticated in or not. The menu item the user is currently visiting gets a border at the bottom to tell the user where in the site they are.


![Navigation bar for unauthenticated user](assets/screenshots/navbar-guest.png)

* Authenticated users see links not only to Qblog and Qforum but also a dropdown menu which toggles the link to the profile page and a logout menu item.


![Navigation bar for authenticated user](assets/screenshots/navbar-authenticated.png)

* **Search form:** Users who are looking for a particular concept may search for related posts and forums by typing a keyword in the search input form. If the keyword exists in Qblog and/or Qforum, the results are displayed in a separate search results page.

  ![Search form](assets/screenshots/search-form.png)

* **Search results page:** This page renders the search results when a user searches for a specific keyword and a matching entry is found in either Qblog or Qforum or both. 

 ![Search results](assets/screenshots/search-result.png)

* If the keyword the user types in the search form does not exist, the results page shows the following feedback message. 

 ![Search with no results to show](assets/screenshots/search-no-result.png)

* **About page:** the [about page](assets/screenshots/about-page.png) is a static page that gives users important information about the background and services of quteba. Users who come across quteba for the first time can read the about page and learn what quteba means and holds. 

* **Qblog:** Qblog lists blog entries showing the author, title, date and excerpts of each blog post. The title is clickable and linked to the blog detail page. By viewing only the list of blog posts, users need not read each blog before they find what they might like. The excerpts will give users enough information to help them decide whether to continue reading or to find another article. There is also a button next to the excerpt which is linked to the details page.

![Blog list page](assets/screenshots/blog-list.png)

* To make adding posts easier, there is a possibility to create a blog post from the blog list page. This functionality is, however, available to superusers in the current scope. The idea is that when Quteba grows and starts having regular contributors, a group of users with specific permissions can be created and authors can then be allowed to use the create post functionality without having the need for admin access.
* [Create post page](assets/screenshots/create-post.png) available only for superuser for now.


* **Blog detail page:** The blog detail page shows the title of the article, author, date, content, likes and comments (if any). Logged in users also see a form where they can type and submit a comment.

![Post detail page](assets/screenshots/post-detail.png)

* The author of the post will see a link to the update post page. A delete functionality is not available at this stage, so only the admin can do that when the need arises. Unlike all other parts of the website, the font type of the post content comes from summernote, as mentioned earlier.
 
* **Qforum:** The purpose of having the Qforum on the menu bar and a list of forum entries (thread list) is similar to that of Qblog. Users can click on the Qforum menu item and land on a page that lists discussion forums. As each forum has a topic and description (question text), users can get an idea of what a particular discussion forum is about. 

![Forum list page](assets/screenshots/forum-list.png)

* **Categories:** refer to broad areas of economics that encapsulate the particular discussion topics. For example, a category can be Finance while the discussion topics may relate to specific concepts such as exchange rate. Only the admin creates categories for now, but in future implementations, categories will be useful to help users sort articles and discussion topics.

* **Create forum:** The Qforum page has a form for users to submit questions. It is placed at the top but users need to click and a modal will pop up. This is efficient because the form does not cover the most central part of the page for users who are interested in reading the forums. It is also intuitively self-evident that a user should click it to create a forum.

![Create forum modal](assets/screenshots/create-forum.png)

* Qforum lists forums based on the date they were created, starting with the most recent ones. Users can see the number of upward votes (green arrow), downward votes (red arrow), and comments and replies associated with each discussion forum. Voting and commenting are possible only in the forum detail page.

* **Forum detail page:** When a user clicks on a particular discussion forum topic in the Qforum list page, a separate page will open with the particular forum at the top and any comments and replies under it. 

![Forum detail page](assets/screenshots/forum-detail.png)

* A user can [edit or delete](assets/screenshots/edit-forum.png) their own discussion forum and reply to comments and replies except their own. To this effect, the buttons a user sees in this page vary depending on whether the user is authenticated or not and if the entries are their own or those of others.

![Forum detail page](assets/screenshots/forum-reply.png)

* The numbers indicated in the above screenshot of a typical forum detail page represent the following use cases.
    1. Voting up if you like the discussion forum in general
    2. Voting down if you do not like the discussion forum in general
    3. Like a particular comment or reply
    4. Dislike a particular comment or reply
    5. Reply to a particular comment or another reply (not available for own comment or reply).

* The forum comment modal is used to add comments. (Comments and replies can be confusing. I use 'comment' to refer to comments given directly to a forum entry. Replies are also comments but they have a parent comment.)

![Forum comment modal](assets/screenshots/forum-comment.png)

* **Sign up page:** New users are encouraged to sign up so that they can not only read what others have written but also engage in conversations by creating forums and through comments and replies. Users who decide to sign up at the very beginning will see the sign up menu item, which is also available throughout the quteba pages. 

![Sign up page](assets/screenshots/signup.png)

* **Sign in Page:** If a user has an account, they can login so that they can interact with Quteba in more ways than they otherwise would. 

![Login page](assets/screenshots/login.png)

* An authenticated user can do many CRUD operations: 
  - read all contents that others have created
  - add comments to blog posts
  - like blog posts 
  - create a discussion forum 
  - comment on a forum
  - reply to comments 
  - vote up or down on forums
  - like or unlike replies
  - edit or delete their own forums
  - update and delete their profiles 

* **Profile page:** When a user logs in, they see on the menu bar their profile picture and a dropdown menu that toggles their username and logout menu. By clicking on their username, the user can view their profile which has two buttons linked to (1) profile update form and (2) profile delete page.

![Profile page](assets/screenshots/profile.png)


* **Update profile:** The profile update page enables users to edit and update their profiles. The user can change their profile picture and update their bio. When they save the changes, they are redirected to the profile page.

  * [Update profile page](assets/screenshots/profile-update.png)

* **Delete profile:** If a user wants to delete their profile, they can do so by using the link provided in the profile view page. To make sure that a user does not suddenly delete their profile, the user is asked confirm that they want to delete the profile. If the user does not want to continue with the deletion of the profile, they can cancel the process in the confirmation page and go back to the profile view page.

  * [Delete profile page](assets/screenshots/profile-delete.png)

* **Logout page:** When a logged in user wants to sign out, they can do so by clicking on the sign out menu in the navigation bar. They can sign out from any page because the navigation bar is available on all pages.
Once they click on sign out, they are asked to confirm that they want to logout. If the user does not want to complete the process, they can cancel it and go back to the (profile page).

  * [Logout confirmation page](assets/screenshots/logout.png)

* **Footer:** The footer section is displayed at the bottom of each page to help users follow the social links or click on **Quteba** in the copyright section to go back to the home page. The social links open in new tabs.

![Main color](assets/screenshots/footer.png)

### **User Interaction**

One of the key principles of Quteba is user engagement. Users can create discussion forums that can be big threaded forums with many comments and replies. 

Here is a recap of what actions are available for authenticated users. 

  - **Create a forum:** A lLogged in user can create forums using the create forum form modal. They choose a category from a given list of categories, enter a topic and write a description of the issue they want other quteba users to address. On submitting the forum, an ajax call handles the backend interaction and the user sees the forum they just created without a page reload. This gives the user a good user experience.

  - **Leave comment:** Comments and replies are technically the same. The only difference is that a comment is the direct child of a forum while a reply follows a comment or another reply. A forum, its comments, replies to comments and replies to replies create a nested tree. Users can add comments to forums by using a comment form modal that pops up when a user clicks on the comment button which displays a down arrow to hint that a click on the button opens a form. Comments in forums are handled by ajax call and the page updates without reload.

  - **Reply:** As mentioned above, a reply is just a comment on a comment or another reply. Their action takes effect in real time, thanks to ajax. Users see the same form when they subit a comment as when they write a reply. In this implementation, users cannot edit or delete comments or replies.
   
  - **Like/unlike a comment/reply:** For users who want to express their views with minimal effort, each comment as well as reply has like and dislike features. A logged in user can like a comment or a reply, or dislike a comment or a reply. Ajax code takes care of the request and page update.

  - **Up/down vote a forum:** The voting feature is added only to forums. A user who likes or dislikes a thread (a forum and the comments and replies thereof) can vote up or down respectively. While this captures the user's opinion about the whole issue in a particular forum, it is possible, perhaps in future enhancement, to use the votes as a basis for ranking forums such that forums with highest number of positive votes are, for example, featured in the landing page. For better user experience, the votes are also handled by ajax code behind the scenes.

A common characteristic of the above modes of user interactions are that they use ajax calls to make the user experience smooth. For the likes and dislikes, one can only like or dislike, but not both, at a time. The same applies to votes: if one has voted up and click on vote down, the up vote is removed and the down vote increases by one.

## Future Enhancements
    
- ### Email notifications
     - In the future, implementing the functionality to send automated email notifications of new content to registered users can enhance the useability of quteba.

- ### Ability to view others' profiles and follow them

     - I want to improve the user profile view such that users can see other users' profiles and follow their activities on Quteba such as the forums they create and the comments they give.

- ### Ability to filter content by category and other criteria

     - I want ti implement filter and sort functionalities with different options to filter content with such as categories, most popular and similar to previously viewed content.
     - I want to use the votes as a basis for ranking forums so that users can sort forums based on this ranking.

- ### Ability to use audio and video in the forum

     - As the digital society today is often using audio and video content in most social media platforms, I want to create functionalities for Quteba users to exchange their economic information using audio or video.

- ### Register with social media

     - To make it easier for first time users to register in Quteba, I would like to implement in the future the ability to register with social media such as Facebook or with Google.


## Technologies Used

This project requires the use of Full Stack Tools. Django was used for the backend and JavaScript, HTML and CSS for the front-end. 

Postgresql was used for the database and psycopg2 was used as an Object Relational Mapper (ORM) tool. Below is a [list of all the technologies](https://github.com/Amareteklay/quteba/blob/main/requirements.txt) used in this project.

- ### **Languages:**

    + [Python 3.8.11:](https://www.python.org/downloads/release/python-385/) is the primary language used to develop the back-end.
    + [JS:](https://www.javascript.com/) was used to add interactivity to the website.
    + [HTML5:](https://developer.mozilla.org/en-US/docs/Web/HTML) was used to create the structure of the website.
    + [CSS:](https://developer.mozilla.org/en-US/docs/Web/css) was used for beautifying the website.

- ### **Frameworks and libraries:**

    + [Django:](https://www.djangoproject.com/) framework was used to handle all the logic.
    + [jQuery:](https://jquery.com/) was used to control events and send AJAX calls.
    + [Bootstrap5:](https://getbootstrap.com/) was used to make the website responsive.

- ### **Databases:**
    + [PostgreSQL:](https://www.postgresql.org/) the database used to store all the data.
- ### **Other tools:**
    + [Git:](https://git-scm.com/) the version control system used to manage the code.
    + [Pip3:](https://pypi.org/project/pip/) the package manager used to install the dependencies.
    + [Spycopg2:](https://www.python.org/dev/peps/pep-0249/) the ORM used to connect to the database.
    + [Django-allauth:](https://django-allauth.readthedocs.io/en/latest/) was used to create the user accounts.
    + [Django-crispy-forms:](https://django-cryptography.readthedocs.io/en/latest/) was used to control the rendering behavior of Django forms.
    + [Heroku:](https://dashboard.heroku.com/) was used to host the website.
    + [GitHub:](https://github.com/) was used to host the quteba's source code and resources.
    + [Gitpod](https://gitpod.io/) and [VSCode:](https://code.visualstudio.com/) were used to develop the website.
    + [Chrome DevTools:](https://developer.chrome.com/docs/devtools/open/) was used to debug the website and to conduct lighthouse test.
    + [Font Awesome:](https://fontawesome.com/) was used to create the icons used in the website.
    + [Coolors:](https://coolors.co/202a3c-1c2431-181f2a-0b1523-65e2d9-925cef-6b28e0-ffffff-eeeeee) was used to make a color palette for the website.
    + [BGJar:](https://www.bgjar.com/) was used to make a background images for the website.
    + [W3C Validator:](https://validator.w3.org/) was used to validate HTML5 code for the website.
    + [W3C CSS validator:](https://jigsaw.w3.org/css-validator/) was used to validate CSS code for the website.
    + [JShint:](https://jshint.com/) was used to validate JavaScript code for the website.
    + [PEP8:](https://pep8.org/) was used to validate Python code for the website.
    + [Cloudinary:](https://cloudinary.com/) was used to upload images and other media files.
    + [Techsini:](https://techsini.com/multi-mockup/index.php) was used to generate a mock up for responsive design for various screen sizes.
    + [Responsive viewer:](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?hl=en) chrome extension was used to test quteba on different screen sizes and download screenshots.
    + [Balsamiq Cloud:](https://balsamiq.cloud/) to create wireframes.


# Testing

Detailed testing and documentation of test results [are presented in a dedicated file here](TESTING.md).

* I used both manual and automated testing to test the functionalities of the website work as intended.

* All the code for the website has been validated using tools like:

   * W3C Markup validator for HTML
   * Jigsaw CSS validator for CSS
   * JSHint for JavaScript
   * PEP8 for python code

* Responsiveness has been checked and the website is fully responsive.

* Lighthouse test was used to inspect the compliance of the website to best practices and to measure its performance. The scores are high (well above 90 for most pages in both mobile and desktop views.)

* All user stories have been tested and the features that are intended to address all user stories are working. 
#
## Bugs

- Commenting on a forum entry for the first time failed because the function after a successful Ajax connection was not able to find the comment box. The new comment is supposed to be added to the comment box, but I had specified the 'afterbegin' parameter while the box never began. I fixed this by putting a div with the target comment-box class. 

![Ajax bug fixed](assets/screenshots/ajax-bug-fixed.png)

- The text below the forum entry prompts users to be the first to comment. While this is its face value, the div containing this text was added to help the JavaScript code that runs after a successful Ajax call to find the right place where the new comment should be placed.

- I have noticed that the google fonts I set in the CSS do not override the summernote font family in the blog detail page. I haven't fixed this because it is a minor bug, in terms of its effect in this particular case, because the summernote 'Verdana' font looks good in the blog post page. 
- There was a problem in some pages having not enough content and the footer hanging in the middle of the page. I followed [these tips](https://www.freecodecamp.org/news/how-to-keep-your-footer-where-it-belongs-59c6aa05c59c/) to fix this problem. I give credit to the source in the credit section as well.


# Deployment

Quteba is deployed using Heroku hosting service, and it is live at [quteba.herokuapp.com](https://quteba.herokuapp.com/).
## Deployment to Heroku

The following steps are followed to deploy the website to Heroku.
1. Create an account and Login to [Heroku](https://www.heroku.com/).
2. Create a new app on Heroku using the following steps.
    - Go to your Heroku dashboard.
    - Click on the "New" button.
    - Click on the "Create new app" button.
    - Give your app a name, e.g., Quteba.
    - Choose your nearest region.
    - Click on the "Create app" button.
3. In your app go to the "Resources" tab.
    - Add a Heroku Postgres database.
4. In your app go to the "Settings" tab, press "Reveal Config Vars", and add the following config vars or check if they are already added.
      - `DATABASE_URL` = The URL of the database provided by Heroku Postgres.
      - `SECRET_KEY` = The secret key for your Django project.
      - `CLOUDINARY_CLOUD_NAME` = Your Cloudinary Cloud Name.
      - `CLOUDINARY_API_KEY` = Your Cloudinary API Key.
      - `CLOUDINARY_API_SECRET` = Your Cloudinary API Secret.
      - `DEBUG` = True during development, False during production.
      - `DISABLE_COLLECTSTATIC` = Set to `1` to disable collectstatic during the development.


     *Note that you should change the DEBUG config var to False and remove the DISABLE_COLLECTSTATIC config var from the config vars on heroku after completing the development.*


    - To get cloudinary cloud name, api key, and api secret:

        - Go to the Cloudinary [website](https://cloudinary.com/).
        - Create an account, or log in to your account if you already have an account.
        - Go to the Cloudinary dashboard.
        - At the top of the page you will see your cloud name, api key, and api secret.
        - Copy these values and paste them into the config vars on heroku and into your env.py file.

5. In your app go to the "Deploy" tab.
  - Using GitHub:
      - Connect your Heroku account to your GitHub account and then click on the "Deploy" button. 
      - You can enable automatic deployment. 
      
  - Using Heroku CLI: 
      - Go to your local repository
      - Login to your Heroku account in your terminal and connect your local repository to your heroku app.
          ```
          heroku login -i
          ```
      - Enter your Heroku credentials.
      - Enter the following command to connect your heroku app and your local repository.
          ```
          heroku git:remote -a <your-heroku-app-name>
          ```
6. Create a Procfile.

7. Create requirements.txt. This can be done by running the following command:
          ```
          pip freeze > requirements.txt
          ```
8. Add and commit all changes.
9. Push your changes to Heroku.
    ```
    git push heroku <master or main>
    ```
10. Check the logs of your app in the Heroku dashboard for potential errors or click on the "Open app" button to see your deployed site.

## Local Deployment
### **Forking Quteba**

To fork the repository:

1. Log in (or sign up) to Github.
2. Go to the repository for this project, [Quteba](https://github.com/Amareteklay/quteba).
3. Click the Fork button in the top right corner.

### **Cloning Quteba**

To clone the repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, [Quteba](https://quteba.herokuapp.com/).
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.


# Credits

- I followed [this tutorial](https://replit.com/talk/learn/DjangoPython-and-HTML-Coding-Campus-Tutorial-1-Create-a-Blog-with-Django/142238?order=new) to create the initial structure of blog posts.

- I used the articles and code in [this page](https://www.devhandbook.com/django/user-registration/) to create user registration and profile.

- I began the blog list page by borrowing code from [this](https://replit.com/talk/learn/DjangoPython-and-HTML-Coding-Campus-Tutorial-1-Create-a-Blog-with-Django/142238?order=new) and [this](https://github.com/Code-Institute-Solutions/Django3blog/blob/master/10_likes/templates/index.html), which I later changed substantially.

- I took the data model for the forum from [this article](https://vertabelo.com/blog/database-model-for-an-online-discussion-forum-part-1/).

- I followed [this tutorial](https://focusustech.com/blog/create-a-comment-and-reply-system-in-django) to modify forum views and templates.

- I followed [this tutorial](https://learndjango.com/tutorials/django-search-tutorial) to implement search functionality.

- I used [this online converter](https://svgtopng.com/) to generate png from svg, which was created using [bgjar](https://bgjar.com/).

- Nav bar and footer background color was inspired by [this](https://www.mp.se/goteborg/just-nu/goteborg-ska-vara-en-karnvapenfri-zon/).

- I copied and edited the deployment procedure in this documentation from our [hackathon project readme](https://github.com/PratimaGurav/Team4-May-Hackathon).
- Code for user registration and signals was adapted from [this](https://www.devhandbook.com/django/user-registration/) and [this](https://www.devhandbook.com/django/user-profile/).
- I followed [these steps](https://medium.com/analytics-vidhya/provisioning-a-test-postgresql-database-on-heroku-for-your-django-app-febb2b5d3b29) to run the first unittest.
- I also used [this tutrial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing#overview) as an example and to copy and adapt code for testing views.
- I took this [Female avatar](https://www.iconspng.com/uploads/female-avatar/female-avatar.png) and this [Male avatar](https://www.w3schools.com/howto/img_avatar.png), and used them as profile images for a test users.
- In some pages where the content is small, the footer would hang in the middle of the page. I followed [these tips](https://www.freecodecamp.org/news/how-to-keep-your-footer-where-it-belongs-59c6aa05c59c/) to keep the footer at the bottom of the page even when there no enough content.

## Acknowledgements

I have learnt from [Daisy](https://github.com/Daisy-McG), my mentor at the [Code Institute](https://codeinstitute.net/), many ways to make this project better. Her valuable comments have enhanced the quality of this website a lot. Thank you [Daisy](https://github.com/Daisy-McG)! 

# 

## [BACK TO TOP](https://github.com/Amareteklay/quteba#readme)