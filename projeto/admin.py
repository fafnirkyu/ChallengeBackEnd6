from django.contrib import admin
from projeto.models import Tutor, Pet, Abrigo, Adocao

class Tutores(admin.ModelAdmin):
    list_display = ('id_tutor','email_tutor' , 'nome', 'telefone', 'cidade', 'sobre')
    list_display_links = ('id_tutor', 'nome', 'email_tutor')
    search_fields = ('id_tutor','nome', 'email_tutor',)
    list_per_page = 20

admin.site.register(Tutor, Tutores)


class Pets(admin.ModelAdmin):
    list_display = ('id_pet', 'nome_pet', 'sobre_pet', 'cidade_pet', 'adotado')
    list_display_links = ('id_pet', 'nome_pet', 'adotado')
    search_fields = ('id_pet', 'nome_pet', 'adotado')
    list_per_page = 20

admin.site.register(Pet, Pets)

class Abrigos(admin.ModelAdmin):
    list_display = ('id_abrigo','email_abrigo' , 'nome_abrigo', 'telefone_abrigo', 'cidade_abrigo', 'sobre_abrigo')
    list_display_links = ('id_abrigo', 'nome_abrigo', 'email_abrigo')
    search_fields = ('id_abrigo', 'nome', 'email',)
    list_per_page = 20

admin.site.register(Abrigo, Abrigos)

class Adocoes(admin.ModelAdmin):
    list_display = ('id_adocao',)
    list_display_links = ('id_adocao',)
    search_fields = ('id_adocao', 'id_tutor', 'id_pet')
    list_per_page = 20

admin.site.register(Adocao, Adocoes)
