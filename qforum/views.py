from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .models import Thread, Comment, Category
from .forms import ThreadForm, CommentForm
from qblog.models import Post


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
            return JsonResponse({
                    'topic': new_thread.topic,
                    'slug': new_thread.slug,
                    'description': new_thread.description,
                    'category': new_thread.category.subject,
                    'name': new_thread.name.username,
                    'created': new_thread.created_on.date(),
                    'profile': new_thread.name.user_profile.image.url
                })


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

    def post(self, request, slug, pk=None, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        queryset = Thread.objects.all()
        thread = get_object_or_404(queryset, slug=slug)
        comments = thread.comments.filter(active=True).order_by('created')
        parent_comment = None
        if pk:
            parent_comment = comment.objects.get(pk=pk)
        thread_list = Thread.objects.all()
        category_list = Category.objects.all()
        if comment_form.is_valid():
            content = comment_form.cleaned_data['content']
            try:
                parent = comment_form.cleaned_data['parent']
            except:
                parent=None 
        new_comment = Comment(content=content, name=self.request.user, thread=thread, parent=parent_comment)
        new_comment.save()
        return redirect(self.request.path_info)


# Adapted from https://github.com/legionscript/socialnetwork/blob/tutorial11/social/templates/social/post_detail.html
class ReplyView(LoginRequiredMixin, View):

    def post(self, request, slug, pk, *args, **kwargs):
        thread = Thread.objects.get(slug=slug)
        parent_comment = Comment.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = request.user
            new_comment.thread = thread
            new_comment.parent = parent_comment
            new_comment.save()

        return redirect('qforum:thread_detail', slug=slug)


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


@login_required
def vote_up(request):
    slug = request.POST.get('slug')
    if request.POST.get('action') == 'votingup':
        thread = Thread.objects.get(slug=slug)
        if request.user in thread.up_votes.all():
            thread.up_votes.remove(request.user)
            thread.save()
        else:
            thread.up_votes.add(request.user)
            thread.save()
        return JsonResponse({ 
            'upvotes': thread.no_of_upvotes(),
            'downvotes': thread.no_of_downvotes()
        })


@login_required
def vote_down(request):
    slug = request.POST.get('slug')
    if request.POST.get('action') == 'votingdown':
        thread = Thread.objects.get(slug=slug)
        if request.user in thread.down_votes.all():
            thread.down_votes.remove(request.user)
            thread.save()
        else:
            thread.down_votes.add(request.user)
            thread.save()
        return JsonResponse({ 
            'upvotes': thread.no_of_upvotes(),
            'downvotes': thread.no_of_downvotes()
        })

@login_required
def like_view(request):
    pk = request.POST.get('pk')
    if request.POST.get('action') == 'liking':
        comment = Comment.objects.get(pk=pk)
        if request.user in comment.likes.all():
            comment.likes.remove(request.user)
            comment.save()
        else:
            comment.likes.add(request.user)
            comment.save()
        return JsonResponse({ 
            'likes': comment.no_of_likes(),
            'dislikes': comment.no_of_dislikes()
        })

@login_required
def dislike_view(request):
    pk = request.POST.get('pk')
    if request.POST.get('action') == 'disliking':
        comment = Comment.objects.get(pk=pk)
        if request.user in comment.dislikes.all():
            comment.dislikes.remove(request.user)
            comment.save()
        else:
            comment.dislikes.add(request.user)
            comment.save()
        return JsonResponse({ 
            'likes': comment.no_of_likes(),
            'dislikes': comment.no_of_dislikes()
        })