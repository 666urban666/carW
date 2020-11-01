from django.contrib import admin
from django.urls import path, include
from .views import index, galeria, insumo, registroUsuario, vicion, login, logout_vista

urlpatterns = [
    path('', index , name='index'),
    path('galeria/', galeria , name='galeria'),
    path('insumos/', insumo , name='insumo'),
    path('registroUsuario/', registroUsuario , name='registroUsuario'),
    path('vicion/', vicion , name='vicion'),
    path('login/', login , name='login'),
    path('logout_vista/',logout_vista, name='logout')
]