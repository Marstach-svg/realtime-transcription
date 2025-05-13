from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["name", "email", "password1", "password2"]


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
