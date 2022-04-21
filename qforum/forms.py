from django.forms import ModelForm
from .models import Thread, Comment, Reply
 

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ('category', 'topic', 'description')
 

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('thread', 'content')


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ('comment', 'message')