from django.shortcuts import render
from django.views import generic
from .models import Thread, Post, Category


class ThreadList(generic.ListView):
    model = Thread
    template_name = 'qforum/thread_list.html'


class PostList(generic.ListView):
    model = Post
    template_name = 'qforum/post_list.html'


class CategoryList(generic.ListView):
    model = Category
    template_name = 'qforum/forum_base.html'
