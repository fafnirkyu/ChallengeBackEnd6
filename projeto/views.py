from rest_framework import viewsets, generics
from projeto.models import Tutor
from projeto.serializer  import TutorSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class TutorViewSet(viewsets.ModelViewSet):
    """Exibindo todos os tutores"""
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]