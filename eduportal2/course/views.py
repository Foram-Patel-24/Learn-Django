from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>Home Page</h1>')

def learn_django(request):
    return HttpResponse('<h1>Hello Django</h1>')

def learn_python(request):
    return HttpResponse('<h1>Hello Python</h1>')

def learn_var(request): 
    f = ('<h1>Hello Variable</h1>')
    return HttpResponse(f)

def learn_math(request):
    f = 3 + 5
    return HttpResponse(f)

def learn_format(request):
    f = "Guys"
    return HttpResponse(f'Hello How are You {f}') 