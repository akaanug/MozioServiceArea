from providers.models import Provider
from django.contrib.gis.db import models
from djmoney.models.fields import MoneyField


class ServiceArea(models.Model):
    name = models.CharField(max_length=255)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    price = MoneyField(max_digits=20, decimal_places=10, blank=True, null=True)
    polygon = models.PolygonField()

    def __str__(self):
        return 'Service Area Name: {}, Provider Name: {}'.format(self.name, self.provider.name)
