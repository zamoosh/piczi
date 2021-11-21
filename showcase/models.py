from django.db import models
from django.contrib.auth.models import User


class Picture(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return self.name
