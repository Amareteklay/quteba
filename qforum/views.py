from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['category_list'] = Category.objects.all()
        return data


class ActiveTopicsList(generic.ListView):
    """
    To show a list of active topics in the side bar.
    """
    model = Thread
    template_name = 'qforum/side_bar.html'


class CategoryList(generic.ListView):
    model = Category
    template_name = 'qforum/forum_base.html'


class ThreadDetailView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Thread.objects.all()
        thread = get_object_or_404(queryset, slug=slug)
        thread_form = ThreadForm()
        comment_form = CommentForm()
        comments = thread.comments.filter(active=True).order_by('created')
        thread_list = Thread.objects.all()
        category_list = Category.objects.all()
        context = {
            'thread': thread,
            'thread_form': thread_form,
            'comment_form': comment_form,
            'comments': comments,
            'thread_list': thread_list,
            'category_list': category_list
        }
        return render(request, 'qforum/thread_detail.html', context=context)

    def post(self, request, slug, *args, **kwargs):
        #thread_form = ThreadForm(request.POST)
        comment_form = CommentForm(request.POST)
        queryset = Thread.objects.all()
        thread = get_object_or_404(queryset, slug=slug)
        comments = thread.comments.filter(active=True).order_by('created')
        thread_list = Thread.objects.all()
        category_list = Category.objects.all()
        if comment_form.is_valid():
            content = comment_form.cleaned_data['content']
            try:
                parent = comment_form.cleaned_data['parent']
            except:
                parent=None 
        new_comment = Comment(content=content, name=self.request.user, thread=thread, parent=parent)
        new_comment.save()
        context = {
            'thread': thread,
            #'thread_form': thread_form,
            'comment_form': comment_form,
            'comments': comments,
            'thread_list': thread_list,
            'category_list': category_list
        }
        return redirect(self.request.path_info)


class ThreadDetail(DetailView):
    
    def post(self, request, slug, *args, **kwargs):
        if self.request.method == 'POST':
            form = CommentForm(self.request.POST)
            if form.is_valid():
                content = form.cleaned_data['content']
                try:
                    parent = form.cleaned_data['parent']
                except:
                    parent=None 
        new_comment = Comment(content=content, name =self.request.user, thread=self.get_object(), parent=parent)
        new_comment.save()
        return redirect(self.request.path_info)


class CreateForum(LoginRequiredMixin, CreateView):
    model = Thread
    form_class = ThreadForm
    template_name = 'qforum/forum_base.html'
    success_url = reverse_lazy('qforum:thread_list')

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


class VoteUpView(generic.View):

    def post(self, request):
        pass


class VoteDownView(generic.View):

    def post(self, request):
        pass