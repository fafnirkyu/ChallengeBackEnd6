from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


letrasregex = RegexValidator(r'^[a-zA-Z_ áàâãéèêíïóôõöúçñ]*$', 'Não inclua números neste campo')

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	email = models.EmailField(verbose_name="email", max_length=60, unique=True)
	username = models.CharField(max_length=30, unique=True)
	date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_tutor = models.BooleanField(default=False)
	is_shelter = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = MyAccountManager()

	def __str__(self):
		return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True

class User(models.Model):
    username = models.CharField("Usuário", max_length=255 ,validators=[letrasregex]) 
    email = models.EmailField("Email" ,max_length=255, unique=True)
    password = models.CharField("Senha", max_length=35)
    password2 = models.CharField(max_length=35)
    is_tutor = models.BooleanField("É Tutor", default=False)
    is_shelter = models.BooleanField("É Abrigo", default=False)
    is_active = models.BooleanField("Ativo", default=False)


class Tutor(models.Model):
    id_tutor = models.AutoField(primary_key=True)
    email_tutor = models.EmailField("Email" ,max_length=255, unique=True)
    nome = models.CharField("Nome completo", max_length=255,validators=[letrasregex])
    telefone = models.CharField("Telefone", max_length=25)
    cidade = models.CharField(max_length=255,validators=[letrasregex])
    sobre = models.CharField(max_length=255, validators=[letrasregex])
    foto_tutor = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Abrigo(models.Model):
    id_abrigo = models.AutoField(primary_key=True)
    email_abrigo = models.EmailField(max_length=255, unique=True)
    nome_abrigo = models.CharField(max_length=255, validators=[letrasregex])
    telefone_abrigo = models.CharField(max_length=25)
    cidade_abrigo = models.CharField(max_length=255,validators=[letrasregex])
    sobre_abrigo = models.CharField(max_length=255)
    foto_abrigo = models.ImageField(blank=True, null=True)


class Pet(models.Model):
    id_pet = models.AutoField(primary_key=True)
    nome_pet = models.CharField(max_length=30,validators=[letrasregex])
    cidade_pet = models.CharField(max_length=50,validators=[letrasregex])
    idade_pet = models.CharField(max_length=255, blank=True, null=True)
    sobre_pet = models.CharField(max_length=255,validators=[letrasregex])
    adotado = models.BooleanField(default=False)
    foto_pet = models.ImageField(blank=True, null=True)
    id_abrigo = models.ForeignKey(  Abrigo, on_delete=models.CASCADE, blank=True)
    def __str__(self):
        return self.nome_pet    


class Adocao(models.Model):
    id_adocao = models.AutoField(primary_key=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    data_adocao = models.DateField()