from django.shortcuts import render
from .models import Student

# Create your views here.

def studentinfo(request):
    stud = Student.objects.all()
    # stud = Student.objects.get(pk=1)
    print('MyOutput',stud)
    return render(request , 'enroll/studentdetails.html' , {'stu' : stud})