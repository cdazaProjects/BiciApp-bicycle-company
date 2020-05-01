from django import forms
from companies.models import Company


def my_portal_authenticate(nit, password):
    if nit == 'fooDjango' and password == 'barDjango':
        return True
    return False


class MyPortalBackend(object):
    def authenticate(self, request, **kwargs):
        '''
        kwargs will receive the python dict that may contain
        nit & password to authenticate which will be
        received from the Custom admin site.
        '''
        try:
            company = Company.objects.get(nit=kwargs['nit'])
            if company.check_password(kwargs['password']) and company.is_active:
                return company
        except KeyError as e:
            raise forms.ValidationError("Programming Error")

        except Company.DoesNotExist:
            return None

    def get_user(self, company_id):
        try:
            return Company.objects.get(pk=company_id)
        except Company.DoesNotExist:
            # Djano Admin treats None user as anonymous your who have no right at all.
            return None


