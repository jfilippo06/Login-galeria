from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    imagen = models.ImageField(upload_to='')

    def __str__(self) -> str:
        return self.imagen