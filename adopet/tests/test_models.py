from django.test import TestCase
from projeto.models import *

class TutorModelTestCase(TestCase):
    def setUp(self):
        self.tutor = Tutor(
            id_tutor = 1,
            email_tutor = 'teste@gmail.com',
            nome = 'testando teste',
            telefone = '11-91234-1234',
            cidade = 'cidade do teste',
            sobre=  'este é um teste',
            )

    def test_verifica_atributos_de_tutor(self):
        self.assertEqual(self.tutor.id_tutor, 1)
        self.assertEqual(self.tutor.email_tutor, 'teste@gmail.com')
        self.assertEqual(self.tutor.nome, 'testando teste')
        self.assertEqual(self.tutor.telefone, '11-91234-1234')
        self.assertEqual(self.tutor.cidade, 'cidade do teste')
        self.assertEqual(self.tutor.sobre, 'este é um teste')
        self.assertEqual(self.tutor.foto_tutor, None)


class PetModelTestCase(TestCase):
    
    def setUp(self):        
        self.pet = Pet(
        id_pet = '1',
        nome_pet = 'teste',
        cidade_pet = 'teste',
        idade_pet = 'teste',
        sobre_pet = 'teste'
        )

    def test_verifica_atributos_de_pet(self):
        self.assertEqual(self.pet.id_pet, '1')
        self.assertEqual(self.pet.nome_pet, 'teste')
        self.assertEqual(self.pet.cidade_pet, 'teste')
        self.assertEqual(self.pet.idade_pet, 'teste')
        self.assertEqual(self.pet.sobre_pet, 'teste')
        self.assertEqual(self.pet.adotado, False)