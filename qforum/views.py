from django.shortcuts import render
from django.views import generic
from .models import Forum


class ForumList(generic.ListView):
    model = Forum
    queryset = Forum.objects.all()
    template_name = 'qforum/forum.html'
