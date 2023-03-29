from django.contrib import admin
from projeto.models import Tutor, Pet

class Tutores(admin.ModelAdmin):
    list_display = ('id_tutor','email' , 'nome', 'telefone', 'cidade', 'sobre')
    list_display_links = ('id_tutor', 'nome', 'email')
    search_fields = ('nome', 'email',)
    list_per_page = 20

admin.site.register(Tutor, Tutores)


class Pets(admin.ModelAdmin):
    list_display = ('id_pet', 'nome_pet', 'especie', 'personalidade', 'sobre_pet', 'porte', 'especie', 'cidade_pet', 'status')
    list_display_links = ('id_pet', 'nome_pet', 'especie')
    search_fields = ('nome_pet', 'especie',)
    list_per_page = 20

admin.site.register(Pet, Pets)
