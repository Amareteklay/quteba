from django.forms import ModelForm
from .models import Thread, Comment
 

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ('category', 'topic', 'description')


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')