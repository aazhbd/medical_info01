# -*- coding: utf-8 -*-

from django import forms
from django.forms.extras import widgets
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.contrib.auth.hashers import UNUSABLE_PASSWORD
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import get_current_site
from django.utils.http import int_to_base36
from django.template import loader
from django.utils.http import base36_to_int


class AuthenticationForm(forms.Form):
    """
    A custom Authentication Form.
    """
    username = forms.CharField(
        label=_("Username/Email"), required=True,
        widget=forms.TextInput(attrs={'placeholder':_("Username")})
    )
    password = forms.CharField(
        label=_("Password"), required=True,
        widget=forms.PasswordInput(attrs={'placeholder':_("Password")}, render_value=False)
    )

    error_messages = {
        'invalid_login': _("Please enter a correct username and password. Note that both fields are case-sensitive."),
        'no_cookies': _("Your Web browser doesn't appear to have cookies enabled. Cookies are required for logging in."),
        'inactive': _("Your account is inactive."),
        'not_activated': _("Your account is inactive. Please check your email and click the link to activate your account."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        If request is passed in, the form will validate that cookies are
        enabled. Note that the request (a HttpRequest object) must have set a
        cookie with the key TEST_COOKIE_NAME and value TEST_COOKIE_VALUE before
        running this validation.
        """
        self.request = request
        self.user_cache = None

        if self.request:
            self.request.session.set_test_cookie()

        super(AuthenticationForm, self).__init__(*args, **kwargs)

    def clean(self):
        """
        Checks for the username and password.
        """
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username, password=password)

            if self.user_cache is None:
                raise forms.ValidationError(self.error_messages['invalid_login'])
            elif not self.user_cache.is_active and self.user_cache.activation_set.filter(used=False):
                raise forms.ValidationError(self.error_messages['not_activated'])
            elif not self.user_cache.is_active:
                raise forms.ValidationError(self.error_messages['inactive'])

        self.check_for_test_cookie()
        return self.cleaned_data

    def check_for_test_cookie(self):
        if self.request and not self.request.session.test_cookie_worked():
            raise forms.ValidationError(self.error_messages['no_cookies'])

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache
