from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'qpages/about.html')