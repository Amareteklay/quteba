from . import views
from django.urls import path

app_name = 'qforum'

urlpatterns = [
    path('', views.ThreadList.as_view(), name='threads'),
    path('create/', views.CreateForum.as_view(), name='create_forum'),
    path('<slug:slug>/', views.ThreadDetailView.as_view(), name='thread_detail'),
    path('edit/<slug:slug>/', views.ThreadEditView.as_view(), name='edit-thread'),
     path('delete/<slug:slug>/', views.ThreadDeleteView.as_view(), name='delete-thread'),
    path('<slug:slug>/comment/<int:pk>/like', views.CommentLikeView.as_view(), name='comment-like'),
    path('<slug:slug>/comment/<int:pk>/dislike', views.CommentUnlikeView.as_view(), name='comment-dislike'),
]