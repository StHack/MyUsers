#-*- coding: utf-8 -*-
from app.forms import ConnexionForm, UserForm
from app.models import MyUser
from django.http import HttpResponseRedirect
from app.decorators import logout_required
from django.template import RequestContext
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, logout, login
from django.views.generic import CreateView, DetailView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@logout_required
def connexion(request):
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                error = True
    else:
        form = ConnexionForm()
    return render(request, 'app/login.html', locals())

def home(request):
    users = MyUser.objects.all()
    return render(request, 'app/index.html', locals())

@login_required
def deconnexion(request):                                                                               
    logout(request)                                                                                     
    return redirect(reverse(home))

class UserCreate(CreateView):
    model = MyUser
    template_name = 'app/new.html'
    form_class = UserForm
    success_url = reverse_lazy('connexion')

@login_required
def poke(request, username):
    megalo = False
    if request.user.username == username:
        megalo = True
    else:
        u = get_object_or_404(MyUser,username=username)
        u.nbPoke += 1
        u.save()
    users = MyUser.objects.all()
    return render(request, 'app/index.html', locals())

class UserDetail(DetailView):
    context_object_name = "u"
    model = MyUser
    template_name = "app/user.html"
