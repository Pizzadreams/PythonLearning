# views are Python functions that take a web request and return a web response
import random
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def gallery(request):
    template = loader.get_template('index.html')
    random_number = random.randint(1, 1000)
    context = {
        'random_number': random_number,
    }
    return HttpResponse(template.render())

