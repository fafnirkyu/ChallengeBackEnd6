from rest_framework import serializers
from projeto.models import Tutor, Pet, Abrigo, Adocao
from projeto.validators import *

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

    def validate(self, data):
        if not telefone_valido(data['telefone']):
            raise serializers.ValidationError({'telefone':"O número de celular deve seguir este modelo: 11 91234-1234."})
        return data

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'
    
class AbrigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abrigo
        fields = '__all__'

    def validate(self, data):
        if not telefone_valido(data['telefone_abrigo']):
            raise serializers.ValidationError({'telefone':"O número de celular deve seguir este modelo: 11 91234-1234."})
        return data

class AdocaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adocao
        fields = '__all__'