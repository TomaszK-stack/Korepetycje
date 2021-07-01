from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Register(UserCreationForm):
    email = forms.EmailField()
    class meta():
        model = User
        fields = ['email']

