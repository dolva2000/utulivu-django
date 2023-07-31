from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class autiste (models.Model):
    name=models.CharField(max_length=250,unique=True)

    class Meta:
        db_table="tb_autiste"

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Meta:
        db_table="tb_user"

     