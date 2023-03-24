from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    measure_unit = models.CharField(max_length=10)