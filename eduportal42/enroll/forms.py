from django.core import validators
from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    email = forms.EmailField()
    
''' def clean(self):
        clean_data = super().clean()
        vlname = self.cleaned_data['name']
        vlemail = self.cleaned_data['email']

        if len(vlname) < 8 :
            raise forms.ValidationError('Name should be more than or equal 8 character ')
        
        if len(vlemail) < 20 :
            raise forms.ValidationError('Email should be more than or equal 20 character')
    '''