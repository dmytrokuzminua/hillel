from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm, UserProfileForm, CustomPasswordChangeForm
from django.contrib.auth.models import User


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Реєстрація успішна!")
            return redirect('profile', username=user.username)
    else:
        form = RegistrationForm()
    return render(request, 'myapp/register.html', {'form': form})


@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'myapp/profile.html', {'profile_user': user})


@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        u_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, "Профіль оновлено!")
            return redirect('profile', username=request.user.username)
    else:
        u_form = UserProfileForm(instance=request.user.profile)
    return render(request, 'myapp/edit_profile.html', {'u_form': u_form})


@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # Не дає вийти з системи
            messages.success(request, "Пароль змінено!")
            return redirect('profile', username=request.user.username)
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'myapp/change_password.html', {'form': form})


@login_required
def redirect_to_own_profile(request):
    return redirect('profile', username=request.user.username)
