"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os

# API Root view
@api_view(['GET'])
def api_root(request):
    return Response({
        'message': 'OctoFit Tracker API',
        'version': '1.0.0'
    })

# Router for API endpoints
router = DefaultRouter()

urlpatterns = [
    path('', api_root, name='root'),
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
    path('api/users/', include('users.urls')),
    path('api/teams/', include('teams.urls')),
    path('api/activities/', include('activities.urls')),
    path('api/workouts/', include('workouts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('dj_rest_auth.urls')),
]
