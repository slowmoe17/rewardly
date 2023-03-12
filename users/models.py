from urllib import response
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.conf import settings
from django.http import HttpResponse

class User(AbstractUser):
    

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True)
    first_name = None
    last_name = None

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]


objects = CustomUserManager()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)


    def __str__(self):
        return self.user.username + " Profile"
    



