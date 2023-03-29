from django.contrib import admin
from django.urls import path, include
from projeto.views import TutorViewSet, PetViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tutores', TutorViewSet, basename='Tutores')
router.register('pets', PetViewSet, basename='Pets')


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
