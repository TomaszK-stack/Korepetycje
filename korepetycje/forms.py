from django import forms

class Search(forms.Form):
    name = forms.CharField()
