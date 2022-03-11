from django.contrib import admin
from django.urls import path
from kali import views

urlpatterns = [
    path("", views.index, name='kali'),
    path("about", views.about, name='about'),
    path("punjabi", views.punjabi, name='punjabi'),
    path("south", views.south, name='south'),
    path("italian", views.italian, name='italian'),
    path("contact", views.contact, name='contact')
    
]