# Testing Quteba
#

## Manual Testing
# 

|     | User Actions           | Expected Results | Y/N | Comments    |
|-------------|------------------------|------------------|------|-------------|
|Home page           |  |  |  | 
|1           |Click on the 'Create Account' button  |  |  | 
|2           |Click on the 'Sign in' button  |  |  | 
|3           |Click on the 'Qblog' heading  |  |  |  
|4           |Click on the 'Qforum' heading  |  |  | 
|5           |Click on the 'Sign up' links in the Recent Posts and Recent Forums sections  |  |  | 
|6           |Click on the 'Sign in' links in the Recent Posts and Recent Forums sections  |  |  | 
|7           |Click on the title of each post  |  |  | 
|8           |Click on the title of each forum entry  |  |  |  
| Sign Up     |                        |                  |      |             |
| 1           | Click on Sign Up button | Redirection to Sign Up page | Y |          |
| 2           | Click on the Login link in the form | Redirection to Login page | Y |          |
| 3           | Enter valid email | Field will only accept email address format + unique email | Y |          |
| 4           | Enter the same email in the field email | Field will only accept email address format and the email that has been entered in the previous field | Y |          |
| 5           | Enter valid password  | Field will only accept secure passwords | Y |          |
|Login           |  |  |  | 
|1           |Click on the 'Sign in' button  |  |  | 
|2           |If you don't have an account yet, Click on the 'Sign up' link in the login page  |  |  | 
|3           |Enter your username in the Username field |  |  |  
|4           |Enter your password in the 'Password' field  |  |  | 
|5           |Click on the 'Sign in' button  |  |  |  
|Qblog          |  |  |  | 
|1         |If you are logged in as superuser, Click on the 'Create Blog' button  |  |  | 
|2           |Click on the title of each blog post  |  |  | 
|3           |Click on the 'Read More' button at the end of each excerpt  |  |  | 
|Single blog page           |  |  |  | 
|1           |If you are logged in as superuser, click on the 'Edit post' link  |  |  | 
|2           |Click on the like button (thumbs up icon)  |  |  | 
|3           |Type a comment in the text area and click on the Submit button   |  |  | 
|Qforum           |  |  |  | 
|1           |Click on the 'Create Forum' button  |  |  | 
|2          |Click on the title of each forum entry  |  |  | 
|3         |Click on the title of each item on the recent topics in the side bar  |  |  | 
|Thread page (Single forum entry)           |  |  |  | 
|1           |Click on the green upward arrow  |  |  | 
|2          |Click on the red downward arrow  |  |  | 
|3          |Click on the 'Comment' button  |  |  | 
|4           |If you click on the 'Comment' button, type your comments in the text are that pops up and click on Submit  |  |  |
|5          |If you are the author of the forum entry, Click on the pencil icon  |  |  | 
|6          |If you are the author, click on the delete (trash) icon  |  |  | 
|7           |Click on the like icon (thumbs up symbol)  |  |  | 
|8           |Click on the dislike icon (thumbs down symbol)  |  |  | 
|9           |If you're not the author of a comment or a reply, click on the 'Reply' button  |  |  | 
|10          |If you click on the 'Reply' button, type your reply in the text area that expands and click on Submit  |  |  | 
|Navigation bar           |  |  |  | 
|1           |Click on the 'Home' menu item  |  |  | 
|2           |Click on the 'About' menu item  |  |  | 
|3           |Click on the 'Contact us' menu item  |  |  | 
|4           |Click on the 'Qblog' menu item  |  |  | 
|5           |Click on the 'Qforum' menu item  |  |  | 
|6           |Click on your <username> in the menu bar  |  |  | 
|7           |Click on the 'Logout' menu item  |  |  |
|8           |Click on the 'Sign out' button  |  |  | 
|9           |Click on the 'Cancel' button in the sign out page  |  |  | 
|Search           |  |  |  | 
|1           |Enter search word in the search form  |  |  | 
|2           |Click on the search icon  |  |  | 
|Contact page           |  |  |  | 
|1           |Enter your name in the Name field  |  |  | 
|2           |Enter your email in the Email field  |  |  | 
|3           |Enter a subject in the Subject field  |  |  | 
|4           |Write your message in the Message field  |  |  | 
|5           |Click on the 'Send Message' button  |  |  | 
|Profile page           |  |  |  | 
|1           |If you have logged in, click on your <username> in the menu bar  |  |  | 
|To update profile           |  |  |  |
|2           |Click on the 'Update Profile' button  |  |  |  
|3           |You can edit or change your username in the 'Username' field  |  |  | 
|4           |You can edit or change your email in the 'Email' field  |  |  | 
|5           |You can edit or change your bio in the 'Bio' field  |  |  | 
|6           |You can click on the 'Choose File' button to upload a new profile image  |  |  | 
|7           |Click on the 'Update' button to save changes  |  |  |
|To delete profile           |  |  |  | 
|2           |Click on the 'Delete Profile' button  |  |  | 
|3           |Click in the 'Confirm Delete' button  |  |  | 
|4           |Click on the 'Cancel' button  |  |  | 
|           |  |  |  | 
 

