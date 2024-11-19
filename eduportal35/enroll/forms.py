from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'somecss1' , 'id' : 'uniqueid'}))
    password = forms.CharField(widget=forms.PasswordInput())
    image = forms.CharField(widget=forms.FileInput())
  
   