from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ola_mundo(request):
    a = {"<h1> Ola mundo </h1>"}
    return render( request, "template.html")