from django.shortcuts import render, get_list_or_404
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Thread, Post, Category
from .forms import ThreadForm


class ThreadList(generic.ListView):
    model = Thread
    template_name = 'qforum/thread_list.html'


class PostList(generic.ListView):
    model = Post
    template_name = 'qforum/post_list.html'


class CategoryList(generic.ListView):
    model = Category
    template_name = 'qforum/forum_base.html'



class CreateForum(CreateView):
    model = Thread
    fields = ['topic', 'description']
    template_name = 'qforum/create_forum.html'

    def post(request):
        pass


class VoteUpView(generic.View):
    def post(request):
        pass


class VoteDownView(generic.View):
    def post(request):
        pass