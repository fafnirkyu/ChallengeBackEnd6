from django.contrib import admin
from django.urls import path, include
from projeto.views import  TutorViewSet, PetViewSet, AbrigoViewSet, AdocaoViewSet
from rest_framework import routers

app_name = 'account'
router = routers.DefaultRouter()
router.register('tutores', TutorViewSet, basename='Tutores')
router.register('pets', PetViewSet, basename='Pets')
router.register('abrigos', AbrigoViewSet, basename='Abrigos')
router.register('adocao', AdocaoViewSet, basename='Adoção')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),

]
