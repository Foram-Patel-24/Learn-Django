from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def showformdata(request):
    fm = StudentRegistration(auto_id='some_%s' , label_suffix='' , initial= { 'name' : 'username' , 'email' : 'useremail@example.com'})
    return render(request , 'enroll/userregistration.html' , {'form' : fm})