from django.db import models


class CrowdFund(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


class Gift(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    fund = models.ForeignKey(CrowdFund, on_delete=models.CASCADE)
    price = models.IntegerField()


class Supporter(models.Model):
    user = models.ForeignKey("register.User", on_delete=models.CASCADE)
    choice_gift = models.ForeignKey(Gift, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=255)
    payment_check = models.BooleanField()
