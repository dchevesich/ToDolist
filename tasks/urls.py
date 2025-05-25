from django.urls import path
from . import views

urlpatterns = [
    path("", views.saludar),
    path("tareas/", views.modelando, name="datatodo")
]
