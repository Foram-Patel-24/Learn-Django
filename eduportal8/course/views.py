from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def learn_django(request):
    d = "<h1>This is Django...</h1>"
    return HttpResponse(d)

def learn_python(reuest):
    return HttpResponse("<h1>This is Python...</h1>")