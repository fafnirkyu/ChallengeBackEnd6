from rest_framework import serializers
from projeto.models import Tutor, Pet


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ['id_tutor','email' , 'nome', 'telefone', 'cidade', 'sobre']

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id_pet', 'nome_pet', 'raca', 'especie', 'personalidade', 'sobre_pet', 'porte', 'especie', 'cidade_pet', 'status']