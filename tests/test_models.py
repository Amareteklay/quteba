import datetime
from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from qforum.models import Category, Thread, Comment
from qblog.models import Comment as PostComment
from qblog.models import Post


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='Aman', email='aman@mail.com', password='123someTet')
        Category.objects.create(name=user, subject='Finance', description='Financial analysis', created_on=datetime.date.today(), status=0, thread_count=0)

    def test_subject_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('subject').max_length
        self.assertEqual(max_length, 50)

    def test_description_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('description').max_length
        self.assertEqual(max_length, 255)
    
    def test_category_username(self):
        user = User.objects.get(id=1)
        category = Category.objects.get(id=1)
        username = category._meta.get_field('name').value_from_object(category)
        self.assertEqual(username, user.pk)
    
    def test_category_status(self):
        category = Category.objects.get(id=1)
        status = category._meta.get_field('status').value_from_object(category)
        self.assertEqual(status, 0)
    
    def test_no_of_threads(self):
        category = Category.objects.get(id=1)
        no_of_threads = category._meta.get_field('thread_count').value_from_object(category)
        self.assertEqual(no_of_threads, 0)


class ThreadModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create(id=1, username='Aman', email='aman@mail.com', password='123someTet')
        category = Category.objects.create(id=1, name=user1, subject='Finance', description='Financial analysis', created_on=datetime.date.today(), status=0, thread_count=0)
        Thread.objects.create(id=1, name=user1, topic='Some topic', slug='some-topic', description='First test', category=category, status=1, created_on=datetime.date.today())
    
    def test_thread_username(self):
        user = User.objects.get(username='Aman')
        category = Category.objects.get(id=1)
        username = category._meta.get_field('name').value_from_object(category)
        self.assertEqual(username, user.pk)

    def test_thread_topic_max_length(self):
        thread = Thread.objects.get(id=1)
        max_length = thread._meta.get_field('topic').max_length
        self.assertEqual(max_length, 300)
    
    def test_thread_category(self):
        category = Category.objects.get(id=1)
        thread = Thread.objects.get(id=1)
        thread_category = thread._meta.get_field('category').value_from_object(thread)
        self.assertEqual(thread_category, category.pk)

    def test_thread_status(self):
        thread = Thread.objects.get(id=1)
        status = thread._meta.get_field('status').value_from_object(thread)
        self.assertEqual(status, 1)
    
    def test_thread_slug_max_length(self):
        thread = Thread.objects.get(id=1)
        max_length = thread._meta.get_field('slug').max_length
        self.assertEqual(max_length, 300)

    def test_thread_description_max_length(self):
        thread = Thread.objects.get(id=1)
        max_length = thread._meta.get_field('description').max_length
        self.assertEqual(max_length, 500)


# Testing post model
class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='Aman', email='aman@mail.com', password='123someTet')
        Post.objects.create(id=1, title='First post', slug='first-post', author=user, last_updated=datetime.date.today(), content='This is a sample post. It has a content.', created_on=datetime.date.today(), status=0)

    def test_post_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)
    
    def test_post_slug_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('slug').max_length
        self.assertEqual(max_length, 200)

    def test_post_author(self):
        user = User.objects.get(username='Aman')
        post = Post.objects.get(id=1)
        author = post._meta.get_field('author').value_from_object(post)
        self.assertEqual(author, user.pk)
    
    def test_post_last_updated(self):
        post = Post.objects.get(id=1)
        last_updated = post._meta.get_field('last_updated').value_from_object(post)
        self.assertEqual(last_updated, datetime.date.today())

    def test_post_content(self):
        post = Post.objects.get(id=1)
        content = post._meta.get_field('content').value_from_object(post)
        self.assertEqual(content, 'This is a sample post. It has a content.')

    def test_post_status(self):
        post = Post.objects.get(id=1)
        status = post._meta.get_field('status').value_from_object(post)
        self.assertEqual(status, 0)
# Testing post comment model
class PostCommentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='Aman', email='aman@mail.com', password='123someTet')
        post = Post.objects.create(title='First post', slug='first-post', author=user, last_updated=datetime.date.today(), content='This is a sample post. It has a content.', created_on=datetime.date.today(), status=0)
        PostComment.objects.create(post=post, name=user, email=user.email, body='Nice post', created_on=datetime.date.today(), approved=True)
    
    def test_post_comment_post(self):
        comment = PostComment.objects.get(id=1)
        post = Post.objects.get(id=1)
        comment_post = comment._meta.get_field('post').value_from_object(comment)
        self.assertEqual(comment_post, post.pk)

    def test_post_comment_name_max_length(self):
        comment = PostComment.objects.get(id=1)
        max_length = comment._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)
    
    def test_post_comment_name_max_length(self):
        comment = PostComment.objects.get(id=1)
        max_length = comment._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def test_post_comment_author_email(self):
        user = User.objects.get(username='Aman')
        comment = PostComment.objects.get(id=1)
        email = comment._meta.get_field('email').value_from_object(comment)
        self.assertEqual(email, user.email)
    

    def test_post_comment_created(self):
        comment = PostComment.objects.get(id=1)
        created_on = comment._meta.get_field('created_on').value_from_object(comment)
        self.assertEqual(created_on, datetime.date.today())
    
    def test_post_comment_status(self):
        comment = PostComment.objects.get(id=1)
        status = comment._meta.get_field('approved').value_from_object(comment)
        self.assertTrue(status)
    
    def test_post_comment_body_max_length(self):
        comment = PostComment.objects.get(id=1)
        max_length = comment._meta.get_field('body').max_length
        self.assertEqual(max_length, 200)

    def test_post_comment_body_content(self):
        comment = PostComment.objects.get(id=1)
        body = comment._meta.get_field('body').value_from_object(comment)
        self.assertEqual(body, 'Nice post')

# Testing thread comment model