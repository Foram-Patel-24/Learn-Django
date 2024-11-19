from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(label='Your Name' , label_suffix=' ' , initial='Your_Name' , required=False , disabled=True , help_text='Limit 80Ch ')
  
   