from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration

# Create your views here.

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('Form validated.')
            print('Name : ' , fm.cleaned_data['name'])
            print('Roll No : ' , fm.cleaned_data['rollno'])
            print('Price : ' , fm.cleaned_data['price'])
            print('Rate : ' , fm.cleaned_data['rate'])
            print('Email : ' , fm.cleaned_data['email'])
            print('Comment : ' , fm.cleaned_data['comment'])
            print('Website : ' , fm.cleaned_data['website'])
            print('Password : ' , fm.cleaned_data['password'])
            print('Description : ' , fm.cleaned_data['desc'])
            print('Feedback : ' , fm.cleaned_data['feedback'])
            print('Notes : ' , fm.cleaned_data['notes'])
            print('Agree : ' , fm.cleaned_data['agree'])
         
    else:

        fm = StudentRegistration()
        
    return render(request , 'enroll/userregistration.html' , {'form' : fm})