from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=125)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=125)
    cretated_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User,related_name = 'user', on_delete=models.CASCADE)
    Location = models.CharField(max_length = 120)
    title = models.CharField(max_length=100)
    About = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.user.name