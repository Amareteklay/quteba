from . import views
from django.urls import path

urlpatterns = [
    path('', views.ThreadList.as_view(), name='threads'),
    path('category/', views.CategoryList.as_view(), name='categories'),
    path('create/', views.CreateForum.as_view(), name='create_forum'),
    path('comment/', views.CreateComment.as_view(), name='comment'),
    path('reply/', views.CreateReply.as_view(), name='reply'),
    path('<slug:slug>/', views.ThreadDetailView.as_view(), name='thread_detail'),
]