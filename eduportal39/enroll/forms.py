from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(min_length=3 ,max_length=8,strip=False,empty_value='username',error_messages={'required' : 'Enter Your Name'})
    rollno = forms.IntegerField(min_value=1 , max_value=9999)
    price = forms.DecimalField(min_value=100 , max_value=99999 , max_digits=8 , decimal_places=2)
    rate = forms.FloatField(min_value=1 , max_value=5)
    email = forms.EmailField(min_length=10 , max_length=80)
    comment = forms.SlugField()
    website = forms.URLField(min_length=20 , max_length=80)
    password = forms.CharField(min_length=8 , max_length=30 , widget=forms.PasswordInput)
    desc = forms.CharField(widget=forms.Textarea)
    feedback = forms.CharField(min_length=25 , max_length=88 , widget=forms.TextInput(attrs={'class':'somecss1 somecss2' , 'id' : 'uniqueid'}))
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows':3 , 'cols': 50}))
    agree = forms.BooleanField(label_suffix=' ' , label='I Agree')
   