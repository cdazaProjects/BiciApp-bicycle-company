from django.conf.urls import url
from django.urls import path

from companies.views import CompanyViewSet

urlpatterns = [
    url(r'^register', CompanyViewSet.as_view(), name='register'),
]