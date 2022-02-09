from django.db import models

# Create your models here.

class Post(models.Model):
    imagen = models.ImageField(upload_to='')