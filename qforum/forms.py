from django.forms import ModelForm
from .models import Thread, Comment
 

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ('category', 'topic', 'description')


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs = {'placeholder': 'Comment here...', 'class': 'form-control', 'rows': '5'}