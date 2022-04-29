from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    
    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('Precisa informar o e-mail')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super Usuário precisa estar com o "is_staff = True"')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super Usuário precisa estar com o "is_superuser = True"')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Super Usuário precisa estar com o "is_active = True"')
        
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='E-mail', unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = CustomUserManager()


    def __str__(self):
        return self.email