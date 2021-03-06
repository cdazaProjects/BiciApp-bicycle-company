from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Nit', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': ''}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': ''
        }
        )
    )

    # overriding clean method to change default authentication behaviour
    def clean(self):
        userid = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if userid and password:
            # the backends will be picked from the settings from the variable named AUTHENTICATION_BACKENDS
            # and the authentication method of each of one will be called in the same order as the order in the AUTHENTICATION_BACKENDS list
            self.user_cache = authenticate(nit=userid, password=password)

            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data