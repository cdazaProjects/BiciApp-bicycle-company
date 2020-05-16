import json
import os
from random import randint

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()
from django.test import TestCase
from rest_framework.test import APIClient
from companies.models import Company



class AddOpenQuestionTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = '/api/company/register'
        self.headers = {'Content-Type': 'application/json'}

    def test_add_company(self):
        nit = "3"
        if Company.objects.filter(nit=nit).exists():
            nit += str(randint(0, 10))
        payload = {
            "nit": nit,
            "name": "3",
            "address": "3",
            "password": "pass",
            "confirm_password": "pass"
        }
        response = self.client.post(self.url,  payload, format='json')
        current_data = json.loads(response.content)
        company = Company.objects.filter(nit=nit)
        self.assertTrue(company.exists())
        company = company.first()
        self.assertEquals(company.name, payload['name'])
        self.assertEquals(company.address, payload['address'])
