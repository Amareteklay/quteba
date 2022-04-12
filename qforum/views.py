from django.shortcuts import render
from django.views import generic
from .models import Thread, Post


class ThreadList(generic.ListView):
    model = Thread
    template_name = 'qforum/thread_list.html'


class PostList(generic.ListView):
    model = Post
    template_name = 'qforum/post.html'
