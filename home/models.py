from django.db import models

# Create your models here.
class Artigo(models.Model):

    artigo_id = models.AutoField(primary_key=True)
    artigo_autor_nome = models.CharField(max_length=40)
    artigo_data_criacao = models.DateField(auto_now_add=True)
    aritcle_data_modificacao = models.DateField(auto_now_add=True)
    artigo_titulo = models.CharField(max_length=20)
    artigo_texto = models.CharField(max_length=1024)
    artigo_autor_ip = models.CharField(max_length=15)

    def __ster__(self):
        return self.artigo_title