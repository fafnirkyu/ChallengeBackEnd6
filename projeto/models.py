from django.db import models

class Tutor(models.Model):
    id_tutor = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=15)
    cidade = models.CharField(max_length=35)
    sobre = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    
class Pet(models.Model):

    PET_STATUS = [
        ('I', 'Indisponível'),
        ('D', 'Disponível'),
        ('E', 'Em espera'),
        ('A', 'Adotado')
    ]

    ESPECIE = [
        'Cachorro',
        'Gato'
    ]

    id_pet = models.AutoField(primary_key=True)
    nome_pet = models.CharField(max_length=30)
    especie = models.CharField(max_length=1, choices=ESPECIE, blank=False, null=False, default='Cachorro' )
    raca = models.CharField(max_length=100)
    personalidade = models.CharField(max_length=30)
    porte = models.CharField(max_length=30)
    especie = models.CharField(max_length=15)
    cidade_pet = models.CharField(max_length=35)
    sobre_pet = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=PET_STATUS, blank=False, null=False, default='I' )

    def __str__(self):
        return self.nome_pet
