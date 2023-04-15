from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('Tutores-list')
        self.user = User.objects.create_user('test_user', password= '123456')

    def test_authenticacao_user_com_credenciais_corretas(self):
        user = authenticate(username='test_user', password = '123456')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_requisicao_get_nao_autoriazada(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_autenticacao_de_user_com_username_incorreto(self):
        user = authenticate(username='test_user errado', password = '123456')
        self.assertFalse((user is not None) and user.is_authenticated)        

    def test_requisicao_get_com_user_autenticado(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)