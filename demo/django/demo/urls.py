"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # Import Django's admin module
from django.urls import path, include  # Import Django's path and include functions for URL routing
from anymap import views  # Import views from the anymap application
from django.conf import settings  # Import Django's settings object

urlpatterns = [
    path('admin/', admin.site.urls),  # Route for admin site
    path('', views.home, name='home'),  # Home page route
    path('leaflet/', views.leaflet, name='leaflet'),  # Route for leaflet map view
    path('google/', views.google, name='google'),  # Route for google map view
    path('openlayers/', views.openlayers, name='openlayers'),  # Route for openlayers map view
    path('djangoMapCluster/', include('djangoMapCluster.api.urls')),  # Route for djangoMapCluster API
]

from django.conf.urls.static import static  # Import Django's static file serving function
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Append static file serving route