from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Comment
from .forms import CommentForm


class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'qblog/blog.html'
    paginate_by = 3


class PostDetail(View):
    """
    View for details page
    """
    def get(self, request, slug, *args, **kwargs):
        form = CommentForm()
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "qblog/post_detail.html",
            {
                "post": post,
                "has_commentd": False,
                "comments": comments,
                "liked": liked,
                "form": form
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.instance.email = request.user.email
            form.instance.name = request.user.username
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            form = CommentForm()

        return render(
            request,
            "qblog/post_detail.html",
            {
                "post": post,
                "has_commented": True,
                "comments": comments,
                "liked": liked,
                "form": form
            },
        )

class PostLike(View):
    """
    A view to toggle like and unlike
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=request.POST.get('slug'))
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))