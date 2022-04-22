from . import views
from django.urls import path

app_name = 'qforum'

urlpatterns = [
    path('', views.ThreadList.as_view(), name='threads'),
    path('category/', views.CategoryList.as_view(), name='categories'),
    path('create/', views.CreateForum.as_view(), name='create_forum'),
    path('comment/reply', views.CreateComment.as_view(), name='reply'),
    path('<slug:slug>/', views.ThreadDetailView.as_view(), name='thread_idetail'),
    path('<slug:thread>/', views.thread_detail, name='thread_detail'),
]