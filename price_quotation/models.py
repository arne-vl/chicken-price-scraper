from django.db import models

# Create your models here.
class PriceQuotation(models.Model):
    date = models.DateField()
    week = models.IntegerField()
    deinze = models.FloatField(max_length=10)
    abc = models.FloatField(max_length=10)

