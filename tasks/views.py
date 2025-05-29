from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm
# Create your views here.


def saludar(request):
    return render(request, "tasks/base.html")


def modelando(request):
    datosbd = Tarea.objects.all()
    context = {"tareas": datosbd}

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
