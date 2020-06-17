from django.shortcuts import render
from .models import Artigo 

# Create your views here.

def home_page(request):
    artigos = Artigo.objects.all()
    

    return render( request, "home.html", {'artigos': artigos})