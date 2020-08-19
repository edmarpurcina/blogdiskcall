  
from django import forms
from .models import Artigo

class ContatoForm(forms.ModelForm):
	class Meta:
		model = Artigo
		fields = ['artigo_titulo']
        