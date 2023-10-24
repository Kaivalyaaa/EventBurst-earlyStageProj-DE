#--------for user-admin
# user_admin/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class AdminLoginForm(AuthenticationForm):
    pass
