# views are Python functions that take a web request and return a web response
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def gallery(request):
    return HttpResponse("Hello world!")