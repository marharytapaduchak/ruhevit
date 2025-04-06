from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPES = [
        ('military', 'Військовий'),
        ('volunteer', 'Волонтер'),
        ('admin', 'Адміністратор'),
    ]
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=USER_TYPES)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.username} ({self.type})'
