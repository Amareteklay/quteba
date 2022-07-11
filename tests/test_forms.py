from django.test import TestCase
from django.contrib.auth.models import User
from qforum.forms import ThreadForm, CommentForm
from qblog.forms import CommentForm as PostCommentForm
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from users.models import Profile
from qforum.models import Category


class TestThreadForm(TestCase):
    """
    Unittest for thread form
    """
    @classmethod
    def setUp(self):
        self.user1 = UserRegisterForm(data={
            "username": "amuser",
            "email": "usermail@mail.com",
            "password1": "resdhjh12A.",
            "password2": "resdhjh12A."
            })
        self.user2 = User.objects.create(id=1, username='Aman',
                                         email='aman@mail.com',
                                         password='123someTest')
        self.category = Category.objects.create(id=1,
                                                subject='Technology',
                                                name=self.user2,
                                                description='Test category')
    def test_empty_form(self):
        form = ThreadForm()
        self.assertIn('topic', form.fields)
        self.assertIn('category', form.fields)
        self.assertIn('description', form.fields)

    def test_thread_form_is_valid(self):
        form = ThreadForm(data={
            "category": self.category,
            "topic": "Django for beginners",
            "description": "I want to know how to learn django effectively."
            })
        self.assertTrue(form.is_valid())

    def test_thread_form_is_invalid(self):
        form = ThreadForm(data={
            'category': "Technology",
            'topic': "",
            'description': "I want to know how to learn django effectively."
            })
        self.assertFalse(form.is_valid())


class TestCommentForm(TestCase):
    """
    Unittest for thread comment form - forum app
    """
    def test_empty_form(self):
        form = CommentForm()
        self.assertIn('content', form.fields)

    def test_comment_form_is_valid(self):
        form = CommentForm(data={"content": "I will comment later."})
        self.assertTrue(form.is_valid())

    def test_comment_form_is_invalid(self):
        form = CommentForm(data={"content": ""})
        self.assertFalse(form.is_valid())


class TestPostCommentForm(TestCase):
    """
    Unittest for post comment form - blog app
    """
    def test_empty_form(self):
        form = PostCommentForm()
        self.assertIn('body', form.fields)

    def test_post_comment_form_is_valid(self):
        form = PostCommentForm(data={
            "body": "I will comment on this post later."
            })
        self.assertTrue(form.is_valid())

    def test_post_comment_form_is_invalid(self):
        form = PostCommentForm(data={"body": ""})
        self.assertFalse(form.is_valid())


class TestUserRegisterForm(TestCase):
    """
    Unittest for user sign up form
    """
    def test_empty_form(self):
        form = UserRegisterForm()
        fields = ['username', 'email', 'password1', 'password2']
        for field in fields:
            self.assertIn(field, form.fields)

    def test_user_register_form_is_valid(self):
        form = UserRegisterForm(data={
            "username": "newuser",
            "email": "usermail@mail.com",
            "password1": "resdhjh12A.",
            "password2": "resdhjh12A."
            })
        self.assertTrue(form.is_valid())

    def test_user_register_form_is_invalid(self):
        form = UserRegisterForm(data={
            "username": "newuser",
            "email": "usermail.com",
            "password1": "resdhjh12A.",
            "password2": "resdhjh12A."
            })
        self.assertFalse(form.is_valid())


class TestUserUpdateForm(TestCase):
    """
    Unittest for user update form
    """
    @classmethod
    def setUpTestData(cls):
        cls.user = UserRegisterForm(data={
            "username": "amuser",
            "email": "usermail@mail.com",
            "password1": "resdhjh12A.",
            "password2": "resdhjh12A."
            })

    def test_empty_form(self):
        form = UserUpdateForm()
        fields = ['username', 'email']
        for field in fields:
            self.assertIn(field, form.fields)

    def test_user_update_form_is_valid(self):
        form = UserUpdateForm(data={
            "username": "amieco",
            "email": "amail@mail.com"
            })
        self.assertTrue(form.is_valid())

    def test_user_update_form_is_invalid(self):
        form = UserUpdateForm(data={
            "username": "newuser",
            "email": "usermail.com"
            })
        self.assertFalse(form.is_valid())


class TestProfileUpdateForm(TestCase):
    """
    Unittest for user profile update form
    """
    @classmethod
    def setUp(self):
        self.user = User.objects.create(id=1, username='Aman',
                                         email='aman@mail.com',
                                         password='123someTest')

    def test_empty_form(self):
        form = ProfileUpdateForm()
        fields = ['bio', 'image']
        for field in fields:
            self.assertIn(field, form.fields)

    def test_profile_update_form_is_valid(self):
        form = ProfileUpdateForm(data={
            "bio": "I love coding.",
            "image": "media/qbrand.png"
            })
        self.assertTrue(form.is_valid())

