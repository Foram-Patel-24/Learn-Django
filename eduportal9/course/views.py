from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def learn_django(request):
    return HttpResponse("<h1>Django</h1>")

def learn_python(request):
    return HttpResponse("<h1>Python</h1>")