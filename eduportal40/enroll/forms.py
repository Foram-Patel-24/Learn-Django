from typing import Any
from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_name(self):
        vlnm = self.cleaned_data['name']
        if len(vlnm) < 8:
            raise forms.ValidationError('Enter more than or equal 8 character')
        return vlnm