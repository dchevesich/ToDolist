from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm
from django.contrib import messages
# Create your views here.


def saludar(request):
    return render(request, "tasks/base.html")


def modelando(request):
    datosbd = Tarea.objects.all()

    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("datatodo")
    else:
        form = TareaForm()

    context = {"tareas": datosbd, "form": form}
    return render(request, "tasks/tareas.html", context)


def modificando(request, pk):
    datosdb = Tarea.objects.get(pk=pk)
    if request.method == "POST":
        form = TareaForm(request.POST, instance=datosdb)
        if form.is_valid():
            form.save()
            return redirect("datatodo")
    else:
        form = TareaForm(instance=datosdb)

    context = {"form": form}

    return render(request, 'tasks/modificar_tarea.html', context)


def eliminar_tarea(request, pk):
    tarea_a_eliminar = get_object_or_404(Tarea, pk=pk)
    if request.method == "POST":
        nombre_tarea_eliminada = tarea_a_eliminar.nombre
        tarea_a_eliminar.delete()
        messages.success(
            request, f"Tarea '{nombre_tarea_eliminada}' eliminada exitosamente.")
        return redirect('datatodo')
    else:
        context = {
            'tarea': tarea_a_eliminar
        }
        return render(request, 'tasks/eliminar_tarea.html', context)
