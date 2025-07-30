from django.urls import path
from . import views

urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
    path('gallery3d/', views.gallery3d, name='gallery3d'),
]