from django.shortcuts import render
import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect
from main.forms import LoginForm


def get_base_context(request, pagename):
    return {
        'pagename': pagename,
    }


def index_page(request):
    context = get_base_context(request, 'PythonBin')
    return render(request, 'main/index.html', context)

def login_page(request):
    if request.method == 'POST':
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username = loginform.data['username']
            password = loginform.data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Авторизация успешна")
            else:
                messages.add_message(request, messages.ERROR, "Неправильный логин или пароль")
        else:
            messages.add_message(request, messages.ERROR, "Некорректные данные в форме авторизации")
    else: loginform = LoginForm()
    context = {
        "LoginForm": loginform,
    }
    return render(request, 'main/login.html', context)

