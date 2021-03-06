from django.db import models
from django.contrib.auth.models import User


class Mercadoria(models.Model):
    nome = models.CharField(max_length=45)
    codigo = models.CharField(max_length=10)
    preco = models.FloatField()
    tipo = models.CharField(max_length=45)
    img_name = models.CharField(max_length=45, default='')


class Operacao(models.Model):
    mercadoria = models.ForeignKey(Mercadoria, on_delete=models.CASCADE)
    datahora = models.DateTimeField(auto_now=True)
    quantidade = models.PositiveIntegerField()
    usuario = models.ForeignKey(User, default=None)


class Compra(Operacao):
    precoCompra = models.FloatField()


class Venda(Operacao):
    precoVenda = models.FloatField()
