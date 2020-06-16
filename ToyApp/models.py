from django.db import models

class Toy(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)