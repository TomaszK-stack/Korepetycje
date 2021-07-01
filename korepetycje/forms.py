from django import forms

class Search(forms.Form):
    subject = forms.CharField(label='Znajdź swojego korepetytora!',required=False)
