from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def showformdata(request):
    fm = StudentRegistration(initial={ 'name' : 'Geeky Shows'})
    return render(request , 'enroll/userregistration.html' , {'form' : fm})