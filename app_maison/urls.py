from django.urls import path
from .import views

urlpatterns = [
    path('', views.maison, name="maison"),
]