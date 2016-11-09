from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User


class LoginForm(forms.Form):

    username = forms.CharField(label=_(""), max_length=70)
    password = forms.CharField(label=_(""), widget=forms.PasswordInput)

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['username'].widget.attrs['class'] = 'input-text-box'
        self.fields['password'].widget.attrs['class'] = 'input-text-box'

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            self.user_cache = authenticate(username=username,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(('invalid_login'))
            elif not self.user_cache.is_active:
                raise forms.ValidationError(('inactive'))
            return self.cleaned_data


    def get_user(self):
        return self.user_cache
