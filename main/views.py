from django.shortcuts import render
import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect
from main.forms import LoginForm, UserRegistrationForm, CreateVote, ToVote
from django.http import HttpResponse
from .models import Vote
from django.contrib.auth.decorators import login_required


def get_base_context(request, pagename):
    return {
        'pagename': pagename,
    }


def index_page(request):
    his = Vote.objects.all()
    context = {
        "vote_db": his
    }
    return render(request, 'main/index.html', context)

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def registr_page(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'main/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/registration.html',{'user_form': user_form})

@login_required
def create_page(request):
    if request.method == 'POST':
        vote_form = CreateVote(request.POST)
        if vote_form.is_valid():
            record = Vote(
                question=vote_form.data['question'],
                ans1=vote_form.data['ans1'],
                ans2=vote_form.data['ans2'],
            )
            record.save()
            id = record.id
            context = {
                "vote_form" : vote_form
            }
    else:
        vote_form = CreateVote()
        context = {
            "vote_form" : vote_form
           }
    return render(request, 'main/create.html', context)

def vote_page(request, id):
    his = Vote.objects.get(id=id)
    if request.method == 'POST':
        form = ToVote(request.POST)
        if form.is_valid():
            context = {
                "vote_db" : his,
                "ToVote" : form
            }
    else:
        form = ToVote()
        context = {
            "vote_db" : his,
            "ToVote" : form,
        }


    return render(request, 'main/vote.html', context)

def edit_page(request):
    return render(request, 'main/edit.html')

def profil_page(request):
    return render(request, 'main/profil.html')

def logout_page(request):
    logout(request)
    return redirect('index')