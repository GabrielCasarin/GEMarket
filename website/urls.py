from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^cadastro$', views.cadastro),
	url(r'^login$', views.login),
	url(r'^home$', views.home),
	url(r'^logout$', views.logout_view),
	url(r'^vender$', views.vender),
	url(r'^comprar$', views.comprar),
	url(r'^historico$', views.historico),
]
