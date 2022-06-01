import datetime
from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from qforum.models import Category, Thread, Comment


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
