from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.contrib.auth.models import User

class ViewTestCase(TestCase):
      
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_tutor_view(self):
        response = self.client.get('/tutores/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pet_view(self):
        response = self.client.get('/pets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_abrigo_view(self):
        response = self.client.get('/abrigos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_adocao_view(self):
        response = self.client.get('/adocao/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ViewTestUnnauthorized:
    
    def setUp(self):
        self.client = APIClient()
    
    def test_sem_auth_view(self):
        response = self.client.get('/tutores/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)