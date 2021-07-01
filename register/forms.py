from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Register(UserCreationForm):
    email = forms.EmailField(help_text='')
    username = forms.CharField(help_text='')

    class meta():
        model = User
        fields = ['email']

