from django.forms import ModelForm
from .models import *
 
class AddForum(ModelForm):
    class Meta:
        model= Qforum
        fields = "__all__"
 
class AddDiscussion(ModelForm):
    class Meta:
        model= Discussion
        fields = "__all__"