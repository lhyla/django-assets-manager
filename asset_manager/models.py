from django.db import models


class Counter(models.Model):
    key = models.CharField(max_length=10)
    value = models.IntegerField()
class Asset(models.Model):
    value = models.DecimalField(max_digits=12, decimal_places=2)
    name = models.CharField(max_length=30)


class Income(models.Model):
    value = models.DecimalField(max_digits=12, decimal_places=2)
    name = models.CharField(max_length=30)


class Outcome(models.Model):
    value = models.DecimalField(max_digits=12, decimal_places=2)
    name = models.CharField(max_length=30)