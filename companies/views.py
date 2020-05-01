from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView

from companies.models import Company
from companies.serializers import CompanySerializer


class CompanyViewSet(CreateAPIView):
    serializer_class = CompanySerializer
    query = Company.objects.all()