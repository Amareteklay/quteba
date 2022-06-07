from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('search/', views.SearchView.as_view(), name='search_results'),
     path('contact/', views.ContactView.as_view(), name='contact'),
]