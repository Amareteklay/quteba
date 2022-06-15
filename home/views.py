from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from qblog.models import Post
from qforum.models import Thread
from .models import Contact
from .forms import ContactForm
from django.db.models import Q


def index(request):
    recent_posts = Post.objects.filter(status=1).order_by('-created_on')
    active_topics = Thread.objects.all().order_by('-created_on')
    return render(request, 'home/index.html', {'post': recent_posts, 'thread': active_topics})

def about(request):
    return render(request, 'home/about.html')


class SearchView(View):

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("query")
        post_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        thread_list = Thread.objects.filter(
            Q(topic__icontains=query) | Q(description__icontains=query)
        )
        context = {
            'post_list': post_list,
            'thread_list': thread_list
        }
        return render(request, 'home/search_list.html', context=context)
    

class ContactView(View):
    template_name = 'home/contact.html'
    form_class = ContactForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Thank You for contacting us. Your message has been submitted successfully.')
            return HttpResponseRedirect('/')
        else:
            errors = form.errors
            for error in errors:
                messages.error(self.request, 'Please, enter valid ' + error)
            return render(request, self.template_name, {'form': form})