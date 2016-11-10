from django.shortcuts import render
from django.contrib.auth.views import login as login_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import HttpResponseRedirect
from chat.models import Chat

from .forms import LoginForm


def home(request):
    form = LoginForm()
    chats = Chat.objects.all().order_by('created_on').reverse
    all_users = User.objects.filter(is_staff=False).exclude(username=request.user.username)
    return render(request, "home.html",locals())


def login(request):
    is_authenticated = request.user.is_authenticated()
    if is_authenticated:
        return HttpResponseRedirect('/chat_home/')
    else:
        return login_view(request,'home.html',authentication_form=LoginForm)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

