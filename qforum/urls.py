from . import views
from django.urls import path

app_name = 'qforum'

urlpatterns = [
    path('', views.ThreadList.as_view(), name='threads'),
    path('upvote/', views.vote_up, name='upvotes'),
    path('downvote/', views.vote_down, name='downvotes'),
    path('like/', views.like_dislike_view, name='comment-like'),
    path('<slug:slug>/', views.ThreadDetailView.as_view(),
         name='thread_detail'),
    path('edit/<slug:slug>/', views.ThreadEditView.as_view(),
         name='edit-thread'),
    path('delete/<slug:slug>/', views.ThreadDeleteView.as_view(),
         name='delete-thread'),
]
