from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class SignUp(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm = models.CharField(max_length=255)