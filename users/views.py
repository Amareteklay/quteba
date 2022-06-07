## Code from https://www.devhandbook.com/django/user-registration/
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create account
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            username = form.cleaned_data.get('username') 
            form.save() 
            messages.success(request, f'Your account has been created! You are now able to log in') 
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# Update profile
@login_required
def update_profile(request, *args, **kwargs):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.user_profile) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request,
                f'Your profile has been updated successfully!'
            )
            return HttpResponseRedirect(
                reverse('profile')
            )

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.user_profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/update_profile.html', context)

# View profile
@login_required
def profile(request, *args, **kwargs):
    user = get_object_or_404(User, username=request.user.username)
    user_profile = get_object_or_404(
            Profile,  user=user
        )
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.user_profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'users/profile.html', context)


# Delete profile
@login_required
def delete_profile(request, pk, *args, **kwargs):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        user.delete()
        return redirect('home')
    return render(request, "users/delete_profile.html")