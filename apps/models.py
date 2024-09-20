from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    staff = models.CharField(max_length=120, blank=True, null=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    discription = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images')
