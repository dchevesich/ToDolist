from django.shortcuts import render, redirect
from .models import Tarea
# Create your views here.


def saludar(request):
    return render(request, "tasks/base.html")


def modelando(request):
    datosbd = Tarea.objects.all()
    context = {"tareas": datosbd}

    if request.method == "POST":
        agregar = request.POST['nombre']
        nueva_tarea = Tarea(nombre=agregar)
        nueva_tarea.save()

        return redirect("datatodo")

    return render(request, "tasks/tareas.html", context)
