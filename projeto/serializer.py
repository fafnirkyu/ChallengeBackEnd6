from rest_framework import serializers
from projeto.models import Tutor, Pet
from projeto.validators import *

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

    def validate_tutor(self, data):
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Não inclua números neste campo"})
        if not cidade_valida(data['cidade']):
            raise serializers.ValidationError({'cidade':"Não inclua números neste campo"})
        if not telefone_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O número de celular deve seguir este modelo: 11 91234-1234."})
        return data 

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

    def validate_pet(self, data):
        if not nome_pet_valido(data['nome_pet']):
            raise serializers.ValidationError({'nome_pet':"Não inclua números neste campo"})
        if not raca_valido(data['raca']):
            raise serializers.ValidationError({'raca':"Não inclua números neste campo"})
        if not especie_valido(data['especie']):
            raise serializers.ValidationError({'especie':"Não inclua números neste campo"})
        if not personalidade_valido(data['personalidade']):
            raise serializers.ValidationError({'personalidade':"Não inclua números neste campo"})
        if not sobre_pet_valido(data['sobre_pet']):
            raise serializers.ValidationError({'sobre_pet':"Não inclua números neste campo"})
        if not porte_valido(data['porte']):
            raise serializers.ValidationError({'porte':"Não inclua números neste campo"})
        if not cidade_pet_valido(data['cidade_pet']):
            raise serializers.ValidationError({'cidade_pet':"Não inclua números neste campo"})
        return data 