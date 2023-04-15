from rest_framework import viewsets, filters
from rest_framework.permissions import DjangoModelPermissions
from projeto.models import User, Tutor, Pet, Adocao, Abrigo
from projeto.serializer  import  UserSerializer, TutorSerializer, PetSerializer, AbrigoSerializer, AdocaoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class TutorViewSet(viewsets.ModelViewSet):
    """Exibindo todos os tutores"""
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['nome']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

   

class PetViewSet(viewsets.ModelViewSet):
    """Exibindo os pets não adotados"""
    queryset = Pet.objects.filter(adotado=False)
    serializer_class = PetSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['adotado']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



class AbrigoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os abrigos"""
    queryset = Abrigo.objects.all()
    serializer_class = AbrigoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class AdocaoViewSet(viewsets.ModelViewSet):
    """Exibindo Adocoes"""
    queryset = Adocao.objects.all()
    serializer_class = AdocaoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = (DjangoModelPermissions, )
