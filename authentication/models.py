from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    tags = models.ManyToManyField(Tag)