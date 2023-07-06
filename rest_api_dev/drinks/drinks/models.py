from django.db import models


class Drinks(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
