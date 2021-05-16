from django.contrib.auth.models import User
from django.db import models


class Player(models.Model):
    display_name = models.CharField(max_length=40,unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)