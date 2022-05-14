from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .models import Thread, Comment, Category
from .forms import ThreadForm, CommentForm


class ThreadList(View):

    def get(self, request, *args, **kwargs):
        thread_list = Thread.objects.all()
        category_list = Category.objects.all()
        thread_form = ThreadForm()
        context = {
            'thread_list': thread_list,
            'thread_form': thread_form,
            'category_list': category_list
        }
        return render(request, 'qforum/thread_list.html', context=context)
    def post(self, request, *args, **kwargs):
        thread_list = Thread.objects.all()
        category_list = Category.objects.all()
        thread_form = ThreadForm(request.POST)
        if thread_form.is_valid():
            topic = thread_form.cleaned_data['topic']
            description = thread_form.cleaned_data['description']
            category = thread_form.cleaned_data['category'] 
        new_thread = Thread(topic=topic, category=category, name=self.request.user, description=description)
        new_thread.save()
        context = {
            'thread_list': thread_list,
            'thread_form': thread_form,
            'category_list': category_list
        }
        return render(request, 'qforum/thread_list.html', context=context)
        


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


class ThreadEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):   
    model = Thread
    fields = ['category', 'topic', 'description']
    template_name = 'qforum/edit_thread.html'

    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse_lazy('qforum:thread_detail', kwargs={'slug': slug})

    def test_func(self):
        thread = self.get_object()
        return self.request.user == thread.name


class ThreadDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Thread
    template_name = 'qforum/delete_thread.html'
    success_url = reverse_lazy('qforum:threads')

    def test_func(self):
        thread = self.get_object()
        return self.request.user == thread.name


class VoteUpView(LoginRequiredMixin, View):
    """
    Code adapted from https://github.com/legionscript/socialnetwork/blob/tutorial11/social/views.py
    """
    def post(self, request, pk, *args, **kwargs):
        thread = Thread.objects.get(pk=pk)

        voted_down = False

        for down_vote in thread.down_votes.all():
            if down_vote == request.user:
                voted_down = True
                break

        if voted_down:
            thread.down_votes.remove(request.user)

        voted_up = False

        for up_vote in thread.up_votes.all():
            if up_vote == request.user:
                voted_up = True
                break

        if not voted_up:
            thread.up_votes.add(request.user)

        if voted_up:
            thread.up_votes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class VoteDownView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        thread = Thread.objects.get(pk=pk)

        voted_up = False

        for up_vote in thread.up_votes.all():
            if up_vote == request.user:
                voted_up = True
                break

        if voted_up:
            thread.up_votes.remove(request.user)

        voted_down = False

        for down_vote in thread.down_votes.all():
            if down_vote == request.user:
                voted_down = True
                break

        if not voted_down:
            thread.down_votes.add(request.user)

        if voted_down:
            thread.down_votes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class CommentLikeView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)

        is_dislike = False

        for dislike in comment.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            comment.dislikes.remove(request.user)

        is_like = False

        for like in comment.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            comment.likes.add(request.user)

        if is_like:
            comment.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class CommentUnlikeView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)

        is_like = False

        for like in comment.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            comment.likes.remove(request.user)

        is_dislike = False

        for dislike in comment.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            comment.dislikes.add(request.user)

        if is_dislike:
            comment.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)