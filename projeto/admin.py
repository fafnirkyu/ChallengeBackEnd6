from django.contrib import admin
from projeto.models import Tutor

class Tutores(admin.ModelAdmin):
    list_display = ('id_tutor', 'nome', 'telefone', 'cidade', 'sobre')
    list_display_links = ('id_tutor', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Tutor, Tutores)
