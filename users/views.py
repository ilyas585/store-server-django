from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth, messages

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm

# Create your views here.


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():  # проверяем данные корректно введены или нет
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
    else:
        form = UserLoginForm()
    context = {'title': 'Store - Авторизация', 'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()  # создать или обновлять данные
            messages.success(request, 'Вы успешно зарегистрировались')
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {'title': 'Регистрация', 'form': form}
    return render(request, 'users/registration.html', context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {'title': 'Store - Профиль', 'form': form}
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


