from . import views
from django.urls import path

app_name = 'qforum'

urlpatterns = [
    path('', views.ThreadList.as_view(), name='threads'),
    path('list/', views.get_thread_list, name='list'),
    path('<slug:slug>/', views.ThreadDetailView.as_view(), name='thread_detail'),
    path('<int:pk>/upvote', views.VoteUpView.as_view(), name='thread-vote-up'),
    path('<int:pk>/downvote', views.VoteDownView.as_view(), name='thread-vote-down'),
    path('<slug:slug>/comment/<int:pk>/reply', views.ReplyView.as_view(), name='reply'),
    path('edit/<slug:slug>/', views.ThreadEditView.as_view(), name='edit-thread'),
    path('delete/<slug:slug>/', views.ThreadDeleteView.as_view(), name='delete-thread'),
    path('<slug:slug>/comment/<int:pk>/like', views.CommentLikeView.as_view(), name='comment-like'),
    path('<slug:slug>/comment/<int:pk>/dislike', views.CommentUnlikeView.as_view(), name='comment-dislike'),
]