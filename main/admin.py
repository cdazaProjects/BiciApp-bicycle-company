from django.contrib.admin import AdminSite

from companies.models import Company
from .login import CustomLoginForm
from django.utils.translation import ugettext_lazy as _


class CustomLoginAdminSite(AdminSite):
    site_title = _('My site admin')
    site_header = _('Company site')
    index_title = _('CustomLogin')
    login_form = CustomLoginForm


#create a Admin_site object to register models
admin_site = CustomLoginAdminSite()
