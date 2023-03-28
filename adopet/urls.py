from django.contrib import admin
from django.urls import path, include
from projeto.views import TutorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tutores', TutorViewSet, basename='Tutores')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
