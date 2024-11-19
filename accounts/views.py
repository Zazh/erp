from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import UserInfo
from clients.models import ClientType
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserRegistrationForm, UserInfoForm

def user_info_view(request, username):
    user = get_object_or_404(User, username=username)
    user_info, created = UserInfo.objects.get_or_create(user=user)
    context = {'user': user, 'user_info': user_info}
    return render(request, 'accounts/user_info.html', context)

def edit_user_info(request):
    user_info, created = UserInfo.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserInfoForm(request.POST, instance=user_info)
        if form.is_valid():
            form.save()
            messages.success(request, 'Информация успешно обновлена!')
            return redirect('user_info', username=request.user.username)
        else:
            messages.error(request, 'Произошла ошибка при обновлении информации.')
    else:
        form = UserInfoForm(instance=user_info)

    return render(request, 'accounts/update_user_info.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('user_info', username=user.username)
    else:
        user_form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'user_form': user_form})
