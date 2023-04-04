from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin  

letrasregex = RegexValidator(r'^[a-zA-Z_ áàâãéèêíïóôõöúçñ]*$', 'Não inclua números neste campo')

class Usuario(models.Model):
    nome_user = models.CharField("Nome completo", max_length=255,validators=[letrasregex])
    email_user = models.EmailField("Email" ,max_length=255, unique=True)
    senha1_user = models.CharField(max_length=100)
    senha2_user = models.CharField(max_length=100)

class Tutor(models.Model):
    id_tutor = models.AutoField(primary_key=True)
    email = models.EmailField("Email" ,max_length=255, unique=True)
    nome = models.CharField("Nome completo", max_length=255,validators=[letrasregex])
    telefone = models.CharField("Telefone", max_length=25)
    cidade = models.CharField(max_length=255,validators=[letrasregex])
    sobre = models.CharField(max_length=255, validators=[letrasregex])
    foto_tutor = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Abrigo(models.Model):
    id_abrigo = models.AutoField(primary_key=True)
    email_abrigo = models.EmailField(max_length=255, unique=True)
    nome_abrigo = models.CharField(max_length=255, validators=[letrasregex])
    telefone_abrigo = models.CharField(max_length=25)
    cidade_abrigo = models.CharField(max_length=255,validators=[letrasregex])
    sobre_abrigo = models.CharField(max_length=255)
    foto_abrigo = models.ImageField(blank=True, null=True)


class Pet(models.Model):
    id_pet = models.AutoField(primary_key=True)
    nome_pet = models.CharField(max_length=30,validators=[letrasregex])
    cidade_pet = models.CharField(max_length=50,validators=[letrasregex])
    idade_pet = models.CharField(max_length=255, blank=True, null=True)
    sobre_pet = models.CharField(max_length=255,validators=[letrasregex])
    adotado = models.BooleanField(default=False)
    foto_pet = models.ImageField(blank=True, null=True)
    id_abrigo = models.ForeignKey(Abrigo, on_delete=models.CASCADE, blank=True)
    def __str__(self):
        return self.nome_pet    


class Adocao(models.Model):
    id_adocao = models.AutoField(primary_key=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    data_adocao = models.DateField()