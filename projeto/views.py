from rest_framework import viewsets, filters
from projeto.models import Tutor, Pet, Abrigo, Adocao
from projeto.serializer  import TutorSerializer, PetSerializer, AbrigoSerializer, AdocaoSerializer
from django_filters.rest_framework import DjangoFilterBackend


class TutorViewSet(viewsets.ModelViewSet):
    """Exibindo todos os tutores"""
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['nome']
   

class PetViewSet(viewsets.ModelViewSet):
    """Exibindo todos os pets"""
    queryset = Pet.objects.filter(adotado=False)
    serializer_class = PetSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['adotado']


class AbrigoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os abrigos"""
    queryset = Abrigo.objects.all()
    serializer_class = AbrigoSerializer


class AdocaoViewSet(viewsets.ModelViewSet):
    """Exibindo Adocoes"""
    queryset = Adocao.objects.all()
    serializer_class = AdocaoSerializer

