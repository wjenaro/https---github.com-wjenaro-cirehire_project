from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    firstname=forms.CharField(max_length=100)
    lastname=forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    tel=forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ["firstname", "lastname", "username", "email","tel", "password1", "password2"]