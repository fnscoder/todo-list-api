from django.contrib.auth.models import User
from django.db import models


class List(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(List, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name
