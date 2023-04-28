from django.urls import path
from Main import views

urlpatterns = [
    path("", views.index, name="home"),
    path("name", views.get_name, name="form"),
    path("caesar", views.caesar, name="caesar")
]
