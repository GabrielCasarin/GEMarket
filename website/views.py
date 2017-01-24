import sys
from datetime import datetime
# Render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Auth
import django.contrib.auth as auth
# Models
from .models import *


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
        mercadorias = Mercadoria.objects.all()
        return render(request, 'website/home.html', {'mercadorias': mercadorias})
    return HttpResponseRedirect('/')


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def vender(request):
    if request.user.is_authenticated():
        mercadoria = Mercadoria.objects.get(codigo=request.POST['codigo'])
        if mercadoria is not None:
            nova_venda = Venda(mercadoria=mercadoria,
                                    quantidade=int(request.POST['qtdeVendaInput']),
                                    precoVenda=float(request.POST['precoVendaInput']),
                                    usuario=request.user)
            nova_venda.save()
    return HttpResponseRedirect('/home')


def comprar(request):
    print(request.POST)
    if request.user.is_authenticated():
        mercadoria = Mercadoria.objects.get(codigo=request.POST['codigo'])
        if mercadoria is not None:
            nova_compra = Compra(mercadoria=mercadoria,
                                    quantidade=int(request.POST['qtdeCompraInput']),
                                    precoCompra=mercadoria.preco,
                                    usuario=request.user)
            nova_compra.save()
    return HttpResponseRedirect('/home')
