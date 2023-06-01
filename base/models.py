from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    