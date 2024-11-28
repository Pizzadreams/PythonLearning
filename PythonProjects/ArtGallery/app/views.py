import requests
from django.conf import settings
from django.shortcuts import render


def random_image(request):
    api_key = UNSPLASH_API_KEY
    url = f"https://api.unsplash.com/photos/random?client_id={api_key}"

    response = request.get(url)
    data = response.json

    # Check if the response contains an image
    if 'urls' in data:
        image_url = data['urls']['regular']
    else:
        image_url = None

    return render(request, 'index.html', {'image_url': image_url})