from rest_framework import viewsets, filters, status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from projeto.models import User, Pet, Adocao
from projeto.serializer  import  TutorSerializer, PetSerializer, AbrigoSerializer, AdocaoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated



class TutorViewSet(viewsets.ModelViewSet):
    """Exibindo todos os tutores"""
    queryset = User.objects.filter(is_tutor=True, is_shelter=False, is_active=True)
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
    queryset = User.objects.filter(is_tutor=True, is_shelter=True, is_active=True)
    serializer_class = AbrigoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class AdocaoDRU(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(is_tutor=False, is_shelter=True, is_active=True)
    serializer_class = AdocaoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data={"msg": "Adoção deletada com sucesso."}, status=status.HTTP_200_OK)



class AdocaoViewSet(viewsets.ModelViewSet):
    """Exibindo Adocoes"""
    queryset = Adocao.objects.all()
    serializer_class = AdocaoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

