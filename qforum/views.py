from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def forum(request):
    return render(request, 'qforum/forum.html')