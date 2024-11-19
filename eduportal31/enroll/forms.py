from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(initial='User' , help_text="write only 30ch in this Field ! ")
    email = forms.EmailField()
   