from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]


class AdminSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "login-input",
            "placeholder": "Enter username"
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "login-input",
            "placeholder": "Password"
        })
    )