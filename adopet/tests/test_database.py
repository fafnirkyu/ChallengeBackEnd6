from django.test import TestCase
from projeto.models import *

class TutorTestCase(TestCase):
    def setUp(self):
        Tutor.objects.create(
            id_tutor = 1,
            email_tutor = 'emailteste@teste.com',
            nome="Tutor Teste",
            telefone = '11 91234-1234',
            cidade='Cidade Teste',
            sobre= 'teste sobre o tutor',
            foto_tutor = None
            )

    def teste_modelo_tutor(self):
        
        self.assertEqual(Tutor.objects.count(), 1)

        Nome = Tutor.objects.get(nome="Tutor Teste")
        self.assertEqual(Nome.id_tutor, 1)
        self.assertEqual(Nome.email_tutor, 'emailteste@teste.com')
        self.assertEqual(Nome.telefone, '11 91234-1234')
        self.assertEqual(Nome.sobre,  'teste sobre o tutor')
        self.assertEqual(Nome.cidade, 'Cidade Teste')