import datetime
from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 
from django.test import Client
from qblog.models import Post
from qblog.models import Comment as PostComment
from qforum.models import Thread, Category, Comment

class HomePageViewTests(TestCase):

    def test_home_page_url_exists(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_home_page_url_name(self):  
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
    
    def test_home_page_template_name(self):  
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home/index.html")

    def test_home_page_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, '<h1 class="text-center">RECENT STORIES</h1>')
        self.assertContains(response, '<h1 class="text-center">ACTIVE TOPICS</h1>')


class AboutPageViewTests(TestCase):

    def test_about_page_url_exists(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_url_name(self):  
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_template_name(self):  
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "home/about.html")

    def test_about_page_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, '<h1 class="post-title text-center">What is Quteba?</h1>')
        self.assertNotContains(response, '<h6 class="post-title text-center">What is Quteba?</h6>')


class PostListViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='Aman', email='aman@mail.com', password='123someTet')
        number_of_posts = 11
        for post_id in range(number_of_posts):
            Post.objects.create(
                title=f'Blog post {post_id}',
                slug=f'blog-post-{post_id}',
                author=user,
                last_updated=datetime.date.today(),
                content=f'Content blog post {post_id}',
            )

    def test_post_list_view_url_exists(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_url_name(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_template(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'qblog/blog.html')

    def test_post_list_pagination_is_ten(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['post_list']), 10)

    def test_post_list_lists_all_posts(self):
        response = self.client.get(reverse('blog')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['post_list']), 1)


class PostDetailViewTests(TestCase):
    pass


class ThreadListViewTests(TestCase):
    pass


class ThreadDetailViewTests(TestCase):
    pass