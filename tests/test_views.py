import datetime
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from qblog.models import Post
from qblog.models import Comment as PostComment
from qforum.models import Thread, Category, Comment
#from qblog.views import Post, PostDetail
#from home.views import SearchView, index, about


class HomePageViewTests(TestCase):
    """
    Testing home page view
    """
    def setUp(self):
        user = User.objects.create(username='Aman',
                                   email='aman@mail.com',
                                   password='123someTest')
        self.client = Client()
        self.home_url = reverse("home")

    def test_home_page_url_unauthorized_user(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_home_page_url_authorized_user(self):
        self.client.login(username='Aman', password='123someTest')
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template_content(self):
        response = self.client.get(self.home_url)
        self.assertContains(response,
                            '<h2 class="text-center">RECENT POSTS</h2>')
        self.assertContains(response,
                            '<h2 class="text-center">RECENT FORUMS</h2>')


class AboutPageViewTests(TestCase):
    """
    Testing about page view
    """
    def setUp(self):
        self.client = Client()
        self.about_url = reverse("about")

    def test_about_page_url_exists(self):
        response = self.client.get(self.about_url)
        self.assertEqual(response.status_code, 200)

    def test_about_page_template_name(self):
        response = self.client.get(self.about_url)
        self.assertTemplateUsed(response, "home/about.html")


class PostListViewTests(TestCase):
    """
    Testing blog post list view
    """
    @classmethod
    def setUp(self):
        self.user = User.objects.create(username='Aman',
                                        email='aman@mail.com',
                                        password='123someTet')
        number_of_posts = 11
        for post_id in range(number_of_posts):
            Post.objects.create(
                title=f'Blog post {post_id}',
                slug=f'blog-post-{post_id}',
                author=self.user,
                last_updated=datetime.date.today(),
                status=1,
                content=f'Content blog post {post_id}'
            )
        self.client = Client()
        self.blog_url = reverse("qblog:blog")

    def test_post_list_view_url_exists(self):
        response = self.client.get(self.blog_url)
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_template(self):
        response = self.client.get(self.blog_url)
        self.assertTemplateUsed(response, 'qblog/blog.html')

    def test_post_list_pagination_is_ten(self):
        response = self.client.get(self.blog_url)
        self.assertTrue('is_paginated' in response.context)
        self.assertEqual(len(response.context['post_list']), 10)

    def test_post_list_lists_all_posts(self):
        response = self.client.get(self.blog_url+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertEqual(len(response.context['post_list']), 1)


class PostDetailViewTests(TestCase):
    """
    Testing blog detail view
    """
    def setUp(self):
        self.user = User.objects.create(username='Aman',
                                        email='aman@mail.com',
                                        password='123someTet')
        self.post = Post.objects.create(
                title='Blog post',
                slug='blog-post',
                author=self.user,
                last_updated=datetime.date.today(),
                status=1,
                content='Content blog post'
            )
        self.client = Client()
        self.post_url = reverse("qblog:post_detail", args=(self.post.slug,))

    def test_post_detail_view_url_exist(self):
        response = self.client.get(self.post_url)
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view_template(self):
        response = self.client.get(self.post_url)
        self.assertTemplateUsed(response, 'qblog/post_detail.html')


class ThreadListViewTests(TestCase):
    """
    Testing thread list view in qforum app
    """
    def setUp(self):
        self.user = User.objects.create(username='Aman',
                                        email='aman@mail.com',
                                        password='123someTet')
        self.category = Category.objects.create(
            name=self.user,
            subject='Finance',
            description='Financial analysis',
            created_on=datetime.date.today(),
            status=0, thread_count=0
            )
        number_of_threads = 5
        for thread_id in range(number_of_threads):
            Thread.objects.create(
                name=self.user,
                topic=f'Thread topic {thread_id}',
                slug=f'thread-topic-{thread_id}',
                description=f'Description of thread {thread_id}',
                category=self.category,
                created_on=datetime.date.today()
            )
        self.client = Client()
        self.forum_url = reverse("qforum:threads")

    def test_thread_list_view_url_exists(self):
        response = self.client.get(self.forum_url)
        self.assertEqual(response.status_code, 200)

    def test_thread_list_view_template(self):
        response = self.client.get(self.forum_url)
        self.assertTemplateUsed(response, 'qforum/thread_list.html')

    def test_thread_list_lists_all_posts(self):
        response = self.client.get(self.forum_url)
        self.assertEqual(len(response.context['thread_list']), 5)


class ThreadDetailViewTests(TestCase):
    """
    Testing thread detail view
    """
    def setUp(self):
        self.user = User.objects.create(
            username='Aman',
            email='aman@mail.com',
            password='123someTest')
        self.category = Category.objects.create(
            name=self.user,
            subject='Finance',
            description='Financial analysis',
            created_on=datetime.date.today(),
            status=1,
            thread_count=0)
        self.thread = Thread.objects.create(
            name=self.user,
            topic='Thread topic',
            slug='thread-topic',
            description='Description of thread',
            category=self.category,
            created_on=datetime.date.today(),
            status=1)
        self.client = Client()
        self.thread_url = reverse(
            "qforum:thread_detail", 
            kwargs={'slug': self.thread.slug})

    def test_thread_detail_view_url_exist(self):
        self.client.login(username='Aman', password='123someTest')
        self.assertEqual(self.thread_url, '/forum/thread-topic/')
