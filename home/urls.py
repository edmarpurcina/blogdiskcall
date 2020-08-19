from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('artigo/<int:artigo_id>', ver_artigo, name='artigo'),
    path('pesquisa', pesquisar, name='pesquisar'),
    
]