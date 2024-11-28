import requests
from django.shortcuts import render

def display_image(request):
    # Fetch a random Unsplash image
    image_url = 'https://source.unsplash.com/random'
    return render(request, 'index.html', {'image_url': image_url})
