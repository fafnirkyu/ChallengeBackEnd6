from rest_framework import serializers
from projeto.models import Tutor


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ['id_tutor', 'nome', 'telefone', 'cidade', 'sobre']
