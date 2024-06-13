
from django.db import models

class Usuario(models.Model):
    nome_completo = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=12, unique=True)
    cnh = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nome_completo

