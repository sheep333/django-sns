from django.db import models


class Product(models.Model):
    name = models.CharField()
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    apply_deadline = models.DateTimeField()
