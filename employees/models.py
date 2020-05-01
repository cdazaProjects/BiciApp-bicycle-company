from django.db import models

# Create your models here.
from companies.models import Company


class Employee(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    okta_id = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=False, blank=False)
    age = models.IntegerField(default=20, null=False, blank=False)
    company = models.ForeignKey(Company, null=False, blank=False, on_delete=models.CASCADE)
