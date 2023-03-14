from django.contrib.auth.models import User
from django.db import models


class Preference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='preference')
    tags = models.JSONField()
