from django.shortcuts import render
from .models import Artigo 

# Create your views here.

def home_page(request):
    artigos = Artigo.objects.all()
    
    return render( request, "home.html", {'artigos': artigos})

def ver_artigo(request, artigo_id):
    artigos = Artigo.objects.all()

    return render(request, "ver_artigo.html", {'artigos': artigos})