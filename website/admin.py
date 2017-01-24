from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Mercadoria)
admin.site.register(Compra)
admin.site.register(Venda)
