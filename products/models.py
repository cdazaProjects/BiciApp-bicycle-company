from django.conf import settings
from django.db import models

# Create your models here.
from companies.models import Company
from django.db.models.signals import post_save
from django.dispatch import receiver

from main.clients import BicycleApi


class Bicycle(models.Model):
    model = models.CharField(max_length=255, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    company = models.ForeignKey(Company, null=False, blank=False, on_delete=models.CASCADE)
    price = models.FloatField(null=False, blank=False)


imported_bicycles = []


@receiver(post_save, sender=Bicycle)
def register_bicycle(sender, instance, **kwargs):
    if instance.pk not in imported_bicycles:
        bicycle_api = BicycleApi()
        payload = dict(company_id=instance.company.nit,
                       model=instance.model,
                       address=instance.address,
                       price=instance.price,
                       company_name=instance.company.name)
        bicycle_api.register_bicycle(payload)
    imported_bicycles.append(instance.pk)

