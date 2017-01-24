from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Auth
import django.contrib.auth as auth
# Models
from .models import *

# Create your views here.
def index(request):
    return render(request, 'website/index.html')

def cadastro(request):
    username = request.POST['username']
    password = request.POST['password']
    nome = request.POST['nome']
    email = request.POST['email']

    u = auth.models.User.objects.create_user(username=username, email=email, password=password)
    u.first_name = nome
    u.save()

    return HttpResponseRedirect('/')

def login(request):
    if request.method == "POST":
        username = request.POST['inputUsername']
        password = request.POST['inputPassword']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('home')
    return render(request, 'website/index.html')

def home(request):
    if request.user.is_authenticated():
        return render(request, 'website/home.html')

    return HttpResponseRedirect('/')
