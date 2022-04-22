from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.urls import reverse_lazy
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
    context_object_name = 'thread'
    template_name = 'qforum/thread_detail.html'


def thread_detail(request, thread):
    thread = get_object_or_404(Thread, slug=thread, status=1)
    comments = thread.comments.filter(active=True)
    new_comment = None
    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.thread = thread
            new_comment.save()
            return redirect(thread.get_absolute_url()+'#'+str(new_comment.id))
    else:
        comment_form = CommentForm()
    return render(request, 'qforum/thread_detail.html', {"thread": thread, "comments": comments, "comment_form": comment_form})


def reply_view(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            thread_id = request.POST.get('thread_id')
            parent_id = request.POST.get('parent')
            thread_url = request.POST.get('thread_url')
            reply = form.save(commit=False)
            reply.thread = Thread(id=thread_id)
            reply.parent = Comment(id=parent_id)
            reply.save()
            return redirect(thread_url+'#'+str(reply.id))
    return redirect("/") 


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


class VoteUpView(generic.View):

    def post(self, request):
        pass


class VoteDownView(generic.View):

    def post(self, request):
        pass