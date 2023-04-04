import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adopet.settings')
django.setup()

from faker import Faker
import random
from projeto.models import Tutor

def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        nome = fake.name()
        email = '{}@{}'.format(nome.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        cidade = fake.address()
        telefone = "{} 9{}-{}".format(random.randrange(10, 21), random.randrange(4000, 9999), random.randrange(4000, 9999))
        sobre = fake.text()
        p = Tutor(nome=nome, email=email, cidade=cidade, telefone=telefone, sobre=sobre)
        p.save()

criando_pessoas(50)