from . import views
from django.urls import path

urlpatterns = [
    path('', views.ThreadList.as_view(), name='threads'),
    path('category/', views.CategoryList.as_view(), name='categories'),
]