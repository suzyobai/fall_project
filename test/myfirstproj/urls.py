"""
URL configuration for myfirstproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from myfirstproj import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myfirstproj/', views.myfirstproj, name='myfirstproj'),
    path('view_reviews/', views.view_reviews, name='view_reviews'), #after pushing data for reviews should be able to see them here
    path('/',views.home) #added for homepage

    #path('blog/', include("blog.urls")), 
]
