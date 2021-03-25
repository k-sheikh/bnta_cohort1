from django import forms


class NewAuthorForm(forms.Form):
    name = forms.CharField(max_length=200)
    year_of_birth = forms.IntegerField()
