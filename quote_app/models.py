from django.db import models
# quote/models.py


class ParcelQuote(models.Model):
    from_country = models.CharField(max_length=100)
    from_postcode = models.CharField(max_length=20)
    to_country = models.CharField(max_length=100)
    to_postcode = models.CharField(max_length=20)
    quantity = models.IntegerField(default=1)
    weight = models.FloatField()
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    unit_metric = models.BooleanField(default=True)  # True = kg/cm, False = lb/in

