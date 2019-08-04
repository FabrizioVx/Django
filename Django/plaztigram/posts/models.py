""" Posts models. """
from django.db import models

class User(models.Model):
    """User model."""

    email = models.EmailField(unique = True)
    password = models.CharField(max_length=80)

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank=True)

    birthday = models.DateField(blank = True, null = True)
    country = models.CharField(max_length=80, null = True)

    #Almacena ademas de la fecha, la hora
    create = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now = True)

def __str__(self):
    #""" Return name """
    return self.first_name