## Automated Testing
# 


- I followed [these steps](https://medium.com/analytics-vidhya/provisioning-a-test-postgresql-database-on-heroku-for-your-django-app-febb2b5d3b29) to run the first unittest.
- I also used [this tutrial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing#overview) as an example and to copy and adapt code for testing views.


## Testing User Stories
# 


|User Stories     |Acceptance Criteria met? (Y/N)           |  |  | Comments    |
|-------------|------------------------|------------------|------|-------------|
|As a first time visitor I want to get information about the site so that I can understand the what the site focuses on and how I can make the best out of it.           | Y |  |  | 
|As a first time visitor, I want to be able to navigate the site so that I can find the most important information with the least amount of effort.            | Y |  |  | 
|As an engaged user, I want to see relevant feedback so that I can understand if my interactions with the site are successful or not.           | Y |  |  | 
|As a user, I want to know which menu item is active so that I can know which part of the site I am navigating at each moment.     |  Y  |   |  |
| As a user, I want to be able to access quteba's contents and functionalities from my mobile or tablet so that I do not have to wait until I find a computer.  |  Y |   | |
| As a frequent user, I want to follow the site owner on social media so that I can see recent activities and updates from my favourite social media apps.  |  Y  |    | |
| As a first time visitor I want to sign up so that I can have login credentials which I can use to login to the site every time I want to use it. | Y |  |
| As a registered user, I want to be able to login with my registereg credentials so that I can access my profile as well as all the contents and functionalities that require that users be logged in. | Y |  |
| As a logged in user, I want to be able to logout easily so that I feel safe that others do not interact with the site via my account. |Y  |  |
| As a registered user I want to have a profile so that I can choose a profile picture and share my bio with other quteba users. |  Y|  |
| As a registered user I want to update and delete my profile so that I have control of what I want to do with my personal information. | Y |  |
| As a reader I want to read excerpts of blog posts so that I choose which articles to read without going through the whole content of each post. | Y |  |
| As a contributor I can create drafts and publish posts without entering the admin page so that I can quickly share my views and analyses with readers. | Y |  |
| As a regular reader, I want to read the contents of each post on its own page so that I can focus on the contents of the specific post at a time while being able to see other users' feedbacks to the particular post. | Y |  |
| As a registered user I want to like posts and add comments so that I can express my impression and engage in a discussion. | Y |  |
| As a first time visitor I want to see sample forum entries so that I can decide if I want to join the discussions. | Y |  |
| As a registered user, I want to create a discussion forum so that I can get answers to my questions and start conversations. As a user, I want update or delete my own discussion forum so that I can opt out from a conversation that takes a different direction from I initially intended. | Y |  |
| As a frequent user, I want to vote up or vote down a forum so that I can quickly reward or punish contents based on their importance and relevance without having to write comments. | Y |  |
| As a dedicated user, I want to reply to comments on a forum I created so that I can open and lead an engaging conversation on relevant topics. | Y |  |
| As a registered user, I want to leave comments on discussion forums so that I can express my views and lead to further discussions. | Y |  |
| As a frequent user, I want to like or unlike comments and replies to express my opinions of them without having to write comments or replies. | Y |  |
| As a registered user, I want to reply to other users' comments and replies so that I can follow the threads and identify the forkroads that emerge from the discussions. | Y |  |
| As a forum reader, I want to see nested threads of forum topics, comments and replies so that I can visually see which replies are given to which comment. | Y |  |
| As a user, I want to search for specific content so that I can find quick answers to the questions I have in mind. | Y |  |
| As a user, I want to see excerpts of my search results so that I can quickly identify the most relevant content I want to read further. |Y  |  |
| As a user, I want to interact with the site smoothly so that I can see the effect of my actions without refreshing the pages. | Y |  |
| As a user I want to contact the site admin directly so that I can ask questions and send comments to get clarifications and to express my opinions and expectations. |  Y|  |
|    |  |  |



## Validation
#

### Python Validation

I used [pep8 online checker](http://pep8online.com/) to validate all python code. The whole pep8 validation report is available [here](/assets/testing/pep8_validation.pdf).

- Home app
Python files in the home app checked for pep8 compatibility:
    - [Home app-py](/assets/testing/home-app.png)
    - [Home admin-py](/assets/testing/home-admin.png)
    - [Home forms-py](/assets/testing/home-forms.png)
    - [Home models-py](/assets/testing/home-models.png)
    - [Home urls-py](/assets/testing/home-urls.png)
    - [Home views-py](/assets/testing/home-views.png)


- Qblog
    - [Qblog app-py](/assets/testing/qblog-app.png)
    - [Qblog admin-py](/assets/testing/qblog-admin.png)
    - [Qblog forms-py](/assets/testing/qblog-forms.png)
    - [Qblog models-py](/assets/testing/qblog-models.png)
    - [Qblog urls-py](/assets/testing/qblog-urls.png)
    - [Qblog views-py](/assets/testing/qblog-views.png)

- Qforum
    - [Qforum app-py](/assets/testing/qforum-app.png)
    - [Qforum admin-py](/assets/testing/qforum-admin.png)
    - [Qforum forms-py](/assets/testing/qforum-forms.png)
    - [Qforum models-py](/assets/testing/qforum-models.png)
    - [Qforum urls-py](/assets/testing/qforum-urls.png)
    - [Qforum views-py](/assets/testing/qforum-views.png)

- Quteba
    - [Quteba app-py](/assets/testing/quteba-asgi.png)
    - [Quteba admin-py](/assets/testing/quteba-settings.png)
    - [Quteba forms-py](/assets/testing/quteba-urls.png)
    - [Quteba models-py](/assets/testing/quteba-views.png)
    - [Quteba urls-py](/assets/testing/quteba-wsgi.png)

- Users
    - [Users app-py](/assets/testing/users-app.png)
    - [Users admin-py](/assets/testing/users-admin.png)
    - [Users forms-py](/assets/testing/users-forms.png)
    - [Users models-py](/assets/testing/users-models.png)
    - [Users urls-py](/assets/testing/users-urls.png)
    - [Users views-py](/assets/testing/users-views.png)

- Testing
    - [Testing app-py](/assets/testing/tests-forms.png)
    - [Testing models-py](/assets/testing/tests-models.png)
     - [Testing urls-py](/assets/testing/tests-signals.png)
    - [Testing urls-py](/assets/testing/tests-urls.png)
    - [Testing views-py](/assets/testing/tests-views.png)



### HTML Validation

[HTML validation report](/assets/testing/html_validation.pdf)
### JavaScript Validation


### CSS Validation

<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

## Responsiveness
#

