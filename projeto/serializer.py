from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from projeto.models import User, Tutor, Pet, Abrigo, Adocao
from projeto.validators import *


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(label="Confirme sua senha", max_length=128, write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'is_tutor', 'is_shelter', 'is_active')
        extra_kwargs = {"password": {"write_only": True}}
    
    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError("Password não são iguais.")
        return attrs

    def validate_password(self, value):
        validate_password(value)
        return value

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
        fields = ('nome_pet', 'cidade_pet', 'idade_pet', 'sobre_pet', 'adotado', 'id_abrigo', 'foto_pet')
    
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