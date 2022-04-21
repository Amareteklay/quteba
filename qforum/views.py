from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .models import Thread, Comment, Category, Reply
from .forms import ThreadForm, CommentForm, ReplyForm


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

    def get(self, request, slug, *args, **kwargs):
        form = ThreadForm()
        queryset = Thread.objects.filter(status=1)
        thread = get_object_or_404(queryset, slug=slug)
        comments = thread.thread_comments.all()
        return render(
            request,
            "qforum/thread_detail.html",
            {
                "thread": thread,
                "comments": comments,
                "form": form
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Thread.objects.filter(status=1)
        thread = get_object_or_404(queryset, slug=slug)
        comments = thread.thread_comments.filter()
        form = ThreadForm(data=request.POST)
        if form.is_valid():
            form.instance.email = request.user.email
            form.instance.name = request.user.username
            comment = form.save(commit=False)
            comment.thread = thread
            comment.save()
        else:
            form = CommentForm()

        return render(
            request,
            "qforum/thread_detail.html",
            {
                "thread": thread,
                "comments": comments,
                "form": form
            },
        )



class CreateForum(LoginRequiredMixin, CreateView):
    model = Thread
    form_class = ThreadForm
    template_name = 'qforum/create_forum.html'
    success_url = reverse_lazy('threads')

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


class CreateComment(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'qforum/comment.html'
    success_url = reverse_lazy('threads')

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


class CreateReply(LoginRequiredMixin, CreateView):
    model = Reply
    form_class = ReplyForm
    template_name = 'qforum/reply.html'
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