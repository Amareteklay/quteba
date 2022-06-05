from django.forms import ModelForm
from .models import Thread, Comment
 

class ThreadForm(ModelForm):
    """ Form for a user to create a discussion forum """
    class Meta:
        model = Thread
        fields = ('topic', 'description')
    
    def __init__(self, *args, **kwargs):
        super(ThreadForm, self).__init__(*args, **kwargs)
        self.fields['topic'].widget.attrs = {'placeholder': 'Enter a topic...', 'class': 'form-control', 'rows': '2'}
        self.fields['description'].widget.attrs = {'placeholder': 'Enter a description here...', 'class': 'form-control', 'rows': '5'}


class CommentForm(ModelForm):
    """ Form for a user to give comment or reply """
    class Meta:
        model = Comment
        fields = ('content',)
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs = {'placeholder': 'Comment here...', 'class': 'form-control text-area', 'rows': '5', 'cols': '40'}