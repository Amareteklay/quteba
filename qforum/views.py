from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .models import Thread, Comment, Category
from .forms import ThreadForm, CommentForm


class ThreadList(generic.ListView):
    model = Thread
    template_name = 'qforum/thread_list.html'


class PostList(generic.ListView):
    model = Comment
    template_name = 'qforum/post_list.html'


class CategoryList(generic.ListView):
    model = Category
    template_name = 'qforum/forum_base.html'


class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'qforum/thread_detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(thread=self.get_object())
        number_of_comments = comments.count()
        data['comments'] = comments
        data['no_of_comments'] = number_of_comments
        data['form'] = CommentForm()
        return data

    def post(self, request, slug, *args, **kwargs):
        if self.request.method == 'POST':
            form = CommentForm(self.request.POST)
            if form.is_valid():
                content = form.cleaned_data['content']
                try:
                    parent = form.cleaned_data['parent']
                except:
                    parent=None 
        new_comment = Comment(content=content , name =self.request.user, thread=self.get_object(), parent=parent)
        new_comment.save()
        return redirect(self.request.path_info)


class CreateForum(LoginRequiredMixin, CreateView):
    model = Thread
    form_class = ThreadForm
    template_name = 'qforum/create_forum.html'
    success_url = reverse_lazy('threads')

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


class VoteUpView(generic.View):

    def post(self, request):
        pass


class VoteDownView(generic.View):

    def post(self, request):
        pass