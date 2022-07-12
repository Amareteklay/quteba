"""Tests for the urls"""
from django.test import TestCase
from django.urls import reverse, resolve
from home.views import (
    index,
    about,
    SearchView,
    ContactView
)
from qblog.views import (
    PostCreateView,
    PostEditView, 
    PostList,
    PostDetail,
    PostLike
)
from qforum.views import (
    ThreadList,
    ThreadDetailView,
    ThreadEditView,
    ThreadDeleteView
)


class TestHomeUrls(TestCase):
    """Test the urls for the home app"""

    def test_home_url_resolves(self):
        """Test the home url"""
        url = reverse('home')
        self.assertEquals(resolve(url).func, index)

    def test_about_url_resolves(self):
        """Test the about url"""
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)

    def test_search_url_resolves(self):
        """Test the search results url"""
        url = reverse('search_results')
        self.assertEquals(resolve(url).func.view_class, SearchView)

    def test_contact_url_resolves(self):
        """Test the contact url"""
        url = reverse('contact')
        self.assertEquals(resolve(url).func.view_class, ContactView)


class TestBlogUrls(TestCase):
    """Test the urls for the blog app"""

    def test_create_post_url_resolves(self):
        """Test the create post url"""
        url = reverse('qblog:post_create')
        self.assertEquals(resolve(url).func.view_class, PostCreateView)

    def test_edit_post_url_resolves(self):
        """Test the edit post url"""
        url = reverse('qblog:edit_post', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, PostEditView)

    def test_post_list_url_resolves(self):
        """Test the post list url"""
        url = reverse('qblog:blog')
        self.assertEquals(resolve(url).func.view_class, PostList)

    def test_post_detail_url_resolves(self):
        """Test the post detail url"""
        url = reverse('qblog:post_detail', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, PostDetail)

    def test_post_like_url_resolves(self):
        """Test the post like url"""
        url = reverse('qblog:post_like', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, PostLike)


class TestForumUrls(TestCase):
    """Test the urls for the forum app"""

    def test_thread_list_url_resolves(self):
        """Test the thread list url"""
        url = reverse('qforum:threads')
        self.assertEquals(resolve(url).func.view_class, ThreadList)

    def test_thread_detail_url_resolves(self):
        """Test the thread detail url"""
        url = reverse('qforum:thread_detail', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, ThreadDetailView)

    def test_edit_thread_url_resolves(self):
        """Test the edit thread url"""
        url = reverse('qforum:edit-thread', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, ThreadEditView)

    def test_delete_thread_url_resolves(self):
        """Test the delete thread url"""
        url = reverse('qforum:delete-thread', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, ThreadDeleteView)

