from django.urls import path
from .views import random_image_view

urlpatterns = [
    path('', random_image_view, name='random_image'),  # Root URL for the gallery
]