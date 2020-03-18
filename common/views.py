from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy


def index(request):
    context = {}
    if request.user.is_authenticated:
        context['username'] = request.user.username
    return render(request, 'index.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect(reverse_lazy('common:index'))
    else:
        context = {'form': AuthenticationForm()}
        return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse_lazy('common:index'))
