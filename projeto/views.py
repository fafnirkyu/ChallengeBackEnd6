from rest_framework import viewsets, generics
from projeto.models import Tutor, Pet
from projeto.serializer  import TutorSerializer, PetSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class TutorViewSet(viewsets.ModelViewSet):
    """Exibindo todos os tutores"""
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class PetViewSet(viewsets.ModelViewSet):
    """Exibindo todos os pets"""
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

