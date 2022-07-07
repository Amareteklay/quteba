# Testing Quteba

## Unittests

- I followed [these steps](https://medium.com/analytics-vidhya/provisioning-a-test-postgresql-database-on-heroku-for-your-django-app-febb2b5d3b29) to run the first unittest.
- I also used [this tutrial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing#overview) as an example and to copy and adapt code for testing views.


## Manual Testing





|     | User Actions           | Expected Results | Y/N | Comments    |
|-------------|------------------------|------------------|------|-------------|
| Sign Up     |                        |                  |      |             |
| 1           | Click on Sign Up button | Redirection to Sign Up page | Y |          |
| 2           | Click on the Login link in the form | Redirection to Login page | Y |          |
| 3           | Enter valid email | Field will only accept email address format + unique email | Y |          |
| 4           | Enter the same email in the field email | Field will only accept email address format and the email that has been entered in the previous field | Y |          |
| 5           | Enter valid password  | Field will only accept secure passwords | Y |          |
| 6          |  |  |  |  




### Python Validation

I used [pep8 online checker](http://pep8online.com/) to validate all python code. 

- Home app


- Qblog


- Qforum


- Quteba


- Users


- Testing




### HTML Validation


### JavaScript Validation


### CSS Validation

<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>
