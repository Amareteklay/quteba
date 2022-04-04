from django.shortcuts import render
from django.views import generic
from .models import Forum


class ForumList(generic.ListView):
    model = Forum
    queryset = Forum.objects.filter(status=1).order_by('-date_created')
    template_name = 'qforum/forum.html'
