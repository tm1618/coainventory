from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required


# Create your views here.

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/devices/')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def invalid_login(request):
    return render_to_response('invalidlogin.html')


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')
