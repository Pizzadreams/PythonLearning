# views are Python functions that take a web request and return a web response
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def gallery(request):
    template = loader.get_template('gallery/index.html')
    return HttpResponse("Hello world!")