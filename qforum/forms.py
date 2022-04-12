from django.forms import ModelForm
from .models import Thread, Post
 

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = "__all__"
 

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"