from . import views
from django.urls import path

urlpatterns = [
    path('', views.ForumList.as_view(), name='forum'),
]