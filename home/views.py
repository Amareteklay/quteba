from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from qblog.models import Post
from qforum.models import Thread
from .forms import ContactForm


def index(request):
    """ Quteba home page view
     showing most recent three posts and three threads"""
    recent_posts = Post.objects.filter(status=1).order_by('-created_on')
    active_topics = Thread.objects.all().order_by('-created_on')
    return render(request, 'home/index.html', {'post': recent_posts,
                                               'thread': active_topics})


def about(request):
    """ View for the about page """
    return render(request, 'home/about.html')


class SearchView(View):
    """ View for search results
     Shows results from blog, forum or both """
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
    """ View for the contact form
     renders contact form and saves valid messages"""
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
            messages.success(self.request, 'Thank You for contacting us.\
             Your message has been submitted successfully.')
            return HttpResponseRedirect('/')
        else:
            errors = form.errors
            for error in errors:
                messages.error(self.request, 'Please, enter valid ' + error)
            return render(request, self.template_name, {'form': form})
