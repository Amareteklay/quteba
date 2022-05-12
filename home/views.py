from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from qblog.models import Post
from qforum.models import Thread


def index(request):
    recent_posts = Post.objects.filter(status=1).order_by('-created_on')
    active_topics = Thread.objects.filter(status=1).order_by('-created_on')
    return render(request, 'home/index.html', {'post': recent_posts, 'thread': active_topics})

def about(request):
    return render(request, 'qpages/about.html')