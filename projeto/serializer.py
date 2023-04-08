from rest_framework import serializers
from projeto.models import Account, User, Tutor, Pet, Abrigo, Adocao
from projeto.validators import *


class RegistrationSerializer(serializers.ModelSerializer):

	password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = Account
		fields = ['email', 'username', 'password', 'password2']
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	def	save(self):

		conta = Account(
					email=self.validated_data['email'],
					username=self.validated_data['username']
				)
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		conta.set_password(password)
		conta.save()
		return conta


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ('id_tutor', 'nome', 'email_tutor', 'telefone', 'cidade',  'sobre', 'foto_tutor')

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