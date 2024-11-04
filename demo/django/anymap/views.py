from django.conf import settings  # Import Django's settings module to access project settings
from django.shortcuts import render  # Import Django's render function to render templates

def home(request):
    # View function for the home page
    return render(request, 'base.html', {})

def leaflet(request):
    # View function for displaying the Leaflet map
    return render(request, 'leaflet.html', {})

def google(request):
    # View function for displaying the Google Maps map
    context = {
        'google_maps_api_key': getattr(settings, 'GOOGLE_MAPS_API_KEY', None)  # Retrieve the Google Maps API key from settings
    }
    return render(request, 'google.html', context)

def openlayers(request):
    # View function for displaying the OpenLayers map
    return render(request, 'openlayers.html', {})