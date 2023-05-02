from django.urls import path
from Main import views

urlpatterns = [
    path("", views.index, name="home"),
    path("caesar", views.caesar, name="caesar"),
    path("playfair", views.playfair, name="playfair")
]
