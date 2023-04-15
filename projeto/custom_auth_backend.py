from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import AuthenticationFailed

UserModel = get_user_model()

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password):
                return user
            else:
                raise AuthenticationFailed("Invalid email or password")
        except ObjectDoesNotExist:
            raise AuthenticationFailed("Invalid email or password")