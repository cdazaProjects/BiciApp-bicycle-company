from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Company(AbstractUser):
    name = models.CharField(max_length=255, null=False, blank=False)
    nit = models.CharField(max_length=255, primary_key=True)
    address = models.CharField(max_length=255, null=False, blank=False)


@receiver(pre_save, sender=settings.AUTH_USER_MODEL)
def set_username_as_email(sender, instance, **kwargs):
    instance.username = instance.nit

