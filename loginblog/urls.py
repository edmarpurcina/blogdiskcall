from django.contrib import admin
from django.urls import path, include
from loginblog.views import *

urlpatterns = [
    path('', ola_mundo)
]