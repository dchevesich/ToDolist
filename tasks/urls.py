from django.urls import path
from . import views

urlpatterns = [
    path("", views.saludar),
    path("tareas/", views.modelando, name="datatodo"),
    path("modificar/<int:pk>", views.modificando, name="modificar_tarea"),
    path("eliminar/<int:pk>", views.eliminar_tarea, name="eliminar_tarea")
]
