"""geekshop URL Configuration

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
from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('gallery/', mainapp.gallery, name='gallery'),

    path('gallery/battlefield_1', mainapp.gallery, name='battlefield_1'),
    path('gallery/star_wars', mainapp.gallery, name='star_wars'),
    path('gallery/battlefield_4', mainapp.gallery, name='battlefield_4'),
    path('gallery/world_of_tanks', mainapp.gallery, name='world_of_tanks'),
    path('gallery/for_honor', mainapp.gallery, name='for_honor'),
    path('gallery/world_of_warships', mainapp.gallery, name='world_of_warships'),
    path('gallery/call_of_duty', mainapp.gallery, name='call_of_duty'),

    path('contacts/', mainapp.contacts, name='contacts'),
    path('gallery/assasin', mainapp.assasin, name='assasin'),
    path('admin/', admin.site.urls),
]
