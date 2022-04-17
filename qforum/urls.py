from . import views
from django.urls import path

urlpatterns = [
    path('', views.ThreadList.as_view(), name='threads'),
    path('category/', views.CategoryList.as_view(), name='categories'),
    path('create/', views.CreateForum.as_view(), name='create_forum'),
]