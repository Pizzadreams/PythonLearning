# gallery/views.py
import requests
from django.shortcuts import render
from django.conf import settings
import random

def random_image_view(request):
    # Fetch a random image from Unsplash
    url = f'https://api.unsplash.com/photos/random?client_id={settings.UNSPLASH_ACCESS_KEY}'
    response = requests.get(url)
    
    if response.status_code == 200:
        artwork = response.json()
        image_url = artwork['urls']['regular']
        title = artwork['description'] if artwork['description'] else "Untitled"
    else:
        image_url = None
        title = "Error fetching image"

    return render(request, 'gallery/index.html', {'image_url': image_url, 'title': title})