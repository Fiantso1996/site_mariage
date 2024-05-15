from django.urls import path
from .import views

urlpatterns = [
    path('', views.nouvelle, name="nouvelle"),
]