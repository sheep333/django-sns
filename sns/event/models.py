from django.db import models


class Event(models.Model):
    name = models.CharField()
    description = models.TextField()
    date = models.DateTimeField()
    apply_deadline = models.DateTimeField()
    price = models.IntegerField()
