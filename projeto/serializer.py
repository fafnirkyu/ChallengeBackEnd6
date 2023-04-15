from rest_framework import serializers
from projeto.models import User, Tutor, Pet, Abrigo, Adocao
from projeto.validators import *
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'}, label='Password')
    repita_senha = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'}, label='Confirm Password')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'senha', 'repita_senha']

    def validate(self, data):
        if data['senha'] != data['repita_senha']:
            raise serializers.ValidationError("As senhas não coincidem.")
        del data['repita_senha']
        return data

    def create(self, validated_data):
        password = validated_data.pop('senha')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user




class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

    def validate(self, data):   
        if not telefone_valido(data['telefone']):
            raise serializers.ValidationError({'telefone':"O número de celular deve seguir este modelo: 11 91234-1234."})
        return data
  
class AbrigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abrigo
        fields = '__all__'

    def validate(self, data):
        if not telefone_valido(data['telefone_abrigo']):
            raise serializers.ValidationError({'telefone':"O número de celular deve seguir este modelo: 11 91234-1234."})
        return data

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('nome_pet', 'cidade_pet', 'idade_pet', 'sobre_pet', 'adotado', 'foto_pet')

class AdocaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adocao
        fields = '__all__'