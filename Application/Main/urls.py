from django.urls import path
from Main import views

urlpatterns = [
    path("", views.index, name="home"),
    path("caesar", views.caesar, name="caesar"),
    path("playfair", views.playfair, name="playfair"),
    path("hill", views.hill, name="hill"),
    path("vigenere", views.vigenere, name="vigenere"),
    path("vernam", views.vernam, name="vernam"),
    path("railfence-conv", views.railfence, name="railfence-conv"),
    path("railfence-new", views.railfenceNew, name="railfence-new"),
    path("rc-transform", views.rcTransform, name="rc-transform"),
]
