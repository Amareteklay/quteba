from django.forms import ModelForm
from .models import Thread, Comment
 

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ('category', 'topic', 'description')
    
    def __init__(self, *args, **kwargs):
        super(ThreadForm, self).__init__(*args, **kwargs)
        self.fields['topic'].widget.attrs = {'placeholder': 'Enter a topic...', 'class': 'form-control', 'rows': '2'}
        self.fields['description'].widget.attrs = {'placeholder': 'Enter a description here...', 'class': 'form-control', 'rows': '5'}


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs = {'placeholder': 'Comment here...', 'class': 'form-control', 'rows': '5'}