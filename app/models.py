from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

class CustomUser(AbstractUser, PermissionsMixin):
    last_login_time = models.DateTimeField(null=True, blank=True)
    products = models.TextField(null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


