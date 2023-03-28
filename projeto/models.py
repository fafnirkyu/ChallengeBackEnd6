from django.db import models

class Tutor(models.Model):
    id_tutor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=15)
    cidade = models.CharField(max_length=35)
    sobre = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
