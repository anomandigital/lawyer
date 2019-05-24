from django import forms
from ClassicUserAccounts.models import *
from django.contrib.auth.models import User
from ClassicUserAccounts import models
from django.conf import settings
import re


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    email = forms.CharField(label=None, required=True, max_length=60)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = models.User
        fields = ('first_name', 'last_name', 'password1', 'email', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_email(self):
        if hasattr(settings, 'CLASSIC_VALIDATE_EMAIL') and settings.CLASSIC_VALIDATE_EMAIL:
            if not self.valid_email(self.cleaned_data["email"]):
                raise forms.ValidationError("Please enter valid email")

        return self.cleaned_data["email"]

    def valid_email(self, email):
        if re.match(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email) != None:
            return True
        return False
