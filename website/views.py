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
    return HttpResponseRedirect('/')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('home')
    return render(request, 'website/index.html')

def home(request):
    return render(request, 'website/home.html')
