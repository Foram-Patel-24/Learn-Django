from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration

# Create your views here.
def thankyou(request):
    return render(request , 'enroll/success.html')

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('Form validated.')
            name = fm.cleaned_data['name']
            email =fm.cleaned_data['email']
            password =fm.cleaned_data['password']
            print('Name : ' , name)
            print('Email : ' , email)
            print('Password : ' , password)
            return HttpResponseRedirect('/regi/success/')
           # return render(request , 'enroll/success.html' , {'nm' : name})

    else:
        fm = StudentRegistration()
    return render(request , 'enroll/userregistration.html' , {'form' : fm})