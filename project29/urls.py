"""project29 URL Configuration

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
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("insert_games/",insert_games,name="insert_games"),
    path('insert_player/',insert_player,name='insert_name'),
    path('insert_location/',insert_location,name='insert_location'),
    
    path('retrieve_data/',retrieve_data,name="retrieve_data"),
    path("display_player/",display_player,name="display_player"),
    path('checkbox/',checkbox,name="checkbox"),
    
    path("retrieve_data_player/",retrieve_data_player,name="retrieve_data_player"),
    path('display_location/',display_location,name="display_location"),
    
    path('radio/',radio,name="radio"),
    
    path("checkbox_player/",checkbox_player,name="checkbox_player"),
    
    path("updating_data/",updating_data,name="updating_data"),
    
  
]
