# views are Python functions that take a web request and return a web response
import random
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import json

def gallery(request):
    paintings = [
        {"img": "https://picsum.photos/800/600?random=1", "title": "Art 1", "desc": "Lorem ipsum dolor sit amet."},
        {"img": "https://picsum.photos/800/600?random=2", "title": "Art 2", "desc": "Consectetur adipiscing elit."},
        {"img": "https://picsum.photos/800/600?random=3", "title": "Art 3", "desc": "Sed do eiusmod tempor."},
    ]
    return render(request, 'index.html', {
        'paintings': paintings,
        'paintings_json': json.dumps(paintings)
    })