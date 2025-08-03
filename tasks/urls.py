from django.urls import path
from . import views

urlpatterns = [
    path("", views.LoginForm, name="login"),
    path("modificar/<int:pk>", views.modificando, name="modificar_tarea"),
    path("eliminar/<int:pk>", views.eliminar_tarea, name="eliminar_tarea"),
    path("tareas", views.modelando, name="datatodo"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
]
