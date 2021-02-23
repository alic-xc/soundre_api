from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)


class Profile(models.Model):
    """ """

    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='client')
    avater = models.FileField(null=True, upload_to='users')

    def __str__(self):
        return self.user.username
