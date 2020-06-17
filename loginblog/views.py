from django.shortcuts import render

# Create your views here.

def ola_mundo(request):
    a = ["<h1> Ola mundo </h1>"]
    return render(request, a)